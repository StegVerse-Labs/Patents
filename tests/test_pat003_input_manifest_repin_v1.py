"""Source-only checks for the v2 input manifest repin; no recovered data bytes."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "research" / "pat003"
sys.path.insert(0, str(ROOT))
from private_input_gate_v1 import verify

V1 = ROOT / "input_manifest_v1.json"
V2 = ROOT / "input_manifest_v2.json"


class InputManifestV2(unittest.TestCase):
    def setUp(self):
        self.v1 = json.loads(V1.read_text())
        self.v2 = json.loads(V2.read_text())

    def test_supersedes_exact_v1_bytes(self):
        self.assertEqual(self.v2["supersedes"]["sha256"], hashlib.sha256(V1.read_bytes()).hexdigest())

    def test_mp4_repinned_to_publisher_original(self):
        mp4 = [e for e in self.v2["expected_sources"] if e["name"] == "DP_free_drop_video.mp4"]
        self.assertEqual(len(mp4), 1)
        self.assertEqual(mp4[0]["size_bytes"], 7271648696)
        self.assertEqual(mp4[0]["sha256"], "8197492b6e244b28f7948cf7e5e74d3e198e1b1d39a78981ee607484d30c38d1")
        self.assertEqual(mp4[0]["source_url"], "https://data.mendeley.com/datasets/z4hvxjgtbz/2")

    def test_superseded_entry_preserved(self):
        old = [e for e in self.v1["expected_sources"] if e["name"] == "DP_free_drop_video.mp4"][0]
        kept = self.v2["superseded_entries"][0]
        for key, value in old.items():
            self.assertEqual(kept[key], value)
        self.assertEqual(kept["status"], "NOT_AUTHORITATIVE")

    def test_other_entries_and_controls_unchanged(self):
        others = lambda m: [e for e in m["expected_sources"] if e["name"] != "DP_free_drop_video.mp4"]
        self.assertEqual(others(self.v1), others(self.v2))
        for key in ("classification", "runner_input_contract", "disposition", "publication_control"):
            self.assertEqual(self.v1[key], self.v2[key])
        self.assertFalse(self.v2["runner_input_contract"]["public_raw_data_distribution"])

    def test_every_v2_source_has_digest(self):
        self.assertTrue(all(e["sha256"] for e in self.v2["expected_sources"]))

    def test_gate_fails_closed_without_private_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            result = verify(Path(d), self.v2)
            self.assertEqual(result["disposition"], "FAIL_CLOSED")
            self.assertTrue(all(r["reason"] == "MISSING_SOURCE" for r in result["results"]))


if __name__ == "__main__":
    unittest.main()
