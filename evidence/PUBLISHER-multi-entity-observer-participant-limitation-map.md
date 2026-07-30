# Multi-Entity Observer-Participant Admissibility — Limitation-Level Evidence Map

## Scope

This is a non-legal technical support map. It distinguishes verified formal written-description support from unsupported executable or combination-level assumptions. It does not determine claim scope, novelty, inventorship, ownership, patentability, priority, or filing strategy.

## Verified source identities

| Source | Immutable identity | Evidence class |
|---|---|---|
| `Admissible-Existence/DC/README.md` | blob `415ddab2ec9b11b39243e3ee5b0dd78bafd2cf6a` | formal written description |
| `Admissible-Existence/RTG/README.md` | blob `8e68292d2ce914b50df7713683c2bf20a1bd86ff` | mathematical and relational substrate |

## Limitation mapping

| Candidate technical limitation | Verified support | Current evidence decision | Missing support |
|---|---|---|---|
| Multiple bounded entities participate in or observe one proposed transition | DC describes coherence among multiple entities, nodes, observers, systems, repositories, and agents | `FORMAL_SUPPORT_PRESENT` | canonical protocol representation and executable schema |
| Distinct proposal, performance, observation, or review roles may be represented without requiring one fixed role count | DC supports multiple entities, observers, and authority relations | `PARTIAL_FORMAL_SUPPORT` | explicit role model, role assignment rules, and tested role transitions |
| Each entity has a local state and an authority relation relevant to the proposed transition | DC describes local/global coherence and authority relations; RTG describes relational state and authority substrate | `FORMAL_SUPPORT_PRESENT` | immutable state schema and runtime authority evaluation |
| Observation lag or stale information affects admissibility | DC identifies partial observability, lag, and lag-induced invalidity | `FORMAL_SUPPORT_PRESENT` | lag thresholds, clocks, stale-observation policy, and retained test outputs |
| Participant and observer records are linked through receipts | DC describes conflicting receipts and reconciliation | `PARTIAL_FORMAL_SUPPORT` | immutable receipt schema, parent linkage, signatures or hashes, and validator |
| Local coherence and global coherence are evaluated separately | DC expressly separates local and global coherence | `FORMAL_SUPPORT_PRESENT` | executable evaluator and positive/negative fixtures |
| Locally coherent but mutually incompatible states are detected | DC identifies split-brain, receipt divergence, and incompatible distributed outcomes | `FORMAL_SUPPORT_PRESENT` | deterministic conflict detector and retained traces |
| Returned observations and participant records are reconciled into a candidate shared post-transition state | DC supports reconciliation; RTG supports reconstruction and bounded transition evaluation | `PARTIAL_COMBINATION_SUPPORT` | canonical reconciliation algorithm, state output schema, and tests |
| Observation informs admissibility without automatically conferring execution authority | RTG states geometric describability does not prove admissibility; DC separates authority relations from observation | `FORMAL_BOUNDARY_SUPPORT` | explicit runtime separation between observation authority and execution authority |
| Transition is denied, quarantined, or held when authority, receipts, lag, or recoverability cannot be reconciled | DC supports distributed failure modes and global recoverability; RTG supports admissibility and recoverability boundaries | `PARTIAL_FORMAL_SUPPORT` | canonical ALLOW, DENY, FAIL_CLOSED, and QUARANTINE implementation |
| A reconstruction path preserves the observer-visible and participant-visible decision history | RTG supports reconstruction; DC supports receipt reconciliation | `PARTIAL_FORMAL_SUPPORT` | replay format, reconstruction validator, fixtures, and retained outputs |

## Combination-level decision

```text
FORMAL_WRITTEN_DESCRIPTION_SUPPORT_PRESENT
EXECUTABLE_COMBINATION_UNVERIFIED
IMMUTABLE_MULTI_PARTY_RECEIPT_SCHEMA_UNVERIFIED
RUNTIME_ADMISSIBILITY_DECISION_UNVERIFIED
```

The verified sources support important primitives and relationships, but they do not establish the complete observer-participant admissibility combination as an implemented system.

## Unsupported assumptions that must not enter a filing packet as facts

- a mandatory three-party proposer / performer / observer architecture;
- a universally fixed observer location or identity;
- a canonical observer-participant protocol;
- a complete executable implementation;
- a specific receipt serialization, cryptographic construction, or validator;
- deterministic conversion of observations into an admissibility result;
- formal drawing details not grounded in verified implementation;
- conception dates, disclosure dates, contributors, inventorship, ownership, priority, novelty, or patentability.

## Required evidence package

```text
evidence/PUBLISHER-multi-entity-observer-participant-implementation/
  source-identity.md
  schemas/
  manifests/
  tests/
  fixtures/
  traces/
  negative-cases/

data/receipts/PUBLISHER-multi-entity-observer-participant/
  authoritative-execution-receipt.json
  output-hashes.json
```

Representative retained cases should cover:

- compatible local states and reconciled global state;
- incompatible locally coherent states;
- stale observer state;
- observer without execution authority;
- authority expiry or loss;
- broken or divergent receipt linkage;
- reconciliation failure;
- replay or reconstruction failure;
- ALLOW, DENY, FAIL_CLOSED, and QUARANTINE outcomes where those states are implemented.

## Automation continuation

After immutable implementation evidence is supplied, this map can be reconciled at executable limitation level and used to support only those specification and drawing details actually verified. Legal family mapping and patentability conclusions remain reserved for counsel.
