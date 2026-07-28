# Publisher Commit-Time Admissibility Source Inventory

## Status

`verified_source_inventory_complete_for_current_known_paths`

This record inventories source material only. It does not determine conception, inventorship, ownership, novelty, patentability, legal disclosure effect, family boundaries, or filing authority.

## Verified source repository

`GCAT-BCAT-Engine/Publisher`

## Verified sources

### 1. Provisional patent framework

- Path: `patents/prep/provisional_patent_framework.md`
- Blob SHA: `4ab2c0c10a9bff47e6228b25d8dad09495440373`
- Recorded title: `Provisional Patent Framework: Commit-Time Triage Engine`
- Evidenced content classes:
  - commit-time triage framing;
  - sufficiency/admissibility/scalar separation;
  - candidate claims;
  - candidate drawing list;
  - specification outline;
  - filing checklist.
- Reliability boundary:
  - contributor-percentage inventorship guidance is not a valid legal inventorship determination;
  - novelty table and prior-art statements are unverified working assertions;
  - stated fees, deadlines, and filing recommendations require current practitioner verification;
  - `framework complete` does not mean filing-ready or filed.

### 2. Commit-time triage paper

- Path: `docs/commit_time_triage_paper.md`
- Blob SHA: `41bcc67c74844cfbc96c12138a6ebfd48df1a0c6`
- Recorded metadata: `April 2026`, `Draft for submission`.
- Evidenced content classes:
  - domain-agnostic embodied-system triage framing;
  - sufficiency registry;
  - fail-closed admissibility gate;
  - scalar reserve calculation;
  - triage levels;
  - cryptographic commit record;
  - implementation and invariant assertions;
  - patent-relevant claim appendix.
- Reliability boundary:
  - the recorded month is not independently verified as a public-disclosure date;
  - implementation, test, proof, and cross-domain assertions require repository and execution evidence;
  - medical, robotic, and embodied-AI examples require careful enablement and risk review;
  - the source does not determine inventorship or priority.

### 3. Commit-time synthesis paper

- Path: `papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex`
- Blob SHA: `4be83f75d214b44495d7f3c95628f888a76c89c8`
- Recorded title: `Commit-Time Governance: Enforcing Recoverability at the Point of Action`
- Evidenced content classes:
  - recoverability-based commit admissibility;
  - robust recoverable region under lag;
  - post-commit transition evaluation;
  - fail-closed executable gate framing;
  - barrier-style certification concepts;
  - adversarial analysis framing.
- Reliability boundary:
  - author line is anonymized;
  - the file alone does not establish a conception date, publication date, proof validity, implementation correspondence, or inventorship;
  - mathematical support must be mapped to exact executable and test artifacts before being treated as enabled.

## Candidate sources requiring the next verification pass

- `papers/GCAT-BCAT/P5_CommitTime_Execution_v1.tex`
- `papers/GCAT-BCAT/P6_CommitGate_Executable_v1.tex`

For each candidate source, record the blob SHA, document status, authorship metadata, exact limitations supported, implementation references, public/private status, and earliest verified availability date.

## Cross-source concept clusters

1. **Commit boundary** — evaluation occurs immediately before an action becomes binding or irreversible.
2. **Fail-closed gate** — unverifiable or triggered conditions deny execution.
3. **Recoverability** — post-commit state remains inside a recoverable or certified-safe region.
4. **Sufficiency** — required evidence or signals must be present before a substantive decision.
5. **Receipt or binding record** — decision basis is bound to a canonical or cryptographic record.
6. **Domain configuration** — common evaluation core with domain-specific parameters.
7. **Authority and observability** — insufficient authority or observability can block action.

## Missing factual records

- exact repository creation and commit dates for each source;
- whether and when each source was publicly accessible;
- contributor identities and factual conception contributions;
- exact implementation paths and commits corresponding to each asserted limitation;
- retained test outputs and execution receipts;
- relationship to PAT-001 through PAT-005;
- relationship among Commit-Time Admissibility Gate, Commit-Time Triage Engine, and Commit-Time Governance terminology.

## Next machine step

Complete `evidence/PUBLISHER-commit-time-admissibility-limitation-mapping.md`, verify P5 and P6 source hashes, then refresh the Publisher-family completion ledger without making a legal family determination.
