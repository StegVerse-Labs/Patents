#!/usr/bin/env python3

import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "reconcile_publisher_family_status.py"
SPEC = importlib.util.spec_from_file_location("publisher_reconciler", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class PublisherFamilyReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.ledger = MODULE.load_json(MODULE.LEDGER)

    def test_reconcile_covers_all_eight_families_and_preserves_invariants(self):
        reconciled, changes = MODULE.reconcile(deepcopy(self.ledger))
        self.assertEqual(reconciled["schema_version"], "0.7")
        self.assertEqual(reconciled["dedicated_handoff_coverage"], 8)
        self.assertEqual(len(reconciled["families"]), 8)
        self.assertGreater(len(changes), 0)
        for key, expected in MODULE.EXPECTED_INVARIANTS.items():
            self.assertEqual(reconciled["portfolio_invariants"][key], expected)
        for family in reconciled["families"]:
            self.assertTrue(family["dedicated_handoff"].endswith("_MIRROR_HANDOFF.md"))
            self.assertIsNone(family["filing_receipt"])
            self.assertIsNone(family["application_number"])
            self.assertIsNone(family["actual_filing_date"])
            self.assertIsNone(family["nonprovisional_deadline"])
            self.assertEqual(family["filing_packet"], "not_authorized")
            self.assertEqual(family["human_filing"], "not_started")

    def test_rejects_nonzero_filing_invariant(self):
        ledger = deepcopy(self.ledger)
        ledger["portfolio_invariants"]["filed_families"] = 1
        with self.assertRaisesRegex(ValueError, "portfolio invariant changed"):
            MODULE.reconcile(ledger)

    def test_rejects_unsupported_family_identity(self):
        ledger = deepcopy(self.ledger)
        ledger["families"][0]["family_key"] = "invented_family"
        with self.assertRaisesRegex(ValueError, "family identity mismatch"):
            MODULE.reconcile(ledger)

    def test_status_guard_rejects_filing_activation(self):
        status = {
            "filed": True,
            "filing_receipt": None,
            "application_number": None,
            "actual_filing_date": None,
            "nonprovisional_deadline": None,
            "human_filing": "not_started",
            "filing_packet": "not_authorized",
        }
        with self.assertRaisesRegex(ValueError, "prohibited lifecycle activation"):
            MODULE.assert_fail_closed_status("example", status)

    def test_rendered_output_is_valid_json(self):
        reconciled, _ = MODULE.reconcile(deepcopy(self.ledger))
        rendered = json.dumps(reconciled)
        self.assertIsInstance(json.loads(rendered), dict)


if __name__ == "__main__":
    unittest.main()
