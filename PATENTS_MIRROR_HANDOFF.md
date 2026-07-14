# Patents Mirror Handoff

## Authoritative priority

Patent filing preparation for the StegVerse foundational architecture is Priority 1.

## Active task

Prepare the earliest defensible filing package for:

1. PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing
2. PAT-002 — Heartbeat-Governed Entity and Reflected-State Computing
3. PAT-003 — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
4. PAT-004 — Manifest-Governed Bidirectional Neural Communication

## Current execution order

1. Lock PAT-001 claim scope, technical evidence, inventorship, and disclosure chronology.
2. Produce a provisional-quality PAT-001 specification without waiting for the remaining families.
3. Preserve reusable shared claim structures for PAT-002 through PAT-004.
4. Prepare dependent family drafts in parallel without delaying PAT-001 filing readiness.
5. Validate the filing-packet engine against PAT-001 only after the claim-sensitive source draft is ready for authorized review.

## Current evidence finding

A dated architecture document titled `StegVerse-Micro-Node-Agency.md` was created on 2026-06-16. It describes micro-node agency as the newest refinement after governed multi-tier AI hierarchy, defines a micro-node as a scoped, receipt-bearing, revocable and non-sovereign AI work unit, and identifies cost, compute, state-drift, review, receipt, and authority problems in larger recursive-agent structures.

This evidence predates the later June 28–July 2 runtime implementation discussions and must be treated as an earlier documented conception milestone, subject to inventorship and corroboration review.

## Filing-packet engine installed

The repository now includes:

- `tools/patent_ai.py` — positive-trigger-only patent candidate watcher. A candidate is admitted only when a commit contains `[PATENT]`, touches `patent_candidates/**`, or is associated with a PR labeled `patent-candidate`. Each admission emits a trigger receipt.
- `tools/filing_packet_emitter.py` — filesystem-only provisional packet emitter producing a specification DOCX, cover data, fee estimate, filing checklist, and hash manifest.
- `docs/FILING_PACKET_SPEC.md` — canonical filing-packet lifecycle, invariants, and StegFin integration boundary.
- `samples/sample_specification.md` — substantive rendering of the uploaded DOCX sample, pinned to source SHA-256 `0a31faeed211448bafb632ac2a6dc8ea4a977634d3b173badb61de54c9a28c59`.

Local pre-install validation completed:

- `python -m py_compile` passed for both Python tools.
- imports for `requests` and `python-docx` passed.
- the uploaded sample DOCX hash was recorded.

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

The repository contains:

- `schemas/claim.schema.json`
- `schemas/patent-family.schema.json`
- `data/master_claims.json`
- `scripts/render_patent_families.py`
- `docs/CLAIM_DATA_MODEL.md`
- `tests/test_master_claims.py`
- `tools/patent_ai.py`
- `tools/filing_packet_emitter.py`
- `docs/FILING_PACKET_SPEC.md`
- `samples/sample_specification.md`

Priority tracking issue: #1.

## Next required artifacts and validations

- `evidence/PAT-001_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md`
- claim-element-to-repository-evidence map
- human inventorship worksheet by claimed limitation
- prior-art search ledger
- provisional specification draft
- figure list and system diagrams
- tests for all three positive candidate triggers and negative/no-trigger behavior
- emitter fixture test verifying fail-closed behavior, warning state, manifest hashes, and null filed dates
- verify whether `requirements.txt` already includes both `requests` and `python-docx`; update only if needed
- commit or regenerate a binary DOCX fixture through a binary-capable repository path
- consolidate the current workflow count toward the 1–2 dispatcher standard as a separate remediation task

## Ownership and continuation scope

Issue #1 remains the authoritative filing-priority record. Continuation may install tests, fixtures, schemas, dispatch tasks, and filing-readiness documentation. It may not automatically file, declare inventorship from commit metadata, publish claim-sensitive drafts outside the authorized repository, or treat StegFin execution as USPTO submission authority.

## Constraints

- No automatic USPTO submission.
- Human and patent-counsel review is required before filing.
- Commit authorship does not establish inventorship.
- Repository publication does not establish novelty.
- Do not expand public disclosure of claim-sensitive implementation details before filing review.
