# Publisher Commit-Time Admissibility Limitation Mapping

## Purpose

Map currently verified Publisher source language to technical limitation clusters without deciding claim scope, family identity, novelty, inventorship, ownership, or patentability.

## Source keys

- `S1` — `GCAT-BCAT-Engine/Publisher/patents/prep/provisional_patent_framework.md`, blob `4ab2c0c10a9bff47e6228b25d8dad09495440373`
- `S2` — `GCAT-BCAT-Engine/Publisher/docs/commit_time_triage_paper.md`, blob `41bcc67c74844cfbc96c12138a6ebfd48df1a0c6`
- `S3` — `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex`, blob `4be83f75d214b44495d7f3c95628f888a76c89c8`

## Mapping states

- `TEXT_PRESENT` — source expressly describes the limitation.
- `ASSERTED_IMPLEMENTED` — source says implementation or tests exist; exact artifacts are not yet anchored here.
- `PROPOSED` — source presents a claim, future embodiment, or outline without verified execution evidence.
- `UNRESOLVED` — current sources do not establish the limitation.

## Limitation clusters

| ID | Technical limitation | S1 | S2 | S3 | Current evidence posture |
|---|---|---|---|---|---|
| CTA-01 | Detect or define a commit boundary where a proposed transition becomes binding or effectively irreversible | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Strong textual convergence; exact runtime boundary evidence still required |
| CTA-02 | Evaluate the proposed post-commit state rather than relying solely on pre-action legitimacy or static authorization | PROPOSED | TEXT_PRESENT | TEXT_PRESENT | Textually supported; implementation correspondence unresolved |
| CTA-03 | Fail closed when mandatory state, evidence, authority, observability, or safety conditions cannot be established | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Strong textual convergence; exact condition sets differ by source |
| CTA-04 | Separate sufficiency evaluation from substantive admissibility evaluation | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | Strong in triage sources; relationship to generalized gate requires counsel review |
| CTA-05 | Evaluate recoverability of the post-commit state under lag or disturbance | UNRESOLVED | TEXT_PRESENT | TEXT_PRESENT | Central in synthesis source; triage paper uses recoverable-state framing |
| CTA-06 | Compute a continuous reserve, margin, or distance-to-failure quantity | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Different mathematical forms may represent separate embodiments |
| CTA-07 | Apply hard-trigger conditions that override favorable scalar or aggregate results | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Textually supported; exact trigger taxonomy and generalization unresolved |
| CTA-08 | Generate a canonical or cryptographically bound decision record | TEXT_PRESENT | TEXT_PRESENT | ASSERTED_IMPLEMENTED | Strong textual support; exact schemas, hashes, and retained receipts must be anchored |
| CTA-09 | Use a common evaluation core with domain-specific configuration | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | Triage embodiment only unless broader support is established |
| CTA-10 | Receive evidence from sensors, state records, authority records, or other required input registries | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | General input abstraction needs specification alignment |
| CTA-11 | Produce bounded outcomes such as allow, deny, restrict, defer, quarantine, or fail closed | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Outcome taxonomies vary; legal claim strategy unresolved |
| CTA-12 | Preserve replay, reconstruction, or forensic review capability | PROPOSED | TEXT_PRESENT | ASSERTED_IMPLEMENTED | Requires exact retained artifacts and verifier paths |
| CTA-13 | Receive canonical updates that can alter local rules or configuration | TEXT_PRESENT | TEXT_PRESENT | UNRESOLVED | Bidirectional Publisher/Triage embodiment; separate-family relevance unresolved |
| CTA-14 | Evaluate authority as a current commit-time condition | TEXT_PRESENT | TEXT_PRESENT | TEXT_PRESENT | Text present; exact authority model requires comparison with PAT-001 and AI output-to-action family |
| CTA-15 | Evaluate affected entities or observer-participant consequences | UNRESOLVED | UNRESOLVED | UNRESOLVED | Not established by the currently verified three sources |

## Candidate relationship questions

The mapping supports technical overlap review but not a legal conclusion. Counsel should determine whether:

1. the generalized Commit-Time Admissibility Gate is broader than the triage embodiment;
2. recoverability is a mandatory root limitation or a dependent embodiment;
3. sufficiency/admissibility/scalar separation is a separate triage family;
4. receipt-backed transition validation is mandatory, dependent, or separately claimable;
5. PAT-001 supplies executable micro-node architecture for the generalized gate or remains a distinct computing family;
6. AI output-to-action, Publisher disclosure, application correction, and master-record reconstruction are examples, dependent claims, continuations, or separate families.

## Machine-verifiable next evidence

- verify and inventory P5 and P6 Publisher sources;
- locate exact Triage implementation repository paths and commit SHAs;
- locate test files supporting sufficiency, fail-closed behavior, scalar monotonicity, observability dominance, coherence enforcement, commit binding, and domain equivalence;
- locate exact receipt examples and replay or reconstruction tools;
- compare anchored limitations against PAT-001 verified-core evidence without merging families;
- update the completion ledger from `partial_publisher_sources_identified` to `verified_source_inventory_and_nonlegal_mapping_present` only after the source files remain accessible.

## Human and counsel blockers

- factual contributor interviews;
- earliest conception and disclosure chronology;
- public/private status and exact public availability dates;
- inventorship determination limitation by limitation;
- ownership and assignment review;
- professional prior-art analysis;
- family and continuation strategy;
- explicit owner disposition and filing authorization.
