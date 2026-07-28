# Patents Mirror Handoff

## Authoritative priority

Patent filing preparation for the StegVerse foundational architecture remains Priority 1.

## Current family order

1. `PAT-001` — Transition-Table-Native Dynamic Micro-Node Computing
2. `PAT-002` — Heartbeat-Governed Entity and Reflected-State Computing
3. `PAT-003` — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
4. `PAT-004` — Manifest-Governed Bidirectional Neural Communication
5. `PAT-005` — Governed Device Continuity and Destination-Bound Hardware Abstraction

`PAT-005` remains the urgent disclosure-review candidate because the tracked public technical paper date is 2026-07-13. Earliest enabling disclosure, inventorship, claim scope, and foreign-filing consequences remain unresolved.

## Governing boundary

This repository may prepare, validate, organize, and emit first-party patent drafting and filing-support artifacts. It must not automatically submit an application, pay fees, sign or certify declarations, determine inventorship or patentability as legal conclusions, authorize filing, invent missing facts, or claim `patent pending` before an actual filing receipt exists.

## Machine-readable portfolio source

```text
data/portfolio-completion-status.json
```

Current schema version: `0.4`.

## Numbered-family state

### PAT-001

```text
status: practitioner_review_ready_with_blockers
specification and abstract: working drafts present
verified-core evidence map: present
formal drawing sources: present; review rendering pending
inventorship and ownership: unresolved
filing packet: not authorized
```

### PAT-002

```text
status: structured_review_preparation_with_blockers
status record: data/PAT-002-completion-status.json
readiness index: filing-readiness/PAT-002_FILING_READINESS_INDEX.md
action packet: reviews/PAT-002-human-action-packet.md
```

### PAT-003

```text
status: structured_review_preparation_with_blockers
status record: data/PAT-003-completion-status.json
readiness index: filing-readiness/PAT-003_FILING_READINESS_INDEX.md
action packet: reviews/PAT-003-human-action-packet.md
```

### PAT-004

```text
status: structured_review_preparation_with_blockers
status record: data/PAT-004-completion-status.json
readiness index: filing-readiness/PAT-004_FILING_READINESS_INDEX.md
action packet: reviews/PAT-004-human-action-packet.md
```

The PAT-004 structured family record defines an inventive center, technical problem, technical effects, shared clauses, parent-family relationships, and method/system claim identifiers. No implementation anchors, dates, inventorship, ownership, practitioner recommendation, or filing authorization have been inferred.

### PAT-005

```text
status: practitioner_review_ready
filed: false
patent pending authorized: false
expected decision: FAIL_CLOSED_BLOCKERS
human action packet: reviews/PAT-005-human-action-packet.md
```

The PAT-005 technical package includes its disclosure, working provisional, claim architecture, evidence maps, drawings, prior-art working charts, conception and contribution worksheets, practitioner handoff, validators, and executable negative-case records. It remains blocked by verified prior-art references, interviews, inventorship, disclosure audit, drawing approval, practitioner recommendation, and explicit owner filing authorization.

## Publisher-family reconciliation

The following Publisher families remain controlled candidates whose legal relationship to numbered PAT families is unresolved:

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

Do not silently merge, split, abandon, publish, or treat these as covered by PAT-001 through PAT-005. Each requires an explicit disposition supported by factual records and practitioner advice.

## Filing and deadline invariant

No numbered or Publisher family currently has a recorded official filing receipt, application number, or actual filing date. Therefore:

```text
filed: false
patent pending: not authorized
nonprovisional deadline: null
PCT deadline: null
```

No deadline may be calculated from a draft date, packet-generation date, repository commit, or assumed submission date.

## Current next machine work

1. Locate exact PAT-002 implementation anchors and build its standalone disclosure and limitation evidence map.
2. Locate verified PAT-003 source anchors and build its standalone disclosure and limitation evidence map.
3. Locate verified PAT-004 source anchors and build its standalone disclosure and limitation evidence map while keeping supported and proposed embodiments distinct.
4. Add a portfolio filing-state validator that rejects `filed`, `patent_pending`, or calculated-deadline states without an actual filing receipt and filing date.
5. Continue PAT-001 corroboration, drawing review outputs, and authoritative readiness validation.
6. Preserve PAT-005 fail-closed status until the exact factual, practitioner, owner, and filing-human outputs are committed.
7. Reconcile Publisher families through explicit controlled disposition records.

## Human-boundary protocol

Every blocked family must have an action packet identifying:

```text
family and stage
why automation stopped
blocker class
unresolved facts or decisions
exact source files
ordered human steps
required input or document
expected output or receipt
repository destination
automation resumption step
disclosure or deadline risk
```

A generic statement that counsel or human review is required is insufficient.

## Issue and pull-request state

Priority issue: `#1`.

No open patent pull request was found in the current check. Direct commits therefore require later authoritative-dispatch validation before release or filing-packet authorization.

## Required ecosystem updates after an explicit disposition

When any family reaches an approved filing, trade-secret, defensive-publication, abandonment, tag, or release state, verify bounded updates in:

```text
StegVerse-Labs/Site
GCAT-BCAT-Engine/Publisher
admissibility-wiki
stegguardian-wiki
```

Do not expose unpublished claims, inventorship disputes, counsel advice, or unfiled patent-sensitive details.

## Archive readiness

This handoff contains the current family states, exact stasis locations, portfolio ledger, filing invariant, next machine work, and ecosystem continuation boundary. The prior conversation is not required for forward progress.
