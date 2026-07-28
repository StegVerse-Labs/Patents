# PAT-004 Exact Human-Action Packet

## Application and current stage

```text
family: PAT-004 — Manifest-Governed Bidirectional Neural Communication
stage: structured review preparation
status: FAIL_CLOSED_BLOCKERS
filing status: not filed
```

## Why automation stopped

Automation can organize the known family record and search for verified technical evidence, but it cannot establish missing human facts or legal conclusions. No verified implementation anchors, conception dates, public-disclosure dates, contributor facts, inventorship determination, ownership record, practitioner recommendation, or filing authorization are currently recorded.

## Blocker classes

### Factual-human

- who conceived each material limitation and claimed combination;
- when each conception occurred;
- which dated records corroborate it;
- which public artifacts disclosed enabling subject matter;
- whether any implementation or retained test evidence exists;
- which embodiments were actually built, described, proposed, or unsupported.

### Legal-practitioner

- relationship to PAT-001, PAT-002, and PAT-003;
- patentability and prior-art interpretation;
- enablement and written-description sufficiency;
- supported technical scope and appropriate terminology;
- separation of observation, interpretation, communication, action, disengagement, and recovery authority;
- inventorship claim by claim;
- disclosure-date and foreign-rights consequences;
- filing sequence and confidentiality strategy.

### Owner authorization

Record one explicit decision: `FILE`, `FILE_WITH_REVISIONS`, `DEFER_FOR_EVIDENCE`, `RETAIN_AS_TRADE_SECRET`, `DEFENSIVE_PUBLICATION`, or `ABANDON`.

### Filing-human

Only after an approved application exists: sign into USPTO Patent Center, enter confirmed bibliographic data, upload approved files, certify applicable statements and entity status, pay the confirmed fee, and preserve the official receipt.

## Exact source files

```text
data/master_claims.json
data/PAT-004-completion-status.json
filing-readiness/PAT-004_FILING_READINESS_INDEX.md
PATENTS_MIRROR_HANDOFF.md
```

## Ordered human steps

### Stage A — Factual contribution record

1. Identify every person who may have contributed to each proposed limitation and combination.
2. Record the factual contribution without assigning legal inventorship.
3. Link each contribution to dated notes, messages, diagrams, source files, commits, demonstrations, or retained outputs.
4. Preserve conflicting accounts.

Expected output:

```text
inventorship/PAT-004-contributor-interview-packet.md
```

### Stage B — Conception and disclosure chronology

1. Locate the earliest written description for each limitation and combination.
2. Identify the earliest executable implementation, if one exists.
3. Identify every public repository artifact, paper, website page, social post, presentation, video, or shared document that may disclose enabling subject matter.
4. Record exact dates, stable identifiers, and disclosed limitations.
5. Do not infer legal materiality.

Expected outputs:

```text
evidence/PAT-004_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md
evidence/PAT-004-public-disclosure-audit.md
```

### Stage C — Technical evidence boundary

1. Classify each embodiment as executable and retained, written-description-only, proposed, or unsupported.
2. Separate passive observation from interpretation, communication, external action, disengagement, and recovery authority.
3. Record exact implementation paths, commits, schemas, tests, receipts, and retained outputs.
4. Do not assert efficacy, safety, or medical validity without appropriate evidence and review.

Expected output:

```text
evidence/PAT-004_CLAIM_ELEMENT_EVIDENCE_MAP.md
```

### Stage D — Practitioner review

Provide, in order:

```text
filing-readiness/PAT-004_FILING_READINESS_INDEX.md
data/PAT-004-completion-status.json
data/master_claims.json
evidence/PAT-004_CONCEPTION_AND_DISCLOSURE_CHRONOLOGY.md
evidence/PAT-004-public-disclosure-audit.md
evidence/PAT-004_CLAIM_ELEMENT_EVIDENCE_MAP.md
inventorship/PAT-004-contributor-interview-packet.md
```

Request written determinations on family relationships, supported claim scope, prior-art search strategy, enablement, technical and safety boundaries, drawings, inventorship, disclosure consequences, confidentiality, and filing sequence.

Expected outputs:

```text
reviews/PAT-004-practitioner-recommendation.md
inventorship/PAT-004-inventorship-determination.md
```

### Stage E — Owner decision

Record the explicit disposition in:

```text
reviews/PAT-004-owner-decision.md
```

A filing authorization must identify the approved specification version, drawing version, known inventors, filing entity, and conditions. General continuation instructions are not filing authorization.

### Stage F — Patent Center boundary

After written filing authorization only:

1. Resolve every placeholder and warning.
2. Emit the final specification, drawings, cover data, checklist, and hash manifest.
3. Verify the approved artifact hashes.
4. Sign into Patent Center using the owner's verified account.
5. Start the application workflow selected by the practitioner.
6. Upload approved files and enter confirmed applicant, inventor, correspondence, and entity-status data.
7. Review the submission summary, certify, and pay.
8. Download the official filing receipt.
9. Save it at:

```text
filing_packets/PAT-004/uspto_filing_receipt.pdf
```

10. Record the actual application number and filing timestamp.
11. Calculate later deadlines only from the actual filing date.

## Automation resumption

- chronology committed → validate source links;
- implementation anchors committed → populate the limitation evidence map;
- interviews committed → assemble the practitioner packet;
- practitioner recommendation committed → refresh readiness and warning reports;
- owner authorization committed → emit the final filing packet;
- filing receipt committed → validate hashes, record the application number and actual filing date, calculate tracked deadlines, and prepare bounded ecosystem status updates.

## Current disclosure or deadline risk

Unknown. No filing deadline is calculated because no actual filing date exists. Public-disclosure risk remains unclassified until the audit is complete.
