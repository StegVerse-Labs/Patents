# Publisher Patent-Family Disposition Action Packet

## Purpose

This packet governs the eight Publisher-origin invention candidates that are not yet legally mapped to `PAT-001` through `PAT-005`.

It does not determine patentability, inventorship, ownership, legal family boundaries, filing strategy, or filing authority.

Machine-readable status:

```text
data/publisher-family-completion-status.json
```

## Current Stage

```text
stage: controlled family reconciliation
status: FAIL_CLOSED_MAPPING_AND_FACT_BLOCKERS
filing authorized: false
filed: false
patent pending authorized: false
```

## Why Automation Stopped

Automation can inventory source material, preserve candidate distinctions, create status records, draft factual templates, and validate filing-state invariants.

Automation cannot decide whether a concept is:

- already supported by a numbered patent family;
- a separate inventive family;
- a dependent embodiment;
- a continuation candidate;
- better retained as a trade secret;
- suitable for defensive publication;
- deferred for evidence;
- or abandoned.

Those decisions require factual contribution records, disclosure chronology, technical support review, and qualified practitioner advice.

## Families Requiring Explicit Disposition

```text
commit_time_admissibility_gate
receipt_based_state_transition_validation
publisher_governed_disclosure_pipeline
application_correction_gate
ai_output_to_action_boundary
recoverability_aware_execution_boundary
master_records_reconstruction_and_verification
multi_entity_observer_participant_admissibility
```

## Required Disposition Values

Each family must receive exactly one controlled decision:

```text
MAP_TO_PAT_001
MAP_TO_PAT_002
MAP_TO_PAT_003
MAP_TO_PAT_004
MAP_TO_PAT_005
CREATE_NEW_FAMILY
DEPENDENT_EMBODIMENT
CONTINUATION_CANDIDATE
RETAIN_AS_TRADE_SECRET
DEFENSIVE_PUBLICATION
DEFER_FOR_EVIDENCE
ABANDON
```

A map decision must identify the exact supported limitations and may not state that the entire candidate is covered merely because terminology overlaps.

## Exact Source Review — Commit-Time Admissibility Gate

Start with the following verified repository paths:

```text
GCAT-BCAT-Engine/Publisher/patents/prep/provisional_patent_framework.md
GCAT-BCAT-Engine/Publisher/docs/commit_time_triage_paper.md
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P5_CommitTime_Execution_v1.tex
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P6_CommitGate_Executable_v1.tex
```

For each source, record:

1. exact repository path;
2. commit identifier;
3. creation or publication date if factually verifiable;
4. whether it was public or controlled at that time;
5. limitations actually described;
6. whether the source is conceptual, mathematical, executable, or evidentiary;
7. named human contributors and their factual contributions;
8. any earlier corroborating record;
9. any later refinement that must not be backdated.

Expected factual output:

```text
evidence/PUBLISHER-commit-time-admissibility-source-inventory.md
```

## Exact Ordered Human Steps

### A. Factual source and contributor development

For each family:

1. Identify all known source documents, repository paths, commits, papers, demonstrations, public posts, and private records.
2. Record exact dates only from preserved evidence.
3. Separate executable implementation from written-description-only and proposed embodiments.
4. Identify every human who may have contributed to conception of a material limitation or claimed combination.
5. Conduct factual contributor interviews without suggesting legal inventorship conclusions.
6. Preserve disputes and uncertainty rather than resolving them by assumption.

Required outputs:

```text
evidence/PUBLISHER-<family-key>-source-inventory.md
evidence/PUBLISHER-<family-key>-conception-and-disclosure-chronology.md
inventorship/PUBLISHER-<family-key>-contributor-interview-packet.md
```

### B. Limitation mapping

1. Extract each candidate limitation from the controlled counsel packet and verified source material.
2. Map each limitation to exact evidence.
3. Compare the limitation against `PAT-001` through `PAT-005` records.
4. Mark each relationship as `SUPPORTED_OVERLAP`, `PARTIAL_OVERLAP`, `NO_VERIFIED_OVERLAP`, or `UNRESOLVED`.
5. Do not infer legal priority or coverage from technical overlap.

Required output:

```text
evidence/PUBLISHER-<family-key>-limitation-mapping.md
```

### C. Qualified practitioner review

Provide counsel:

```text
data/publisher-family-completion-status.json
reviews/PUBLISHER_TO_PATENT_FAMILY_RECONCILIATION.md
reviews/PUBLISHER_FAMILY_DISPOSITION_ACTION_PACKET.md
all family source inventories
all factual chronologies
all limitation mappings
all contributor interview packets
numbered-family status records and relevant specifications
```

Counsel should provide a written recommendation for each family addressing:

- family relationship;
- written-description and enablement support;
- prior-art search scope;
- inventorship review scope;
- disclosure consequences;
- trade-secret boundary;
- filing sequence;
- foreign-filing considerations;
- whether more evidence is required.

Expected output:

```text
reviews/PUBLISHER-<family-key>-practitioner-recommendation.md
```

### D. Owner disposition

After practitioner review, the owner records the selected disposition and its approved scope.

Expected output:

```text
reviews/PUBLISHER-<family-key>-owner-decision.md
```

The decision must identify:

- selected disposition value;
- approved technical scope;
- source and drawing versions, if applicable;
- known or counsel-determined inventors, if applicable;
- ownership or applicant status, if confirmed;
- public-disclosure restrictions;
- filing or publication authorization, if any;
- unresolved conditions.

A general instruction to continue building is not filing or publication authorization.

## Filing-Human Boundary

For any family explicitly authorized for filing:

1. Create or update the numbered or newly registered family record.
2. Resolve all placeholders and warnings.
3. Produce the approved specification, abstract, claims or claim themes, and formal drawings.
4. Emit the filing packet, checklist, cover data, fee estimate, and hash manifest.
5. Verify the exact approved artifact hashes.
6. Sign into USPTO Patent Center using the authorized verified account.
7. Select the practitioner-approved application type.
8. Upload the approved documents.
9. Enter confirmed inventor, applicant, correspondence, and entity-status data.
10. Review the generated submission summary.
11. Certify and pay through the human-controlled interface.
12. Download the official filing receipt.
13. Save the receipt at:

```text
filing_packets/<registered-family-id>/uspto_filing_receipt.pdf
```

14. Record the actual application number and actual filing date.
15. Calculate later deadlines only from the actual filing event.
16. Authorize `patent pending` language only after filing evidence passes the portfolio validator.

## Automation Resumption

After a factual source inventory is committed, automation may:

- build limitation-level evidence maps;
- create standalone invention disclosures;
- draft factual specification sections;
- generate figure plans and source sheets;
- prepare prior-art search ledgers without inventing search results;
- update completion ledgers and readiness indexes.

After a practitioner recommendation and owner decision are committed, automation may:

- register or map the family;
- revise the approved drafting package;
- emit the final filing or defensive-publication packet;
- run validators;
- preserve manifests and receipts;
- prepare bounded ecosystem status updates.

After an official filing receipt is committed, automation may:

- validate filed state;
- calculate the nonprovisional and other practitioner-approved deadlines;
- update the patent registry;
- prepare accurate bounded `patent pending` status language;
- verify whether updates are required in `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `admissibility-wiki`, and `stegguardian-wiki`.

## Current Disclosure and Deadline Posture

No official filing receipt or actual filing date is recorded for any Publisher family. Therefore:

```text
filed: false
patent pending: not authorized
application number: null
nonprovisional deadline: null
PCT deadline: null
```

Public repository and paper materials may create disclosure risk, but legal consequences and earliest enabling dates remain unverified and require the chronology audit described above.
