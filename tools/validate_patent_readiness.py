#!/usr/bin/env python3
"""Deterministic patent-family filing-readiness validator.

This tool validates repository readiness records only. It never files, submits,
certifies, or authorizes a patent application.

Usage:
    python tools/validate_patent_readiness.py --family PAT-001 --root .

Exit codes:
    0  READY_FOR_REVIEW_PACKET
    2  FAIL_CLOSED_BLOCKERS
    3  INVALID_READINESS_RECORD
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from dataclasses import dataclass, asdict
from typing import Iterable

SIG = "patent-readiness-validation:v1"


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: str
    detail: str


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def readiness_path(root: pathlib.Path, family: str) -> pathlib.Path:
    return root / "filing-readiness" / f"{family}_FILING_READINESS_INDEX.md"


def parse_checkboxes(text: str) -> list[tuple[bool, str]]:
    matches = re.findall(r"^\s*- \[([ xX])\]\s+(.+?)\s*$", text, re.MULTILINE)
    return [(mark.lower() == "x", label.strip()) for mark, label in matches]


def extract_disposition(text: str, label: str) -> str | None:
    pattern = rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip().lower() if match else None


def required_family_artifacts(root: pathlib.Path, family: str) -> Iterable[pathlib.Path]:
    if family == "PAT-001":
        relative = [
            "evidence/PAT-001_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md",
            "evidence/PAT-001_CLAIM_ELEMENT_EVIDENCE_MAP.md",
            "evidence/PAT-001_INVENTORSHIP_WORKSHEET.md",
            "evidence/PAT-001_PRIOR_ART_SEARCH_LEDGER.md",
            "provisionals/PAT-001_provisional.md",
            "figures/PAT-001_FIGURE_DESCRIPTIONS.md",
            "diagrams/PAT-001-formal-drawing-sheets.md",
            "docs/FILING_PACKET_SPEC.md",
            "tools/filing_packet_emitter.py",
        ]
    else:
        relative = []
    return [root / item for item in relative]


def validate(root: pathlib.Path, family: str) -> tuple[dict, int]:
    index = readiness_path(root, family)
    checks: list[CheckResult] = []

    if not index.exists():
        report = {
            "sig": SIG,
            "family": family,
            "decision": "INVALID_READINESS_RECORD",
            "checks": [asdict(CheckResult("readiness-index", "FAIL", f"missing {index}"))],
        }
        return report, 3

    text = index.read_text(encoding="utf-8")
    checkboxes = parse_checkboxes(text)
    if not checkboxes:
        checks.append(CheckResult("blocking-checkboxes", "FAIL", "no blocking checkboxes found"))
    else:
        open_items = [label for complete, label in checkboxes if not complete]
        checks.append(CheckResult(
            "blocking-checkboxes",
            "PASS" if not open_items else "FAIL",
            "all blocking items resolved" if not open_items else f"{len(open_items)} unresolved blocking items",
        ))

    missing_artifacts: list[str] = []
    artifact_hashes: list[dict[str, str]] = []
    for artifact in required_family_artifacts(root, family):
        if not artifact.exists():
            missing_artifacts.append(str(artifact.relative_to(root)))
        else:
            artifact_hashes.append({
                "path": str(artifact.relative_to(root)),
                "sha256": sha256_file(artifact),
            })
    checks.append(CheckResult(
        "required-artifacts",
        "PASS" if not missing_artifacts else "FAIL",
        "all required artifacts present" if not missing_artifacts else "missing: " + ", ".join(missing_artifacts),
    ))

    packet_authorized = extract_disposition(text, "Review packet authorized")
    filed = extract_disposition(text, "Filed")
    patent_pending = extract_disposition(text, "Patent pending language authorized")

    checks.append(CheckResult(
        "packet-authorization",
        "PASS" if packet_authorized == "yes" else "FAIL",
        f"review packet authorized={packet_authorized or 'missing'}",
    ))
    checks.append(CheckResult(
        "filing-boundary",
        "PASS" if filed in {"no", "yes"} and patent_pending in {"no", "yes"} else "FAIL",
        f"filed={filed or 'missing'}; patent_pending_authorized={patent_pending or 'missing'}",
    ))

    invalid = any(check.check_id == "blocking-checkboxes" and check.detail == "no blocking checkboxes found" for check in checks)
    if invalid:
        decision, exit_code = "INVALID_READINESS_RECORD", 3
    elif any(check.status == "FAIL" for check in checks):
        decision, exit_code = "FAIL_CLOSED_BLOCKERS", 2
    else:
        decision, exit_code = "READY_FOR_REVIEW_PACKET", 0

    report = {
        "sig": SIG,
        "family": family,
        "decision": decision,
        "readiness_index": str(index.relative_to(root)),
        "readiness_index_sha256": sha256_file(index),
        "checks": [asdict(check) for check in checks],
        "unresolved_items": [label for complete, label in checkboxes if not complete],
        "artifact_hashes": artifact_hashes,
        "boundary": {
            "review_packet_authorized": packet_authorized,
            "filed": filed,
            "patent_pending_language_authorized": patent_pending,
            "external_submission_performed": False,
        },
    }
    return report, exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    report, exit_code = validate(root, args.family)
    encoded = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output = pathlib.Path(args.output)
        if not output.is_absolute():
            output = root / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
