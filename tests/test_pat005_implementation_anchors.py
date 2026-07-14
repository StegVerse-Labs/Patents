from __future__ import annotations

import json
from pathlib import Path

from tools.validate_pat005_implementation_anchors import validate


def test_real_pat005_anchor_record_is_valid() -> None:
    result = validate(Path("data/PAT-005-implementation-anchors.json"))
    assert result["decision"] == "PAT005_IMPLEMENTATION_ANCHORS_VALID"
    assert result["anchor_count"] == 11
    assert result["repository_count"] == 4
    assert result["executable_repository_count"] == 3
    assert result["guardian_boundary_present"] is True
    assert result["guardian_receipt_present"] is True


def test_rejects_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    source["authority_boundary"]["filing_authorized"] = True
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("filing_authorized" in error for error in result["errors"])


def test_rejects_duplicate_repository_commit_path(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    source["anchors"].append(dict(source["anchors"][0]))
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("duplicate anchor" in error for error in result["errors"])


def test_verified_state_requires_guardian_boundary_and_receipt(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    source["anchors"] = [
        item for item in source["anchors"]
        if item["repository"] != "StegVerse-002/stegguardian-wiki"
    ]
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("Guardian" in error or "four" in error for error in result["errors"])


def test_guardian_document_cannot_claim_executable_authority(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    guardian = next(item for item in source["anchors"] if item["anchor_type"] == "boundary_document")
    guardian["anchor_type"] = "executable_validator"
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("must not be classified as executable authority" in error for error in result["errors"])
