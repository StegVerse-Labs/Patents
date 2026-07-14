#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ARXIV = re.compile(r"^arXiv:\d{4}\.\d{4,5}$")
FAMILIES = {"PAT-001", "PAT-005"}


def validate(path: Path) -> dict:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "PRIOR_ART_IDENTIFIERS_INVALID", "errors": [str(exc)]}

    if data.get("decision") not in {
        "PRIOR_ART_IDENTIFIERS_PARTIALLY_VERIFIED",
        "PRIOR_ART_IDENTIFIERS_VERIFIED",
    }:
        errors.append("invalid decision")

    families = data.get("families")
    if not isinstance(families, dict) or set(families) != FAMILIES:
        errors.append("families must contain PAT-001 and PAT-005")
        families = {}

    seen: set[str] = set()
    verified_count = 0
    patent_count = 0
    for family_id, family in families.items():
        refs = family.get("verified_non_patent_references", []) if isinstance(family, dict) else []
        if not isinstance(refs, list):
            errors.append(f"{family_id}.verified_non_patent_references must be an array")
            refs = []
        for index, ref in enumerate(refs):
            identifier = ref.get("identifier") if isinstance(ref, dict) else None
            if not isinstance(identifier, str) or not ARXIV.fullmatch(identifier):
                errors.append(f"{family_id}.reference[{index}].identifier invalid")
                continue
            if identifier in seen:
                errors.append(f"duplicate identifier: {identifier}")
            seen.add(identifier)
            verified_count += 1
            if not ref.get("title") or not ref.get("publication_date") or not ref.get("source"):
                errors.append(f"{family_id}.reference[{index}] missing metadata")
        patents = family.get("verified_patent_publications", []) if isinstance(family, dict) else []
        if not isinstance(patents, list):
            errors.append(f"{family_id}.verified_patent_publications must be an array")
            patents = []
        patent_count += len(patents)
        if not patents and family.get("patent_search_status") != "NO_PUBLICATION_NUMBER_VERIFIED":
            errors.append(f"{family_id}.patent_search_status inconsistent")

    if data.get("decision") == "PRIOR_ART_IDENTIFIERS_VERIFIED" and patent_count == 0:
        errors.append("verified decision requires at least one verified patent publication")

    boundary = data.get("search_boundary", {})
    for key in [
        "absence_is_novelty_evidence",
        "patentability_determined",
        "freedom_to_operate_determined",
        "inventorship_determined",
        "filing_authorized",
        "filing_performed",
        "patent_pending_authorized",
    ]:
        if boundary.get(key) is not False:
            errors.append(f"search_boundary.{key} must be false")

    return {
        "decision": "PRIOR_ART_IDENTIFIERS_VALID" if not errors else "PRIOR_ART_IDENTIFIERS_INVALID",
        "verified_non_patent_count": verified_count,
        "verified_patent_count": patent_count,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    result = validate(args.record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PRIOR_ART_IDENTIFIERS_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
