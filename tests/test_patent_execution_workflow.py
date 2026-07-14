from __future__ import annotations

from pathlib import Path


WORKFLOW = Path(".github/workflows/test-readiness.yml")


def test_readiness_workflow_runs_canonical_portfolio_entrypoint() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "python tools/patent_portfolio.py --repo-root ." in text
    assert "workflow_dispatch:" in text
    assert "push:" in text
    assert "pull_request:" in text


def test_readiness_workflow_publishes_execution_evidence() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "actions/upload-artifact@v4" in text
    for path in (
        "receipts/patent-portfolio-dispatch.json",
        "data/patent-workstream-status.json",
        "data/patent-machine-queue.json",
        "data/patent-evidence-acquisition-queue.json",
        "continuation/patent-portfolio-machine-continuation.json",
    ):
        assert path in text


def test_readiness_workflow_keeps_repository_read_only() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "contents: read" in text
    assert "contents: write" not in text
