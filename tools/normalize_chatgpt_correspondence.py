#!/usr/bin/env python3
"""Normalize bounded ChatGPT correspondence into governed patent-intake records.

This utility preserves provenance and routing metadata only. It does not determine
inventorship, ownership, patentability, filing strategy, disclosure consequences,
filing status, application numbers, or deadlines.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"
CLASSIFICATION_VERSION = "1.0.0"
ALLOWED_ROLES = {"USER", "ASSISTANT", "COUNSEL", "SYSTEM", "UNKNOWN"}
KNOWN_FAMILIES = {
    "PAT-001", "PAT-002", "PAT-003", "PAT-004", "PAT-005",
    "Commit-Time Admissibility Gate",
    "Receipt-Based State Transition Validation",
    "Publisher Governed Disclosure Pipeline",
    "Application Correction Gate",
    "AI Output-to-Action Boundary",
    "Recoverability-Aware Execution Boundary",
    "Master-Records Reconstruction and Verification",
    "Multi-Entity Observer-Participant Admissibility",
}
RELATIONSHIPS = {
    "STANDALONE", "CONFIRMS", "NARROWS", "CONTRADICTS", "CORRECTS",
    "SUPERSEDES", "IS_SUPERSEDED_BY",
}
REVIEW_STATES = {
    "UNREVIEWED", "ROUTED_UNCONFIRMED", "USER_ATTRIBUTED",
    "CORROBORATION_PENDING", "CORROBORATED_BY_EXTERNAL_RECORD",
    "CONTRADICTED", "SUPERSEDED", "COUNSEL_REVIEW_PENDING",
    "COUNSEL_ATTRIBUTED", "OWNER_DECISION_INPUT_ONLY", "EXCLUDED",
}
CONFIDENTIALITY = {"PUBLIC", "INTERNAL", "COUNSEL_RESTRICTED", "PERSONAL_RESTRICTED", "EXCLUDED"}
CATEGORIES = {
    "INVENTION_CAPTURE", "CONCEPTION_CHRONOLOGY", "CONTRIBUTOR_ASSERTION",
    "CORROBORATION_LEAD", "PUBLIC_DISCLOSURE_LEAD", "IMPLEMENTATION_EVIDENCE_LEAD",
    "CLAIM_OR_LIMITATION_DRAFT", "WRITTEN_DESCRIPTION_SUPPORT", "ENABLEMENT_SUPPORT",
    "PRIOR_ART_DISTINCTION_HYPOTHESIS", "COUNSEL_QUESTION", "DRAWING_OR_FIGURE_INPUT",
    "OWNER_PREFERENCE", "FILING_CLERICAL_INPUT", "CONTRADICTION", "CORRECTION",
    "SUPERSESSION", "OUT_OF_SCOPE",
}


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "unclassified"


def fail(decision: str, reason: str) -> int:
    print(json.dumps({"decision": decision, "reason": reason}, sort_keys=True))
    return 2


def list_field(message: dict[str, Any], name: str) -> list[str]:
    value = message.get(name, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"{name} must be an array of strings")
    return list(dict.fromkeys(value))


def normalize(source: dict[str, Any], source_path: Path, root: Path, prior_receipt: str | None) -> dict[str, Any]:
    conversation_id = source.get("conversation_id")
    source_reference = source.get("source_reference")
    messages = source.get("messages")
    if not isinstance(conversation_id, str) or not conversation_id.strip():
        raise ValueError("missing stable conversation_id")
    if not isinstance(source_reference, str) or not source_reference.strip():
        raise ValueError("missing source_reference")
    if not isinstance(messages, list):
        raise ValueError("messages must be an array")

    ingested = datetime.now(timezone.utc).isoformat()
    records: list[dict[str, Any]] = []
    global_warnings: list[str] = []
    seen_ids: set[str] = set()

    for ordinal, raw in enumerate(messages, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"message {ordinal} must be an object")
        message_id = raw.get("message_id_or_ordinal", ordinal)
        stable_id = str(message_id)
        if stable_id in seen_ids:
            raise ValueError(f"duplicate message identifier: {stable_id}")
        seen_ids.add(stable_id)
        content = raw.get("content")
        if not isinstance(content, str) or not content.strip():
            raise ValueError(f"empty content for message {stable_id}")
        role = str(raw.get("author_role", "UNKNOWN")).upper()
        if role not in ALLOWED_ROLES:
            role = "UNKNOWN"

        families = list_field(raw, "related_families")
        categories = list_field(raw, "categories") or ["OUT_OF_SCOPE"]
        bad_categories = sorted(set(categories) - CATEGORIES)
        if bad_categories:
            raise ValueError(f"unknown categories for message {stable_id}: {bad_categories}")
        relationship = raw.get("relationship_status", "STANDALONE")
        review = raw.get("review_status", "UNREVIEWED")
        confidentiality = raw.get("confidentiality_class", "INTERNAL")
        if relationship not in RELATIONSHIPS:
            raise ValueError(f"invalid relationship_status for message {stable_id}")
        if review not in REVIEW_STATES:
            raise ValueError(f"invalid review_status for message {stable_id}")
        if confidentiality not in CONFIDENTIALITY:
            raise ValueError(f"invalid confidentiality_class for message {stable_id}")

        warnings = list_field(raw, "warnings")
        for family in families:
            if family not in KNOWN_FAMILIES:
                warnings.append(f"UNKNOWN_FAMILY_ROUTING:{family}")
        if role == "ASSISTANT" and (
            "CONTRIBUTOR_ASSERTION" in categories
            or review == "CORROBORATED_BY_EXTERNAL_RECORD"
            or list_field(raw, "external_corroboration_refs")
        ):
            warnings.append("ASSISTANT_CONTENT_NOT_INDEPENDENT_CORROBORATION")

        record = {
            "schema_version": SCHEMA_VERSION,
            "source_system": "ChatGPT",
            "conversation_id": conversation_id,
            "conversation_title": source.get("conversation_title"),
            "message_id_or_ordinal": message_id,
            "timestamp_utc_or_null": raw.get("timestamp_utc_or_null"),
            "author_role": role,
            "author_attribution_or_null": raw.get("author_attribution_or_null"),
            "source_reference": source_reference,
            "verbatim_content_path_or_inline_hash": raw.get("verbatim_content_path_or_inline_hash"),
            "content_sha256": sha256_bytes(content.encode("utf-8")),
            "ingested_utc": ingested,
            "classification_version": CLASSIFICATION_VERSION,
            "related_families": sorted(families),
            "categories": sorted(categories),
            "related_claims_or_limitations": list_field(raw, "related_claims_or_limitations"),
            "related_figures": list_field(raw, "related_figures"),
            "related_chronology_entries": list_field(raw, "related_chronology_entries"),
            "relationship_status": relationship,
            "related_message_refs": list_field(raw, "related_message_refs"),
            "review_status": review,
            "confidentiality_class": confidentiality,
            "external_corroboration_refs": list_field(raw, "external_corroboration_refs"),
            "warnings": sorted(set(warnings)),
        }
        records.append(record)
        global_warnings.extend(record["warnings"])

    base = root / "intake/chatgpt"
    normalized_path = base / "normalized" / f"{slug(conversation_id)}.jsonl"
    contradiction_path = base / "contradiction_reports" / f"{slug(conversation_id)}.json"
    receipt_path = base / "ingestion_receipts" / f"{slug(conversation_id)}.json"
    for path in (normalized_path, contradiction_path, receipt_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    normalized_text = "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in records)
    normalized_path.write_text(normalized_text, encoding="utf-8")

    family_indexes: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        for family in record["related_families"]:
            family_indexes.setdefault(family, []).append({
                "conversation_id": conversation_id,
                "message_id_or_ordinal": record["message_id_or_ordinal"],
                "content_sha256": record["content_sha256"],
                "review_status": record["review_status"],
                "warnings": record["warnings"],
            })
    for family, entries in sorted(family_indexes.items()):
        path = base / "family_indexes" / f"{slug(family)}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"family": family, "routing_only": True, "records": entries}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    contradiction_records = [
        {
            "message_id_or_ordinal": r["message_id_or_ordinal"],
            "relationship_status": r["relationship_status"],
            "related_message_refs": r["related_message_refs"],
        }
        for r in records
        if r["relationship_status"] in {"CONTRADICTS", "CORRECTS", "SUPERSEDES", "IS_SUPERSEDED_BY"}
    ]
    contradiction_path.write_text(json.dumps({"conversation_id": conversation_id, "records": contradiction_records}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    receipt = {
        "schema_version": SCHEMA_VERSION,
        "conversation_id": conversation_id,
        "source_path": str(source_path),
        "source_sha256": sha256_bytes(source_path.read_bytes()),
        "normalized_path": str(normalized_path.relative_to(root)),
        "normalized_sha256": sha256_bytes(normalized_path.read_bytes()),
        "normalized_message_count": len(records),
        "family_index_count": len(family_indexes),
        "contradiction_record_count": len(contradiction_records),
        "generated_utc": ingested,
        "decision": "NORMALIZED_WITH_WARNINGS" if global_warnings else "NORMALIZED",
        "prior_receipt_sha256": prior_receipt,
    }
    receipt["receipt_sha256"] = sha256_bytes(canonical_json(receipt))
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Bounded ChatGPT JSON export or excerpt")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--prior-receipt-sha256", default=None)
    args = parser.parse_args()
    source_path = Path(args.source).resolve()
    root = Path(args.root).resolve()
    if not source_path.is_file():
        return fail("REFUSED_SOURCE_INVALID", "source file does not exist")
    try:
        source = json.loads(source_path.read_text(encoding="utf-8"))
        if not isinstance(source, dict):
            raise ValueError("source root must be an object")
        receipt = normalize(source, source_path, root, args.prior_receipt_sha256)
    except json.JSONDecodeError as exc:
        return fail("REFUSED_SOURCE_INVALID", str(exc))
    except ValueError as exc:
        return fail("REFUSED_PROVENANCE_INCOMPLETE", str(exc))
    except OSError as exc:
        return fail("REFUSED_SOURCE_INVALID", str(exc))
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
