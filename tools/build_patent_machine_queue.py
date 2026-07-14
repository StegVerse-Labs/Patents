#!/usr/bin/env python3
"""Build the next authorized machine-work queue from patent completion records.

Human, practitioner, approval, payment, signature, inventorship, and filing tasks
are never admitted to the machine queue.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROHIBITED_TERMS = {
    "inventorship",
    "inventor",
    "contributor interview",
    "practitioner",
    "counsel",
    "approve",
    "approval",
    "authorize",
    "authorization",
    "file",
    "filing",
    "submit",
    "signature",
    "payment",
    "fee payment",
    "patent pending",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("family_id"), str):
        raise ValueError(f"invalid completion record: {path}")
    return data


def is_machine_authorized(task: str) -> bool:
    normalized = " ".join(task.lower().split())
    return bool(normalized) and not any(term in normalized for term in PROHIBITED_TERMS)


def build_queue(status_files: list[Path]) -> dict[str, Any]:
    queue: list[dict[str, str]] = []
    excluded: list[dict[str, str]] = []
    errors: list[str] = []

    for path in status_files:
        try:
            record = _load(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
            continue
        family_id = record["family_id"]
        for task in record.get("next_machine_tasks", []):
            task_text = str(task).strip()
            item = {"family_id": family_id, "task": task_text}
            if is_machine_authorized(task_text):
                queue.append(item)
            else:
                excluded.append({**item, "reason": "human_or_legal_boundary"})

    decision = "MACHINE_QUEUE_READY" if not errors else "INVALID_MACHINE_QUEUE_SOURCE"
    return {
        "schema_version": "1.0",
        "generated_at": _utc_now(),
        "decision": decision,
        "queue": queue,
        "excluded": excluded,
        "errors": errors,
        "authority_boundary": {
            "human_tasks_admitted": False,
            "filing_tasks_admitted": False,
            "inventorship_tasks_admitted": False,
            "approval_tasks_admitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status_files", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/patent-machine-queue.json"))
    args = parser.parse_args()
    result = build_queue(args.status_files)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "MACHINE_QUEUE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
