#!/usr/bin/env python3
"""Render patent-family working drafts from data/master_claims.json.

This script intentionally produces review artifacts only. It does not file,
publish, or submit anything to a patent office.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "master_claims.json"
DEFAULT_OUTPUT = ROOT / "generated" / "families"


def load_data(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_cross_references(data)
    return data


def validate_cross_references(data: dict[str, Any]) -> None:
    clauses = {item["clause_id"] for item in data.get("shared_clauses", [])}
    families = {item["family_id"] for item in data.get("families", [])}
    claims = {item["claim_id"] for item in data.get("claims", [])}

    duplicates = []
    for label, values, records, key in (
        ("clause", clauses, data.get("shared_clauses", []), "clause_id"),
        ("family", families, data.get("families", []), "family_id"),
        ("claim", claims, data.get("claims", []), "claim_id"),
    ):
        if len(values) != len(records):
            duplicates.append(label)
    if duplicates:
        raise ValueError(f"duplicate identifiers detected: {', '.join(duplicates)}")

    for family in data.get("families", []):
        missing_clauses = set(family.get("shared_clause_ids", [])) - clauses
        missing_claims = set(family.get("claim_ids", [])) - claims
        missing_parents = set(family.get("parent_family_ids", [])) - families
        if missing_clauses or missing_claims or missing_parents:
            raise ValueError(
                f"invalid references in {family['family_id']}: "
                f"clauses={sorted(missing_clauses)}, "
                f"claims={sorted(missing_claims)}, "
                f"parents={sorted(missing_parents)}"
            )

    for claim in data.get("claims", []):
        if claim["family_id"] not in families:
            raise ValueError(f"claim {claim['claim_id']} references unknown family")
        missing_dependencies = set(claim.get("depends_on", [])) - claims
        if missing_dependencies:
            raise ValueError(
                f"claim {claim['claim_id']} has unknown dependencies: "
                f"{sorted(missing_dependencies)}"
            )
        for limitation in claim.get("limitations", []):
            source = limitation.get("source_clause_id")
            if source is not None and source not in clauses:
                raise ValueError(
                    f"claim {claim['claim_id']} limitation "
                    f"{limitation['limitation_id']} references unknown clause {source}"
                )


def render_claim(claim: dict[str, Any]) -> str:
    lines = [
        f"### {claim['claim_id']}",
        "",
        f"**Type:** {claim['claim_type']} {claim['category']}",
        f"**Status:** {claim['status']}",
        "",
        claim.get("preamble", ""),
    ]
    limitations = claim.get("limitations", [])
    for index, limitation in enumerate(limitations):
        ending = ";" if index < len(limitations) - 1 else "."
        lines.append(f"{index + 1}. {limitation['text']}{ending}")
    if claim.get("technical_effects"):
        lines.extend(["", "**Technical effects**"])
        lines.extend(f"- {effect}" for effect in claim["technical_effects"])
    if claim.get("prior_art_collision_zones"):
        lines.extend(["", "**Prior-art collision zones for review**"])
        lines.extend(f"- {zone}" for zone in claim["prior_art_collision_zones"])
    return "\n".join(lines)


def render_family(family: dict[str, Any], claims_by_id: dict[str, dict[str, Any]]) -> str:
    lines = [
        f"# {family['family_id']} — {family['title']}",
        "",
        "> Working invention-disclosure and claim-architecture artifact. Not legal advice or a filed application.",
        "",
        f"**Priority:** {family['priority_order']}",
        f"**Status:** {family['status']}",
        f"**Parent families:** {', '.join(family.get('parent_family_ids', [])) or 'None'}",
        "",
        "## Inventive center",
        "",
        family["inventive_center"],
        "",
        "## Technical problem",
        "",
        family.get("technical_problem", "Not yet recorded."),
        "",
        "## Technical effects",
        "",
    ]
    lines.extend(f"- {effect}" for effect in family.get("technical_effects", []))
    lines.extend(["", "## Working claims", ""])
    for claim_id in family["claim_ids"]:
        lines.extend([render_claim(claims_by_id[claim_id]), ""])

    lines.extend(["## Implementation evidence", ""])
    evidence = family.get("implementation_evidence", [])
    if not evidence:
        lines.append("- No implementation evidence recorded yet.")
    else:
        for item in evidence:
            suffix = []
            if item.get("path"):
                suffix.append(f"path `{item['path']}`")
            if item.get("commit"):
                suffix.append(f"commit `{item['commit']}`")
            detail = f" ({'; '.join(suffix)})" if suffix else ""
            lines.append(f"- `{item['repository']}`{detail}: {item['description']}")

    lines.extend(["", "## Disclosure and inventorship record", ""])
    for key, value in family.get("disclosure_dates", {}).items():
        lines.append(f"- {key.replace('_', ' ').title()}: {value or 'TO BE DETERMINED'}")
    lines.append(
        "- Inventor candidates: "
        + ", ".join(family.get("inventor_candidates", []))
    )
    if family.get("notes"):
        lines.extend(["", "## Notes", "", family["notes"]])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    data = load_data(args.data)
    if args.check:
        print("master claim data cross-references are valid")
        return 0

    args.output.mkdir(parents=True, exist_ok=True)
    claims_by_id = {claim["claim_id"]: claim for claim in data["claims"]}
    for family in sorted(data["families"], key=lambda item: item["priority_order"]):
        target = args.output / f"{family['family_id'].lower()}.md"
        target.write_text(render_family(family, claims_by_id), encoding="utf-8")
        print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
