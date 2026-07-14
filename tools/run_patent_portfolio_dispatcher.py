#!/usr/bin/env python3
"""Run the complete machine-owned patent validation surface and emit one receipt.

This dispatcher performs repository-local validation only. It never files,
signs, pays, determines inventorship, approves drawings, authorizes a packet,
or represents that an application is patent pending.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.synchronize_patent_portfolio_state import write_synchronized_state


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _run(command: list[str], cwd: Path, accepted_returncodes: set[int]) -> dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )
    parsed: Any = None
    try:
        parsed = json.loads(completed.stdout) if completed.stdout.strip() else None
    except json.JSONDecodeError:
        parsed = None
    return {
        "command": command,
        "accepted_returncodes": sorted(accepted_returncodes),
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "parsed_result": parsed,
        "passed": completed.returncode in accepted_returncodes,
    }


def build_commands() -> list[dict[str, Any]]:
    py = sys.executable
    active_status = [
        "data/PAT-001-completion-status.json",
        "data/PAT-005-completion-status.json",
    ]
    return [
        {
            "id": "pat001_completion",
            "command": [py, "tools/validate_completion_status.py", active_status[0], "--repo-root", "."],
            "accepted_returncodes": {0},
        },
        {
            "id": "pat005_completion",
            "command": [py, "tools/validate_completion_status.py", active_status[1], "--repo-root", "."],
            "accepted_returncodes": {0},
        },
        {
            "id": "pat001_readiness",
            "command": [py, "tools/validate_patent_readiness.py", "--family", "PAT-001", "--root", "."],
            "accepted_returncodes": {0, 2},
        },
        {
            "id": "pat001_drawing_sources",
            "command": [py, "tools/lint_patent_drawings.py", "figures"],
            "accepted_returncodes": {0},
        },
        {
            "id": "pat001_rendered_drawings",
            "command": [py, "tools/verify_rendered_drawings.py", "rendered/PAT-001/manifest.json", "--repo-root", "."],
            "accepted_returncodes": {0},
        },
        {
            "id": "machine_queue",
            "command": [
                py,
                "tools/build_patent_machine_queue.py",
                *active_status,
                "--output",
                "data/patent-machine-queue.json",
            ],
            "accepted_returncodes": {0},
        },
        {
            "id": "workstream_selection",
            "command": [py, "tools/select_patent_workstream.py", *active_status],
            "accepted_returncodes": {0},
        },
        {
            "id": "pytest",
            "command": [py, "-m", "pytest", "-q"],
            "accepted_returncodes": {0},
        },
    ]


def dispatch(repo_root: Path) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for item in build_commands():
        result = _run(item["command"], repo_root, item["accepted_returncodes"])
        result["id"] = item["id"]
        results.append(result)

    failures = [result["id"] for result in results if not result["passed"]]
    workstream = next((r.get("parsed_result") for r in results if r["id"] == "workstream_selection"), None)
    queue = next((r.get("parsed_result") for r in results if r["id"] == "machine_queue"), None)
    decision = "PORTFOLIO_MACHINE_VALIDATION_PASSED" if not failures else "PORTFOLIO_MACHINE_VALIDATION_FAILED"
    return {
        "schema_version": "1.5",
        "generated_at": _utc_now(),
        "decision": decision,
        "failed_checks": failures,
        "workstream_decision": workstream.get("decision") if isinstance(workstream, dict) else None,
        "machine_queue": queue if isinstance(queue, dict) else None,
        "machine_queue_size": len(queue.get("queue", [])) if isinstance(queue, dict) else None,
        "checks": results,
        "authority_boundary": {
            "filing_performed": False,
            "filing_authorized": False,
            "inventorship_determined": False,
            "drawing_approval_granted": False,
            "patent_pending_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--receipt", type=Path, default=Path("receipts/patent-portfolio-dispatch.json"))
    parser.add_argument("--status-output", type=Path, default=Path("data/patent-workstream-status.json"))
    parser.add_argument(
        "--continuation-output",
        type=Path,
        default=Path("continuation/patent-portfolio-machine-continuation.json"),
    )
    parser.add_argument("--skip-state-sync", action="store_true")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    receipt_path = args.receipt if args.receipt.is_absolute() else repo_root / args.receipt
    status_output = args.status_output if args.status_output.is_absolute() else repo_root / args.status_output
    continuation_output = (
        args.continuation_output
        if args.continuation_output.is_absolute()
        else repo_root / args.continuation_output
    )

    receipt = dispatch(repo_root)
    receipt["state_synchronization"] = {
        "performed": not args.skip_state_sync,
        "status_output": str(status_output.relative_to(repo_root)) if not args.skip_state_sync else None,
        "continuation_output": str(continuation_output.relative_to(repo_root)) if not args.skip_state_sync else None,
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if not args.skip_state_sync:
        write_synchronized_state(
            repo_root,
            receipt_path,
            status_output,
            continuation_output,
        )

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["decision"] == "PORTFOLIO_MACHINE_VALIDATION_PASSED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
