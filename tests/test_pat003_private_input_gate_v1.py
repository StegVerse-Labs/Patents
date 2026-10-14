"""Source-only input gate controls with no recovered data bytes."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from private_input_gate_v1 import verify

class InputGateControls(unittest.TestCase):
    def test_missing_source(self):
        with tempfile.TemporaryDirectory() as d:
            result = verify(Path(d), {"expected_sources":[{"name":"source.bin","size_bytes":3,"sha256":"a"*64}]})
            self.assertEqual(result["results"][0]["reason"], "MISSING_SOURCE")
            self.assertEqual(result["disposition"], "FAIL_CLOSED")
    def test_size_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/"source.bin").write_bytes(b"x")
            result = verify(Path(d), {"expected_sources":[{"name":"source.bin","size_bytes":3,"sha256":"a"*64}]})
            self.assertEqual(result["results"][0]["reason"], "SIZE_MISMATCH")
    def test_unverified_video_digest(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/"source.bin").write_bytes(b"xyz")
            result = verify(Path(d), {"expected_sources":[{"name":"source.bin","size_bytes":3,"sha256":None}]})
            self.assertEqual(result["results"][0]["reason"], "EXPECTED_DIGEST_UNVERIFIED")
    def test_digest_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/"source.bin").write_bytes(b"xyz")
            result = verify(Path(d), {"expected_sources":[{"name":"source.bin","size_bytes":3,"sha256":"a"*64}]})
            self.assertEqual(result["results"][0]["reason"], "DIGEST_MISMATCH")
    def test_verified_source(self):
        import hashlib
        with tempfile.TemporaryDirectory() as d:
            (Path(d)/"source.bin").write_bytes(b"xyz")
            result = verify(Path(d), {"expected_sources":[{"name":"source.bin","size_bytes":3,"sha256":hashlib.sha256(b"xyz").hexdigest()}]})
            self.assertEqual(result["disposition"], "ALLOW_SOURCE_BYTES_ONLY")
if __name__ == "__main__":
    unittest.main()
