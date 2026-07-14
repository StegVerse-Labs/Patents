from __future__ import annotations

import json
from pathlib import Path

from tools.build_patent_evidence_queue import build_queue, is_machine_authorized if False else build_queue
from tools.validate_patent_evidence_queue import validate


def _write_status(path: Path, family_id: str, tasks: list[str]) -> None:
    path.write_text(json.dumps({"family_id": family_id, "next_machine_tasks": tasks}), encoding="utf-8")


def test_build_queue_normalizes_and_classifies(tmp_path: Path) -> None:
    pat001 = tmp_path / "pat001.json"
    pat005 = tmp_path / "pat005.json"
    _write_status(pat001, "PAT-001", [
        "locate exact canonical source repositories and commit anchors",
        "collect executable evidence for expiry and heartbeat",
        "populate stable patent and non-patent prior art identifiers after verified searches",
    ])
    _write_status(pat005, "PAT-005", ["collect exact source implementation commit anchors"])
    result = build_queue([pat001, pat005])
    assert result["decision"] == "EVIDENCE_QUEUE_READY"
    assert len(result["queue"]) == 4
    classes = {item["evidence_class"] for item in result["queue"]}
    assert "canonical_source_recovery" in classes
    assert "lifecycle_evidence_collection" in classes
    assert "prior_art_identifier_verification" in classes
    assert all(item["claimed_legal_effect"] is False for item in result["queue"])


def test_build_queue_excludes_non_delegable_tasks(tmp_path: Path) -> None:
    status = tmp_path / "status.json"
    _write_status(status, "PAT-001", ["obtain practitioner approval", "decide whether to file"])
    result = build_queue([status])
    assert result["queue"] == []
    assert len(result["excluded"]) == 2


def test_validator_accepts_generated_queue(tmp_path: Path) -> None:
    status = tmp_path / "status.json"
    output = tmp_path / "queue.json"
    _write_status(status, "PAT-001", ["run the canonical portfolio entry point through the authoritative execution path"])
    result = build_queue([status])
    output.write_text(json.dumps(result), encoding="utf-8")
    assert validate(output)["decision"] == "EVIDENCE_QUEUE_VALID"


def test_validator_rejects_claimed_legal_effect(tmp_path: Path) -> None:
    status = tmp_path / "status.json"
    output = tmp_path / "queue.json"
    _write_status(status, "PAT-001", ["collect executable evidence for capability resolution"])
    result = build_queue([status])
    result["queue"][0]["claimed_legal_effect"] = True
    output.write_text(json.dumps(result), encoding="utf-8")
    checked = validate(output)
    assert checked["decision"] == "INVALID_EVIDENCE_QUEUE"
    assert any("claimed_legal_effect" in error for error in checked["errors"])
