#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SHA40 = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_PREDICATES = {
    "DISTINCT_SECOND_ACTIVE_NODE_OBSERVED": {"P1-L17", "P1-L18"},
    "NETWORK_PRESENT_PROVEN": {"P1-L17", "P1-L18"},
    "REAL_FRAGMENTATION_AND_REFORMATION_OBSERVED": {"P1-L18", "P1-L20", "P1-L21"},
    "EXACT_MULTI_NODE_REPLAY_RECONSTRUCTION_EQUALITY": {"P1-L18", "P1-L20", "P1-L21"},
}
REQUIRED_FIELDS = {
    "source_repository", "source_path", "source_commit_sha", "source_blob_sha",
    "runtime_or_physical_receipt_ids", "artifact_sha256", "node_identities",
    "interlock_identities", "transition_lineage", "negative_or_fail_closed_evidence",
    "reconstruction_output", "observation_date", "disclosure_chronology_implications",
}


def validate(path: Path) -> dict:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"decision": "PAT001_STEGOS_PROOF_MATRIX_INVALID", "errors": [str(exc)]}

    if data.get("family_id") != "PAT-001":
        errors.append("family_id must be PAT-001")
    if data.get("goal_task_id") != "STEGOS-NODE-MANIFOLD-001":
        errors.append("goal_task_id mismatch")
    if data.get("physical_proof_claimed") is not False:
        errors.append("physical_proof_claimed must remain false until authentic retained proof is ingested")
    if data.get("claim_rewriting_on_ingestion_permitted") is not False:
        errors.append("claim rewriting on ingestion must be prohibited")
    if not SHA40.fullmatch(str(data.get("software_anchor_commit", ""))):
        errors.append("software_anchor_commit invalid")

    required_declared = set(data.get("required_evidence_package_fields", []))
    if required_declared != REQUIRED_FIELDS:
        errors.append("required_evidence_package_fields drift")

    seen: set[str] = set()
    for item in data.get("predicates", []):
        predicate = item.get("predicate")
        if predicate not in REQUIRED_PREDICATES:
            errors.append(f"unexpected predicate: {predicate}")
            continue
        if predicate in seen:
            errors.append(f"duplicate predicate: {predicate}")
        seen.add(predicate)
        if set(item.get("supports_candidate_limitations", [])) != REQUIRED_PREDICATES[predicate]:
            errors.append(f"limitation mapping drift: {predicate}")
        evidence = item.get("minimum_evidence")
        if not isinstance(evidence, dict) or set(evidence) != REQUIRED_FIELDS:
            errors.append(f"minimum_evidence field drift: {predicate}")
        status = item.get("status")
        if status not in {"PENDING_AUTHENTIC_RETAINED_EVIDENCE", "AUTHENTIC_RETAINED_EVIDENCE_INGESTED"}:
            errors.append(f"invalid status: {predicate}")
        if status == "AUTHENTIC_RETAINED_EVIDENCE_INGESTED":
            scalar_required = ["source_repository", "source_path", "source_commit_sha", "source_blob_sha", "observation_date"]
            for field in scalar_required:
                if not evidence.get(field):
                    errors.append(f"completed predicate missing {field}: {predicate}")
            for field in ["runtime_or_physical_receipt_ids", "artifact_sha256", "node_identities", "interlock_identities", "transition_lineage"]:
                if not evidence.get(field):
                    errors.append(f"completed predicate missing {field}: {predicate}")
    if seen != set(REQUIRED_PREDICATES):
        errors.append("required predicate set incomplete")

    rules = data.get("ingestion_rules", {})
    for key in [
        "source_only_or_ci_only_proof_is_sufficient",
        "deterministic_fixture_substitutes_for_physical_evidence",
        "single_node_result_substitutes_for_multi_node_proof",
        "claim_text_may_be_rewritten_to_fit_observed_result",
        "patentability_determined",
        "inventorship_determined",
        "filing_authorized",
    ]:
        if rules.get(key) is not False:
            errors.append(f"ingestion_rules.{key} must be false")
    if rules.get("predicate_status_upgrade_requires_authentic_retained_artifacts") is not True:
        errors.append("authentic retained artifact requirement must be true")

    return {
        "decision": "PAT001_STEGOS_PROOF_MATRIX_VALID" if not errors else "PAT001_STEGOS_PROOF_MATRIX_INVALID",
        "predicate_count": len(seen),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    result = validate(args.record)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "PAT001_STEGOS_PROOF_MATRIX_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
