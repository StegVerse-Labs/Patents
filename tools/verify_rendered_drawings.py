#!/usr/bin/env python3
"""Verify rendered patent drawing manifests and SVG review artifacts.

This tool checks local repository artifacts only. It does not approve drawings,
authorize filing, or make any legal determination.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REFERENCE_RE = re.compile(r"(?<!\d)(\d{3,4})(?!\d)")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _svg_text(path: Path) -> str:
    root = ET.parse(path).getroot()
    return " ".join(text.strip() for text in root.itertext() if text and text.strip())


def verify_manifest(repo_root: Path, manifest_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    verified: list[dict[str, Any]] = []

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "INVALID_DRAWING_MANIFEST", "errors": [str(exc)], "warnings": []}

    if manifest.get("filing_authorized") is not False:
        errors.append("filing_authorized must remain false for review drawings")
    if manifest.get("patent_pending_authorized") is not False:
        errors.append("patent_pending_authorized must remain false for review drawings")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("artifacts must be a non-empty array")
        artifacts = []

    seen_figures: set[str] = set()
    seen_paths: set[str] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            errors.append(f"artifact[{index}] must be an object")
            continue
        figure = artifact.get("figure")
        relative_path = artifact.get("path")
        expected_hash = artifact.get("sha256")
        if not isinstance(figure, str) or not figure.startswith("FIG-"):
            errors.append(f"artifact[{index}].figure must be FIG-* string")
            continue
        if figure in seen_figures:
            errors.append(f"duplicate figure: {figure}")
        seen_figures.add(figure)
        if not isinstance(relative_path, str) or not relative_path.endswith(".svg"):
            errors.append(f"artifact[{index}].path must be an SVG path")
            continue
        if relative_path in seen_paths:
            errors.append(f"duplicate path: {relative_path}")
        seen_paths.add(relative_path)
        if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
            errors.append(f"artifact[{index}].sha256 must be lowercase SHA-256")
            continue

        path = repo_root / relative_path
        if not path.is_file():
            errors.append(f"missing rendered drawing: {relative_path}")
            continue
        try:
            actual_hash = _sha256(path)
            text = _svg_text(path)
        except (OSError, ET.ParseError) as exc:
            errors.append(f"invalid SVG {relative_path}: {exc}")
            continue
        if actual_hash != expected_hash:
            errors.append(f"hash mismatch: {relative_path}")
        references = sorted(set(REFERENCE_RE.findall(text)))
        if not references:
            warnings.append(f"no reference numerals detected: {relative_path}")
        if figure not in text:
            warnings.append(f"figure label not present in SVG text: {relative_path}")
        verified.append({
            "figure": figure,
            "path": relative_path,
            "sha256": actual_hash,
            "reference_numerals": references,
        })

    decision = "DRAWING_MANIFEST_VALID" if not errors else "INVALID_DRAWING_MANIFEST"
    return {
        "family_id": manifest.get("family_id"),
        "decision": decision,
        "verified_artifacts": verified,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()
    result = verify_manifest(args.repo_root.resolve(), args.manifest.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "DRAWING_MANIFEST_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
