# PAT-003 Exact Human-Action Packet

## Application and current stage

```text
family: PAT-003 — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
stage: structured review preparation
status: FAIL_CLOSED_BLOCKERS
filing status: not filed
```

## Why automation stopped

Automation can organize the known technical concept and search for repository evidence, but it cannot establish missing human facts or legal conclusions. The current family record contains no verified implementation anchors, conception dates, public-disclosure dates, contributor facts, inventorship determination, ownership record, practitioner recommendation, or filing authorization.

## Blocker classes

### Factual-human

- who conceived each material limitation and combination;
- when each conception occurred;
- which dated documents corroborate it;
- which public artifacts disclosed enabling subject matter;
- whether any executable scanner implementation or retained test output exists;
- which sensor, organism, device, or signal embodiments were actually built or described.

### Legal-practitioner

- patentability and prior-art interpretation;
- whether PAT-003 should remain dependent on PAT-001 and PAT-002 or be filed separately;
- enablement and written-description sufficiency;
- treatment of medical, biological, neural, safety, or diagnostic language;
- inventorship claim by claim;
- disclosure-date and foreign-rights consequences;
- claim breadth and filing sequence.

### Owner authorization

- file as drafted;
- file with revisions;
- defer for evidence;
- retain as trade secret;
- defensively publish;
- abandon.

### Filing-human

Only after an approved application exists:

- sign into USPTO Patent Center;
- enter confirmed bibliographic and correspondence information;
- certify applicable statements and entity status;
- upload approved files;
- pay the confirmed fee;
- download and preserve the official filing receipt.

## Exact source files

Begin with:

```text
data/master_claims.json
data/PAT-003-completion-status.json
filing-readiness/PAT-003_FILING_READINESS_INDEX.md
PATENTS_MIRROR_HANDOFF.md
```

Machine discovery should add exact source paths and commits before the human review package is treated as complete.

## Ordered human steps

### Stage A — Factual conception record

1. Identify every person who may have contributed to the following limitation groups:
   - manifest-defined scanning scope;
   - detection that active capability is absent;
   - minimum acquisition, decoding, or comparative node construction;
   - return-delta comparison;
   - dynamic observation interval;
   - explicit non-inference result;
   - receipt-backed observation disposition.
2. Record what each person contributed without assigning legal inventorship.
3. Link each factual contribution to dated notes, messages, diagrams, source files, commits, demonstrations, or retained outputs.
4. Preserve conflicting accounts rather than collapsing them.

Expected output:

```text
inventorship/PAT-003-contributor-interview-packet.md
```

### Stage B — Conception and disclosure chronology

1. Locate the earliest written description for each limitation and each proposed combination.
2. Identify the earliest executable implementation, if one exists.
3. Identify every public GitHub commit, paper, website page, LinkedIn post, presentation, video, or shared document that may disclose enabling subject matter.
4. Record exact dates, stable identifiers, and disclosed limitations.
5. Do not infer that a public reference is enabling or legally material.

Expected outputs:

```text
evidence/PAT-003_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md
evidence/PAT-003-public-disclosure-audit.md
```

### Stage C — Technical evidence boundary

1. Review each scanner embodiment and classify it as:
   - executable and retained;
   - written-description-only;
   - proposed;
   - unsupported.
2. Separate general signal acquisition from medical or diagnostic interpretation.
3. Do not claim diagnostic performance, safety, clinical validity, neural efficacy, or biological meaning without appropriate evidence.
4. Preserve exact implementation paths, commits, schemas, tests, receipts, and outputs.

Expected output:

```text
evidence/PAT-003_CLAIM_ELEMENT_EVIDENCE_MAP.md
```

### Stage D — Practitioner review

Provide the practitioner, in order:

```text
filing-readiness/PAT-003_FILING_READINESS_INDEX.md
data/PAT-003-completion-status.json
data/master_claims.json
evidence/PAT-003_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md
evidence/PAT-003-public-disclosure-audit.md
evidence/PAT-003_CLAIM_ELEMENT_EVIDENCE_MAP.md
inventorship/PAT-003-contributor-interview-packet.md
```

Ask for written determinations on:

- relationship to PAT-001 and PAT-002;
- supported claim scope;
- prior-art search strategy;
- enablement and drawings;
- inventorship;
- disclosure consequences;
- whether sensitive embodiments should be removed, narrowed, retained privately, or separately filed.

Expected outputs:

```text
reviews/PAT-003-practitioner-recommendation.md
inventorship/PAT-003-inventorship-determination.md
```

### Stage E — Owner decision

Record one explicit disposition in:

```text
reviews/PAT-003-owner-decision.md
```

A filing authorization must identify the approved specification version, drawings version, known inventors, filing entity, and conditions. A general instruction to continue building is not filing authorization.

### Stage F — Patent Center boundary

After written filing authorization only:

1. Resolve all placeholders and warnings.
2. Emit the final packet and hash manifest.
3. Verify specification and drawing hashes.
4. Sign into Patent Center using the owner's verified account.
5. Start the appropriate new provisional or other application workflow selected by the practitioner.
6. Upload the approved specification and drawings.
7. Complete confirmed applicant, inventor, correspondence, and entity-status fields.
8. Review the generated submission summary.
9. Certify and pay.
10. Download the official filing receipt.
11. Save it at:

```text
filing_packets/PAT-003/uspto_filing_receipt.pdf
```

12. Record the actual application number and filing timestamp in the family ledger.
13. Calculate any later deadline only from that actual filing date.

## Automation resumption

Automation resumes after each committed output:

- chronology committed → build and validate source chronology links;
- implementation anchors committed → populate limitation evidence map;
- interviews committed → assemble practitioner review packet;
- practitioner recommendation committed → refresh readiness and warning report;
- owner authorization committed → emit final filing packet;
- filing receipt committed → validate hashes, record the application number and actual date, calculate the tracked deadline, and prepare bounded status updates.

## Current disclosure or deadline risk

Unknown. No deadline is calculated because no actual filing date is recorded. Public-disclosure risk remains unclassified until the audit is completed.