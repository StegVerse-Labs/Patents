from __future__ import annotations

import json
from pathlib import Path

from tools.validate_source_corroboration import validate_record


def _valid_record() -> dict:
    return {
        "schema_version": "1.0",
        "family_id": "PAT-999",
        "status": "PARTIALLY_CORROBORATED",
        "anchors": [
            {
                "anchor_id": "PAT999-A001",
                "repository": "Example/Repo",
                "commit_sha": "a" * 40,
                "path": "docs/source.md",
                "blob_sha": "b" * 40,
                "source_date_status": "commit-bound",
                "support_level": "implemented_policy",
                "supported_limitations": ["bounded_scope"],
                "does_not_establish": ["inventorship"],
            }
        ],
        "corroborated_limitations": ["bounded_scope"],
        "still_uncorroborated": ["default_expiry"],
        "authority_boundary": {
            "inventorship_determined": False,
            "patentability_determined": False,
            "priority_date_determined": False,
            "filing_authorized": False,
            "patent_pending_authorized": False,
        },
    }


def _write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data), encoding="utf-8")


def test_valid_record(tmp_path: Path) -> None:
    path = tmp_path / "record.json"
    _write(path, _valid_record())
    result = validate_record(path)
    assert result["decision"] == "CORROBORATION_RECORD_VALID"
    assert result["anchor_count"] == 1


def test_duplicate_anchor_fails(tmp_path: Path) -> None:
    data = _valid_record()
    data["anchors"].append(dict(data["anchors"][0]))
    path = tmp_path / "record.json"
    _write(path, data)
    result = validate_record(path)
    assert result["decision"] == "INVALID_CORROBORATION_RECORD"
    assert any("duplicate anchor_id" in error for error in result["errors"])


def test_unsupported_declared_limitation_fails(tmp_path: Path) -> None:
    data = _valid_record()
    data["corroborated_limitations"].append("not_in_anchor")
    path = tmp_path / "record.json"
    _write(path, data)
    result = validate_record(path)
    assert result["decision"] == "INVALID_CORROBORATION_RECORD"
    assert any("lack anchor support" in error for error in result["errors"])


def test_authority_boundary_must_remain_false(tmp_path: Path) -> None:
    data = _valid_record()
    data["authority_boundary"]["filing_authorized"] = True
    path = tmp_path / "record.json"
    _write(path, data)
    result = validate_record(path)
    assert result["decision"] == "INVALID_CORROBORATION_RECORD"
    assert "authority_boundary.filing_authorized must remain false" in result["errors"]


def test_actual_pat001_record_validates() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    result = validate_record(repo_root / "data" / "PAT-001-source-corroboration.json")
    assert result["decision"] == "CORROBORATION_RECORD_VALID"
    assert result["anchor_count"] == 3
