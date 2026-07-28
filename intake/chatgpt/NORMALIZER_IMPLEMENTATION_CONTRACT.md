# Portfolio ChatGPT Correspondence Normalizer — Implementation Contract

## Purpose

Define the executable behavior required to transform bounded ChatGPT exports or excerpts into governed patent-intake records without inventing facts or promoting assistant-authored text into evidence.

## Required executable

```text
tools/normalize_chatgpt_correspondence.py
```

## Required inputs

A JSON object containing:

```text
conversation_id
conversation_title (optional)
source_reference
messages[]
```

Each message must contain:

```text
message_id_or_ordinal
author_role
content
```

Optional classification fields may include related families, categories, claims, figures, chronology entries, relationship status, related message references, review status, confidentiality class, corroboration references, and warnings.

## Required behavior

1. Reject a source with no stable conversation identifier.
2. Reject messages with empty content.
3. Preserve message order and stable source references.
4. Hash the complete source and each message body with SHA-256.
5. Normalize every item against `intake/chatgpt/correspondence-record.schema.json`.
6. Preserve user, assistant, counsel, system, and unknown author roles distinctly.
7. Warn when assistant-authored content is classified as contributor testimony or independent corroboration.
8. Preserve corrections, contradictions, narrowing, confirmation, and supersession links.
9. Generate one JSONL normalized conversation record.
10. Generate per-family indexes without establishing legal family identity.
11. Generate contradiction and correction reports.
12. Generate a hash-chained ingestion receipt.
13. Fail closed when schema validation, source integrity, or required provenance fails.

## Required outputs

```text
intake/chatgpt/normalized/<conversation-id>.jsonl
intake/chatgpt/family_indexes/<family-slug>.json
intake/chatgpt/contradiction_reports/<conversation-id>.json
intake/chatgpt/ingestion_receipts/<conversation-id>.json
```

## Receipt fields

```text
schema_version
conversation_id
source_path
source_sha256
normalized_path
normalized_sha256
normalized_message_count
family_index_count
contradiction_record_count
generated_utc
decision
prior_receipt_sha256
receipt_sha256
```

## Allowed decisions

```text
NORMALIZED
NORMALIZED_WITH_WARNINGS
REFUSED_SOURCE_INVALID
REFUSED_SCHEMA_INVALID
REFUSED_PROVENANCE_INCOMPLETE
```

## Legal and governance boundary

The normalizer must not determine inventorship, ownership, patentability, disclosure consequences, family scope, filing strategy, filing authorization, filing status, application numbers, or deadlines.

Family classification is routing metadata only. User statements remain attributable assertions unless corroborated. Assistant-authored text remains drafting, synthesis, analytical input, or an evidence lead. Counsel material may be treated as counsel output only when identity and attribution are preserved.

## Required tests

```text
tests/test_correspondence_intake.py
```

Coverage must include:

- valid bounded export;
- missing conversation identifier refusal;
- empty message refusal;
- stable message hashing;
- assistant-corroboration warning;
- unknown family warning;
- contradiction-link preservation;
- confidentiality preservation;
- deterministic family indexes;
- receipt hash verification;
- refusal without lifecycle mutation.

## Current status

```text
contract: INSTALLED
executable: NOT_INSTALLED
regression tests: NOT_INSTALLED
authoritative execution: NOT_RUN
current decision: FAIL_CLOSED_IMPLEMENTATION_PENDING
```
