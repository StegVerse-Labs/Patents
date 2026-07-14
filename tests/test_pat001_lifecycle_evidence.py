from __future__ import annotations

import json
from pathlib import Path

from tools.validate_pat001_lifecycle_evidence import validate


def test_real_lifecycle_record_is_valid() -> None:
    result = validate(Path("data/PAT-001-lifecycle-evidence.json"))
    assert result["decision"] == "PAT001_LIFECYCLE_EVIDENCE_VALID"
    assert result["positive_anchor_count"] == 2
    assert result["negative_finding_count"] == 6


def test_rejects_missing_negative_limitation(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-001-lifecycle-evidence.json").read_text(encoding="utf-8"))
    source["explicit_negative_findings"] = source["explicit_negative_findings"][:-1]
    record = tmp_path / "record.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT001_LIFECYCLE_EVIDENCE"
    assert any("missing explicit negative" in error for error in result["errors"])


def test_rejects_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-001-lifecycle-evidence.json").read_text(encoding="utf-8"))
    source["authority_boundary"]["patentability_determined"] = True
    record = tmp_path / "record.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT001_LIFECYCLE_EVIDENCE"
    assert any("patentability_determined" in error for error in result["errors"])


def test_rejects_duplicate_limitation(tmp_path: Path) -> None:
    source = json.loads(Path("data/PAT-001-lifecycle-evidence.json").read_text(encoding="utf-8"))
    source["explicit_negative_findings"].append(dict(source["explicit_negative_findings"][0]))
    record = tmp_path / "record.json"
    record.write_text(json.dumps(source), encoding="utf-8")
    result = validate(record)
    assert result["decision"] == "INVALID_PAT001_LIFECYCLE_EVIDENCE"
    assert any("duplicate limitation" in error for error in result["errors"])
