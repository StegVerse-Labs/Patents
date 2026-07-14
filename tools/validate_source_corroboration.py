#!/usr/bin/env python3
"""Validate cross-repository patent corroboration records.

The validator checks record structure, duplicate anchors, commit/blob identifiers,
limitation classifications, and authority boundaries. It does not determine
inventorship, patentability, priority, filing authority, or patent-pending status.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_SUPPORT = {"implemented_policy", "executable_schema", "architecture_reference", "runtime_evidence"}


def validate_record(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_CORROBORATION_RECORD", "errors": [str(exc)], "warnings": []}

    if not isinstance(data, dict):
        return {"decision": "INVALID_CORROBORATION_RECORD", "errors": ["record must be an object"], "warnings": []}
    if not isinstance(data.get("family_id"), str) or not data["family_id"].startswith("PAT-"):
        errors.append("family_id must be PAT-* string")

    anchors = data.get("anchors")
    if not isinstance(anchors, list) or not anchors:
        errors.append("anchors must be a non-empty array")
        anchors = []

    seen_ids: set[str] = set()
    seen_sources: set[tuple[str, str, str]] = set()
    supported_union: set[str] = set()
    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict):
            errors.append(f"anchor[{index}] must be an object")
            continue
        anchor_id = anchor.get("anchor_id")
        if not isinstance(anchor_id, str) or not anchor_id:
            errors.append(f"anchor[{index}].anchor_id missing")
        elif anchor_id in seen_ids:
            errors.append(f"duplicate anchor_id: {anchor_id}")
        else:
            seen_ids.add(anchor_id)

        repo = anchor.get("repository")
        commit = anchor.get("commit_sha")
        source_path = anchor.get("path")
        blob = anchor.get("blob_sha")
        if not isinstance(repo, str) or "/" not in repo:
            errors.append(f"anchor[{index}].repository invalid")
        if not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
            errors.append(f"anchor[{index}].commit_sha must be lowercase 40-character SHA")
        if not isinstance(blob, str) or not SHA_RE.fullmatch(blob):
            errors.append(f"anchor[{index}].blob_sha must be lowercase 40-character SHA")
        if not isinstance(source_path, str) or not source_path or source_path.startswith("/"):
            errors.append(f"anchor[{index}].path invalid")
        if isinstance(repo, str) and isinstance(commit, str) and isinstance(source_path, str):
            source_key = (repo, commit, source_path)
            if source_key in seen_sources:
                errors.append(f"duplicate source anchor: {repo}@{commit}:{source_path}")
            seen_sources.add(source_key)

        support = anchor.get("support_level")
        if support not in ALLOWED_SUPPORT:
            errors.append(f"anchor[{index}].support_level invalid")
        limitations = anchor.get("supported_limitations")
        if not isinstance(limitations, list) or not limitations or not all(isinstance(x, str) and x for x in limitations):
            errors.append(f"anchor[{index}].supported_limitations must be non-empty strings")
        else:
            supported_union.update(limitations)
        exclusions = anchor.get("does_not_establish")
        if not isinstance(exclusions, list) or not all(isinstance(x, str) and x for x in exclusions):
            errors.append(f"anchor[{index}].does_not_establish must be strings")

    declared = data.get("corroborated_limitations")
    if not isinstance(declared, list) or not all(isinstance(x, str) and x for x in declared):
        errors.append("corroborated_limitations must be an array of strings")
        declared_set: set[str] = set()
    else:
        declared_set = set(declared)
        missing_from_anchors = sorted(declared_set - supported_union)
        if missing_from_anchors:
            errors.append("declared corroborated limitations lack anchor support: " + ", ".join(missing_from_anchors))
        unlisted_support = sorted(supported_union - declared_set)
        if unlisted_support:
            warnings.append("anchor-supported limitations not listed as corroborated: " + ", ".join(unlisted_support))

    uncorroborated = data.get("still_uncorroborated")
    if not isinstance(uncorroborated, list) or not all(isinstance(x, str) and x for x in uncorroborated):
        errors.append("still_uncorroborated must be an array of strings")
    elif declared_set.intersection(uncorroborated):
        errors.append("a limitation cannot be both corroborated and still_uncorroborated")

    boundary = data.get("authority_boundary")
    if not isinstance(boundary, dict):
        errors.append("authority_boundary must be an object")
    else:
        required_false = {
            "inventorship_determined",
            "patentability_determined",
            "priority_date_determined",
            "filing_authorized",
            "patent_pending_authorized",
        }
        for key in required_false:
            if boundary.get(key) is not False:
                errors.append(f"authority_boundary.{key} must remain false")

    decision = "CORROBORATION_RECORD_VALID" if not errors else "INVALID_CORROBORATION_RECORD"
    return {
        "family_id": data.get("family_id"),
        "decision": decision,
        "anchor_count": len(anchors),
        "corroborated_limitation_count": len(declared_set),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    result = validate_record(args.record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "CORROBORATION_RECORD_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
