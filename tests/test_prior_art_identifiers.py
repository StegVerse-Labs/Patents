from __future__ import annotations

import json
from pathlib import Path

from tools.validate_prior_art_identifiers import validate


def test_real_prior_art_identifier_record_is_valid() -> None:
    result = validate(Path("data/active-family-prior-art-identifiers.json"))
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_VALID"
    assert result["verified_non_patent_count"] == 4
    assert result["verified_patent_count"] == 3


def test_partial_state_can_include_verified_patent_publications() -> None:
    result = validate(Path("data/active-family-prior-art-identifiers.json"))
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_VALID"
    assert result["verified_patent_count"] > 0


def test_rejects_false_complete_state_without_patent_publication(tmp_path: Path) -> None:
    source = json.loads(Path("data/active-family-prior-art-identifiers.json").read_text(encoding="utf-8"))
    source["decision"] = "PRIOR_ART_IDENTIFIERS_VERIFIED"
    source["families"]["PAT-001"]["verified_patent_publications"] = []
    source["families"]["PAT-001"]["patent_search_status"] = "NO_PUBLICATION_NUMBER_VERIFIED"
    record = tmp_path / "prior-art.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_INVALID"
    assert any("requires at least one verified patent publication" in error for error in result["errors"])


def test_rejects_malformed_patent_identifier(tmp_path: Path) -> None:
    source = json.loads(Path("data/active-family-prior-art-identifiers.json").read_text(encoding="utf-8"))
    source["families"]["PAT-001"]["verified_patent_publications"][0]["publication_number"] = "NOT-A-PATENT"
    record = tmp_path / "prior-art.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_INVALID"
    assert any("publication_number invalid" in error for error in result["errors"])


def test_rejects_legal_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("data/active-family-prior-art-identifiers.json").read_text(encoding="utf-8"))
    source["search_boundary"]["patentability_determined"] = True
    record = tmp_path / "prior-art.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PRIOR_ART_IDENTIFIERS_INVALID"
    assert any("patentability_determined" in error for error in result["errors"])
