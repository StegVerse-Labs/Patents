# Recoverability-Aware Execution Boundary — Source Inventory

## Controlled family

`Recoverability-Aware Execution Boundary`

## Status

```text
PARTIAL_VERIFIED_WRITTEN_DESCRIPTION
```

This is a technical evidence inventory. It does not determine inventorship, ownership, priority, novelty, patentability, legal family scope, or filing authority.

## Verified source 1 — Commit-Time Governance

```text
repository: GCAT-BCAT-Engine/Publisher
path: papers/GCAT-BCAT/P0_CommitTime_Synthesis_v1.tex
blob_sha: 4be83f75d214b44495d7f3c95628f888a76c89c8
evidence_class: mathematical and technical written description
```

Verified concepts:

- evaluation at the exact point an action becomes irreversible;
- post-commit state construction;
- robust recoverability under observation, decision, and actuation lag;
- ALLOW only when the candidate post-state remains in a recoverable region;
- certified safe subset as a conservative executable approximation;
- rejection of some recoverable states as a documented false-negative cost;
- fail-closed denial, safe mode, or external intervention outside calibration;
- explicit limitation to commit events rather than full-trajectory monitoring.

## Verified source 2 — Consequence Horizon paper

```text
repository: GCAT-BCAT-Engine/Publisher
path: papers/GCAT-BCAT/P10_ConsequenceHorizon_v1.tex
blob_sha: 4d7194bf38c0354a8b634795f9755bd3d6776926
evidence_class: mathematical and conceptual written description
```

Verified concepts:

- a final controllable boundary before a transition becomes binding consequence;
- joint recoverability, observability, absorption-capacity, and coherence-retention thresholds;
- DENY before the horizon, FAIL_CLOSED at the horizon, and QUARANTINE after crossing;
- load-versus-capacity evaluation;
- inference-window analysis beyond the immediate candidate state;
- relationship between commit-gate computation and consequence-horizon admissibility.

## Verified source 3 — Formal authority

```text
repository: Admissible-Existence/CHF
path: README.md
blob_sha: cd1fb2277595047bf8ebbf1902152b8d87b0689c
evidence_class: formal-source authority
```

Verified concepts:

- consequence horizons as boundaries of binding, irreversibility, degraded observability, or degraded recoverability;
- inspection, denial, revision, simulation, or containment before commitment;
- absorption, adaptation, propagation, or suffered consequence after commitment;
- overload when consequence admission exceeds absorption;
- the minimum CHF threshold set for recoverability, observability, absorption, and coherence;
- explicit application to AI tool execution and software commit/deploy/release boundaries.

## Candidate limitation clusters

The verified sources support investigation of these non-final technical clusters:

1. receiving a proposed execution transition;
2. constructing or identifying its candidate post-execution state;
3. estimating consequence under a defined lag or inference window;
4. evaluating recoverability, observability, absorption capacity, and retained coherence;
5. permitting execution only when all required threshold conditions are satisfied;
6. applying a conservative certified approximation where exact recoverability is unavailable;
7. denying or failing closed before or at the binding boundary;
8. quarantining or escalating when consequence has already crossed;
9. retaining a receipt or reconstruction residue for the decision;
10. preserving the distinction between pointwise commit governance and full-trajectory governance.

## Unsupported or unresolved elements

The current sources do not yet independently verify:

- the canonical executable repository and implementation paths;
- retained runtime traces for all decision classes;
- a generalized recovery-controller implementation;
- exact calibration procedures and production thresholds;
- contributor chronology and earliest enabling disclosure;
- whether this family is separate from, dependent on, or a limitation cluster within Commit-Time Admissibility Gate;
- claim-level novelty or prior-art distinctions.

## Current decision

```text
FAIL_CLOSED_EXECUTABLE_CHRONOLOGY_AND_FAMILY_BOUNDARY_BLOCKERS
```
