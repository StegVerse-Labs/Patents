#!/usr/bin/env python3
"""Build a normalized evidence-acquisition queue from active patent completion records.

The queue admits repository research, source corroboration, fixture collection,
render validation, and externally verified search preparation. It never admits
inventorship, practitioner judgment, filing authorization, signature, payment,
submission, or patent-pending decisions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROHIBITED = {
    "inventor", "inventorship", "practitioner", "counsel", "approve",
    "authorization", "authorize", "signature", "payment", "file", "filing",
    "submit", "patent pending", "foreign filing", "legal determination",
}

CLASSIFIERS: list[tuple[str, tuple[str, ...]]] = [
    ("canonical_source_recovery", ("canonical", "source repositories", "commit anchors")),
    ("implementation_anchor_collection", ("implementation commit anchors", "validator and test paths", "source implementation")),
    ("executable_fixture_collection", ("executable evidence", "negative fixture", "failure fixture", "validator fixture")),
    ("lifecycle_evidence_collection", ("expiry", "usage lease", "context retention", "heartbeat")),
    ("prior_art_identifier_verification", ("prior art", "patent and non-patent")),
    ("authoritative_execution", ("authoritative execution", "canonical portfolio entry point", "dispatcher")),
]


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _task_id(family_id: str, task: str) -> str:
    digest = hashlib.sha256(f"{family_id}\0{task}".encode("utf-8")).hexdigest()[:12]
    return f"EVID-{family_id}-{digest}"


def _classify(task: str) -> str:
    lowered = task.lower()
    for evidence_class, tokens in CLASSIFIERS:
        if any(token in lowered for token in tokens):
            return evidence_class
    return "technical_evidence_collection"


def _external_verification_required(evidence_class: str) -> bool:
    return evidence_class in {"prior_art_identifier_verification", "canonical_source_recovery"}


def _completion_predicate(evidence_class: str) -> str:
    predicates = {
        "canonical_source_recovery": "exact repository, commit SHA, path, blob SHA, and source-date relevance recorded",
        "implementation_anchor_collection": "exact repository, commit SHA, path, and executable validation surface recorded",
        "executable_fixture_collection": "fixture path, expected outcome, validator path, and reproducible receipt recorded",
        "lifecycle_evidence_collection": "implementation or explicit negative evidence recorded for each lifecycle limitation",
        "prior_art_identifier_verification": "stable publication identifiers and source database metadata recorded",
        "authoritative_execution": "canonical runner receipt committed with synchronized status and continuation hashes",
        "technical_evidence_collection": "repository-bound artifact and verification result recorded",
    }
    return predicates[evidence_class]


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("family_id"), str):
        raise ValueError(f"invalid completion record: {path}")
    return data


def build_queue(status_files: list[Path]) -> dict[str, Any]:
    tasks: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []
    errors: list[str] = []
    seen: set[str] = set()

    for path in status_files:
        try:
            record = _load(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(str(exc))
            continue
        family_id = record["family_id"]
        for position, raw_task in enumerate(record.get("next_machine_tasks", []), start=1):
            task = " ".join(str(raw_task).split())
            lowered = task.lower()
            item_id = _task_id(family_id, task)
            if any(term in lowered for term in PROHIBITED):
                excluded.append({"task_id": item_id, "family_id": family_id, "task": task, "reason": "non_delegable_boundary"})
                continue
            if item_id in seen:
                continue
            seen.add(item_id)
            evidence_class = _classify(task)
            tasks.append({
                "task_id": item_id,
                "family_id": family_id,
                "priority": position,
                "task": task,
                "task_slug": _slug(task),
                "evidence_class": evidence_class,
                "external_verification_required": _external_verification_required(evidence_class),
                "completion_predicate": _completion_predicate(evidence_class),
                "status": "open",
                "claimed_legal_effect": False,
            })

    tasks.sort(key=lambda item: (item["priority"], item["family_id"], item["task_id"]))
    decision = "EVIDENCE_QUEUE_READY" if not errors else "INVALID_EVIDENCE_QUEUE_SOURCE"
    return {
        "schema_version": "1.0",
        "generated_at": _utc_now(),
        "decision": decision,
        "queue": tasks,
        "excluded": excluded,
        "errors": errors,
        "authority_boundary": {
            "inventorship_determined": False,
            "patentability_determined": False,
            "filing_authorized": False,
            "filing_performed": False,
            "patent_pending_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("status_files", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/patent-evidence-acquisition-queue.json"))
    args = parser.parse_args()
    result = build_queue(args.status_files)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "EVIDENCE_QUEUE_READY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
