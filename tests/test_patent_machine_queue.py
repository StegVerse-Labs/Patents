from __future__ import annotations

import json
from pathlib import Path

from tools.build_patent_machine_queue import build_queue, is_machine_authorized


def _write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_machine_task_allowed() -> None:
    assert is_machine_authorized("verify rendered SVG hashes") is True
    assert is_machine_authorized("collect exact source commit anchors") is True


def test_human_and_legal_tasks_excluded() -> None:
    assert is_machine_authorized("determine inventorship") is False
    assert is_machine_authorized("obtain practitioner approval") is False
    assert is_machine_authorized("authorize filing packet") is False
    assert is_machine_authorized("submit USPTO filing") is False


def test_build_queue_separates_authorized_and_excluded(tmp_path: Path) -> None:
    status = tmp_path / "status.json"
    _write(status, {
        "family_id": "PAT-999",
        "next_machine_tasks": [
            "verify rendered drawing hashes",
            "determine inventorship",
            "collect source commit anchors",
        ],
    })
    result = build_queue([status])
    assert result["decision"] == "MACHINE_QUEUE_READY"
    assert [item["task"] for item in result["queue"]] == [
        "verify rendered drawing hashes",
        "collect source commit anchors",
    ]
    assert result["excluded"][0]["task"] == "determine inventorship"
    assert result["authority_boundary"]["human_tasks_admitted"] is False


def test_invalid_source_fails_closed(tmp_path: Path) -> None:
    result = build_queue([tmp_path / "missing.json"])
    assert result["decision"] == "INVALID_MACHINE_QUEUE_SOURCE"
    assert result["queue"] == []
