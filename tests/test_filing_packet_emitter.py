import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "filing_packet_emitter.py"


def load_module():
    spec = importlib.util.spec_from_file_location("filing_packet_emitter", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_fixture(root: Path, invention_id: str = "PAT-TEST") -> None:
    for directory in ("disclosures", "provisionals", "claims", "deadlines"):
        (root / directory).mkdir(parents=True, exist_ok=True)

    (root / "disclosures" / f"{invention_id}.md").write_text(
        "# Disclosure\n\nGoverned test disclosure.\n",
        encoding="utf-8",
    )
    (root / "provisionals" / f"{invention_id}_provisional.md").write_text(
        """# Provisional Patent Draft

**Title:** Governed admissibility gate
**Inventors:** Rigel Randolph et al.

## Field of the Invention
Governed state-transition systems.

## Summary
High-level summary placeholder.

## Detailed Description
A proposal is evaluated before commitment and receives a receipt.
""",
        encoding="utf-8",
    )
    (root / "deadlines" / "deadlines.json").write_text(
        json.dumps(
            {
                "sig": "deadlines:v1",
                "items": [
                    {
                        "invention_id": invention_id,
                        "provisional_filed_utc": None,
                        "nonprovisional_due_utc": None,
                        "pct_due_utc": None,
                        "status": "drafting",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def run_main(monkeypatch, module, root: Path, invention_id: str = "PAT-TEST") -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        [
            str(SCRIPT),
            "--invention-id",
            invention_id,
            "--entity-status",
            "micro",
            "--root",
            str(root),
        ],
    )
    module.main()


def test_missing_provisional_fails_closed(tmp_path, monkeypatch):
    module = load_module()
    with pytest.raises(SystemExit, match="FAIL-CLOSED: no provisional draft"):
        run_main(monkeypatch, module, tmp_path, "MISSING")


def test_emitter_preserves_human_filing_boundary_and_hashes(tmp_path, monkeypatch):
    module = load_module()
    write_fixture(tmp_path)

    run_main(monkeypatch, module, tmp_path)

    packet = tmp_path / "filing_packets" / "PAT-TEST"
    manifest = json.loads((packet / "PACKET_MANIFEST.json").read_text(encoding="utf-8"))
    ledger = json.loads((tmp_path / "deadlines" / "deadlines.json").read_text(encoding="utf-8"))
    item = ledger["items"][0]

    assert manifest["sig"] == "filing-packet:v1"
    assert manifest["status"] == "ready-with-warnings"
    assert "claims-missing: placeholder claim inserted" in manifest["warnings"]
    assert "abstract-placeholder: Summary section is unpopulated template text" in manifest["warnings"]
    assert any(warning.startswith("cover-sheet:") for warning in manifest["warnings"])

    expected_artifacts = {
        "specification.docx",
        "cover_sheet_data.json",
        "fee_estimate.json",
        "FILING_CHECKLIST.md",
    }
    assert {artifact["path"] for artifact in manifest["artifacts"]} == expected_artifacts
    for artifact in manifest["artifacts"]:
        path = packet / artifact["path"]
        assert artifact["sha256"] == sha256(path)
        assert artifact["bytes"] == path.stat().st_size

    assert item["status"] == "packet-emitted"
    assert item["provisional_filed_utc"] is None
    assert item["nonprovisional_due_utc"] is None
    assert item["pct_due_utc"] is None
    assert "application_number" not in item

    checklist = (packet / "FILING_CHECKLIST.md").read_text(encoding="utf-8")
    assert "Human boundary crossing" in checklist
    assert "Save the electronic filing receipt PDF" in checklist
    assert "actual filing date" in checklist


def test_complete_claims_and_summary_avoid_content_placeholders(tmp_path, monkeypatch):
    module = load_module()
    write_fixture(tmp_path, "PAT-COMPLETE")
    (tmp_path / "provisionals" / "PAT-COMPLETE_provisional.md").write_text(
        """# Provisional Patent Draft

**Title:** Governed admissibility gate
**Inventors:** Rigel Randolph

## Field of the Invention
Governed state-transition systems.

## Summary
A governed gate evaluates a proposed transition before commitment and emits a receipt binding the decision to its inputs.

## Detailed Description
A proposal is evaluated before commitment and receives a receipt.
""",
        encoding="utf-8",
    )
    (tmp_path / "claims" / "PAT-COMPLETE_claims.md").write_text(
        "1. A method comprising evaluating a proposed state transition before commitment.\n",
        encoding="utf-8",
    )

    run_main(monkeypatch, module, tmp_path, "PAT-COMPLETE")

    manifest = json.loads(
        (tmp_path / "filing_packets" / "PAT-COMPLETE" / "PACKET_MANIFEST.json").read_text(
            encoding="utf-8"
        )
    )
    assert not any(warning.startswith("claims-missing") for warning in manifest["warnings"])
    assert not any(warning.startswith("abstract-placeholder") for warning in manifest["warnings"])
    assert manifest["source_refs"]["claims"] == "claims/PAT-COMPLETE_claims.md"
