#!/usr/bin/env python3
"""Lint Mermaid patent drawing sources before rendering.

The linter checks source completeness and reference-numeral consistency. It does
not render, approve, or submit drawings.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

FIGURE_RE = re.compile(r"PAT-(?P<family>\d+)-FIG-(?P<number>\d+)")
NUMERAL_RE = re.compile(r"\b([1-9]\d{2})\b")


def lint_source(path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return {"path": str(path), "decision": "INVALID_DRAWING_SOURCE", "errors": [str(exc)], "warnings": []}

    if not text.strip():
        errors.append("source is empty")
    if "flowchart" not in text and "sequenceDiagram" not in text and "stateDiagram" not in text and "classDiagram" not in text:
        errors.append("no supported Mermaid diagram declaration found")
    if "http://" in text or "https://" in text:
        warnings.append("external URL appears in drawing source")

    figure_match = FIGURE_RE.search(path.name)
    if not figure_match:
        warnings.append("filename does not include PAT-###-FIG-## identifier")

    numerals = sorted(set(NUMERAL_RE.findall(text)))
    if not numerals:
        warnings.append("no three-digit reference numerals found")

    bracket_pairs = (("[", "]"), ("(", ")"), ("{", "}"))
    for left, right in bracket_pairs:
        if text.count(left) != text.count(right):
            errors.append(f"unbalanced {left}{right} delimiters")

    decision = "DRAWING_SOURCE_VALID" if not errors else "INVALID_DRAWING_SOURCE"
    return {
        "path": str(path),
        "decision": decision,
        "reference_numerals": numerals,
        "errors": errors,
        "warnings": warnings,
    }


def lint_directory(directory: Path) -> dict[str, Any]:
    sources = sorted(directory.glob("PAT-*-FIG-*.mmd"))
    results = [lint_source(path) for path in sources]
    errors = [item for item in results if item["decision"] != "DRAWING_SOURCE_VALID"]
    return {
        "decision": "DRAWING_SOURCES_VALID" if sources and not errors else "DRAWING_SOURCES_INVALID",
        "source_count": len(sources),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    result = lint_directory(args.path) if args.path.is_dir() else lint_source(args.path)
    print(json.dumps(result, indent=2, sort_keys=True))
    decision = result["decision"]
    return 0 if decision in ("DRAWING_SOURCE_VALID", "DRAWING_SOURCES_VALID") else 2


if __name__ == "__main__":
    raise SystemExit(main())
