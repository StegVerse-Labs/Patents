# Patents Mirror Handoff

## Authoritative priority

Patent filing preparation for the StegVerse foundational architecture is Priority 1.

## Active task

Prepare the earliest defensible filing package for:

1. PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing
2. PAT-002 — Heartbeat-Governed Entity and Reflected-State Computing
3. PAT-003 — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
4. PAT-004 — Manifest-Governed Bidirectional Neural Communication
5. PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction

PAT-005 is an urgent provisional-review candidate because a public technical paper was committed on 2026-07-13. Earliest enabling public disclosure, inventorship, claim scope, and foreign-filing consequences remain under review.

## Current execution order

1. Lock PAT-001 claim scope, technical evidence, inventorship, and disclosure chronology.
2. Produce a provisional-quality PAT-001 specification without waiting for the remaining families.
3. Preserve reusable shared claim structures for PAT-002 through PAT-004.
4. Triage PAT-005 disclosure timing and prepare its provisional-review package without displacing PAT-001 unless legal review determines urgency requires reprioritization.
5. Prepare dependent family drafts in parallel without delaying the earliest defensible filing.
6. Validate the filing-packet engine against a claim-sensitive family only after its source draft is ready for authorized review.

## Current evidence findings

A dated architecture document titled `StegVerse-Micro-Node-Agency.md` was created on 2026-06-16. It describes micro-node agency as the newest refinement after governed multi-tier AI hierarchy, defines a micro-node as a scoped, receipt-bearing, revocable and non-sovereign AI work unit, and identifies cost, compute, state-drift, review, receipt, and authority problems in larger recursive-agent structures.

This evidence predates the later June 28–July 2 runtime implementation discussions and must be treated as an earlier documented conception milestone, subject to inventorship and corroboration review.

PAT-005 has a public-disclosure triage package under `disclosures/`, `claims/`, `evidence/`, and `triage/`. Do not use `patent pending` unless an application has actually been filed.

PAT-001 now has:

- `evidence/PAT-001_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md`;
- `evidence/PAT-001_CLAIM_ELEMENT_EVIDENCE_MAP.md`, including verified July 2 runtime commits and explicit separation between evidenced limitations and later claim refinements;
- `evidence/PAT-001_INVENTORSHIP_WORKSHEET.md`, requiring human contribution analysis limitation by limitation and for the claimed combinations;
- `evidence/PAT-001_PRIOR_ART_SEARCH_LEDGER.md`, separating patentability searching from freedom-to-operate analysis and preserving reproducible search events.

The strongest currently verified PAT-001 implementation combination is transition-table role execution, distinct authority and admissibility evaluation, fail-closed behavior, deterministic hash-bound receipts, governed return-path evidence, and reconstruction witnesses. Demand-only construction, minimum manifest-derived addressability, default expiry, usage-only delayed retention, bounded context reuse, and prohibition on heartbeat-only persistence remain high-value limitations requiring corroboration or implementation evidence.

## Filing-packet engine installed

The repository now includes:

- `tools/patent_ai.py` — positive-trigger-only patent candidate watcher. A candidate is admitted only when a commit contains `[PATENT]`, touches `patent_candidates/**`, or is associated with a PR labeled `patent-candidate`. Each admission emits a trigger receipt.
- `tools/filing_packet_emitter.py` — filesystem-only provisional packet emitter producing a specification DOCX, cover data, fee estimate, filing checklist, and hash manifest.
- `docs/FILING_PACKET_SPEC.md` — canonical filing-packet lifecycle, invariants, and StegFin integration boundary.
- `samples/sample_specification.md` — substantive rendering of the uploaded DOCX sample.
- `samples/sample_specification.docx` — binary DOCX fixture, SHA-256 `0a31faeed211448bafb632ac2a6dc8ea4a977634d3b173badb61de54c9a28c59`.
- `tests/test_patent_ai.py` — executable coverage for T1 commit-tag, T2 candidate-path, T3 PR-label, negative/no-trigger, and idempotent receipt behavior.
- `tests/test_filing_packet_emitter.py` — executable coverage for fail-closed missing input, warning state, artifact hashes, null filing dates, packet-emitted state, and populated claim/summary handling.
- `tests/test_utc_timestamps.py` — regression coverage requiring timezone-aware, `Z`-normalized timestamps and prohibiting deprecated `utcnow()` use.
- `requirements-dev.txt` — reproducible test dependency declaration.

