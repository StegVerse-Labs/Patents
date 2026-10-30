"""Source-only checks for the v2 input manifest (small video primary, publisher original upstream); no data bytes."""
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

    def primary(self):
        mp4 = [e for e in self.v2["expected_sources"] if e["name"] == "DP_free_drop_video.mp4"]
        self.assertEqual(len(mp4), 1)
        return mp4[0]

    def test_small_video_is_primary_demonstration_input(self):
        mp4 = self.primary()
        old = [e for e in self.v1["expected_sources"] if e["name"] == "DP_free_drop_video.mp4"][0]
        for key, value in old.items():
            self.assertEqual(mp4[key], value)
        self.assertEqual(mp4["role"], "PRIMARY_DEMONSTRATION_INPUT")
        self.assertNotIn("superseded_entries", self.v2)
        self.assertNotIn("NOT_AUTHORITATIVE", json.dumps(self.v2))

    def test_primary_digest_present_or_not_computed_with_reason(self):
        mp4 = self.primary()
        if mp4["sha256"] is None:
            self.assertEqual(mp4["sha256_status"], "NOT_COMPUTED")
            self.assertTrue(mp4["sha256_not_computed_reason"])
        else:
            self.assertRegex(mp4["sha256"], r"^[0-9a-f]{64}$")

    def test_publisher_original_listed_as_upstream_reference(self):
        up = self.v2["upstream_sources"]
        self.assertEqual(len(up), 1)
        self.assertEqual(up[0]["role"], "UPSTREAM_SOURCE_REFERENCE")
        self.assertEqual(up[0]["size_bytes"], 7271648696)
        self.assertEqual(up[0]["sha256"], "8197492b6e244b28f7948cf7e5e74d3e198e1b1d39a78981ee607484d30c38d1")
        self.assertEqual(up[0]["source_url"], "https://data.mendeley.com/datasets/z4hvxjgtbz/2")

    def test_size_match_without_digest_never_passes(self):
        with tempfile.TemporaryDirectory() as d:
            with open(Path(d) / "DP_free_drop_video.mp4", "wb") as fh:
                fh.truncate(481804387)
            result = verify(Path(d), {"expected_sources": [self.primary()]})
            self.assertEqual(result["disposition"], "FAIL_CLOSED")
            self.assertEqual(result["results"][0]["reason"], "EXPECTED_DIGEST_UNVERIFIED")

    def test_other_entries_and_controls_unchanged(self):
        others = lambda m: [e for e in m["expected_sources"] if e["name"] != "DP_free_drop_video.mp4"]
        self.assertEqual(others(self.v1), others(self.v2))
        for key in ("classification", "runner_input_contract", "disposition", "publication_control"):
            self.assertEqual(self.v1[key], self.v2[key])
        self.assertFalse(self.v2["runner_input_contract"]["public_raw_data_distribution"])

    def test_non_video_sources_and_upstream_have_digests(self):
        rest = [e for e in self.v2["expected_sources"] if e["name"] != "DP_free_drop_video.mp4"]
        self.assertTrue(all(e["sha256"] for e in rest + self.v2["upstream_sources"]))

    def test_gate_fails_closed_without_private_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            result = verify(Path(d), self.v2)
            self.assertEqual(result["disposition"], "FAIL_CLOSED")
            self.assertTrue(all(r["reason"] == "MISSING_SOURCE" for r in result["results"]))


if __name__ == "__main__":
    unittest.main()
