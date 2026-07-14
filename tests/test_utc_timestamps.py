import datetime as dt
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_patent_watcher_uses_timezone_aware_z_normalized_utc():
    watcher = load_module("patent_ai", ROOT / "tools" / "patent_ai.py")
    value = watcher.utc_now()
    rendered = watcher.utc_iso(value)

    assert value.tzinfo is not None
    assert value.utcoffset() == dt.timedelta(0)
    assert rendered.endswith("Z")
    assert "+00:00Z" not in rendered
    assert dt.datetime.fromisoformat(rendered.replace("Z", "+00:00")).utcoffset() == dt.timedelta(0)


def test_runtime_sources_do_not_use_deprecated_naive_utcnow():
    for relative in ["tools/patent_ai.py", "tools/filing_packet_emitter.py"]:
        source = (ROOT / relative).read_text(encoding="utf-8")
        assert "datetime.utcnow" not in source
        assert ".utcnow(" not in source


def test_emitter_manifest_timestamp_expression_is_z_normalized():
    source = (ROOT / "tools" / "filing_packet_emitter.py").read_text(encoding="utf-8")
    assert 'dt.datetime.now(dt.timezone.utc)' in source
    assert '.replace("+00:00", "Z")' in source