## Validation state

Completed:

- `python -m py_compile` passed for both Python tools;
- imports for `requests` and `python-docx` passed;
- independent `python -m pytest -q` validation passed for the patent-engine test modules before the timestamp remediation;
- the uploaded sample DOCX hash was verified and preserved as a binary fixture;
- naïve `datetime.utcnow()` generation was replaced with timezone-aware UTC helpers producing `Z`-normalized RFC 3339 values;
- timestamp regression tests were committed;
- the original binary DOCX fixture was committed through the Git data API without forcing or overwriting concurrent repository work.

No combined status checks were attached to the latest direct commit. Full authoritative-dispatcher validation therefore remains required before a release tag.

## Human boundary invariant

No automated component may submit a filing to the USPTO or another jurisdiction. The packet emitter may prepare and hash filing artifacts, but the submission, certification, fee confirmation, and recording of the actual filing receipt remain human-controlled transitions. Filed dates must remain null until the human records the actual filing event.

## StegFin integration boundary

The Patents repository or a future patent-registry component may reference these governed services without making them filing authorities:

- `StegVerse-Labs/stegfin-governance` — authorize filing expenditures, assignments, licensing, acquisition, and vendor engagements.
- `StegVerse-Labs/stegfin-provider-banking` — prepare and reconcile authorized filing and maintenance fee records.
- `StegVerse-Labs/stegfin-provider-token-ledger` — register patent-family asset identifiers, ownership state, costs, and licensing events.
- `StegVerse-Labs/stegfin-provider-vendor-payment` — govern payments to counsel, search vendors, illustrators, translators, and related providers.
- `StegVerse-Labs/stegfin-provider-acquisition-close` — govern patent purchases, portfolio transfers, escrow, assignments, and closing evidence.
- `StegVerse-Labs/stegfin-provider-token-ledger-executor` — execute admitted ledger transitions only; it must never perform a patent-office filing.

Dependency rule: patent registry or packet tooling may consume StegFin services through governed interfaces. StegFin runtimes must not depend on claim-sensitive patent drafts or patent filing documents to operate.

## Repository state

The repository contains the claim schemas and master data, family renderer, patent doctrine documentation, filing-packet tools, binary and Markdown sample fixtures, test suites, PAT-001 chronology/evidence/inventorship/prior-art controls, and the PAT-005 triage package.

Priority tracking issue: #1.

## Next required artifacts and validations

- corroborate the canonical June 6 and June 16 PAT-001 architecture sources and commits;
- locate executable evidence for active-node capability resolution, minimum node construction, expiry, usage leases, bounded context retention, and heartbeat non-self-retention;
- populate PAT-001 inventor candidates, corroborators, evidence, and contribution distinctions through human fact collection and counsel review;
- execute and populate the PAT-001 prior-art search ledger using verified patent and non-patent databases;
- PAT-001 provisional specification draft;
- PAT-001 figure list and system diagrams;
- PAT-005 earliest-enabling-disclosure and foreign-filing triage resolution;
- run the full repository test suite in the authoritative dispatcher and preserve its receipt;
- consolidate the current workflow count toward the 1–2 dispatcher standard as a separate remediation task.

## Ownership and continuation scope

Issue #1 remains the authoritative filing-priority record. Continuation may install tests, fixtures, schemas, dispatch tasks, and filing-readiness documentation. It may not automatically file, declare inventorship from commit metadata, publish claim-sensitive drafts outside the authorized repository, treat StegFin execution as USPTO submission authority, or claim `patent pending` before an application is actually filed.

## Constraints

- No automatic USPTO submission.
- Human and patent-counsel review is required before filing.
- Commit authorship does not establish inventorship.
- Repository publication does not establish novelty.
- Do not expand public disclosure of claim-sensitive implementation details before filing review.