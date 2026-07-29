# Master-Records Reconstruction and Verification — Chronology and Disclosure Intake

## Purpose

Collect attributable facts without inferring conception, inventorship, ownership, public-disclosure consequences, priority, or filing deadlines.

## Event record fields

For each event, record:

- event identifier;
- event type;
- date and time, including timezone when known;
- contributor or speaker;
- contributor role;
- exact contribution or disclosed material;
- repository, document, message, issue, pull request, paper, demonstration, or release reference;
- immutable commit, blob, message, or document identifier when available;
- confidentiality or access condition;
- corroborating source;
- later correction, contradiction, or supersession reference;
- reviewer and review date.

Unknown fields must remain `unknown` or `unverified`.

## Events requiring evidence

1. Earliest articulation of master-record custody or canonical record preservation.
2. Earliest source-record hashing and repository binding.
3. Earliest ordered receipt-chain design.
4. Earliest terminal-receipt consistency rule.
5. Earliest fail-closed chain validation.
6. Earliest downstream schema mapping.
7. Earliest separation between mapping and independent downstream verification.
8. Earliest reconstruction report or historical-state reconstruction design.
9. Earliest retention, supersession, rollback, conflict, or custody-transfer design.
10. Earliest executable test, demonstration, release, or deployment.
11. Each internal disclosure and its access conditions.
12. Each public paper, post, repository release, demonstration, or presentation.

## Current verified repository anchors

- `master-records/core-lite/tools/verify_chain.py` — blob `ad85646b57eaac4432b155cf73a1e86defef335c`
- `master-records/core-lite/tools/map_to_spe_chain.py` — blob `75f1bcce287b1b5f0d40e3af9cca468787fe019a`
- `master-records/core-lite/tests/test_spe_mapping.py` — blob `adf728776b36ddbe7b00818a44f230f6e14cdebd`

Repository timestamps and commit dates are evidence leads only. They are not automatically conception dates or public-disclosure dates.

## Evidence destinations

Place source copies or bounded records under:

```text
evidence/PUBLISHER-master-records-reconstruction-chronology-evidence/
```

Place contributor interviews and contribution worksheets under:

```text
inventorship/PUBLISHER-master-records-reconstruction-contributor-interviews.md
inventorship/PUBLISHER-master-records-reconstruction-contribution-worksheet.md
```

## Resumption condition

Automation may normalize chronology and prepare a practitioner chronology packet after dated, attributable records with stable references are committed. Legal counsel must determine inventorship, ownership, priority, disclosure consequences, and filing strategy.