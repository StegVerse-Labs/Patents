# Master Claim Data Model

The patent portfolio is represented as reusable structured data rather than as four isolated documents.

## Source of truth

`data/master_claims.json` is the working source of truth for:

- shared claim clauses;
- patent-family records;
- independent and dependent claim concepts;
- technical effects;
- prior-art collision zones;
- implementation evidence;
- disclosure dates;
- claim-specific inventorship notes.

The master data is not a filed application and does not replace attorney review.

## Reuse model

A shared clause is a reusable technical limitation that may be referenced by more than one patent family. A family selects shared clauses and claim records but remains independently reviewable.

```text
shared clause library
        ↓
family-specific inventive center
        ↓
claim-specific ordered limitations
        ↓
rendered invention disclosure / claim draft
```

Claims should not be assembled by blindly concatenating clauses. Each rendered claim must be reviewed for:

- coherent antecedent basis;
- required ordering of steps;
- technical support in the specification;
- novelty and obviousness risk;
- subject-matter eligibility;
- inventorship by claimed contribution;
- consistency with implementation evidence.

## Current families

| Priority | Family | Working title |
|---:|---|---|
| 1 | `PAT-001` | Transition-Table-Native Dynamic Micro-Node Computing |
| 2 | `PAT-002` | Heartbeat-Governed Entity and Reflected-State Computing |
| 3 | `PAT-003` | Generalized Adaptive Scanner Using Dynamic Micro-Nodes |
| 4 | `PAT-004` | Manifest-Governed Bidirectional Neural Communication |

## Schemas

- `schemas/patent-family.schema.json`
- `schemas/claim.schema.json`

The schemas intentionally separate a patent family from a claim. This allows one family to contain method, system, apparatus, and computer-readable-medium claims without duplicating family metadata.

## Rendering

Run:

```bash
python scripts/render_patent_families.py --check
python scripts/render_patent_families.py
```

The first command validates identifier and cross-reference integrity. The second writes review artifacts under `generated/families/`.

## Evidence discipline

Every claim limitation should eventually contain one or more evidence references pointing to the earliest available:

1. conception record;
2. written description;
3. executable implementation;
4. public disclosure;
5. repository path and commit;
6. test or receipt demonstrating operation.

Do not infer inventorship from repository ownership, commit authorship alone, organizational role, or who requested implementation. Inventorship must be evaluated against conception of the subject matter actually claimed.

## Filing boundaries

`PAT-001` is the foundational computing architecture. `PAT-002` extends it with state-bearing heartbeat and return-delta behavior. `PAT-003` applies the architecture to generalized scanning. `PAT-004` applies it to calibrated bidirectional neural communication.

The dependency records express technical lineage. They do not automatically establish legal priority entitlement. Priority depends on whether an earlier application adequately supports the later claimed subject matter.
