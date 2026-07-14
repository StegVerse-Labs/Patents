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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _run(command: list[str], cwd: Path) -> dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "passed": completed.returncode == 0,
    }


def build_commands(repo_root: Path) -> list[dict[str, Any]]:
    py = sys.executable
    return [
        {
            "id": "pat001_completion",
            "command": [py, "tools/validate_completion_status.py", "data/PAT-001-completion-status.json", "--repo-root", "."],
        },
        {
            "id": "pat005_completion",
            "command": [py, "tools/validate_completion_status.py", "data/PAT-005-completion-status.json", "--repo-root", "."],
        },
        {
            "id": "pat001_readiness",
            "command": [py, "tools/validate_patent_readiness.py", "filing-readiness/PAT-001_FILING_READINESS_INDEX.md", "--repo-root", "."],
        },
        {
            "id": "pat001_drawing_sources",
            "command": [py, "tools/lint_patent_drawings.py", "figures"],
        },
        {
            "id": "pat001_rendered_drawings",
            "command": [py, "tools/verify_rendered_drawings.py", "rendered/PAT-001/manifest.json", "--repo-root", "."],
        },
        {
            "id": "workstream_selection",
            "command": [py, "tools/select_patent_workstream.py", "data/patent-workstream-status.json"],
        },
        {
            "id": "pytest",
            "command": [py, "-m", "pytest", "-q"],
        },
    ]


def dispatch(repo_root: Path) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for item in build_commands(repo_root):
        result = _run(item["command"], repo_root)
        result["id"] = item["id"]
        results.append(result)

    failures = [result["id"] for result in results if not result["passed"]]
    decision = "PORTFOLIO_MACHINE_VALIDATION_PASSED" if not failures else "PORTFOLIO_MACHINE_VALIDATION_FAILED"
    return {
        "schema_version": "1.0",
        "generated_at": _utc_now(),
        "decision": decision,
        "failed_checks": failures,
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
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    receipt_path = args.receipt if args.receipt.is_absolute() else repo_root / args.receipt
    receipt = dispatch(repo_root)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["decision"] == "PORTFOLIO_MACHINE_VALIDATION_PASSED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
