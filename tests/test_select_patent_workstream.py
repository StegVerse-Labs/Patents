from __future__ import annotations

import json
from pathlib import Path

from tools.select_patent_workstream import (
    DECISION_CONTINUE,
    DECISION_INVALID,
    DECISION_REVIEW,
    select,
)


def write_status(tmp_path: Path, name: str, payload: dict) -> Path:
    path = tmp_path / name
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_continues_when_machine_task_remains(tmp_path: Path) -> None:
    path = write_status(tmp_path, "pat001.json", {
        "family_id": "PAT-001",
        "status": "practitioner_review_ready_with_blockers",
        "filed": False,
        "blocking_gates": {"formal_drawings_approved": False},
        "next_machine_tasks": ["render verified drawings"],
    })
    result = select([path])
    assert result["decision"] == DECISION_CONTINUE


def test_reviews_candidates_when_all_families_externally_blocked(tmp_path: Path) -> None:
    first = write_status(tmp_path, "pat001.json", {
        "family_id": "PAT-001",
        "status": "practitioner_review_ready_with_blockers",
        "filed": False,
        "blocking_gates": {
            "contributor_interviews_complete": False,
            "practitioner_written_recommendation": False,
        },
        "next_machine_tasks": [],
    })
    second = write_status(tmp_path, "pat005.json", {
        "family_id": "PAT-005",
        "status": "practitioner_review_ready",
        "filed": False,
        "blocking_gates": {"owner_filing_authorization": False},
        "next_machine_tasks": [],
    })
    result = select([first, second])
    assert result["decision"] == DECISION_REVIEW
    assert all(f["externally_blocked"] for f in result["families"])


def test_reviews_candidates_when_families_submission_ready(tmp_path: Path) -> None:
    path = write_status(tmp_path, "pat001.json", {
        "family_id": "PAT-001",
        "status": "submission_ready",
        "filed": False,
        "blocking_gates": {},
        "next_machine_tasks": [],
    })
    assert select([path])["decision"] == DECISION_REVIEW


def test_invalid_when_nonexternal_gate_has_no_task(tmp_path: Path) -> None:
    path = write_status(tmp_path, "pat001.json", {
        "family_id": "PAT-001",
        "status": "blocked",
        "filed": False,
        "blocking_gates": {"source_commit_anchors_verified": False},
        "next_machine_tasks": [],
    })
    assert select([path])["decision"] == DECISION_INVALID


def test_invalid_without_status_files() -> None:
    assert select([])["decision"] == DECISION_INVALID
