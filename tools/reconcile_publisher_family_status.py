#!/usr/bin/env python3
"""Reconcile dedicated Publisher-family status records into the central ledger.

This tool performs a bounded status-only merge. It does not import claim text,
legal conclusions, inventorship, ownership, filing authority, application data,
receipts, filing dates, or deadlines. Any attempted filing-state activation or
portfolio-invariant change fails closed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "publisher-family-completion-status.json"

STATUS_FILES = {
    "commit_time_admissibility_gate": ROOT / "data" / "publisher-commit-time-admissibility-evidence-status.json",
    "receipt_based_state_transition_validation": ROOT / "data" / "publisher-receipt-based-state-transition-status.json",
    "publisher_governed_disclosure_pipeline": ROOT / "data" / "publisher-governed-disclosure-pipeline-status.json",
    "application_correction_gate": ROOT / "data" / "publisher-application-correction-gate-status.json",
    "ai_output_to_action_boundary": ROOT / "data" / "publisher-ai-output-to-action-boundary-status.json",
    "recoverability_aware_execution_boundary": ROOT / "data" / "publisher-recoverability-aware-execution-status.json",
    "master_records_reconstruction_and_verification": ROOT / "data" / "publisher-master-records-reconstruction-status.json",
    "multi_entity_observer_participant_admissibility": ROOT / "data" / "publisher-multi-entity-observer-participant-status.json",
}

HANDOFFS = {
    "commit_time_admissibility_gate": "COMMIT_TIME_ADMISSIBILITY_MIRROR_HANDOFF.md",
    "receipt_based_state_transition_validation": "RECEIPT_BASED_STATE_TRANSITION_MIRROR_HANDOFF.md",
    "publisher_governed_disclosure_pipeline": "PUBLISHER_GOVERNED_DISCLOSURE_PIPELINE_MIRROR_HANDOFF.md",
    "application_correction_gate": "APPLICATION_CORRECTION_GATE_MIRROR_HANDOFF.md",
    "ai_output_to_action_boundary": "AI_OUTPUT_TO_ACTION_MIRROR_HANDOFF.md",
    "recoverability_aware_execution_boundary": "RECOVERABILITY_AWARE_EXECUTION_MIRROR_HANDOFF.md",
    "master_records_reconstruction_and_verification": "MASTER_RECORDS_RECONSTRUCTION_VERIFICATION_MIRROR_HANDOFF.md",
    "multi_entity_observer_participant_admissibility": "MULTI_ENTITY_OBSERVER_PARTICIPANT_MIRROR_HANDOFF.md",
}

LIFECYCLE_FIELDS = (
    "status",
    "invention_capture",
    "disclosure_chronology",
    "evidence_map",
    "prior_art_distinction_notes",
    "specification",
    "abstract",
    "claim_themes",
    "drawings",
    "inventor_fields",
    "ownership_fields",
    "counsel_questions",
    "filing_packet",
    "warning_resolution",
    "human_filing",
    "filing_receipt",
    "application_number",
    "actual_filing_date",
    "nonprovisional_deadline",
)

EXPECTED_INVARIANTS = {
    "filed_families": 0,
    "patent_pending_authorized_families": 0,
    "application_numbers_recorded": 0,
    "filing_receipts_recorded": 0,
    "calculated_deadlines": 0,
    "ready_for_owner_decision": 0,
}


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"required file missing: {path.relative_to(ROOT)}")
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path.relative_to(ROOT)}")
    return value


def assert_fail_closed_status(family_key: str, status: dict[str, Any]) -> None:
    prohibited_truthy = {
        "patent_pending_authorized": status.get("patent_pending_authorized"),
        "filed": status.get("filed"),
        "approval_required_now": status.get("approval_required_now"),
    }
    activated = [name for name, value in prohibited_truthy.items() if value is True]
    if activated:
        raise ValueError(f"{family_key}: prohibited lifecycle activation: {', '.join(activated)}")

    for field in ("filing_receipt", "application_number", "actual_filing_date", "nonprovisional_deadline"):
        if status.get(field) is not None:
            raise ValueError(f"{family_key}: unsupported non-null {field}")

    if status.get("human_filing") not in (None, "not_started"):
        raise ValueError(f"{family_key}: unsupported human_filing state")
    if status.get("filing_packet") not in (None, "not_authorized"):
        raise ValueError(f"{family_key}: unsupported filing_packet state")


def reconcile(ledger: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    families = ledger.get("families")
    if not isinstance(families, list):
        raise ValueError("central ledger families must be a list")

    by_key = {item.get("family_key"): item for item in families if isinstance(item, dict)}
    if set(by_key) != set(STATUS_FILES):
        missing = sorted(set(STATUS_FILES) - set(by_key))
        unknown = sorted(set(by_key) - set(STATUS_FILES))
        raise ValueError(f"family identity mismatch; missing={missing}, unknown={unknown}")

    changes: list[str] = []
    for family_key, status_path in STATUS_FILES.items():
        status = load_json(status_path)
        if status.get("family_key") != family_key:
            raise ValueError(f"{status_path.name}: family_key mismatch")
        assert_fail_closed_status(family_key, status)

        handoff = HANDOFFS[family_key]
        if not (ROOT / handoff).is_file():
            raise FileNotFoundError(f"dedicated handoff missing: {handoff}")

        target = by_key[family_key]
        for field in LIFECYCLE_FIELDS:
            if field in status and target.get(field) != status[field]:
                target[field] = status[field]
                changes.append(f"{family_key}.{field}")
        if target.get("status_record") != str(status_path.relative_to(ROOT)):
            target["status_record"] = str(status_path.relative_to(ROOT))
            changes.append(f"{family_key}.status_record")
        if target.get("dedicated_handoff") != handoff:
            target["dedicated_handoff"] = handoff
            changes.append(f"{family_key}.dedicated_handoff")
        expected = status.get("expected_decision") or status.get("current_decision")
        if expected is not None and target.get("current_decision") != expected:
            target["current_decision"] = expected
            changes.append(f"{family_key}.current_decision")

    invariants = ledger.get("portfolio_invariants")
    if not isinstance(invariants, dict):
        raise ValueError("portfolio_invariants must be an object")
    for key, expected in EXPECTED_INVARIANTS.items():
        if invariants.get(key) != expected:
            raise ValueError(f"portfolio invariant changed: {key}={invariants.get(key)!r}, expected {expected!r}")

    ledger["schema_version"] = "0.7"
    ledger["reconciliation_method"] = "dedicated_status_only_fail_closed"
    ledger["dedicated_handoff_coverage"] = len(HANDOFFS)
    return ledger, changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="replace the central ledger after validation")
    parser.add_argument("--output", type=Path, help="write reconciled JSON to a separate path")
    args = parser.parse_args()

    ledger = load_json(LEDGER)
    reconciled, changes = reconcile(ledger)
    rendered = json.dumps(reconciled, indent=2, sort_keys=False) + "\n"

    if args.write and args.output:
        parser.error("use either --write or --output, not both")
    if args.write:
        LEDGER.write_text(rendered, encoding="utf-8")
    elif args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    print(f"RECONCILIATION_VALID families={len(STATUS_FILES)} changes={len(changes)}", file=__import__("sys").stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
