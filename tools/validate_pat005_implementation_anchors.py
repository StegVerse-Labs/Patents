#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SHA40 = re.compile(r"^[0-9a-f]{40}$")
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED_TYPES = {
    "executable_builder",
    "executable_validator",
    "acceptance_fixture",
    "contract",
    "receipt",
    "boundary_document",
}
EXECUTABLE_TYPES = {"executable_builder", "executable_validator", "acceptance_fixture"}


def validate(path: Path) -> dict:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_PAT005_IMPLEMENTATION_ANCHORS", "errors": [str(exc)]}

    if data.get("family_id") != "PAT-005":
        errors.append("family_id must be PAT-005")
    if data.get("decision") not in {"IMPLEMENTATION_ANCHORS_PARTIALLY_VERIFIED", "IMPLEMENTATION_ANCHORS_VERIFIED"}:
        errors.append("invalid decision")

    anchors = data.get("anchors")
    if not isinstance(anchors, list) or not anchors:
        errors.append("anchors must be a non-empty array")
        anchors = []

    seen: set[tuple[str, str, str]] = set()
    repositories: set[str] = set()
    executable_repositories: set[str] = set()
    guardian_boundary_present = False
    guardian_receipt_present = False

    for index, item in enumerate(anchors):
        if not isinstance(item, dict):
            errors.append(f"anchors[{index}] must be an object")
            continue

        repository = item.get("repository")
        commit = item.get("commit")
        path_value = item.get("path")
        anchor_type = item.get("anchor_type")

        if not isinstance(repository, str) or not REPOSITORY.fullmatch(repository):
            errors.append(f"anchors[{index}].repository invalid")
        else:
            repositories.add(repository)
            if anchor_type in EXECUTABLE_TYPES:
                executable_repositories.add(repository)

        if not SHA40.fullmatch(str(commit or "")):
            errors.append(f"anchors[{index}].commit invalid")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"anchors[{index}].path missing")

        key = (str(repository), str(commit), str(path_value))
        if key in seen:
            errors.append(f"duplicate anchor: {key}")
        else:
            seen.add(key)

        if not SHA40.fullmatch(str(item.get("blob_sha", ""))):
            errors.append(f"anchors[{index}].blob_sha invalid")
        if anchor_type not in ALLOWED_TYPES:
            errors.append(f"anchors[{index}].anchor_type invalid")

        supports = item.get("supports")
        if not isinstance(supports, list) or not supports:
            errors.append(f"anchors[{index}].supports missing")

        if repository == "StegVerse-002/stegguardian-wiki":
            if anchor_type == "boundary_document":
                guardian_boundary_present = True
            if anchor_type == "receipt":
                guardian_receipt_present = True
            if anchor_type in EXECUTABLE_TYPES:
                errors.append("Guardian wiki evidence must not be classified as executable authority")

    if data.get("decision") == "IMPLEMENTATION_ANCHORS_VERIFIED":
        if len(repositories) < 4:
            errors.append("verified decision requires source, two destination repositories, and Guardian evidence")
        if len(executable_repositories) < 3:
            errors.append("verified decision requires executable source plus two executable destination repositories")
        if not guardian_boundary_present or not guardian_receipt_present:
            errors.append("verified decision requires Guardian boundary document and receipt")

    boundary = data.get("authority_boundary")
    for key in [
        "inventorship_determined",
        "patentability_determined",
        "filing_authorized",
        "filing_performed",
        "patent_pending_authorized",
    ]:
        if not isinstance(boundary, dict) or boundary.get(key) is not False:
            errors.append(f"authority_boundary.{key} must be false")

    return {
        "decision": "PAT005_IMPLEMENTATION_ANCHORS_VALID" if not errors else "INVALID_PAT005_IMPLEMENTATION_ANCHORS",
        "anchor_count": len(anchors),
        "repository_count": len(repositories),
        "executable_repository_count": len(executable_repositories),
        "guardian_boundary_present": guardian_boundary_present,
        "guardian_receipt_present": guardian_receipt_present,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    result = validate(args.record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PAT005_IMPLEMENTATION_ANCHORS_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
