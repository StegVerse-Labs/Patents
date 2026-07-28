import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "normalize_chatgpt_correspondence.py"
spec = importlib.util.spec_from_file_location("normalizer", MODULE_PATH)
normalizer = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(normalizer)


class CorrespondenceNormalizerTests(unittest.TestCase):
    def source(self):
        return {
            "conversation_id": "conv-001",
            "conversation_title": "PAT-005 development",
            "source_reference": "chatgpt-export:conv-001",
            "messages": [
                {
                    "message_id_or_ordinal": "m1",
                    "author_role": "USER",
                    "content": "I conceived a destination-bound continuity gate.",
                    "related_families": ["PAT-005"],
                    "categories": ["INVENTION_CAPTURE", "CONTRIBUTOR_ASSERTION"],
                    "review_status": "USER_ATTRIBUTED",
                    "confidentiality_class": "COUNSEL_RESTRICTED",
                },
                {
                    "message_id_or_ordinal": "m2",
                    "author_role": "ASSISTANT",
                    "content": "Draft claim language follows.",
                    "related_families": ["PAT-005"],
                    "categories": ["CONTRIBUTOR_ASSERTION"],
                    "review_status": "CORROBORATED_BY_EXTERNAL_RECORD",
                    "external_corroboration_refs": ["repo:example"],
                    "relationship_status": "CORRECTS",
                    "related_message_refs": ["m1"],
                    "confidentiality_class": "INTERNAL",
                },
            ],
        }

    def run_normalize(self, source):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "source.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            receipt = normalizer.normalize(source, path, root, None)
            normalized = root / receipt["normalized_path"]
            records = [json.loads(line) for line in normalized.read_text(encoding="utf-8").splitlines()]
            receipt_file = root / "intake/chatgpt/ingestion_receipts/conv-001.json"
            stored_receipt = json.loads(receipt_file.read_text(encoding="utf-8"))
            return receipt, records, stored_receipt, root

    def test_valid_bounded_export_and_hashes(self):
        receipt, records, stored, _ = self.run_normalize(self.source())
        self.assertEqual(receipt["decision"], "NORMALIZED_WITH_WARNINGS")
        self.assertEqual(receipt["normalized_message_count"], 2)
        self.assertEqual(records[0]["content_sha256"], hashlib.sha256(self.source()["messages"][0]["content"].encode()).hexdigest())
        expected = dict(stored)
        receipt_hash = expected.pop("receipt_sha256")
        self.assertEqual(receipt_hash, normalizer.sha256_bytes(normalizer.canonical_json(expected)))

    def test_missing_conversation_identifier_refused(self):
        source = self.source()
        source["conversation_id"] = ""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "conversation_id"):
                normalizer.normalize(source, path, Path(tmp), None)

    def test_empty_message_refused(self):
        source = self.source()
        source["messages"][0]["content"] = ""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "empty content"):
                normalizer.normalize(source, path, Path(tmp), None)

    def test_assistant_corroboration_warning_and_relationship_preserved(self):
        _, records, _, _ = self.run_normalize(self.source())
        self.assertIn("ASSISTANT_CONTENT_NOT_INDEPENDENT_CORROBORATION", records[1]["warnings"])
        self.assertEqual(records[1]["relationship_status"], "CORRECTS")
        self.assertEqual(records[1]["related_message_refs"], ["m1"])

    def test_unknown_family_warning_and_confidentiality_preserved(self):
        source = self.source()
        source["messages"][0]["related_families"].append("Unknown Family")
        _, records, _, _ = self.run_normalize(source)
        self.assertIn("UNKNOWN_FAMILY_ROUTING:Unknown Family", records[0]["warnings"])
        self.assertEqual(records[0]["confidentiality_class"], "COUNSEL_RESTRICTED")

    def test_deterministic_family_index_order(self):
        source = self.source()
        source["messages"][0]["related_families"] = ["PAT-005", "PAT-001"]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "source.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            normalizer.normalize(source, path, root, None)
            first = (root / "intake/chatgpt/family_indexes/pat-005.json").read_text()
            normalizer.normalize(source, path, root, None)
            second = (root / "intake/chatgpt/family_indexes/pat-005.json").read_text()
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
