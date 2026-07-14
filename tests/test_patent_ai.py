import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "patent_ai.py"


def load_module():
    spec = importlib.util.spec_from_file_location("patent_ai", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def commit(message="ordinary change", sha="abcdef0123456789"):
    return {"sha": sha, "commit": {"message": message}}


def test_t1_commit_tag_admits_without_network(monkeypatch):
    module = load_module()

    def unexpected_get(*args, **kwargs):
        raise AssertionError("T1 must not require an API call")

    monkeypatch.setattr(module, "gh_get", unexpected_get)
    result = module.check_triggers("token", "StegVerse-Labs/example", commit("[PATENT] governed gate"))

    assert result is not None
    assert result[0] == "T1-commit-tag"
    assert "[PATENT]" in result[1]


def test_t2_candidate_path_admits(monkeypatch):
    module = load_module()

    def fake_get(token, path, params=None):
        if path.endswith("/commits/abcdef0123456789"):
            return {"files": [{"filename": "patent_candidates/PAT-005.md"}]}
        raise AssertionError(f"unexpected API path: {path}")

    monkeypatch.setattr(module, "gh_get", fake_get)
    result = module.check_triggers("token", "StegVerse-Labs/example", commit())

    assert result == ("T2-candidate-path", "touched patent_candidates/PAT-005.md")


def test_t3_pr_label_admits(monkeypatch):
    module = load_module()

    def fake_get(token, path, params=None):
        if path.endswith("/commits/abcdef0123456789"):
            return {"files": [{"filename": "src/runtime.py"}]}
        if path.endswith("/commits/abcdef0123456789/pulls"):
            return [{"number": 17, "labels": [{"name": "patent-candidate"}]}]
        raise AssertionError(f"unexpected API path: {path}")

    monkeypatch.setattr(module, "gh_get", fake_get)
    result = module.check_triggers("token", "StegVerse-Labs/example", commit())

    assert result == ("T3-pr-label", "PR #17 labeled patent-candidate")


def test_no_positive_trigger_denies_candidate(monkeypatch):
    module = load_module()

    def fake_get(token, path, params=None):
        if path.endswith("/commits/abcdef0123456789"):
            return {"files": [{"filename": "src/runtime.py"}]}
        if path.endswith("/commits/abcdef0123456789/pulls"):
            return [{"number": 18, "labels": [{"name": "documentation"}]}]
        raise AssertionError(f"unexpected API path: {path}")

    monkeypatch.setattr(module, "gh_get", fake_get)
    assert module.check_triggers("token", "StegVerse-Labs/example", commit()) is None


def test_trigger_receipt_is_idempotent_and_traceable(tmp_path):
    module = load_module()
    (tmp_path / "queue").mkdir()

    first = module.write_trigger_receipt(
        tmp_path,
        "example-abcdef0",
        "StegVerse-Labs/example",
        "abcdef0123456789",
        "T1-commit-tag",
        "message contains [PATENT]",
    )
    second = module.write_trigger_receipt(
        tmp_path,
        "example-abcdef0",
        "StegVerse-Labs/example",
        "abcdef0123456789",
        "T1-commit-tag",
        "message contains [PATENT]",
    )

    receipt = (tmp_path / "queue" / "example-abcdef0.trigger.json").read_text(encoding="utf-8")
    assert first is True
    assert second is False
    assert '"sig": "patent-trigger-receipt:v1"' in receipt
    assert '"source": "StegVerse-Labs/example@abcdef0123456789"' in receipt
