# Portfolio-Wide ChatGPT Correspondence Intake Contract

## Purpose

This contract governs intake of pertinent ChatGPT-created correspondence into the StegVerse patent preparation system. It applies to every numbered patent family and every controlled Publisher-origin candidate.

The intake layer preserves reconstructable provenance from conversation to invention capture, chronology, evidence mapping, drafting, counsel review, drawings, owner disposition, and later filing support without treating assistant-generated content as independent factual proof or legal advice.

## Covered families

### Numbered families

```text
PAT-001
PAT-002
PAT-003
PAT-004
PAT-005
```

### Publisher-origin controlled candidates

```text
Commit-Time Admissibility Gate
Receipt-Based State Transition Validation
Publisher Governed Disclosure Pipeline
Application Correction Gate
AI Output-to-Action Boundary
Recoverability-Aware Execution Boundary
Master-Records Reconstruction and Verification
Multi-Entity Observer-Participant Admissibility
```

A correspondence item may map to zero, one, or multiple families. Classification does not merge, split, abandon, file, publish, or establish legal family identity.

## Intake sources

Permitted source forms include:

- complete ChatGPT conversation exports;
- bounded conversation excerpts;
- user messages and corrections;
- assistant responses and generated drafts;
- user confirmations or rejections of assistant language;
- correspondence concerning attached images, diagrams, files, code, or public links;
- counsel correspondence preserved with attributable identity and source context;
- repository records generated from a ChatGPT session when their transition path is recorded.

Sensitive or unrelated content must be excluded, redacted, or access-restricted. Counsel-facing packets should contain only pertinent material.

## Required provenance fields

Every normalized message record must preserve:

```text
source_system
conversation_id
conversation_title
message_id_or_ordinal
timestamp_utc_or_null
author_role
author_attribution_or_null
source_reference
verbatim_content_path_or_inline_hash
content_sha256
ingested_utc
classification_version
related_families
related_claims_or_limitations
related_figures
related_chronology_entries
relationship_status
review_status
confidentiality_class
```

## Author-role treatment

### User-authored factual statement

May be recorded as an attributable factual assertion, conception statement, chronology statement, correction, confirmation, or disclosure lead. It is not automatically corroborated and must retain uncertainty where applicable.

### Assistant-authored material

May be recorded as synthesis, drafting, analytical lead, proposed embodiment, proposed claim language, question, or organizational output. It is not independent corroboration, inventor testimony, counsel advice, or a legal conclusion.

### User confirmation or correction

A user confirmation may elevate a proposed statement to an attributable user assertion while retaining the original assistant source and confirmation relationship. A correction must supersede or contradict the earlier statement without deleting it.

### Counsel-authored material

May be treated as practitioner input only when the practitioner identity, source, timestamp, and attributable content are preserved. Intake does not certify licensure, scope of engagement, privilege, or legal correctness.

## Routing categories

Each normalized item may be routed to one or more categories:

```text
INVENTION_CAPTURE
CONCEPTION_CHRONOLOGY
CONTRIBUTOR_ASSERTION
CORROBORATION_LEAD
PUBLIC_DISCLOSURE_LEAD
IMPLEMENTATION_EVIDENCE_LEAD
CLAIM_OR_LIMITATION_DRAFT
WRITTEN_DESCRIPTION_SUPPORT
ENABLEMENT_SUPPORT
PRIOR_ART_DISTINCTION_HYPOTHESIS
COUNSEL_QUESTION
DRAWING_OR_FIGURE_INPUT
OWNER_PREFERENCE
FILING_CLERICAL_INPUT
CONTRADICTION
CORRECTION
SUPERSESSION
OUT_OF_SCOPE
```

## Review states

```text
UNREVIEWED
ROUTED_UNCONFIRMED
USER_ATTRIBUTED
CORROBORATION_PENDING
CORROBORATED_BY_EXTERNAL_RECORD
CONTRADICTED
SUPERSEDED
COUNSEL_REVIEW_PENDING
COUNSEL_ATTRIBUTED
OWNER_DECISION_INPUT_ONLY
EXCLUDED
```

No automated process may promote an item into `CORROBORATED_BY_EXTERNAL_RECORD`, `COUNSEL_ATTRIBUTED`, or an owner-authorized lifecycle state without the required independent source or attributable decision record.

## Normalized repository layout

```text
intake/chatgpt/
  CORRESPONDENCE_INTAKE_CONTRACT.md
  correspondence-record.schema.json
  portfolio-correspondence-manifest.json
  conversations/
  normalized/
  ingestion_receipts/
  contradiction_reports/
  family_indexes/
```

Recommended stable outputs:

```text
conversations/<conversation-id>/source.md
conversations/<conversation-id>/source-manifest.json
normalized/<conversation-id>.messages.jsonl
family_indexes/<family-id>.json
contradiction_reports/<family-id>.md
ingestion_receipts/<receipt-id>.json
```

## Deduplication and succession

- Exact duplicates are identified by source hash and message hash.
- Near-duplicate generated drafts remain separate unless an explicit supersession relationship exists.
- Corrections do not erase the original record.
- Later statements may confirm, narrow, contradict, or supersede earlier statements.
- The current effective statement must be reconstructable from the succession chain.

## Family classification boundary

Automated classification may propose family mappings and confidence values. It must not:

- determine legal family scope;
- determine inventorship;
- claim that one family covers another;
- silently merge Publisher candidates into numbered families;
- treat classification confidence as practitioner approval.

Ambiguous mappings must remain multi-family or unresolved and be included in counsel questions.

## Pipeline integration

Correspondence intake feeds:

```text
Stage A -> invention capture, contributor assertions, conception chronology, corroboration leads
Stage B -> disclosure leads, URLs, publication statements, accessibility evidence, chronology conflicts
Stage C -> claim drafts, support discussions, prior-art distinction hypotheses, counsel questions
Stage D -> figures, drawing narratives, embodiment relationships, unsupported-figure warnings
Step 5 -> owner preferences as decision input only; never filing authorization by implication
```

PAT-005 is the first implemented adapter. Its family-specific contract and manifest remain valid but must reference this portfolio-wide contract as the governing parent.

## Fail-closed conditions

The intake decision remains fail-closed when:

- no stable source export or excerpt exists;
- source identity or message ordering cannot be reconstructed;
- content hashes are absent;
- author role is unknown;
- a factual assertion is represented as corroborated without external support;
- assistant language is represented as inventor testimony or counsel advice;
- contradictions are discarded rather than preserved;
- sensitive material is exposed outside its allowed confidentiality class;
- filing, deadline, inventorship, ownership, or legal disposition is inferred from correspondence alone.

## Allowed decisions

```text
INGESTED_WITH_PROVENANCE
INGESTED_WITH_WARNINGS
FAIL_CLOSED_SOURCE_NOT_MATERIALIZED
FAIL_CLOSED_PROVENANCE_INCOMPLETE
FAIL_CLOSED_POLICY_VIOLATION
```

An ingestion decision is not a patent-readiness, counsel-readiness, filing-readiness, filing, or lifecycle decision.

## Automation resumption

Once pertinent conversations are materialized with stable provenance, automation may:

1. hash and normalize message records;
2. classify messages across families and pipeline stages;
3. produce family indexes;
4. generate contradiction and corroboration reports;
5. update factual question packets;
6. update counsel question packets;
7. update drawing and embodiment review inputs;
8. feed bounded results into each family readiness manifest.

Human and counsel gates remain unchanged.
