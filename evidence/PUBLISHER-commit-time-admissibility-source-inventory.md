# Publisher Commit-Time Admissibility Source Inventory

## Status

`verified_source_inventory_complete_for_current_known_paths`

This record inventories source material only. It does not determine conception, inventorship, ownership, novelty, patentability, legal disclosure effect, family boundaries, filing authority, filing status, or deadlines.

## Governing handoffs

```text
PATENTS_MIRROR_HANDOFF.md
PUBLISHER_FAMILIES_MIRROR_HANDOFF.md
GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md
```

## Verified source repository

`GCAT-BCAT-Engine/Publisher`

## Verified sources

| # | Path | Blob SHA | Technical classification | Evidenced content surface |
|---|---|---|---|---|
| 1 | `patents/prep/provisional_patent_framework.md` | `4ab2c0c10a9bff47e6228b25d8dad09495440373` | mixed drafting framework | commit-time triage framing; sufficiency/admissibility/scalar separation; candidate claims and drawings; specification outline; filing checklist |
| 2 | `docs/commit_time_triage_paper.md` | `41bcc67c74844cfbc96c12138a6ebfd48df1a0c6` | conceptual, mathematical, implementation-description | sufficiency registry; fail-closed gate; scalar reserve; triage levels; commit record; shared core/domain configuration; stated invariants |
| 3 | `papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex` | `4be83f75d214b44495d7f3c95628f888a76c89c8` | mathematical and evidentiary synthesis | recoverability-based commit admissibility; lag-aware robust region; certified subset; barrier tests; benchmark table; adversarial posture |
| 4 | `papers/GCAT-BCAT/P5_CommitTime_Execution_v1.tex` | `c51cdc8d6b6f3f5b15f0b24a9f9b7b94d7cbe486` | mathematical and algorithmic | commit operator; ideal ALLOW condition; denial reachability; transition-level safety proposition; ALLOW/DENY algorithm |
| 5 | `papers/GCAT-BCAT/P6_CommitGate_Executable_v1.tex` | `57bc163166bf6cbb9a42b87196de35c0f395db4c` | executable-description and evidentiary | certified subset evaluation; barrier tests; recovery step; deterministic reference-implementation description; benchmark outcomes |

The blob identifiers identify the exact contents inspected. Repository commit chronology, authorship, contributor identity, publication status, and public-access dates remain separate unresolved facts.

## Reliability boundaries

1. The provisional framework contains legal and filing assertions, including a purported disclosure deadline, priority statements, fee information, entity assumptions, prior-art conclusions, novelty conclusions, inventorship heuristics, and a statement that the framework is ready for attorney review. None of those assertions are adopted by this inventory.
2. Code-contribution percentages must not be used to determine inventorship.
3. The recorded `April 2026` paper date is document text, not an independently verified creation or public-disclosure date.
4. An anonymized author line does not establish contributor or inventor identity.
5. Mathematical and benchmark assertions require exact executable source, inputs, outputs, tests, and retained receipts before executable support is upgraded.
6. The papers' relationship to the triage framework and to PAT-001 through PAT-005 remains a controlled technical-overlap and practitioner-review question.
7. The paper references `GCAT-BCAT-Engine/Triage`; that repository, its succession identity, paths, commits, tests, and receipts have not yet been verified in this inventory.

## Candidate technical limitation themes

These are non-legal extraction labels, not finalized claims.

1. Commit-boundary evaluation.
2. Candidate post-commit state construction.
3. Recoverability-conditioned admissibility.
4. Conservative certified-subset approximation.
5. Fail-closed denial or restriction.
6. Independent sufficiency evaluation.
7. Non-compensable hard-trigger gate.
8. Continuous reserve or geometric margin evaluation.
9. Observation, decision, or actuation lag adjustment.
10. Commit evidence or integrity-bound decision record.
11. Recovery behavior after denial.
12. Shared core logic with domain-specific configuration.
13. External canonical event and controlled-update path.

## Source-to-theme routing

| Theme | Framework | Triage paper | P0 | P5 | P6 |
|---|---:|---:|---:|---:|---:|
| Commit-boundary evaluation | yes | yes | yes | yes | yes |
| Post-commit state construction | partial | partial | yes | yes | yes |
| Recoverability-conditioned admissibility | partial | yes | yes | yes | yes |
| Certified-subset approximation | no verified passage | no verified passage | yes | limited | yes |
| Fail-closed denial | yes | yes | yes | yes | yes |
| Sufficiency evaluation | yes | yes | no verified passage | no verified passage | no verified passage |
| Hard-trigger gate | yes | yes | no verified passage | no verified passage | no verified passage |
| Reserve or geometric margin | yes | yes | yes | limited | yes |
| Lag adjustment | limited | limited | yes | yes | yes |
| Commit evidence record | yes | yes | limited | no verified passage | outcome evidence only |
| Recovery after denial | implied | limited | yes | reachability only | yes |
| Shared core/domain configuration | yes | yes | no verified passage | no verified passage | no verified passage |
| External canonical update path | yes | yes | no verified passage | no verified passage | no verified passage |

`partial`, `limited`, and `no verified passage` are routing labels, not legal support conclusions.

## Missing factual and executable records

- exact repository creation and commit dates for each source;
- whether and when each source was publicly accessible;
- contributor identities and factual conception contributions;
- canonical identity and exact implementation paths in the referenced Triage repository;
- executable inputs, outputs, tests, and retained receipts;
- relationship to PAT-001 through PAT-005;
- relationship among Commit-Time Admissibility Gate, Commit-Time Triage Engine, and Commit-Time Governance terminology.

## Next machine step

Create and maintain `evidence/PUBLISHER-commit-time-admissibility-limitation-mapping.md`, resolve the referenced implementation repository, then refresh the Publisher-family completion ledger without making a legal family determination.

## Current decision

```text
SOURCE_INVENTORY_VERIFIED
EXECUTABLE_SUPPORT_UNVERIFIED
LEGAL_DISPOSITION_PENDING
FILING_NOT_AUTHORIZED
```
