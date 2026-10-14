"""PAT-003 bounded-memory replay and adversarial research controls."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from pixel_stream_v1 import replay, benchmark

SOURCE = "a" * 64

class PixelStreamTests(unittest.TestCase):
    def test_unchanged_reuse_separately_allowed(self):
        result = list(replay([[[7]], [[7]]], source_sha256=SOURCE))
        self.assertEqual((result[-1].allow, result[-1].deny, result[-1].reuse_allow), (0, 1, 1))
        self.assertTrue(result[-1].reconstruction_equal)

    def test_reuse_denied_fails_closed(self):
        result = list(replay([[[7]], [[7]]], source_sha256=SOURCE, reuse_authorized=False))
        self.assertEqual((result[-1].deny, result[-1].fail_closed), (1, 1))
        self.assertFalse(result[-1].reconstruction_equal)

    def test_changed_pixel_computes(self):
        result = list(replay([[[7]], [[8]]], source_sha256=SOURCE))
        self.assertEqual(result[-1].allow, 1)
        self.assertTrue(result[-1].reconstruction_equal)

    def test_unverified_dependency(self):
        result = list(replay([[[7]]], source_sha256=SOURCE, dependencies_verified=False))
        self.assertEqual(result[0].fail_closed, 1)
        self.assertFalse(result[0].reconstruction_equal)

    def test_invalid_pixel(self):
        result = list(replay([[[300]]], source_sha256=SOURCE))
        self.assertEqual(result[0].fail_closed, 1)

    def test_tampered_pixel_changes_root(self):
        a = list(replay([[[1]], [[2]]], source_sha256=SOURCE))[-1].receipt_root
        b = list(replay([[[1]], [[3]]], source_sha256=SOURCE))[-1].receipt_root
        self.assertNotEqual(a, b)

    def test_source_binding_changes_root(self):
        a = list(replay([[[1]]], source_sha256=SOURCE))[-1].receipt_root
        b = list(replay([[[1]]], source_sha256="b"*64))[-1].receipt_root
        self.assertNotEqual(a, b)

    def test_determinism(self):
        frames = [[[1, 2]], [[1, 3]]]
        self.assertEqual(list(replay(frames, source_sha256=SOURCE)),
                         list(replay(frames, source_sha256=SOURCE)))

    def test_frame_count_missing(self):
        with self.assertRaises(ValueError):
            list(replay([[[1]]], source_sha256=SOURCE, expected_frames=2))

    def test_dimensions_rejected(self):
        with self.assertRaises(ValueError):
            list(replay([[[1]], [[1, 2]]], source_sha256=SOURCE))

    def test_benchmark(self):
        data = benchmark([[[1, 2]], [[1, 3]]], source_sha256=SOURCE)
        self.assertTrue(data["reconstruction_equal"])
        self.assertEqual(data["deny"], 1)
        self.assertEqual(data["allow"], 3)

if __name__ == "__main__":
    unittest.main()
