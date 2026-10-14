import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from first_video_dual_lane_v1 import compare

H = "e"*64

class FirstVideoDualLaneTests(unittest.TestCase):
    def test_exact_three_way_equality(self):
        r = compare([[[1,2]], [[1,2]], [[2,2]]], source_sha256=H)
        self.assertEqual((r["original_vs_frame_mismatches"], r["original_vs_manifold_mismatches"], r["frame_vs_manifold_mismatches"]), (0,0,0))
        self.assertEqual(r["manifold_recompute_deny"], 3)
        self.assertEqual(r["manifold_reuse_allow"], 3)
        self.assertEqual(r["frame_receipt_count"], 3)

    def test_reuse_not_authorized_breaks_equivalence(self):
        r = compare([[[1]], [[1]]], source_sha256=H, reuse_authorized=False)
        self.assertIsNone(r["original_vs_manifold_mismatches"])
        self.assertEqual(r["manifold_fail_closed"], 1)

    def test_unverified_dependencies_break_equivalence(self):
        r = compare([[[1]]], source_sha256=H, dependencies_verified=False)
        self.assertIsNone(r["frame_vs_manifold_mismatches"])

    def test_deterministic_roots(self):
        a = compare([[[1]], [[2]]], source_sha256=H)
        b = compare([[[1]], [[2]]], source_sha256=H)
        self.assertEqual(a["frame_chain_root"], b["frame_chain_root"])
        self.assertEqual(a["manifold_chain_root"], b["manifold_chain_root"])

    def test_change_alters_roots(self):
        a = compare([[[1]], [[2]]], source_sha256=H)
        b = compare([[[1]], [[3]]], source_sha256=H)
        self.assertNotEqual(a["frame_chain_root"], b["frame_chain_root"])
        self.assertNotEqual(a["manifold_chain_root"], b["manifold_chain_root"])

    def test_frame_shape_rejected(self):
        with self.assertRaises(ValueError):
            compare([[[1]], [[1,2]]], source_sha256=H)

    def test_invalid_pixel_rejected(self):
        with self.assertRaises(ValueError):
            compare([[[256]]], source_sha256=H)

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            compare([], source_sha256=H)

    def test_cost_scope_explicit(self):
        r = compare([[[1]]], source_sha256=H)
        self.assertFalse(r["decoder_cost_included"])
        self.assertFalse(r["authentic_governance_verified"])
        self.assertGreaterEqual(r["frame_lane_ns"], 0)
        self.assertGreaterEqual(r["manifold_lane_ns"], 0)

if __name__ == "__main__":
    unittest.main()
