#!/usr/bin/env python3
"""Select the next Patents workstream without abandoning active families.

The controller reads machine-readable completion status files and emits one of:

- CONTINUE_ACTIVE_PATENT_WORK
- REVIEW_ECOSYSTEM_CANDIDATES
- INVALID_PORTFOLIO_STATE

Candidate review is allowed only when every priority family is submission-ready or
externally blocked and no authorized machine task remains for those families.
The controller never files, declares inventorship, or authorizes patent-pending use.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DECISION_CONTINUE = "CONTINUE_ACTIVE_PATENT_WORK"
DECISION_REVIEW = "REVIEW_ECOSYSTEM_CANDIDATES"
DECISION_INVALID = "INVALID_PORTFOLIO_STATE"

EXTERNAL_GATE_KEYS = {
    "contributor_interviews_complete",
    "inventorship_determined",
    "verified_prior_art_references",
    "earliest_public_disclosure_audited",
    "formal_drawings_approved",
    "practitioner_written_recommendation",
    "owner_packet_authorization",
    "owner_filing_authorization",
    "filing_packet_emitted_and_reviewed",
}


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data.get("family_id"):
        raise ValueError(f"invalid completion status: {path}")
    return data


def classify_family(data: dict[str, Any]) -> dict[str, Any]:
    family_id = str(data["family_id"])
    filed = bool(data.get("filed", False))
    status = str(data.get("status", ""))
    machine_tasks = [str(x) for x in data.get("next_machine_tasks", []) if str(x).strip()]
    gates = data.get("blocking_gates", {})
    if not isinstance(gates, dict):
        raise ValueError(f"{family_id}: blocking_gates must be an object")

    unresolved = sorted(str(k) for k, v in gates.items() if v is not True)
    external_unresolved = sorted(k for k in unresolved if k in EXTERNAL_GATE_KEYS)
    nonexternal_unresolved = sorted(k for k in unresolved if k not in EXTERNAL_GATE_KEYS)

    submission_ready = (
        status in {"submission_ready", "ready_for_filing", "filed"}
        or filed
        or (not unresolved and not machine_tasks)
    )
    externally_blocked = (
        not submission_ready
        and not machine_tasks
        and bool(external_unresolved)
        and not nonexternal_unresolved
    )

    return {
        "family_id": family_id,
        "status": status,
        "submission_ready": submission_ready,
        "externally_blocked": externally_blocked,
        "next_machine_tasks": machine_tasks,
        "unresolved_gates": unresolved,
        "external_unresolved_gates": external_unresolved,
        "nonexternal_unresolved_gates": nonexternal_unresolved,
    }


def select(status_files: list[Path]) -> dict[str, Any]:
    if not status_files:
        return {"decision": DECISION_INVALID, "reasons": ["no completion status files supplied"], "families": []}

    try:
        families = [classify_family(_load(path)) for path in status_files]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return {"decision": DECISION_INVALID, "reasons": [str(exc)], "families": []}

    actionable = [f for f in families if f["next_machine_tasks"]]
    unclassified = [
        f for f in families
        if not f["submission_ready"] and not f["externally_blocked"] and not f["next_machine_tasks"]
    ]

    if actionable:
        return {
            "decision": DECISION_CONTINUE,
            "reasons": [f"{f['family_id']} has authorized machine tasks" for f in actionable],
            "families": families,
        }
    if unclassified:
        return {
            "decision": DECISION_INVALID,
            "reasons": [f"{f['family_id']} is neither actionable, submission-ready, nor externally blocked" for f in unclassified],
            "families": families,
        }
    return {
        "decision": DECISION_REVIEW,
        "reasons": ["all active families are submission-ready or externally blocked with no authorized machine tasks"],
        "families": families,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status_files", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = select(args.status_files)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 2 if result["decision"] == DECISION_INVALID else 0


if __name__ == "__main__":
    raise SystemExit(main())
