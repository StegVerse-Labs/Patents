from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from tools.synchronize_patent_portfolio_state import synchronize, write_synchronized_state


def _write_receipt(path: Path, *, workstream: str = "CONTINUE_ACTIVE_PATENT_WORK") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "1.5",
        "decision": "PORTFOLIO_MACHINE_VALIDATION_PASSED",
        "failed_checks": [],
        "workstream_decision": workstream,
        "machine_queue": {
            "decision": "MACHINE_QUEUE_READY",
            "queue": [
                {"family_id": "PAT-001", "task": "corroborate source commits"},
                {"family_id": "PAT-005", "task": "preserve executable fixtures"},
            ],
            "excluded": [],
        },
        "authority_boundary": {
            "filing_performed": False,
            "filing_authorized": False,
            "inventorship_determined": False,
            "drawing_approval_granted": False,
            "patent_pending_authorized": False,
        },
    }
    path.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")


def test_synchronize_builds_status_and_continuation(tmp_path: Path) -> None:
    receipt = tmp_path / "receipts" / "dispatch.json"
    _write_receipt(receipt)

    result = synchronize(tmp_path, receipt)

    assert result["status"]["decision"] == "CONTINUE_ACTIVE_PATENT_WORK"
    assert result["status"]["machine_task_count"] == 2
    assert result["status"]["candidate_review_active"] is False
    assert result["continuation"]["next_machine_task"]["family_id"] == "PAT-001"
    assert result["continuation"]["manual_reconciliation_required"] is False


def test_write_synchronized_state_preserves_receipt_hash(tmp_path: Path) -> None:
    receipt = tmp_path / "receipts" / "dispatch.json"
    _write_receipt(receipt)
    expected_hash = hashlib.sha256(receipt.read_bytes()).hexdigest()
    status = tmp_path / "data" / "status.json"
    continuation = tmp_path / "continuation" / "machine.json"

    write_synchronized_state(tmp_path, receipt, status, continuation)

    status_payload = json.loads(status.read_text(encoding="utf-8"))
    continuation_payload = json.loads(continuation.read_text(encoding="utf-8"))
    assert status_payload["dispatcher_receipt_sha256"] == expected_hash
    assert continuation_payload["source_receipt_sha256"] == expected_hash
    assert hashlib.sha256(receipt.read_bytes()).hexdigest() == expected_hash


def test_candidate_review_activates_from_dispatcher_decision(tmp_path: Path) -> None:
    receipt = tmp_path / "receipts" / "dispatch.json"
    _write_receipt(receipt, workstream="REVIEW_ECOSYSTEM_CANDIDATES")

    result = synchronize(tmp_path, receipt)

    assert result["status"]["candidate_review_active"] is True


def test_synchronize_rejects_missing_queue(tmp_path: Path) -> None:
    receipt = tmp_path / "receipts" / "dispatch.json"
    receipt.parent.mkdir(parents=True)
    receipt.write_text(
        json.dumps({
            "decision": "PORTFOLIO_MACHINE_VALIDATION_PASSED",
            "failed_checks": [],
            "workstream_decision": "CONTINUE_ACTIVE_PATENT_WORK",
        }),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing machine_queue"):
        synchronize(tmp_path, receipt)
