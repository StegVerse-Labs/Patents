import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from pixel_verify_v1 import verify_replay, compare_bounded_sample, adversarial_frame_commitment

S = "c" * 64

class PixelVerifyTests(unittest.TestCase):
    def test_aggregate_counts_and_equality(self):
        r = verify_replay([[[1,2]], [[1,3]], [[1,3]]], source_sha256=S, expected_frames=3)
        self.assertEqual(r["totals"], {"ALLOW": 3, "DENY": 3, "FAIL_CLOSED": 0, "REUSE_ALLOW": 3})
        self.assertTrue(r["reconstruction_equal"])

    def test_reuse_fail_closed(self):
        r = verify_replay([[[1]], [[1]]], source_sha256=S, reuse_authorized=False)
        self.assertEqual(r["totals"]["FAIL_CLOSED"], 1)
        self.assertFalse(r["reconstruction_equal"])

    def test_source_integrity_changes_root(self):
        a = verify_replay([[[1]]], source_sha256=S)["last_root"]
        b = verify_replay([[[1]]], source_sha256="d"*64)["last_root"]
        self.assertNotEqual(a,b)

    def test_frame_reordering_changes_commitment(self):
        self.assertNotEqual(adversarial_frame_commitment([[[1]], [[2]]]),
                            adversarial_frame_commitment([[[2]], [[1]]]))

    def test_frame_modification_changes_commitment(self):
        self.assertNotEqual(adversarial_frame_commitment([[[1]], [[2]]]),
                            adversarial_frame_commitment([[[1]], [[3]]]))

    def test_missing_frame_detected(self):
        with self.assertRaises(ValueError):
            verify_replay([[[1]]], source_sha256=S, expected_frames=2)

    def test_comparative_harness(self):
        r = compare_bounded_sample([[[1]], [[1]]], source_sha256=S)
        self.assertTrue(r["baseline_equal"])
        self.assertTrue(r["reconstruction_equal"])
        self.assertFalse(r["decoder_cost_included"])
        self.assertFalse(r["authentic_governance"])

    def test_unverified_dependencies(self):
        r = verify_replay([[[1]]], source_sha256=S, dependencies_verified=False)
        self.assertFalse(r["reconstruction_equal"])
        self.assertEqual(r["totals"]["FAIL_CLOSED"], 1)

if __name__ == "__main__":
    unittest.main()
