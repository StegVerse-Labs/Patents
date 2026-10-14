"""Synthetic-only positive and negative controls for PAT-003 v1 adapter."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from double_pendulum_adapter_v1 import Series, EvidenceRejected, align, hash_source

D = "a" * 64

def series(**changes):
    values = dict(trial="trial1", source_sha256=D, times=(0., .01, .02, .03),
                  values=(0., 1., 2., 3.), clock="synthetic-clock", calibration="fixture-cal")
    values.update(changes)
    return Series(**values)

class TestAdapter(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(len(align(series(), series(), tolerance=.001, clock_mapping_verified=True)), 4)
    def test_missing_clock_authority(self):
        with self.assertRaises(EvidenceRejected):
            align(series(), series(), tolerance=.001)
    def test_cross_trial_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(), series(trial="trial2"), tolerance=.001, clock_mapping_verified=True)
    def test_different_clock_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(), series(clock="another"), tolerance=.001, clock_mapping_verified=True)
    def test_missing_calibration_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(calibration=""), series(), tolerance=.001, clock_mapping_verified=True)
    def test_altered_timestamp_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(times=(0., .01, .009, .03)), series(), tolerance=.001, clock_mapping_verified=True)
    def test_missing_frame_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(times=(0., .01, .02)), series(values=(0., 1.)), tolerance=.001, clock_mapping_verified=True)
    def test_bad_digest_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(source_sha256="invalid"), series(), tolerance=.001, clock_mapping_verified=True)
    def test_nonfinite_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(values=(0., 1., float("nan"), 3.)), series(), tolerance=.001, clock_mapping_verified=True)
    def test_nonoverlap_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(), series(times=(10., 11., 12., 13.)), tolerance=.001, clock_mapping_verified=True)
    def test_bad_tolerance_rejected(self):
        with self.assertRaises(EvidenceRejected):
            align(series(), series(), tolerance=0, clock_mapping_verified=True)
    def test_hash(self):
        self.assertEqual(len(hash_source(Path(__file__))), 64)

if __name__ == "__main__":
    unittest.main()
