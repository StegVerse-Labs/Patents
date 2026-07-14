from __future__ import annotations

import json
from pathlib import Path

from tools.validate_pat005_implementation_anchors import validate


def test_real_pat005_anchor_record_is_valid() -> None:
    result = validate(Path("data/PAT-005-implementation-anchors.json"))
    assert result["decision"] == "PAT005_IMPLEMENTATION_ANCHORS_VALID"
    assert result["anchor_count"] == 3


def test_rejects_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    source["authority_boundary"]["filing_authorized"] = True
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("filing_authorized" in error for error in result["errors"])


def test_rejects_duplicate_paths(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-005-implementation-anchors.json").read_text(encoding="utf-8"))
    source["anchors"].append(dict(source["anchors"][0]))
    record = tmp_path / "anchors.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT005_IMPLEMENTATION_ANCHORS"
    assert any("duplicate path" in error for error in result["errors"])
