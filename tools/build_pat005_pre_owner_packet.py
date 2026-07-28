#!/usr/bin/env python3
"""Build the PAT-005 Steps 1-4 preparation packet.

This tool performs only bounded, first-party preparation. It does not determine
inventorship, patentability, ownership, filing strategy, legal deadlines, or
filing authorization. Missing human or practitioner outputs remain explicit
blockers and cause a fail-closed result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

FAMILY_ID = "PAT-005"

SOURCE_FILES = [
    "reviews/PAT-005-filing-readiness-index.md",
    "reviews/PAT-005-practitioner-handoff.md",
    "disclosures/PAT-005-governed-device-continuity.md",
    "provisionals/PAT-005-working-provisional-draft.md",
    "claims/PAT-005-claim-architecture.md",
    "evidence/PAT-005-conception-chronology.md",
    "evidence/PAT-005-cross-repository-source-map.md",
    "evidence/PAT-005-destination-and-guardian-anchors.md",
    "evidence/PAT-005-end-to-end-reconstruction.md",
    "evidence/PAT-005-negative-and-failure-paths.md",
    "prior-art/PAT-005-initial-collision-chart.md",
    "prior-art/PAT-005-limitation-claim-chart.md",
    "inventorship/PAT-005-claim-contribution-worksheet.md",
    "inventorship/PAT-005-contributor-interview-packet.md",
    "diagrams/PAT-005-formal-drawing-sheets.md",
    "diagrams/PAT-005-drawing-production-spec.md",
]

REQUIRED_STEP_OUTPUTS = {
    "step_1_factual_interviews": [
        "inventorship/PAT-005-contributor-interview-packet.md",
        "inventorship/PAT-005-claim-contribution-worksheet.md",
    ],
    "step_2_disclosure_audit": [
        "evidence/PAT-005-public-disclosure-audit.md",
    ],
    "step_3_practitioner_review": [
        "inventorship/PAT-005-inventorship-determination.md",
        "reviews/PAT-005-practitioner-recommendation.md",
    ],
    "step_4_drawing_review": [
        "diagrams/PAT-005-drawing-approval.md",
    ],
}

OWNER_GATE = "reviews/PAT-005-owner-decision.md"

PROHIBITED_ASSERTIONS = [
    "filed: true",
    "patent_pending_authorized: true",
    "patent pending: true",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_file(root: Path, relative_path: str) -> dict[str, Any]:
    path = root / relative_path
    record: dict[str, Any] = {
        "path": relative_path,
        "exists": path.is_file(),
        "sha256": None,
        "size_bytes": None,
        "warnings": [],
    }
    if not path.is_file():
        record["warnings"].append("MISSING")
        return record

    record["sha256"] = sha256(path)
    record["size_bytes"] = path.stat().st_size
    text = path.read_text(encoding="utf-8", errors="replace")
    lowered = text.lower()
    for assertion in PROHIBITED_ASSERTIONS:
        if assertion in lowered:
            record["warnings"].append(f"PROHIBITED_UNVERIFIED_ASSERTION:{assertion}")
    if not text.strip():
        record["warnings"].append("EMPTY_FILE")
    return record


def build(root: Path, output_dir: Path) -> int:
    now = datetime.now(timezone.utc).isoformat()
    source_records = [inspect_file(root, path) for path in SOURCE_FILES]
    output_records = {
        stage: [inspect_file(root, path) for path in paths]
        for stage, paths in REQUIRED_STEP_OUTPUTS.items()
    }
    owner_record = inspect_file(root, OWNER_GATE)

    missing_sources = [r["path"] for r in source_records if not r["exists"]]
    warning_records = [
        r for r in source_records
        if r["warnings"]
    ]
    for records in output_records.values():
        warning_records.extend(r for r in records if r["warnings"])

    stage_status: dict[str, str] = {}
    for stage, records in output_records.items():
        if all(r["exists"] and not r["warnings"] for r in records):
            stage_status[stage] = "OUTPUTS_PRESENT_REVIEW_REQUIRED"
        else:
            stage_status[stage] = "BLOCKED_OR_INCOMPLETE"

    steps_1_4_complete = all(
        value == "OUTPUTS_PRESENT_REVIEW_REQUIRED"
        for value in stage_status.values()
    )

    decision = (
        "READY_FOR_OWNER_DECISION_REVIEW"
        if steps_1_4_complete
        else "FAIL_CLOSED_PRE_OWNER_BLOCKERS"
    )

    manifest = {
        "schema_version": "1.0.0",
        "family_id": FAMILY_ID,
        "generated_utc": now,
        "scope": "STEPS_1_THROUGH_4_PREPARATION_ONLY",
        "decision": decision,
        "legal_boundary": {
            "inventorship_determined_by_tool": False,
            "ownership_determined_by_tool": False,
            "legal_deadline_determined_by_tool": False,
            "filing_authorized_by_tool": False,
            "patent_center_submission_performed": False,
        },
        "source_records": source_records,
        "stage_status": stage_status,
        "required_output_records": output_records,
        "owner_gate": owner_record,
        "missing_source_files": missing_sources,
        "warning_count": len(warning_records),
        "automation_resume_condition": (
            "All Steps 1-4 outputs exist without structural warnings; owner reviews counsel recommendation and records an explicit disposition in reviews/PAT-005-owner-decision.md."
        ),
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "PRE_OWNER_PACKET_MANIFEST.json"
    report_path = output_dir / "PRE_OWNER_READINESS_REPORT.md"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    report_lines = [
        "# PAT-005 Pre-Owner Readiness Report",
        "",
        f"Generated: `{now}`",
        "",
        f"Decision: `{decision}`",
        "",
        "## Stage status",
        "",
    ]
    report_lines.extend(f"- `{stage}`: `{status}`" for stage, status in stage_status.items())
    report_lines.extend([
        "",
        "## Missing source files",
        "",
    ])
    report_lines.extend(f"- `{path}`" for path in missing_sources) if missing_sources else report_lines.append("None.")
    report_lines.extend([
        "",
        "## Boundary",
        "",
        "This report does not determine inventorship, ownership, patentability, filing strategy, disclosure consequences, deadlines, entity status, fees, or filing authorization.",
        "",
        "## Next gate",
        "",
        f"Owner decision record: `{OWNER_GATE}`",
        "",
    ])
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    return 0 if steps_1_4_complete else 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--output-dir",
        default="filing_packets/PAT-005/pre_owner",
        help="Directory for the generated manifest and readiness report",
    )
    args = parser.parse_args()
    return build(Path(args.root).resolve(), Path(args.root).resolve() / args.output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
