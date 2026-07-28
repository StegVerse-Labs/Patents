# PAT-005 Steps 1–4 Automated Preparation Pipeline

## Purpose

Automate all bounded preparation work needed to move PAT-005 from `practitioner_review_ready` to the Step 5 owner-decision gate without inventing facts or substituting automation for patent-practitioner judgment.

## Pipeline boundary

The pipeline may:

- inventory and hash source records;
- ingest pertinent ChatGPT correspondence under `intake/chatgpt/PAT-005_CORRESPONDENCE_INTAKE_CONTRACT.md`;
- preserve conversation, message, author-role, timestamp, export-reference, and content-hash provenance;
- classify correspondence as factual assertion, assistant synthesis, draft language, disclosure lead, implementation lead, contributor question, counsel question, contradiction, superseded material, or excluded material;
- route pertinent correspondence into Stages A through D without treating assistant-generated text as independent corroboration;
- assemble contributor interview prompts and track missing responses;
- normalize factual chronology records;
- assemble public-disclosure evidence without drawing legal conclusions;
- assemble limitation-level prior-art questions and counsel review materials;
- assemble drawing review sheets and flag unsupported or unapproved figures;
- produce readiness manifests and exact blocker reports;
- stop at the owner-decision gate.

The pipeline may not:

- decide legal inventorship;
- decide patentability, validity, ownership, or filing strategy;
- determine U.S. or foreign disclosure consequences;
- treat assistant synthesis as factual corroboration;
- treat an owner preference expressed in ordinary correspondence as filing authorization;
- approve drawings as legally adequate;
- authorize filing;
- submit through Patent Center;
- calculate a filing deadline without an official filing receipt.

## ChatGPT correspondence intake

Required files:

```text
intake/chatgpt/PAT-005_CORRESPONDENCE_INTAKE_CONTRACT.md
intake/chatgpt/PAT-005-correspondence-manifest.json
```

All pertinent ChatGPT-created correspondence is eligible for intake, including user statements, assistant responses, generated drafts, corrections, objections, confirmations, attached-image discussions, and chronology statements. Each item must retain stable source identity and be classified before it can support a pipeline output.

Correspondence routes as follows:

```text
contribution or conception -> Stage A
disclosure or publication -> Stage B
prior art, claim support, enablement, scope, or counsel questions -> Stage C
figures, diagrams, embodiments, or drawing corrections -> Stage D
owner preferences or proposed disposition -> Step 5 input only
```

The pipeline fails closed when relied-upon correspondence lacks a stable source reference or content hash, when assistant synthesis is promoted as fact, when a contradiction affecting a material issue remains unresolved, or when ordinary correspondence is represented as legal approval or filing authority.

## Stages

### Stage A — Factual contribution capture

Inputs:

```text
inventorship/PAT-005-contributor-interview-packet.md
inventorship/PAT-005-claim-contribution-worksheet.md
claims/PAT-005-claim-architecture.md
evidence/PAT-005-conception-chronology.md
intake/chatgpt/PAT-005-correspondence-manifest.json
```

Automated outputs:

- contributor response completeness matrix;
- claim-limitation-to-contributor question matrix;
- missing corroboration report;
- uncertainty register;
- correspondence-derived conception and contribution leads with provenance.

Human boundary:

A contributor supplies or confirms factual answers. The pipeline records the answers but does not decide inventorship.

### Stage B — Public-disclosure evidence assembly

Inputs:

```text
evidence/PAT-005-conception-chronology.md
triage/PAT-005-public-disclosure-and-filing-triage.md
intake/chatgpt/PAT-005-correspondence-manifest.json
repository commits, public URLs, archived captures, and screenshots supplied as evidence
```

Automated output:

```text
evidence/PAT-005-public-disclosure-audit.md
```

The audit records dates, URLs, commit identifiers, public accessibility, disclosed limitations, correspondence-derived disclosure leads, and unresolved factual questions. It must not state a legal deadline or foreign-rights conclusion.

### Stage C — Practitioner review packet assembly

Inputs include the disclosure, provisional draft, claim architecture, evidence maps, prior-art working charts, contributor records, disclosure audit, drawings, and categorized ChatGPT correspondence.

Automated outputs:

- source manifest with hashes;
- correspondence provenance index;
- unresolved limitation matrix;
- prior-art verification questions;
- inventorship question matrix;
- written-description and enablement questions;
- disclosure-consequence questions;
- contradiction register;
- explicit disposition form.

Required practitioner outputs:

```text
inventorship/PAT-005-inventorship-determination.md
reviews/PAT-005-practitioner-recommendation.md
```

The practitioner recommendation must use one explicit disposition:

```text
FILE_AS_DRAFTED
FILE_WITH_REVISIONS
DEFER_FOR_EVIDENCE
RETAIN_AS_TRADE_SECRET
DEFENSIVE_PUBLICATION
ABANDON
```

### Stage D — Drawing review packet assembly

Inputs:

```text
diagrams/PAT-005-formal-drawing-sheets.md
diagrams/PAT-005-drawing-production-spec.md
claims/PAT-005-claim-architecture.md
provisionals/PAT-005-working-provisional-draft.md
intake/chatgpt/PAT-005-correspondence-manifest.json
```

Automated outputs:

- figure inventory;
- figure-to-specification support matrix;
- correspondence-derived figure and embodiment notes;
- numbering conflict report;
- unsupported embodiment warnings;
- drawing approval form.

Required authorized-review output:

```text
diagrams/PAT-005-drawing-approval.md
```

Automation may prepare the form and evidence but may not represent the drawings as approved until an authorized reviewer supplies the decision.

## Gate to Step 5

Run:

```text
python tools/build_pat005_pre_owner_packet.py
```

Generated artifacts:

```text
filing_packets/PAT-005/pre_owner/PRE_OWNER_PACKET_MANIFEST.json
filing_packets/PAT-005/pre_owner/PRE_OWNER_READINESS_REPORT.md
```

The tool returns:

```text
0 — all required Steps 1–4 outputs are present and structurally reviewable
2 — one or more Steps 1–4 outputs, source records, or correspondence-intake requirements remain missing or warned
```

A successful result means only:

```text
READY_FOR_OWNER_DECISION_REVIEW
```

It does not mean filing-ready, filed, patent pending, or legally approved.

## Step 5 owner gate

The pipeline stops at:

```text
reviews/PAT-005-owner-decision.md
```

The owner reviews the practitioner recommendation and records an explicit disposition. Only `AUTHORIZE_FILING`, with approved source hashes and confirmed filing data, permits the later filing-packet emission pipeline to begin.
