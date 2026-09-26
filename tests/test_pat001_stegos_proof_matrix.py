from __future__ import annotations

import json
from pathlib import Path

from tools.validate_pat001_stegos_proof_matrix import validate


RECORD = Path("data/PAT-001-stegos-proof-to-patent-evidence-matrix.json")


def test_current_matrix_is_valid_and_pending() -> None:
    result = validate(RECORD)
    assert result["decision"] == "PAT001_STEGOS_PROOF_MATRIX_VALID"
    assert result["predicate_count"] == 4


def test_rejects_physical_proof_claim_without_ingestion(tmp_path: Path) -> None:
    data = json.loads(RECORD.read_text(encoding="utf-8"))
    data["physical_proof_claimed"] = True
    record = tmp_path / "matrix.json"
    record.write_text(json.dumps(data), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PAT001_STEGOS_PROOF_MATRIX_INVALID"


def test_completed_predicate_requires_immutable_evidence(tmp_path: Path) -> None:
    data = json.loads(RECORD.read_text(encoding="utf-8"))
    data["predicates"][0]["status"] = "AUTHENTIC_RETAINED_EVIDENCE_INGESTED"
    record = tmp_path / "matrix.json"
    record.write_text(json.dumps(data), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PAT001_STEGOS_PROOF_MATRIX_INVALID"
    assert any("completed predicate missing source_repository" in error for error in result["errors"])


def test_rejects_post_hoc_limitation_mapping_change(tmp_path: Path) -> None:
    data = json.loads(RECORD.read_text(encoding="utf-8"))
    data["predicates"][0]["supports_candidate_limitations"].append("P1-L21")
    record = tmp_path / "matrix.json"
    record.write_text(json.dumps(data), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "PAT001_STEGOS_PROOF_MATRIX_INVALID"
    assert any("limitation mapping drift" in error for error in result["errors"])
