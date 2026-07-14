#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SHA40 = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_NEGATIVES = {
    "default_expiry",
    "usage_only_delayed_expiry_or_lease",
    "bounded_context_reuse",
    "heartbeat_non_self_retention",
    "demand_only_node_construction_when_no_admissible_node_exists",
    "active_capability_resolution",
}
ALLOWED_NEGATIVE_STATUS = {
    "NOT_IMPLEMENTED_IN_INSPECTED_SURFACE",
    "NOT_ESTABLISHED_BY_INSPECTED_SURFACE",
    "PARTIALLY_SUPPORTED_ONLY",
}


def validate(path: Path) -> dict:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_PAT001_LIFECYCLE_EVIDENCE", "errors": [str(exc)]}
    if data.get("family_id") != "PAT-001":
        errors.append("family_id must be PAT-001")
    if data.get("decision") != "LIFECYCLE_EVIDENCE_PARTIAL_WITH_EXPLICIT_NEGATIVES":
        errors.append("invalid decision")
    if not SHA40.fullmatch(str(data.get("inspected_commit", ""))):
        errors.append("inspected_commit invalid")
    anchors = data.get("positive_anchors", [])
    if not isinstance(anchors, list) or len(anchors) < 2:
        errors.append("at least two positive anchors required")
        anchors = []
    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict) or not anchor.get("path"):
            errors.append(f"positive_anchors[{index}].path missing")
            continue
        if not SHA40.fullmatch(str(anchor.get("blob_sha", ""))):
            errors.append(f"positive_anchors[{index}].blob_sha invalid")
        if not isinstance(anchor.get("supports"), list) or not anchor["supports"]:
            errors.append(f"positive_anchors[{index}].supports missing")
    negatives = data.get("explicit_negative_findings", [])
    limitations = set()
    for index, finding in enumerate(negatives if isinstance(negatives, list) else []):
        limitation = finding.get("limitation") if isinstance(finding, dict) else None
        if limitation in limitations:
            errors.append(f"duplicate limitation: {limitation}")
        limitations.add(limitation)
        if finding.get("status") not in ALLOWED_NEGATIVE_STATUS:
            errors.append(f"explicit_negative_findings[{index}].status invalid")
        if not finding.get("basis"):
            errors.append(f"explicit_negative_findings[{index}].basis missing")
    missing = sorted(REQUIRED_NEGATIVES - limitations)
    if missing:
        errors.append(f"missing explicit negative findings: {missing}")
    if not data.get("retry_triggers"):
        errors.append("retry_triggers required")
    boundary = data.get("authority_boundary", {})
    for key in ["inventorship_determined", "patentability_determined", "filing_authorized", "filing_performed", "patent_pending_authorized"]:
        if boundary.get(key) is not False:
            errors.append(f"authority_boundary.{key} must be false")
    return {
        "decision": "PAT001_LIFECYCLE_EVIDENCE_VALID" if not errors else "INVALID_PAT001_LIFECYCLE_EVIDENCE",
        "positive_anchor_count": len(anchors),
        "negative_finding_count": len(limitations),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    result = validate(args.record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PAT001_LIFECYCLE_EVIDENCE_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
