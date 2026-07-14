#!/usr/bin/env python3
"""Validate machine-readable patent completion records against repository state.

This tool never files, submits, signs, pays, or authorizes a patent application.
It verifies internal consistency and fails closed when required artifacts or
status invariants are missing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_BOOLEAN_FIELDS = ("filed", "patent_pending_authorized")


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("completion record must be a JSON object")
    return data


def validate_record(repo_root: Path, record_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        record = _load(record_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return {"decision": "INVALID_COMPLETION_RECORD", "errors": [str(exc)], "warnings": []}

    family_id = record.get("family_id")
    if not isinstance(family_id, str) or not family_id.startswith("PAT-"):
        errors.append("family_id must be a PAT-* string")

    for field in REQUIRED_BOOLEAN_FIELDS:
        if not isinstance(record.get(field), bool):
            errors.append(f"{field} must be boolean")

    if record.get("patent_pending_authorized") and not record.get("filed"):
        errors.append("patent_pending_authorized cannot be true while filed is false")

    completed = record.get("completed")
    blockers = record.get("blocking_gates")
    if not isinstance(completed, dict) or not completed:
        errors.append("completed must be a non-empty object")
    if not isinstance(blockers, dict) or not blockers:
        errors.append("blocking_gates must be a non-empty object")

    artifact_map = record.get("artifact_map", {})
    if artifact_map and not isinstance(artifact_map, dict):
        errors.append("artifact_map must be an object when present")
    elif isinstance(artifact_map, dict):
        for completion_key, relative_path in artifact_map.items():
            if not isinstance(relative_path, str):
                errors.append(f"artifact_map.{completion_key} must be a string path")
                continue
            exists = (repo_root / relative_path).is_file()
            declared_complete = bool(completed.get(completion_key)) if isinstance(completed, dict) else False
            if declared_complete and not exists:
                errors.append(f"completed artifact missing: {completion_key} -> {relative_path}")
            if exists and not declared_complete:
                warnings.append(f"artifact exists but completion flag is false: {completion_key}")

    unresolved = []
    if isinstance(blockers, dict):
        unresolved = sorted(key for key, value in blockers.items() if value is not True)

    expected = record.get("expected_decision")
    if unresolved and expected not in (None, "FAIL_CLOSED_BLOCKERS"):
        errors.append("expected_decision must fail closed while blocking gates remain")
    if not unresolved and expected == "FAIL_CLOSED_BLOCKERS":
        warnings.append("all blockers are true but expected_decision remains fail closed")

    decision = "VALID_FAIL_CLOSED" if unresolved and not errors else "VALID_NO_BLOCKERS"
    if errors:
        decision = "INVALID_COMPLETION_RECORD"

    return {
        "family_id": family_id,
        "decision": decision,
        "unresolved_blocking_gates": unresolved,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()

    result = validate_record(args.repo_root.resolve(), args.record.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] != "INVALID_COMPLETION_RECORD" else 2


if __name__ == "__main__":
    raise SystemExit(main())
