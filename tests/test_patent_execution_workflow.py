from __future__ import annotations

from pathlib import Path


# G17 (StegVerse-org/.github#166): test-readiness.yml is folded into
# .github/workflows/validation-dispatcher.yml as catalog group test-readiness.repo-smoke.
# Its verbatim record is checked here; the dispatcher runs its sha256-pinned run blocks.
WORKFLOW = Path("tools/tasks/folded/test-readiness.yml")
CATALOG = Path("tools/tasks/task_catalog.json")


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


def test_dispatcher_group_runs_the_folded_readiness_steps() -> None:
    import hashlib
    import json

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    group = next(g for g in catalog["groups"] if g["id"] == "test-readiness.repo-smoke")
    bodies = []
    for step in group["steps"]:
        body = Path(step["run_file"]).read_bytes()
        assert hashlib.sha256(body).hexdigest() == step["run_sha256"], step["run_file"]
        bodies.append(body.decode("utf-8"))
    assert any("python tools/patent_portfolio.py --repo-root ." in b for b in bodies)
    assert set(group["events"]) == {"pull_request", "push"}
