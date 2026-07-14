import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_patent_families.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("render_patent_families", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_master_claim_data_cross_references_are_valid():
    renderer = load_renderer()
    data = renderer.load_data(ROOT / "data" / "master_claims.json")
    assert len(data["families"]) == 4
    assert data["families"][0]["family_id"] == "PAT-001"


def test_each_family_renders_with_working_claims():
    renderer = load_renderer()
    data = renderer.load_data(ROOT / "data" / "master_claims.json")
    claims = {claim["claim_id"]: claim for claim in data["claims"]}
    for family in data["families"]:
        rendered = renderer.render_family(family, claims)
        assert family["family_id"] in rendered
        assert "## Working claims" in rendered
        for claim_id in family["claim_ids"]:
            assert claim_id in rendered
