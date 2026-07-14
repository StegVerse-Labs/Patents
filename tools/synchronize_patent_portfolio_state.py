#!/usr/bin/env python3
"""Synchronize patent portfolio machine state from one dispatcher receipt.

This tool updates repository-local machine-readable continuation records only.
It never files, signs, pays, determines inventorship, approves drawings,
authorizes a review packet, or permits patent-pending representations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_object(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object: {path}")
    return data


def synchronize(repo_root: Path, receipt_path: Path) -> dict[str, Any]:
    receipt = _load_object(receipt_path)
    decision = receipt.get("decision")
    if decision not in {
        "PORTFOLIO_MACHINE_VALIDATION_PASSED",
        "PORTFOLIO_MACHINE_VALIDATION_FAILED",
    }:
        raise ValueError("unsupported dispatcher decision")

    queue = receipt.get("machine_queue")
    if not isinstance(queue, dict):
        raise ValueError("dispatcher receipt missing machine_queue")
    tasks = queue.get("queue", [])
    if not isinstance(tasks, list):
        raise ValueError("machine_queue.queue must be an array")
    if any(not isinstance(item, dict) for item in tasks):
        raise ValueError("machine_queue.queue entries must be objects")

    workstream_decision = receipt.get("workstream_decision")
    if workstream_decision not in {
        "CONTINUE_ACTIVE_PATENT_WORK",
        "REVIEW_ECOSYSTEM_CANDIDATES",
        "INVALID_PORTFOLIO_STATE",
    }:
        raise ValueError("unsupported workstream decision")

    generated_at = _utc_now()
    receipt_relative = str(receipt_path.resolve().relative_to(repo_root.resolve()))
    receipt_hash = _sha256(receipt_path)
    failed_checks = receipt.get("failed_checks", [])
    if not isinstance(failed_checks, list):
        raise ValueError("failed_checks must be an array")

    status = {
        "schema_version": "2.0",
        "generated_at": generated_at,
        "decision": workstream_decision,
        "dispatcher_decision": decision,
        "dispatcher_receipt": receipt_relative,
        "dispatcher_receipt_sha256": receipt_hash,
        "machine_task_count": len(tasks),
        "machine_tasks": tasks,
        "failed_checks": failed_checks,
        "candidate_review_armed": True,
        "candidate_review_active": workstream_decision == "REVIEW_ECOSYSTEM_CANDIDATES",
        "authority_boundary": {
            "filing_performed": False,
            "filing_authorized": False,
            "inventorship_determined": False,
            "drawing_approval_granted": False,
            "patent_pending_authorized": False,
        },
    }

    continuation = {
        "schema_version": "1.0",
        "generated_at": generated_at,
        "source_receipt": receipt_relative,
        "source_receipt_sha256": receipt_hash,
        "portfolio_decision": workstream_decision,
        "dispatcher_decision": decision,
        "next_machine_task": tasks[0] if tasks else None,
        "remaining_machine_task_count": len(tasks),
        "failed_checks": failed_checks,
        "manual_reconciliation_required": False,
        "non_delegable_transitions": [
            "contributor factual testimony",
            "inventorship determination",
            "qualified practitioner legal review",
            "drawing approval",
            "packet authorization",
            "signature and fee payment",
            "filing submission",
            "patent-pending representation",
        ],
    }

    return {"status": status, "continuation": continuation}


def write_synchronized_state(
    repo_root: Path,
    receipt_path: Path,
    status_output: Path,
    continuation_output: Path,
) -> dict[str, Any]:
    result = synchronize(repo_root, receipt_path)
    status_output.parent.mkdir(parents=True, exist_ok=True)
    continuation_output.parent.mkdir(parents=True, exist_ok=True)
    status_output.write_text(json.dumps(result["status"], indent=2, sort_keys=True) + "\n", encoding="utf-8")
    continuation_output.write_text(
        json.dumps(result["continuation"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument(
        "--receipt",
        type=Path,
        default=Path("receipts/patent-portfolio-dispatch.json"),
    )
    parser.add_argument(
        "--status-output",
        type=Path,
        default=Path("data/patent-workstream-status.json"),
    )
    parser.add_argument(
        "--continuation-output",
        type=Path,
        default=Path("continuation/patent-portfolio-machine-continuation.json"),
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    receipt_path = args.receipt if args.receipt.is_absolute() else repo_root / args.receipt
    status_output = args.status_output if args.status_output.is_absolute() else repo_root / args.status_output
    continuation_output = (
        args.continuation_output
        if args.continuation_output.is_absolute()
        else repo_root / args.continuation_output
    )
    result = write_synchronized_state(repo_root, receipt_path, status_output, continuation_output)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
