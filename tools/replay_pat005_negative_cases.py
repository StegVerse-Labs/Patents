#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_HANDOFF_DECISIONS = {
    "accepted_observe_only",
    "accepted_read_control",
    "accepted_input_only",
    "accepted_playback_control",
    "manual_review_required",
    "denied",
}
REQUIRED_REASONS = {
    "wrong destination repo",
    "unexpected handoff status",
    "unexpected destination decision",
    "missing non-authority rule",
    "payload mismatch",
    "destination mismatch",
    "decision not allowed",
    "receipt must be reconstructable",
}


def evaluate(case: dict) -> str:
    mutation = case["mutation"]
    surface = case["validator_surface"]
    if surface == "handoff":
        if "destination_repo" in mutation and mutation["destination_repo"] not in {
            "StegVerse-Labs/StegTalk",
            "StegVerse-Labs/StegMusic",
        }:
            return "wrong destination repo"
        if mutation.get("status") not in {None, "installed_non_authorizing_handoff"}:
            return "unexpected handoff status"
        decisions = mutation.get("allowed_destination_decisions")
        if decisions is not None and not set(decisions) <= ALLOWED_HANDOFF_DECISIONS:
            return "unexpected destination decision"
        rule = mutation.get("non_authority_rule")
        if rule is not None and "handoff candidates only" not in rule:
            return "missing non-authority rule"
    elif surface == "receipt":
        if "receipt.payload_id" in mutation:
            return "payload mismatch"
        if "receipt.destination_repo" in mutation:
            return "destination mismatch"
        if "receipt.decision" in mutation and mutation["receipt.decision"] not in ALLOWED_HANDOFF_DECISIONS:
            return "decision not allowed"
        if mutation.get("receipt.reconstructable") is False:
            return "receipt must be reconstructable"
    return "NO_REJECTION"


def replay(path: Path) -> dict:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("family_id") != "PAT-005":
        errors.append("family_id must be PAT-005")
    seen: set[str] = set()
    results: list[dict] = []
    for case in data.get("cases", []):
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            errors.append("case_id missing")
            continue
        if case_id in seen:
            errors.append(f"duplicate case_id: {case_id}")
            continue
        seen.add(case_id)
        reason = evaluate(case)
        expected = case.get("expected_reason")
        passed = case.get("expected_result") == "REJECT" and reason == expected and reason in REQUIRED_REASONS
        if not passed:
            errors.append(f"case {case_id} did not reproduce expected rejection")
        results.append({"case_id": case_id, "observed_reason": reason, "passed": passed})
    boundary = data.get("authority_boundary", {})
    for key in [
        "filing_performed",
        "filing_authorized",
        "inventorship_determined",
        "patentability_determined",
        "patent_pending_authorized",
    ]:
        if boundary.get(key) is not False:
            errors.append(f"authority_boundary.{key} must be false")
    return {
        "decision": "PAT005_NEGATIVE_CASES_REPLAYED" if not errors else "PAT005_NEGATIVE_CASES_INVALID",
        "case_count": len(results),
        "passed_count": sum(1 for result in results if result["passed"]),
        "results": results,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args()
    result = replay(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PAT005_NEGATIVE_CASES_REPLAYED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
