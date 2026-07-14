from __future__ import annotations

import json
from pathlib import Path

from tools.validate_completion_status import validate_record


REPO_ROOT = Path(__file__).resolve().parents[1]


def _write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_valid_fail_closed_record(tmp_path: Path) -> None:
    artifact = tmp_path / "evidence" / "draft.md"
    artifact.parent.mkdir(parents=True)
    artifact.write_text("draft", encoding="utf-8")
    record = tmp_path / "status.json"
    _write(record, {
        "family_id": "PAT-999",
        "filed": False,
        "patent_pending_authorized": False,
        "completed": {"draft": True},
        "blocking_gates": {"human_review": False},
        "artifact_map": {"draft": "evidence/draft.md"},
        "expected_decision": "FAIL_CLOSED_BLOCKERS",
    })

    result = validate_record(tmp_path, record)
    assert result["decision"] == "VALID_FAIL_CLOSED"
    assert result["unresolved_blocking_gates"] == ["human_review"]


def test_missing_completed_artifact_is_invalid(tmp_path: Path) -> None:
    record = tmp_path / "status.json"
    _write(record, {
        "family_id": "PAT-999",
        "filed": False,
        "patent_pending_authorized": False,
        "completed": {"draft": True},
        "blocking_gates": {"human_review": False},
        "artifact_map": {"draft": "missing.md"},
        "expected_decision": "FAIL_CLOSED_BLOCKERS",
    })

    result = validate_record(tmp_path, record)
    assert result["decision"] == "INVALID_COMPLETION_RECORD"
    assert any("completed artifact missing" in item for item in result["errors"])


def test_completed_key_requires_artifact_map_entry(tmp_path: Path) -> None:
    record = tmp_path / "status.json"
    _write(record, {
        "family_id": "PAT-999",
        "filed": False,
        "patent_pending_authorized": False,
        "completed": {"draft": True},
        "blocking_gates": {"human_review": False},
        "artifact_map": {"other": "other.md"},
        "expected_decision": "FAIL_CLOSED_BLOCKERS",
    })

    result = validate_record(tmp_path, record)
    assert result["decision"] == "INVALID_COMPLETION_RECORD"
    assert "completed artifact has no artifact_map entry: draft" in result["errors"]


def test_patent_pending_requires_filed_state(tmp_path: Path) -> None:
    artifact = tmp_path / "draft.md"
    artifact.write_text("draft", encoding="utf-8")
    record = tmp_path / "status.json"
    _write(record, {
        "family_id": "PAT-999",
        "filed": False,
        "patent_pending_authorized": True,
        "completed": {"draft": True},
        "blocking_gates": {"human_review": False},
        "artifact_map": {"draft": "draft.md"},
        "expected_decision": "FAIL_CLOSED_BLOCKERS",
    })

    result = validate_record(tmp_path, record)
    assert result["decision"] == "INVALID_COMPLETION_RECORD"
    assert "patent_pending_authorized cannot be true while filed is false" in result["errors"]


def test_pat_001_completion_record_matches_repository() -> None:
    record = REPO_ROOT / "data" / "PAT-001-completion-status.json"
    result = validate_record(REPO_ROOT, record)
    assert result["decision"] == "VALID_FAIL_CLOSED"
    assert not result["errors"]


def test_pat_005_completion_record_matches_repository() -> None:
    record = REPO_ROOT / "data" / "PAT-005-completion-status.json"
    result = validate_record(REPO_ROOT, record)
    assert result["decision"] == "VALID_FAIL_CLOSED"
    assert not result["errors"]
