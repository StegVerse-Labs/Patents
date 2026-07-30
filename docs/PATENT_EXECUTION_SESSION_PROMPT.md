# StegVerse Patent Execution Session Prompt

## Purpose

This file is the reusable new-chat execution prompt for continuing the StegVerse patent portfolio with maximum bounded progress and minimum loss of context.

It does not replace any family handoff. Every run must begin by reading the current handoffs and machine ledgers identified below. Verified immutable source artifacts control over summaries.

## Required first reads

Read these files from `StegVerse-Labs/Patents` before making any change:

```text
PATENTS_MIRROR_HANDOFF.md
PUBLISHER_FAMILIES_MIRROR_HANDOFF.md
PAT-001_MIRROR_HANDOFF.md
PAT-002_MIRROR_HANDOFF.md
PAT-003_MIRROR_HANDOFF.md
PAT-004_MIRROR_HANDOFF.md
PAT-005_MIRROR_HANDOFF.md
COMMIT_TIME_ADMISSIBILITY_MIRROR_HANDOFF.md
RECEIPT_BASED_STATE_TRANSITION_MIRROR_HANDOFF.md
PUBLISHER_GOVERNED_DISCLOSURE_PIPELINE_MIRROR_HANDOFF.md
APPLICATION_CORRECTION_GATE_MIRROR_HANDOFF.md
AI_OUTPUT_TO_ACTION_BOUNDARY_MIRROR_HANDOFF.md
RECOVERABILITY_AWARE_EXECUTION_MIRROR_HANDOFF.md
MASTER_RECORDS_RECONSTRUCTION_VERIFICATION_MIRROR_HANDOFF.md
MULTI_ENTITY_OBSERVER_PARTICIPANT_MIRROR_HANDOFF.md
```

Also read the current machine ledgers and custody state:

```text
data/portfolio-completion-status.json
data/publisher-family-completion-status.json
data/thread-archive-custody-status.json
```

Read any family-specific status, readiness, counsel packet, action packet, evidence map, receipt, issue, pull request, workflow output, or filing-packet artifact referenced by those handoffs.

When work depends on external first-party implementation evidence, inspect the exact connected repositories and immutable paths named in the relevant handoff. Do not substitute memory or inferred repository relationships for direct evidence.

## Current goals

1. Maintain concrete lifecycle status for every numbered and Publisher-origin invention family.
2. Complete all bounded, non-destructive, first-party drafting, evidence mapping, validation, manifest, readiness, packet, receipt, and synchronization work currently supported by repository evidence.
3. Advance another independent family whenever one family is blocked.
4. Preserve exact blockers and next-action packets for every authority-gated or evidence-gated stasis.
5. Reconcile changed family records into the central portfolio ledger, Publisher ledger, root handoffs, and patent-registry snapshot when repository authority permits.
6. Keep filing and deadline claims fail-closed until verified official filing evidence exists.
7. Continue until every family is filed, intentionally held as trade secret, defensively published under an explicit decision, abandoned under an explicit decision, or has a fully documented exact blocker and next-action packet.

## Required lifecycle fields

For each family, maintain explicit status for:

```text
invention capture
disclosure chronology
evidence map
prior-art distinction notes
specification
abstract
claim themes or claims draft
drawings
inventor fields
ownership fields
counsel questions
filing packet emission
warning resolution
human filing
filing receipt
application number
actual filing date
nonprovisional deadline
PCT deadline where tracked
owner disposition
```

## Controlled invention families

Numbered families:

```text
PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing
PAT-002 — Heartbeat-Governed Entity and Reflected-State Computing
PAT-003 — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
PAT-004 — Manifest-Governed Bidirectional Neural Communication
PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction
```

Publisher-origin candidates:

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

Do not silently merge, split, abandon, publish, or treat one family as covered by another.

## Execution rules

Perform all bounded work available in the current run, including:

```text
complete supported drafts
replace scaffolding and placeholders only from verified evidence
create missing handoffs when repository authority permits
update machine-readable lifecycle ledgers
run available repository checks through an authoritative dispatcher where available
preserve deterministic refusal receipts when execution is unavailable or denied
emit manifests, readiness reports, evidence maps, action packets, and synchronization deltas
inspect issues and pull requests
update the root and family handoffs after concrete changes
advance the next independent family when blocked
```

Do not invent or infer unsupported facts, inventorship, ownership, conception dates, disclosure dates, legal conclusions, prior-art results, signatures, certifications, fees, entity status, application numbers, filing receipts, filing dates, or deadlines.

Do not submit to the USPTO, pay fees, certify declarations, sign documents, authorize filing, or act as patent counsel.

No deadline may be calculated from a draft date, repository commit, conversation timestamp, packet-generation date, disclosure template, or assumed submission.

## Human-action packet requirement

When automation reaches a non-automatable or authority-gated stasis, report:

```text
application or family and current stage
precise reason automation stopped
every unresolved field or decision
exact repository file or Patent Center screen involved
ordered steps the human must perform
information or document required
expected outcome or receipt
exact repository destination
automation that resumes afterward
disclosure or deadline risk
```

Separate legal-counsel decisions from clerical human filing actions.

## Notification rule

Notify the user only when:

```text
concrete repository progress occurred
a disclosure or deadline risk was discovered
a family became counsel-ready, filing-ready, filed, or deadline-sensitive
an exact human action is required
```

When no meaningful change occurred and no unresolved human action needs surfacing, do not claim progress.

## Mandatory end-of-response continuation prompt

At the end of every user-visible response, include a fenced block titled `NEXT CHAT PROMPT` containing a ready-to-paste prompt for a new chat.

The prompt must:

1. Direct the next session to read this file first.
2. Direct the next session to read `PATENTS_MIRROR_HANDOFF.md`, `PUBLISHER_FAMILIES_MIRROR_HANDOFF.md`, and every family handoff relevant to the next work.
3. Name any exact status, evidence, counsel, action-packet, filing-packet, registry, issue, pull-request, workflow, or receipt files that changed or must be inspected next.
4. Summarize the latest concrete progress, current blockers, current goals, end goals, and authority boundaries.
5. Instruct the next session to use the connected GitHub repositories directly and continue without asking for confirmation when bounded repository authority permits.
6. Instruct the next session to update this execution prompt and the controlling handoffs whenever new durable context is required for future sessions.
7. Preserve the rule that unsupported facts and legal conclusions must not be invented and that no USPTO submission, signature, certification, or fee payment is authorized.

The continuation prompt must be specific to the work just completed rather than a generic restatement.

## Current priority ordering

Unless the current handoffs show a newer priority:

1. Address PAT-005 public-disclosure factual intake and preserve urgency without inventing legal consequences or deadlines.
2. Complete authoritative portfolio and Publisher-ledger reconciliation after recent family-status and handoff changes.
3. Refresh the patent-registry exact-hash approved-source snapshot and preserve synchronization or deterministic-refusal receipts.
4. Continue bounded source and runtime evidence discovery for blocked numbered and Publisher families.
5. Advance supported specification, abstract, figure, evidence, counsel-packet, and action-packet work for the next independent family.
6. Preserve active-thread status until verified orchestration ingestion, task extraction, assignment, accepted custody, and continuation receipts exist.

## End state

The portfolio is complete only when each family has an explicit, evidence-backed terminal state:

```text
filed
held as trade secret under explicit owner decision
defensively published under explicit owner decision
abandoned under explicit owner decision
or fully documented blocker with exact next-action packet
```

Repository continuation records are not equivalent to legal disposition, filing, or orchestration custody.
