from __future__ import annotations

import json
from pathlib import Path

from tools.replay_pat005_negative_cases import replay


def test_real_negative_case_corpus_replays() -> None:
    result = replay(Path("fixtures/PAT-005-negative-cases.json"))
    assert result["decision"] == "PAT005_NEGATIVE_CASES_REPLAYED"
    assert result["case_count"] == 8
    assert result["passed_count"] == 8


def test_rejects_authority_escalation(tmp_path: Path) -> None:
    source = json.loads(Path("fixtures/PAT-005-negative-cases.json").read_text(encoding="utf-8"))
    source["authority_boundary"]["filing_authorized"] = True
    fixture = tmp_path / "cases.json"
    fixture.write_text(json.dumps(source), encoding="utf-8")
    result = replay(fixture)
    assert result["decision"] == "PAT005_NEGATIVE_CASES_INVALID"
    assert any("filing_authorized" in error for error in result["errors"])


def test_rejects_duplicate_case_id(tmp_path: Path) -> None:
    source = json.loads(Path("fixtures/PAT-005-negative-cases.json").read_text(encoding="utf-8"))
    source["cases"].append(dict(source["cases"][0]))
    fixture = tmp_path / "cases.json"
    fixture.write_text(json.dumps(source), encoding="utf-8")
    result = replay(fixture)
    assert result["decision"] == "PAT005_NEGATIVE_CASES_INVALID"
    assert any("duplicate case_id" in error for error in result["errors"])


def test_rejects_non_reproducing_case(tmp_path: Path) -> None:
    source = json.loads(Path("fixtures/PAT-005-negative-cases.json").read_text(encoding="utf-8"))
    source["cases"][0]["expected_reason"] = "different reason"
    fixture = tmp_path / "cases.json"
    fixture.write_text(json.dumps(source), encoding="utf-8")
    result = replay(fixture)
    assert result["decision"] == "PAT005_NEGATIVE_CASES_INVALID"
    assert any("did not reproduce" in error for error in result["errors"])
