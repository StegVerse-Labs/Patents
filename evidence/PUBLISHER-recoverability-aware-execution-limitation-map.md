# Recoverability-Aware Execution Boundary — Limitation Evidence Map

## Evidence decision

```text
PARTIAL_VERIFIED_WRITTEN_DESCRIPTION_WITH_ADJACENT_ARTIFACT_EXCLUSION
```

This map is a technical drafting aid. It does not determine novelty, patentability, inventorship, ownership, priority, legal family scope, or filing authority.

## Immutable verified sources

1. `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex`
   - blob: `4be83f75d214b44495d7f3c95628f888a76c89c8`
   - class: mathematical and technical written description
2. `GCAT-BCAT-Engine/Publisher/papers/GCAT-BCAT/P10_ConsequenceHorizon_v1.tex`
   - blob: `4d7194bf38c0354a8b634795f9755bd3d6776926`
   - class: mathematical and conceptual written description
3. `Admissible-Existence/CHF/README.md`
   - blob: `cd1fb2277595047bf8ebbf1902152b8d87b0689c`
   - class: formal-source authority
4. Workflow artifact `external-full-results`
   - run: `27597978374`
   - artifact: `7658749562`
   - ZIP SHA-256: `1bf5f2d57b69648772c3115b3ec5b6d035a646a170185c2c7a05aaf02f24d3c5`
   - class: inspected adjacent workflow output
   - direct family support: false

## Limitation-level classification

| Candidate technical limitation | P0 | P10 | CHF | Artifact | Current support decision |
|---|---:|---:|---:|---:|---|
| Receive or identify a proposed execution transition at a binding commit boundary | yes | partial | yes | no | verified written support |
| Construct or identify a candidate post-execution state | yes | partial | partial | no | verified written support |
| Evaluate consequence over observation, decision, actuation, or inference lag | yes | yes | partial | no | verified written support |
| Evaluate recoverability | yes | yes | yes | no | verified written support |
| Evaluate observability | partial | yes | yes | no | verified written support |
| Evaluate absorption capacity or load-versus-capacity | partial | yes | yes | no | verified written support |
| Evaluate retained coherence | partial | yes | yes | no | verified written support |
| Require joint threshold satisfaction before ALLOW | yes | yes | yes | no | verified written support |
| Use a conservative certified-safe subset where exact recoverability is unavailable | yes | partial | partial | no | verified written support |
| DENY before the consequence horizon | yes | yes | yes | no | verified written support |
| FAIL_CLOSED at or outside calibrated certainty | yes | yes | yes | no | verified written support |
| QUARANTINE, contain, or escalate after crossing | partial | yes | yes | no | verified written support |
| Preserve a decision receipt or reconstruction residue | partial | partial | partial | no | conceptually supported; exact schema unverified |
| Implement a generalized recovery controller | no | no | no | no | unsupported |
| Generate production calibration thresholds | no | no | no | no | unsupported |
| Emit retained runtime traces for all decision classes | no | no | no | no | unsupported |
| Implement rollback, supersession, or safe-mode recovery | partial concept only | partial concept only | partial concept only | no | implementation unsupported |

## Combination-level conclusion

The verified sources support a bounded written-description combination in which a proposed execution is evaluated at a binding boundary using a candidate post-state, lag-aware consequence analysis, recoverability, observability, absorption capacity, and coherence thresholds, with conservative execution regions and fail-closed outcomes.

The sources do not establish a complete executable implementation, production calibration process, canonical decision-receipt schema, retained runtime traces, or recovery-controller behavior. The inspected workflow artifact contains staged analytical output and source metadata but does not supply any of those missing executable elements.

## Required executable evidence

Future executable support must identify exact repositories, paths, immutable commits, schemas, tests, and retained outputs for:

- commit-boundary detection;
- candidate post-state construction;
- calibrated threshold generation;
- certified-safe-region generation;
- reserve or barrier evaluation;
- hard-trigger evaluation;
- ALLOW, DENY, RESTRICT, DEFER, QUARANTINE, and FAIL_CLOSED outputs;
- recovery, rollback, containment, or supersession;
- canonical decision receipt generation and validation.

## Current decision

```text
FAIL_CLOSED_DIRECT_EXECUTABLE_CHRONOLOGY_AND_FAMILY_BOUNDARY_BLOCKERS
```
