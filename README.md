# StegVerse Patents — StegPatent-AI-001

This repository manages StegVerse invention disclosures, reusable claim data, provisional-draft artifacts, evidence, and filing deadlines. It does not file automatically with the USPTO or any other patent office.

## Current priority families

1. `PAT-001` — Transition-Table-Native Dynamic Micro-Node Computing
2. `PAT-002` — Heartbeat-Governed Entity and Reflected-State Computing
3. `PAT-003` — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
4. `PAT-004` — Manifest-Governed Bidirectional Neural Communication
5. `PAT-005` — Governed Device Continuity and Destination-Bound Hardware Abstraction

`PAT-001` is the foundational computing architecture. The later families express technical extensions and implementations; dependency in this repository does not by itself establish legal priority entitlement.

`PAT-005` is an urgent practitioner-review candidate because a public technical paper was committed on 2026-07-13. Its earliest enabling public disclosure, inventorship, claim scope, and foreign-filing consequences remain under review.

## PAT-005 working package

### Core drafting

- `disclosures/PAT-005-governed-device-continuity.md`
- `claims/PAT-005-claim-architecture.md`
- `data/PAT-005-family.json`
- `data/PAT-005-completion-status.json`
- `provisionals/PAT-005-working-provisional-draft.md`

### Evidence and chronology

- `evidence/PAT-005-evidence-ledger.md`
- `evidence/PAT-005-cross-repository-source-map.md`
- `evidence/PAT-005-destination-and-guardian-anchors.md`
- `evidence/PAT-005-end-to-end-reconstruction.md`
- `evidence/PAT-005-negative-and-failure-paths.md`
- `evidence/PAT-005-conception-chronology.md`

### Drawings

- `diagrams/PAT-005-figure-descriptions.md`
- `diagrams/PAT-005-formal-drawing-sheets.md`
- `diagrams/PAT-005-drawing-production-spec.md`

### Prior art and inventorship

- `prior-art/PAT-005-initial-collision-chart.md`
- `prior-art/PAT-005-limitation-claim-chart.md`
- `inventorship/PAT-005-claim-contribution-worksheet.md`
- `inventorship/PAT-005-contributor-interview-packet.md`

### Filing and practitioner review

- `triage/PAT-005-public-disclosure-and-filing-triage.md`
- `reviews/PAT-005-filing-readiness-index.md`
- `reviews/PAT-005-practitioner-handoff.md`

### Current completion state

The technical and portfolio preparation package is substantially complete and marked `practitioner_review_ready`. Remaining gates are evidence-dependent or human/legal:

- verified patent publications and exact limitation mappings;
- contributor interviews and claim-by-claim inventorship determination;
- earliest conception and public-disclosure audit;
- executable negative fixtures and retained outputs;
- practitioner-approved formal drawings;
- written legal recommendation and explicit owner filing authorization.

No filing, assignment, payment, inventor declaration, or `patent pending` representation is authorized by completion of the repository package.

## Structured source of truth

- `data/master_claims.json` — shared clauses, family metadata, claim concepts, evidence placeholders, disclosure dates, and inventorship notes
- `data/PAT-005-family.json` — structured working family record for PAT-005
- `data/PAT-005-completion-status.json` — machine-readable readiness and blocking gates
- `schemas/patent-family.schema.json` — reusable family record
- `schemas/claim.schema.json` — reusable claim record
- `docs/CLAIM_DATA_MODEL.md` — architecture and evidence rules
- `scripts/render_patent_families.py` — deterministic review-artifact renderer

Validate and render:

```bash
python scripts/render_patent_families.py --check
python scripts/render_patent_families.py
```

Rendered working drafts are written to `generated/families/`.

## Patent AI functions

- Watches allowlisted StegVerse repositories for potentially patentable changes
- Creates invention-disclosure stubs
- Maintains reusable claim and limitation data
- Generates provisional-draft skeletons and claim tiers
- Links claim limitations to implementation and disclosure evidence
- Tracks provisional-to-nonprovisional and PCT deadlines
- Maintains a central patent manifest for portfolio management

## Evidence and inventorship discipline

Each claimed limitation should eventually link to the earliest known conception, written description, executable implementation, public disclosure, repository path, commit, and test or receipt.

Inventorship is determined from human contribution to conception of the subject matter actually claimed. It is not determined solely from repository ownership, organizational position, prompting, or commit authorship.

## Safety rules

- Never file, publish externally, assign rights, or make legal representations automatically.
- Treat generated claims and drafts as working technical artifacts requiring qualified legal review.
- Preserve nonpublic material and use allowlists for repositories and paths.
- Record uncertainty rather than inventing dates, inventors, evidence, or legal conclusions.
- Do not use `patent pending` unless an application has actually been filed.

## Versioning

Repository epoch and portfolio settings live in `patent_manifest.json`. Structured claim-data versioning lives in `data/master_claims.json`.
