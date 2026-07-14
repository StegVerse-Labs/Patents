#!/usr/bin/env python3
"""Single-command patent portfolio runner with concurrency protection.

This entry point executes the machine-owned dispatcher, preserves synchronized
state, and emits a concise operator summary. It never files, signs, pays,
approves drawings, determines inventorship, or authorizes patent-pending use.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

LOCK_NAME = ".patent-portfolio.lock"


class PortfolioLocked(RuntimeError):
    pass


def acquire_lock(lock_path: Path) -> int:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        return os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise PortfolioLocked(f"portfolio execution already active: {lock_path}") from exc


def release_lock(fd: int, lock_path: Path) -> None:
    try:
        os.close(fd)
    finally:
        lock_path.unlink(missing_ok=True)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object: {path}")
    return data


def summarize(repo_root: Path) -> dict[str, Any]:
    receipt_path = repo_root / "receipts" / "patent-portfolio-dispatch.json"
    status_path = repo_root / "data" / "patent-workstream-status.json"
    continuation_path = repo_root / "continuation" / "patent-portfolio-machine-continuation.json"

    receipt = load_json(receipt_path)
    status = load_json(status_path)
    continuation = load_json(continuation_path)

    return {
        "decision": receipt.get("decision"),
        "workstream_decision": status.get("decision"),
        "failed_checks": receipt.get("failed_checks", []),
        "machine_task_count": status.get("machine_task_count", 0),
        "next_machine_task": continuation.get("next_machine_task"),
        "candidate_review_active": status.get("candidate_review_active", False),
        "manual_reconciliation_required": continuation.get("manual_reconciliation_required", True),
        "receipt": str(receipt_path.relative_to(repo_root)),
        "status": str(status_path.relative_to(repo_root)),
        "continuation": str(continuation_path.relative_to(repo_root)),
        "authority_boundary": {
            "filing_performed": False,
            "filing_authorized": False,
            "inventorship_determined": False,
            "drawing_approval_granted": False,
            "patent_pending_authorized": False,
        },
    }


def run(repo_root: Path) -> tuple[dict[str, Any], int]:
    lock_path = repo_root / "receipts" / LOCK_NAME
    fd = acquire_lock(lock_path)
    try:
        completed = subprocess.run(
            [sys.executable, "tools/run_patent_portfolio_dispatcher.py", "--repo-root", "."],
            cwd=repo_root,
            text=True,
            capture_output=True,
            check=False,
        )
        try:
            summary = summarize(repo_root)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            summary = {
                "decision": "PORTFOLIO_RUNNER_STATE_INVALID",
                "error": str(exc),
                "dispatcher_returncode": completed.returncode,
                "dispatcher_stdout": completed.stdout,
                "dispatcher_stderr": completed.stderr,
            }
            return summary, 3

        summary["dispatcher_returncode"] = completed.returncode
        if completed.stderr.strip():
            summary["dispatcher_stderr"] = completed.stderr
        return summary, completed.returncode
    finally:
        release_lock(fd, lock_path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()

    try:
        summary, code = run(repo_root)
    except PortfolioLocked as exc:
        summary = {
            "decision": "PORTFOLIO_EXECUTION_LOCKED",
            "error": str(exc),
            "manual_reconciliation_required": False,
        }
        code = 4

    print(json.dumps(summary, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
