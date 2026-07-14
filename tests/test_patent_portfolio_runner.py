from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

import tools.patent_portfolio as runner


def _write_state(root: Path) -> None:
    (root / "receipts").mkdir(parents=True, exist_ok=True)
    (root / "data").mkdir(parents=True, exist_ok=True)
    (root / "continuation").mkdir(parents=True, exist_ok=True)
    (root / "receipts" / "patent-portfolio-dispatch.json").write_text(
        json.dumps({"decision": "PORTFOLIO_MACHINE_VALIDATION_PASSED", "failed_checks": []}),
        encoding="utf-8",
    )
    (root / "data" / "patent-workstream-status.json").write_text(
        json.dumps({
            "decision": "CONTINUE_ACTIVE_PATENT_WORK",
            "machine_task_count": 2,
            "candidate_review_active": False,
        }),
        encoding="utf-8",
    )
    (root / "continuation" / "patent-portfolio-machine-continuation.json").write_text(
        json.dumps({
            "next_machine_task": {"family_id": "PAT-001", "task": "corroborate source anchor"},
            "manual_reconciliation_required": False,
        }),
        encoding="utf-8",
    )


def test_lock_rejects_overlapping_execution(tmp_path: Path) -> None:
    lock = tmp_path / "receipts" / runner.LOCK_NAME
    fd = runner.acquire_lock(lock)
    try:
        with pytest.raises(runner.PortfolioLocked):
            runner.acquire_lock(lock)
    finally:
        runner.release_lock(fd, lock)
    assert not lock.exists()


def test_run_emits_synchronized_summary_and_cleans_lock(monkeypatch, tmp_path: Path) -> None:
    _write_state(tmp_path)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=0, stdout="{}", stderr="")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)
    summary, code = runner.run(tmp_path)

    assert code == 0
    assert summary["decision"] == "PORTFOLIO_MACHINE_VALIDATION_PASSED"
    assert summary["workstream_decision"] == "CONTINUE_ACTIVE_PATENT_WORK"
    assert summary["machine_task_count"] == 2
    assert summary["manual_reconciliation_required"] is False
    assert summary["authority_boundary"]["filing_performed"] is False
    assert not (tmp_path / "receipts" / runner.LOCK_NAME).exists()


def test_dispatcher_failure_is_propagated(monkeypatch, tmp_path: Path) -> None:
    _write_state(tmp_path)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=2, stdout="{}", stderr="failed check")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)
    summary, code = runner.run(tmp_path)

    assert code == 2
    assert summary["dispatcher_returncode"] == 2
    assert summary["dispatcher_stderr"] == "failed check"
    assert not (tmp_path / "receipts" / runner.LOCK_NAME).exists()


def test_missing_synchronized_state_fails_closed(monkeypatch, tmp_path: Path) -> None:
    (tmp_path / "receipts").mkdir(parents=True)

    def fake_run(*args, **kwargs):
        return SimpleNamespace(returncode=0, stdout="{}", stderr="")

    monkeypatch.setattr(runner.subprocess, "run", fake_run)
    summary, code = runner.run(tmp_path)

    assert code == 3
    assert summary["decision"] == "PORTFOLIO_RUNNER_STATE_INVALID"
    assert not (tmp_path / "receipts" / runner.LOCK_NAME).exists()
