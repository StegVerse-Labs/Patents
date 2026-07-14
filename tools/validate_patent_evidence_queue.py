#!/usr/bin/env python3
"""Validate normalized patent evidence-acquisition queues."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

TASK_ID_RE = re.compile(r"^EVID-PAT-\d{3}-[0-9a-f]{12}$")
ALLOWED_CLASSES = {
    "canonical_source_recovery",
    "implementation_anchor_collection",
    "executable_fixture_collection",
    "lifecycle_evidence_collection",
    "prior_art_identifier_verification",
    "authoritative_execution",
    "technical_evidence_collection",
}
EXTERNAL_REQUIRED = {"canonical_source_recovery", "prior_art_identifier_verification"}


def validate(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_EVIDENCE_QUEUE", "errors": [str(exc)]}

    if data.get("decision") != "EVIDENCE_QUEUE_READY":
        errors.append("decision must be EVIDENCE_QUEUE_READY")
    queue = data.get("queue")
    if not isinstance(queue, list):
        errors.append("queue must be an array")
        queue = []

    seen: set[str] = set()
    for index, item in enumerate(queue):
        if not isinstance(item, dict):
            errors.append(f"queue[{index}] must be an object")
            continue
        task_id = item.get("task_id")
        if not isinstance(task_id, str) or not TASK_ID_RE.fullmatch(task_id):
            errors.append(f"queue[{index}].task_id invalid")
        elif task_id in seen:
            errors.append(f"duplicate task_id: {task_id}")
        else:
            seen.add(task_id)
        if not isinstance(item.get("family_id"), str) or not item["family_id"].startswith("PAT-"):
            errors.append(f"queue[{index}].family_id invalid")
        if not isinstance(item.get("priority"), int) or item["priority"] < 1:
            errors.append(f"queue[{index}].priority invalid")
        if not isinstance(item.get("task"), str) or not item["task"].strip():
            errors.append(f"queue[{index}].task missing")
        evidence_class = item.get("evidence_class")
        if evidence_class not in ALLOWED_CLASSES:
            errors.append(f"queue[{index}].evidence_class invalid")
        expected_external = evidence_class in EXTERNAL_REQUIRED
        if item.get("external_verification_required") is not expected_external:
            errors.append(f"queue[{index}].external_verification_required inconsistent")
        if not isinstance(item.get("completion_predicate"), str) or not item["completion_predicate"].strip():
            errors.append(f"queue[{index}].completion_predicate missing")
        if item.get("status") not in {"open", "in_progress", "complete", "blocked"}:
            errors.append(f"queue[{index}].status invalid")
        if item.get("claimed_legal_effect") is not False:
            errors.append(f"queue[{index}].claimed_legal_effect must be false")

    boundary = data.get("authority_boundary")
    required_false = {
        "inventorship_determined",
        "patentability_determined",
        "filing_authorized",
        "filing_performed",
        "patent_pending_authorized",
    }
    if not isinstance(boundary, dict):
        errors.append("authority_boundary must be an object")
    else:
        for key in sorted(required_false):
            if boundary.get(key) is not False:
                errors.append(f"authority_boundary.{key} must be false")

    return {
        "decision": "EVIDENCE_QUEUE_VALID" if not errors else "INVALID_EVIDENCE_QUEUE",
        "task_count": len(queue),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("queue", type=Path)
    args = parser.parse_args()
    result = validate(args.queue)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "EVIDENCE_QUEUE_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
