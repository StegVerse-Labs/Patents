import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "validate_portfolio_filing_state.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_portfolio_filing_state", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_ledger(root: Path, families):
    path = root / "data" / "portfolio-completion-status.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"schema_version": "test", "numbered_families": families}), encoding="utf-8")


def test_current_portfolio_state_is_valid_and_unfiled():
    module = load_validator()
    report, exit_code = module.validate(ROOT)
    assert exit_code == 0
    assert report["decision"] == "PORTFOLIO_FILING_STATE_VALID"
    assert report["family_count"] >= 5
    assert report["boundary"]["external_submission_performed"] is False


def test_missing_ledger_is_invalid(tmp_path):
    module = load_validator()
    report, exit_code = module.validate(tmp_path)
    assert exit_code == 3
    assert report["decision"] == "INVALID_PORTFOLIO_RECORD"


def test_filed_state_without_receipt_fails_closed(tmp_path):
    module = load_validator()
    write_ledger(tmp_path, [{
        "family_id": "PAT-X",
        "status": "filed",
        "filed": True,
        "filing_receipt": None,
        "application_number": None,
        "filing_date": None,
        "nonprovisional_deadline": None,
    }])
    report, exit_code = module.validate(tmp_path)
    assert exit_code == 2
    assert report["decision"] == "FAIL_CLOSED_FILING_STATE"
    assert any(item["check_id"] == "filed-state-evidence" for item in report["failures"])


def test_patent_pending_without_filing_fails_closed(tmp_path):
    module = load_validator()
    write_ledger(tmp_path, [{
        "family_id": "PAT-X",
        "status": "drafting",
        "filed": False,
        "patent_pending_authorized": True,
        "filing_receipt": None,
        "application_number": None,
        "filing_date": None,
        "nonprovisional_deadline": None,
    }])
    report, exit_code = module.validate(tmp_path)
    assert exit_code == 2
    assert any(item["check_id"] == "patent-pending-boundary" for item in report["failures"])


def test_deadline_without_actual_filing_date_fails_closed(tmp_path):
    module = load_validator()
    write_ledger(tmp_path, [{
        "family_id": "PAT-X",
        "status": "drafting",
        "filed": False,
        "filing_receipt": None,
        "application_number": None,
        "filing_date": None,
        "nonprovisional_deadline": "2027-07-28",
    }])
    report, exit_code = module.validate(tmp_path)
    assert exit_code == 2
    assert any(item["check_id"] == "deadline-basis" for item in report["failures"])


def test_complete_filed_fixture_passes(tmp_path):
    module = load_validator()
    receipt = tmp_path / "filing_packets" / "PAT-X" / "uspto_filing_receipt.pdf"
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_bytes(b"fixture receipt")
    write_ledger(tmp_path, [{
        "family_id": "PAT-X",
        "status": "filed",
        "filed": True,
        "patent_pending_authorized": True,
        "filing_receipt": "filing_packets/PAT-X/uspto_filing_receipt.pdf",
        "application_number": "00/000,000",
        "filing_date": "2026-07-28",
        "nonprovisional_deadline": "2027-07-28",
    }])
    report, exit_code = module.validate(tmp_path)
    assert exit_code == 0
    assert report["decision"] == "PORTFOLIO_FILING_STATE_VALID"
    assert not report["failures"]
