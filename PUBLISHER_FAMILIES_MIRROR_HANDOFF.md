# Publisher Families Mirror Handoff

## Purpose

This handoff is the source of truth for reconciling Publisher-origin invention candidates with the numbered families in `StegVerse-Labs/Patents`.

Root portfolio handoff:

```text
PATENTS_MIRROR_HANDOFF.md
```

Publisher repository handoff:

```text
GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md
```

## Current Goal

Move each Publisher-origin family into one controlled state:

```text
mapped to an existing numbered family
registered as a new family
dependent embodiment
continuation candidate
retained as trade secret
defensively published
deferred for evidence
abandoned
filed after explicit authorization
```

No family may be silently merged, omitted, published, or treated as covered.

## Current Families

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

Machine-readable status:

```text
data/publisher-family-completion-status.json
```

Exact stasis and resumption packet:

```text
reviews/PUBLISHER_FAMILY_DISPOSITION_ACTION_PACKET.md
```

## Current State

```text
all families: unfiled
all application numbers: null
all filing receipts: null
all actual filing dates: null
all nonprovisional deadlines: null
patent pending authorization: false
```

The Commit-Time Admissibility Gate has the most developed Publisher-side source surface. Verified repository paths currently include:

```text
GCAT-BCAT-Engine/Publisher/patents/prep/provisional_patent_framework.md
GCAT-BCAT-Engine/Publisher/docs/commit_time_triage_paper.md
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P5_CommitTime_Execution_v1.tex
GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P6_CommitGate_Executable_v1.tex
```

These paths establish candidate source locations only. They do not establish conception dates, inventorship, novelty, priority, enablement, ownership, or legal family boundaries.

## Next Machine Work

1. Create `evidence/PUBLISHER-commit-time-admissibility-source-inventory.md` from verified repository paths and commits.
2. Classify each source as conceptual, mathematical, executable, evidentiary, or mixed.
3. Extract candidate limitations without finalizing claims.
4. Compare candidate limitations against numbered-family records using non-legal overlap labels.
5. Create one controlled disposition record per Publisher family.
6. Refresh `data/publisher-family-completion-status.json` after every material change.
7. Refresh the root portfolio ledger only after verified status changes.

## Human and Legal Boundary

The required factual, practitioner, owner, and filing-human sequence is defined in:

```text
reviews/PUBLISHER_FAMILY_DISPOSITION_ACTION_PACKET.md
```

Automation must stop before:

- legal family mapping;
- inventorship determination;
- ownership conclusion;
- patentability opinion;
- disclosure consequence determination;
- trade-secret or defensive-publication election;
- filing authorization;
- Patent Center submission, certification, or payment.

## Required Ecosystem Updates

After an explicit filing, trade-secret, defensive-publication, abandonment, tag, or release decision, verify bounded updates in:

```text
StegVerse-Labs/Site
GCAT-BCAT-Engine/Publisher
admissibility-wiki
stegguardian-wiki
```

Do not expose unpublished claims, contributor disputes, counsel advice, or unfiled claim-sensitive details.

## Archive Readiness

This handoff, the machine-readable status ledger, and the exact action packet contain the current Publisher-family reconciliation state. No prior chat context is required to continue.
