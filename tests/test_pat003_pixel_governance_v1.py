"""Deterministic positive and adversarial controls for PAT-003 pixel research."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from pixel_governance_v1 import execute, summarize, ALLOW, DENY, FAIL_CLOSED

SOURCE = "a" * 64

class PixelGovernanceTests(unittest.TestCase):
    def test_replay_matches_observations(self):
        frames = [[[1, 2], [3, 4]], [[1, 2], [3, 5]], [[1, 2], [3, 5]]]
        output, receipts = execute(frames, source_sha256=SOURCE)
        self.assertEqual(output, tuple(tuple(tuple(row) for row in frame) for frame in frames))
        self.assertEqual(summarize(receipts), {ALLOW: 5, DENY: 7, FAIL_CLOSED: 0})

    def test_temporal_advance_without_change_denies_recomputation(self):
        _, receipts = execute([[[4]], [[4]]], source_sha256=SOURCE)
        self.assertEqual([r.disposition for r in receipts], [ALLOW, DENY])
        self.assertNotEqual(receipts[0].receipt_digest, receipts[1].receipt_digest)

    def test_changed_pixel_allowed(self):
        _, receipts = execute([[[4]], [[5]]], source_sha256=SOURCE)
        self.assertEqual(receipts[-1].disposition, ALLOW)

    def test_unverified_dependency_fails_closed(self):
        output, receipts = execute([[[4]]], source_sha256=SOURCE, dependencies_verified=False)
        self.assertEqual(output[0][0][0], None)
        self.assertEqual(receipts[0].disposition, FAIL_CLOSED)

    def test_invalid_pixel_fails_closed(self):
        output, receipts = execute([[[256]]], source_sha256=SOURCE)
        self.assertIsNone(output[0][0][0])
        self.assertEqual(receipts[0].disposition, FAIL_CLOSED)

    def test_source_binding_changes_receipts(self):
        a = execute([[[2]]], source_sha256=SOURCE)[1][0].receipt_digest
        b = execute([[[2]]], source_sha256="b"*64)[1][0].receipt_digest
        self.assertNotEqual(a, b)

    def test_deterministic_replay(self):
        a = execute([[[2]], [[2]]], source_sha256=SOURCE)
        b = execute([[[2]], [[2]]], source_sha256=SOURCE)
        self.assertEqual(a, b)

    def test_dimension_change_rejected(self):
        with self.assertRaises(ValueError):
            execute([[[1]], [[1, 2]]], source_sha256=SOURCE)

    def test_bad_source_rejected(self):
        with self.assertRaises(ValueError):
            execute([[[1]]], source_sha256="not-a-digest")

if __name__ == "__main__":
    unittest.main()
