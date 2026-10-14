import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
from governance_boundary_v1 import Request, Return, evaluate

H = "a"*64
def request():
    return Request(H, 1, 2, 3, "RECOMPUTE_PIXEL", H, H, H, "OPTICAL-PHYSICAL-STATE-REPLAY-RESEARCH-001")

class GovernanceBoundaryTests(unittest.TestCase):
    def test_absent_return_fails_closed(self):
        self.assertEqual(evaluate(request())[0], "FAIL_CLOSED")

    def test_spoofed_allow_fails_closed(self):
        d = evaluate(request())[2]
        ret = Return(d, "ALLOW", "CHANGED", "ledger", "evidence", True)
        self.assertEqual(evaluate(request(), ret)[1], "SOVEREIGN_RETURN_VERIFIER_NOT_INTEGRATED")

    def test_spoofed_deny_fails_closed(self):
        d = evaluate(request())[2]
        ret = Return(d, "DENY", "UNCHANGED", "ledger", "evidence", True)
        self.assertEqual(evaluate(request(), ret)[0], "FAIL_CLOSED")

    def test_wrong_request_binding(self):
        ret = Return("b"*64, "ALLOW", "CHANGED", "ledger", "evidence", True)
        self.assertEqual(evaluate(request(), ret)[1], "RETURN_NOT_BOUND_TO_REQUEST")

    def test_missing_authority_reference(self):
        d = evaluate(request())[2]
        ret = Return(d, "ALLOW", "CHANGED", "", "evidence", True)
        self.assertEqual(evaluate(request(), ret)[1], "INCOMPLETE_AUTHORITY_EVIDENCE")

    def test_missing_authentication(self):
        d = evaluate(request())[2]
        ret = Return(d, "ALLOW", "CHANGED", "ledger", "evidence", False)
        self.assertEqual(evaluate(request(), ret)[1], "AUTHENTICITY_NOT_ESTABLISHED")

    def test_malformed_return(self):
        self.assertEqual(evaluate(request(), {"disposition":"ALLOW"})[0], "FAIL_CLOSED")

    def test_invalid_source_digest_rejected(self):
        bad = Request("bad", 1, 2, 3, "RECOMPUTE_PIXEL", H, H, H, "task")
        with self.assertRaises(ValueError):
            evaluate(bad)

if __name__ == "__main__":
    unittest.main()
