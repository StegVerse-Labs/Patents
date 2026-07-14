import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "validate_patent_readiness.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_patent_readiness", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_required_artifacts(root: Path, module, family: str = "PAT-001"):
    for path in module.required_family_artifacts(root, family):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n", encoding="utf-8")


def test_pat001_current_index_fails_closed_with_open_blockers():
    module = load_validator()
    report, exit_code = module.validate(ROOT, "PAT-001")
    assert exit_code == 2
    assert report["decision"] == "FAIL_CLOSED_BLOCKERS"
    assert report["boundary"]["external_submission_performed"] is False
    assert report["unresolved_items"]


def test_missing_index_is_invalid(tmp_path):
    module = load_validator()
    report, exit_code = module.validate(tmp_path, "PAT-001")
    assert exit_code == 3
    assert report["decision"] == "INVALID_READINESS_RECORD"


def test_complete_authorized_fixture_is_ready(tmp_path):
    module = load_validator()
    write_required_artifacts(tmp_path, module)
    index = tmp_path / "filing-readiness" / "PAT-001_FILING_READINESS_INDEX.md"
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(
        """# Ready fixture

- [x] source corroborated
- [x] inventorship reviewed
- [x] prior art reviewed

**Review packet authorized:** yes

**Filed:** no

**Patent pending language authorized:** no
""",
        encoding="utf-8",
    )
    report, exit_code = module.validate(tmp_path, "PAT-001")
    assert exit_code == 0
    assert report["decision"] == "READY_FOR_REVIEW_PACKET"
    assert all(check["status"] == "PASS" for check in report["checks"])


def test_missing_required_artifact_fails_closed(tmp_path):
    module = load_validator()
    write_required_artifacts(tmp_path, module)
    missing = next(iter(module.required_family_artifacts(tmp_path, "PAT-001")))
    missing.unlink()
    index = tmp_path / "filing-readiness" / "PAT-001_FILING_READINESS_INDEX.md"
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(
        """# Fixture

- [x] complete

**Review packet authorized:** yes

**Filed:** no

**Patent pending language authorized:** no
""",
        encoding="utf-8",
    )
    report, exit_code = module.validate(tmp_path, "PAT-001")
    assert exit_code == 2
    assert report["decision"] == "FAIL_CLOSED_BLOCKERS"
    assert any(check["check_id"] == "required-artifacts" and check["status"] == "FAIL" for check in report["checks"])
