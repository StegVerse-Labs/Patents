from __future__ import annotations

import json
from pathlib import Path

from tools.validate_canonical_source_search_receipt import validate


def _valid() -> dict:
    return {
        "family_id": "PAT-001",
        "queries": [
            {
                "query": "StegVerse-Micro-Node-Agency",
                "scope": "StegVerse-Labs",
                "result": "REFERENCES_ONLY",
                "matched_paths": ["StegVerse-Labs/Patents/PATENTS_MIRROR_HANDOFF.md"],
            }
        ],
        "decision": "CANONICAL_SOURCE_NOT_RECOVERED",
        "canonical_june_6_source_verified": False,
        "canonical_june_16_source_verified": False,
        "negative_evidence_preserved": True,
        "retry_triggers": ["new repository becomes accessible"],
        "authority_boundary": {
            "conception_date_determined": False,
            "inventorship_determined": False,
            "patentability_determined": False,
            "filing_authorized": False,
            "patent_pending_authorized": False,
        },
    }


def test_accepts_unresolved_fail_closed_receipt(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(_valid()), encoding="utf-8")
    assert validate(path)["decision"] == "SOURCE_SEARCH_RECEIPT_VALID"


def test_rejects_verified_without_canonical_match(tmp_path: Path) -> None:
    data = _valid()
    data["canonical_june_16_source_verified"] = True
    data["decision"] = "CANONICAL_SOURCE_RECOVERED"
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    result = validate(path)
    assert result["decision"] == "INVALID_SOURCE_SEARCH_RECEIPT"
    assert any("CANONICAL_SOURCE_MATCH" in error for error in result["errors"])


def test_rejects_authority_escalation(tmp_path: Path) -> None:
    data = _valid()
    data["authority_boundary"]["inventorship_determined"] = True
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    result = validate(path)
    assert result["decision"] == "INVALID_SOURCE_SEARCH_RECEIPT"
    assert any("inventorship_determined" in error for error in result["errors"])


def test_real_receipt_is_valid() -> None:
    root = Path(__file__).resolve().parents[1]
    result = validate(root / "data/PAT-001-canonical-source-search-receipt.json")
    assert result["decision"] == "SOURCE_SEARCH_RECEIPT_VALID"
