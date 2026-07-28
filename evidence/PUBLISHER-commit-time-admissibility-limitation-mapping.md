# Publisher Commit-Time Admissibility Limitation Mapping

## Purpose

Map verified Publisher source language to technical limitation clusters without deciding claim scope, family identity, novelty, inventorship, ownership, patentability, disclosure effect, or filing strategy.

## Source keys

- `S1` — `GCAT-BCAT-Engine/Publisher/patents/prep/provisional_patent_framework.md`, blob `4ab2c0c10a9bff47e6228b25d8dad09495440373`
- `S2` — `GCAT-BCAT-Engine/Publisher/docs/commit_time_triage_paper.md`, blob `41bcc67c74844cfbc96c12138a6ebfd48df1a0c6`
- `S3` — `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex`, blob `4be83f75d214b44495d7f3c95628f888a76c89c8`
- `S4` — `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P5_CommitTime_Execution_v1.tex`, blob `c51cdc8d6b6f3f5b15f0b24a9f9b7b94d7cbe486`
- `S5` — `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P6_CommitGate_Executable_v1.tex`, blob `57bc163166bf6cbb9a42b87196de35c0f395db4c`

## Mapping states

- `TEXT_PRESENT` — source expressly describes the limitation.
- `ASSERTED_IMPLEMENTED` — source says implementation or tests exist; exact executable artifacts are not yet anchored here.
- `PROPOSED` — source presents a claim, future embodiment, or outline without verified execution evidence.
- `UNRESOLVED` — current sources do not establish the limitation.

## Limitation clusters

| ID | Technical limitation | S1 | S2 | S3 | S4 | S5 | Current evidence posture |
|---|---|---|---|---|---|---|---|
| CTA-01 | Detect or define a commit boundary where a proposed transition becomes binding or effectively irreversible | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Strong textual convergence; exact runtime boundary evidence still required |
| CTA-02 | Compute or identify a candidate post-commit state from current state and proposed action | PROPOSED | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Textually convergent in generalized papers; executable correspondence unresolved |
| CTA-03 | Evaluate the proposed post-state rather than relying solely on pre-action legitimacy or static authorization | PROPOSED | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Central generalized-gate theme |
| CTA-04 | Fail closed when mandatory state, evidence, authority, observability, or safety conditions cannot be established | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Strong textual convergence; exact condition sets differ |
| CTA-05 | Separate sufficiency evaluation from substantive admissibility evaluation | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | UNRESOLVED | UNRESOLVED | Strong triage embodiment; generalized-family role unresolved |
| CTA-06 | Evaluate recoverability of the post-commit state under lag or disturbance | UNRESOLVED | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Central generalized execution theme |
| CTA-07 | Use a conservative certified subset as a sufficient approximation of a robust recoverable region | UNRESOLVED | UNRESOLVED | TEXT_PRESENT | PROPOSED | TEXT_PRESENT | Mathematical/executable-description convergence; implementation artifact unresolved |
| CTA-08 | Compute a continuous reserve, barrier margin, or distance-to-failure quantity | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | TEXT_PRESENT | Different mathematical forms may represent distinct embodiments |
| CTA-09 | Apply non-compensable hard-trigger conditions that override favorable scalar or aggregate results | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | UNRESOLVED | UNRESOLVED | Triage-specific textual support currently strongest |
| CTA-10 | Generate a canonical or cryptographically bound decision record | TEXT_PRESENT | TEXT_PRESENT | ASSERTED_IMPLEMENTED | UNRESOLVED | ASSERTED_IMPLEMENTED | Exact schemas, hash procedures, examples, and receipts must be anchored |
| CTA-11 | Use a shared evaluation core with domain-specific signal, threshold, weight, or coherence configuration | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | UNRESOLVED | UNRESOLVED | Triage embodiment only unless broader support is established |
| CTA-12 | Produce bounded outcomes such as allow, deny, restrict, defer, quarantine, or fail closed | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Outcome taxonomies vary; claim strategy unresolved |
| CTA-13 | Invoke or characterize recovery behavior after denial | PROPOSED | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Recovery control is explicit in P6; executable path remains unverified |
| CTA-14 | Preserve replay, reconstruction, or forensic review capability | PROPOSED | TEXT_PRESENT | ASSERTED_IMPLEMENTED | UNRESOLVED | ASSERTED_IMPLEMENTED | Requires retained artifacts and verifier paths |
| CTA-15 | Receive canonical updates that can alter local rules or configuration | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | UNRESOLVED | UNRESOLVED | Bidirectional triage embodiment; separate-family relevance unresolved |
| CTA-16 | Evaluate authority or observability as a current commit-time condition | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Exact authority and observability models require cross-family comparison |
| CTA-17 | Evaluate affected entities or observer-participant consequences | UNRESOLVED | UNRESOLVED | UNRESOLVED | UNRESOLVED | UNRESOLVED | Not established by the five verified sources |

## Non-legal overlap questions

The mapping permits descriptive comparison but not family disposition. Required comparisons include:

1. generalized recoverability gate versus triage-specific sufficiency, hard-trigger, and scalar architecture;
2. receipt-backed state-transition validation versus commit-record integrity binding;
3. AI Output-to-Action Boundary versus the point at which a proposed output becomes consequence-bearing action;
4. Recoverability-Aware Execution Boundary versus CTA-06, CTA-07, and CTA-13;
5. Master-Records Reconstruction and Verification versus CTA-10 and CTA-14;
6. Multi-Entity Observer-Participant Admissibility versus currently unsupported CTA-17;
7. PAT-001 through PAT-005 implementation architecture without silently merging any family.

Use only these descriptive labels in automated comparison:

```text
DIRECT_TEXTUAL_OVERLAP
PARTIAL_TECHNICAL_OVERLAP
DISTINCT_TECHNICAL_CENTER
EVIDENCE_NOT_YET_COMPARABLE
UNRESOLVED
```

## Machine-verifiable next evidence

- resolve and inspect the referenced `GCAT-BCAT-Engine/Triage` repository;
- locate exact implementation paths and immutable commits for the commit operator, certified tests, denial behavior, recovery step, sufficiency, scalar, and commit binding;
- locate test files supporting fail-closed behavior, monotonicity or barrier conditions, observability, coherence, commit integrity, recovery, and domain equivalence;
- preserve exact executable inputs, outputs, benchmark traces, and receipts;
- build a public-disclosure chronology that separates document-internal dates from verified public accessibility;
- compare anchored limitations against numbered PAT-family records without legal mapping;
- refresh the Publisher-family completion ledger to record the verified five-source inventory and expanded non-legal mapping.

## Human and counsel blockers

- factual contributor interviews and conception chronology;
- verified public/private status and exact availability dates;
- inventorship determination limitation by limitation;
- ownership and assignment review;
- professional prior-art analysis;
- legal family, continuation, and claim strategy;
- explicit owner disposition and filing authorization.

## Current decision

```text
NONLEGAL_LIMITATION_MAPPING_PRESENT
EXECUTABLE_EVIDENCE_PENDING
LEGAL_FAMILY_DISPOSITION_PENDING
FILING_NOT_AUTHORIZED
```
