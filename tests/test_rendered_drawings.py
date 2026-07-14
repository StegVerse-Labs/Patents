from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.verify_rendered_drawings import verify_manifest


def _write_svg(path: Path, label: str = "FIG-01 100 Intake 110 Decision") -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = f'<svg xmlns="http://www.w3.org/2000/svg"><text>{label}</text></svg>'
    path.write_text(payload, encoding="utf-8")
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _write_manifest(path: Path, artifact_path: str, digest: str) -> None:
    path.write_text(json.dumps({
        "family_id": "PAT-999",
        "status": "rendered_for_review_not_approved",
        "filing_authorized": False,
        "patent_pending_authorized": False,
        "artifacts": [{
            "figure": "FIG-01",
            "path": artifact_path,
            "sha256": digest,
        }],
    }), encoding="utf-8")


def test_valid_manifest(tmp_path: Path) -> None:
    relative = "rendered/PAT-999/FIG-01.svg"
    digest = _write_svg(tmp_path / relative)
    manifest = tmp_path / "manifest.json"
    _write_manifest(manifest, relative, digest)

    result = verify_manifest(tmp_path, manifest)
    assert result["decision"] == "DRAWING_MANIFEST_VALID"
    assert result["verified_artifacts"][0]["reference_numerals"] == ["100", "110"]


def test_hash_mismatch_fails(tmp_path: Path) -> None:
    relative = "rendered/PAT-999/FIG-01.svg"
    _write_svg(tmp_path / relative)
    manifest = tmp_path / "manifest.json"
    _write_manifest(manifest, relative, "0" * 64)

    result = verify_manifest(tmp_path, manifest)
    assert result["decision"] == "INVALID_DRAWING_MANIFEST"
    assert any("hash mismatch" in item for item in result["errors"])


def test_review_manifest_cannot_authorize_filing(tmp_path: Path) -> None:
    relative = "rendered/PAT-999/FIG-01.svg"
    digest = _write_svg(tmp_path / relative)
    manifest = tmp_path / "manifest.json"
    _write_manifest(manifest, relative, digest)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["filing_authorized"] = True
    manifest.write_text(json.dumps(payload), encoding="utf-8")

    result = verify_manifest(tmp_path, manifest)
    assert result["decision"] == "INVALID_DRAWING_MANIFEST"
    assert "filing_authorized must remain false for review drawings" in result["errors"]


def test_actual_pat001_manifest_validates() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    manifest = repo_root / "rendered" / "PAT-001" / "manifest.json"
    result = verify_manifest(repo_root, manifest)
    assert result["decision"] == "DRAWING_MANIFEST_VALID"
    assert len(result["verified_artifacts"]) == 4
