from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import tools.run_patent_portfolio_dispatcher as dispatcher


def test_build_commands_covers_active_machine_surface() -> None:
    commands = dispatcher.build_commands()
    ids = [item["id"] for item in commands]
    assert ids == [
        "pat001_completion",
        "pat005_completion",
        "pat001_readiness",
        "pat001_source_corroboration",
        "pat001_canonical_source_search",
        "pat001_lifecycle_evidence",
        "pat005_implementation_anchors",
        "pat005_negative_cases",
        "pat001_drawing_sources",
        "pat001_rendered_drawings",
        "evidence_queue_build",
        "evidence_queue_validate",
        "machine_queue",
        "workstream_selection",
        "pytest",
    ]
    readiness = next(item for item in commands if item["id"] == "pat001_readiness")
    assert readiness["accepted_returncodes"] == {0, 2}


def test_dispatch_passes_expected_fail_closed_readiness(monkeypatch, tmp_path: Path) -> None:
    responses = {
        "pat001_completion": (0, {"decision": "VALID_FAIL_CLOSED"}),
        "pat005_completion": (0, {"decision": "VALID_FAIL_CLOSED"}),
        "pat001_readiness": (2, {"decision": "FAIL_CLOSED_BLOCKERS"}),
        "pat001_source_corroboration": (0, {"decision": "CORROBORATION_RECORD_VALID"}),
        "pat001_canonical_source_search": (0, {"decision": "SOURCE_SEARCH_RECEIPT_VALID"}),
        "pat001_lifecycle_evidence": (0, {"decision": "PAT001_LIFECYCLE_EVIDENCE_VALID"}),
        "pat005_implementation_anchors": (0, {"decision": "PAT005_IMPLEMENTATION_ANCHORS_VALID"}),
        "pat005_negative_cases": (0, {"decision": "PAT005_NEGATIVE_CASES_REPLAYED", "passed_count": 8}),
        "pat001_drawing_sources": (0, {"decision": "DRAWING_SOURCES_VALID"}),
        "pat001_rendered_drawings": (0, {"decision": "DRAWING_MANIFEST_VALID"}),
        "evidence_queue_build": (0, {"decision": "EVIDENCE_QUEUE_READY", "queue": [{"task_id": "EVID-PAT-001-0123456789ab"}]}),
        "evidence_queue_validate": (0, {"decision": "EVIDENCE_QUEUE_VALID"}),
        "machine_queue": (0, {"decision": "MACHINE_QUEUE_READY", "queue": [{"task": "verify hashes"}]}),
        "workstream_selection": (0, {"decision": "CONTINUE_ACTIVE_PATENT_WORK"}),
        "pytest": (0, None),
    }
    command_ids = iter([item["id"] for item in dispatcher.build_commands()])

    def fake_run(command, cwd, text, capture_output, check):
        check_id = next(command_ids)
        returncode, payload = responses[check_id]
        stdout = json.dumps(payload) if payload is not None else ""
        return SimpleNamespace(returncode=returncode, stdout=stdout, stderr="")

    monkeypatch.setattr(dispatcher.subprocess, "run", fake_run)
    receipt = dispatcher.dispatch(tmp_path)
    assert receipt["decision"] == "PORTFOLIO_MACHINE_VALIDATION_PASSED"
    assert receipt["failed_checks"] == []
    assert receipt["workstream_decision"] == "CONTINUE_ACTIVE_PATENT_WORK"
    assert receipt["machine_queue_size"] == 1
    assert receipt["evidence_queue_size"] == 1
    assert receipt["schema_version"] == "2.1"
    assert receipt["authority_boundary"]["filing_performed"] is False


def test_dispatch_reports_failed_check(monkeypatch, tmp_path: Path) -> None:
    command_ids = iter([item["id"] for item in dispatcher.build_commands()])

    def fake_run(command, cwd, text, capture_output, check):
        check_id = next(command_ids)
        returncode = 2 if check_id == "pat001_lifecycle_evidence" else 0
        payload = {"decision": "INVALID_PAT001_LIFECYCLE_EVIDENCE"} if returncode else {"decision": "OK"}
        return SimpleNamespace(returncode=returncode, stdout=json.dumps(payload), stderr="")

    monkeypatch.setattr(dispatcher.subprocess, "run", fake_run)
    receipt = dispatcher.dispatch(tmp_path)
    assert receipt["decision"] == "PORTFOLIO_MACHINE_VALIDATION_FAILED"
    assert receipt["failed_checks"] == ["pat001_lifecycle_evidence"]
