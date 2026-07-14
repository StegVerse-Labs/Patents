#!/usr/bin/env python3
"""Validate fail-closed canonical-source search receipts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ALLOWED_RESULTS = {
    "REFERENCES_ONLY",
    "NO_COMMIT_MATCH",
    "PATENTS_REFERENCE_ONLY_WITH_UNRELATED_EXTERNAL_MATCHES",
    "CANONICAL_SOURCE_MATCH",
}


def validate(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_SOURCE_SEARCH_RECEIPT", "errors": [str(exc)]}

    if data.get("family_id") != "PAT-001":
        errors.append("family_id must be PAT-001")
    queries = data.get("queries")
    if not isinstance(queries, list) or not queries:
        errors.append("queries must be a non-empty array")
        queries = []
    seen: set[tuple[str, str]] = set()
    canonical_match = False
    for index, item in enumerate(queries):
        if not isinstance(item, dict):
            errors.append(f"queries[{index}] must be an object")
            continue
        query = item.get("query")
        scope = item.get("scope")
        result = item.get("result")
        if not isinstance(query, str) or not query.strip():
            errors.append(f"queries[{index}].query missing")
        if not isinstance(scope, str) or not scope.strip():
            errors.append(f"queries[{index}].scope missing")
        key = (str(query), str(scope))
        if key in seen:
            errors.append(f"duplicate query/scope pair: {key}")
        seen.add(key)
        if result not in ALLOWED_RESULTS:
            errors.append(f"queries[{index}].result invalid")
        canonical_match = canonical_match or result == "CANONICAL_SOURCE_MATCH"
        if not isinstance(item.get("matched_paths"), list):
            errors.append(f"queries[{index}].matched_paths must be an array")

    verified = bool(data.get("canonical_june_6_source_verified")) or bool(data.get("canonical_june_16_source_verified"))
    expected_decision = "CANONICAL_SOURCE_RECOVERED" if verified else "CANONICAL_SOURCE_NOT_RECOVERED"
    if data.get("decision") != expected_decision:
        errors.append("decision inconsistent with verification flags")
    if verified and not canonical_match:
        errors.append("verified source requires CANONICAL_SOURCE_MATCH evidence")
    if not verified and data.get("negative_evidence_preserved") is not True:
        errors.append("negative_evidence_preserved must be true while unresolved")
    if not isinstance(data.get("retry_triggers"), list) or not data["retry_triggers"]:
        errors.append("retry_triggers must be non-empty")

    boundary = data.get("authority_boundary")
    if not isinstance(boundary, dict):
        errors.append("authority_boundary must be an object")
    else:
        for key in (
            "conception_date_determined",
            "inventorship_determined",
            "patentability_determined",
            "filing_authorized",
            "patent_pending_authorized",
        ):
            if boundary.get(key) is not False:
                errors.append(f"authority_boundary.{key} must be false")

    return {
        "decision": "SOURCE_SEARCH_RECEIPT_VALID" if not errors else "INVALID_SOURCE_SEARCH_RECEIPT",
        "query_count": len(queries),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    result = validate(args.receipt)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "SOURCE_SEARCH_RECEIPT_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
