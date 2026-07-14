from __future__ import annotations

import json
from pathlib import Path

from tools.validate_prior_art_identifiers import validate


def test_real_prior_art_identifier_record_is_valid() -> None:
    result = validate(Path("data/active-family-prior-art-identifiers.json"))
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_VALID"
    assert result["verified_non_patent_count"] == 4
    assert result["verified_patent_count"] == 0


def test_rejects_false_complete_state_without_patent_publication(tmp_path: Path) -> None:
    source = json.loads(Path("data/active-family-prior-art-identifiers.json").read_text(encoding="utf-8"))
    source["decision"] = "PRIOR_ART_IDENTIFIERS_VERIFIED"
    record = tmp_path / "prior-art.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_INVALID"
    assert any("requires at least one verified patent publication" in error for error in result["errors"])


def test_rejects_legal_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("data/active-family-prior-art-identifiers.json").read_text(encoding="utf-8"))
    source["search_boundary"]["patentability_determined"] = True
    record = tmp_path / "prior-art.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_INVALID"
    assert any("patentability_determined" in error for error in result["errors"])
