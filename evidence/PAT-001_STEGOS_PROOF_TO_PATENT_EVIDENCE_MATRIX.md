# PAT-001 StegOS Proof-to-Patent Evidence Matrix

**Related Goal Task:** `STEGOS-NODE-MANIFOLD-001`  
**Scope:** pre-registered evidence ingestion for the remaining physical StegOS/InTr Network Manifold predicates  
**Boundary:** this artifact does not claim physical proof, patentability, inventorship, priority, filing readiness, or reduction to practice.

The machine-readable source is `data/PAT-001-stegos-proof-to-patent-evidence-matrix.json`.

## Predicate-to-limitation matrix

| Remaining physical predicate | Candidate PAT-001 limitations materially supported if authentic retained proof is later ingested | Current status |
|---|---|---|
| `DISTINCT_SECOND_ACTIVE_NODE_OBSERVED` | `P1-L17`, `P1-L18` | `PENDING_AUTHENTIC_RETAINED_EVIDENCE` |
| `NETWORK_PRESENT_PROVEN` | `P1-L17`, `P1-L18` | `PENDING_AUTHENTIC_RETAINED_EVIDENCE` |
| `REAL_FRAGMENTATION_AND_REFORMATION_OBSERVED` | `P1-L18`, `P1-L20`, `P1-L21` | `PENDING_AUTHENTIC_RETAINED_EVIDENCE` |
| `EXACT_MULTI_NODE_REPLAY_RECONSTRUCTION_EQUALITY` | `P1-L18`, `P1-L20`, `P1-L21` | `PENDING_AUTHENTIC_RETAINED_EVIDENCE` |

`P1-L19` remains separately supported only at `VERIFIED SOFTWARE ARCHITECTURE + CLAIM REFINEMENT`; physical completion of the four predicates is not needed to prove that the source architecture separates observation, credential, transition, execution, and reconstruction authority, but those predicates may later corroborate that separation in operation.

## Pre-registered immutable evidence package

Every future completed physical predicate must retain all of the following before its PAT-001 posture can be upgraded:

1. exact source repository, source path, commit SHA, and blob SHA;
2. authentic runtime or physical receipt identifiers;
3. SHA-256 digests for every retained source/export/network/manifold/replay artifact used as evidence;
4. exact Node identities and device bindings where applicable;
5. exact source/destination Interlock identities;
6. transition lineage from local receipt head through admitted transition packet, network observation, origination manifest, resultant manifest, and replay/reconstruction as applicable;
7. negative/fail-closed evidence for rejected substitutions or tampering cases relevant to that predicate;
8. the retained reconstruction output and equality result where applicable;
9. observation date(s), separate from repository commit dates; and
10. disclosure/chronology implications without assigning an earlier conception or reduction-to-practice date by inference.

A future ingestion event may populate evidence fields and change a predicate status only when the evidence package is complete. It may not rewrite the candidate limitation to fit the observed result.

## Predicate-specific requirements

### DISTINCT_SECOND_ACTIVE_NODE_OBSERVED → P1-L17 / P1-L18

Required proof must establish two genuinely distinct Node identities, device bindings, source Interlocks, and local receipt heads. The existing `stegos/real_peer_manifold_pipeline.py` source fails closed when any of those distinctness checks collapse. The second Node export itself must be authentic retained physical evidence; a fixture or copied first-Node artifact is insufficient.

### NETWORK_PRESENT_PROVEN → P1-L17 / P1-L18

Required proof must retain two admitted physical Network observations bound to reciprocal but distinct Interlocks and an exact manifold resultant showing `LOCAL_ONLY -> NETWORK_PRESENT`. Connectivity, HeartBeat observation, addressability, or a single-node result is insufficient.

### REAL_FRAGMENTATION_AND_REFORMATION_OBSERVED → P1-L18 / P1-L20 / P1-L21

Required proof must retain six ordered physical Network observations for the same two Nodes: initial reciprocal pair, divergent active/non-stale pair, and recovered reciprocal pair. The divergent observations must target different external Interlocks, must use new observation digests, and must be descriptively later. The retained state sequence must show `LOCAL_ONLY -> NETWORK_PRESENT -> NETWORK_PRESENT -> NETWORK_FRAGMENTED -> NETWORK_PRESENT -> NETWORK_PRESENT`.

### EXACT_MULTI_NODE_REPLAY_RECONSTRUCTION_EQUALITY → P1-L18 / P1-L20 / P1-L21

Required proof must replay the exact retained multi-node sequence and establish `replay_matches_live_cycle=true` and `expected_states_match=true` from the same Node set, Interlock set, source observation digests, origination manifest, transition order, and resultant manifest. Deterministic fixture equality is useful validation but cannot substitute for physical evidence.

## Current immutable software anchors

Current StegOS `main` anchor observed during this investigation: `07fe74c4eb4b2657dc1838d87836a6872a9da751`.

- `StegVerse-Labs/StegOS/stegos/real_peer_manifold_pipeline.py` — blob `4a9ed2e9b3c1433eb8886f63c3c9713cb039de0a`; second-peer distinctness and two-node `NETWORK_PRESENT` pipeline.
- `StegVerse-Labs/StegOS/stegos/real_relationship_cycle.py` — blob `a4613223e4643b8542af5fa7cbbd08f654512ca1`; physical fragmentation/reformation cycle and replay checks.
- `StegVerse-Labs/StegOS/stegos/heartbeat_protocol_sample.py` — blob `1007b124fa67ec611839273bbe036e7e8b68c8c5`; HeartBeat observation is non-causal, non-authorizing, credential-free, and separate from the transition payload.

These anchors prove source behavior and validators only. They do not satisfy any of the four physical predicates.

## Blocker investigation performed now

### Demand construction

Repository-wide search found adjacent admissibility and minimal-micro-node rules but no first-party implementation that directly establishes the PAT-001 proposition: resolve whether an active admissible capable node exists, and construct the bounded node only when no such node exists. The existing `StegVerse-002/micro-node-runtime` lifecycle record therefore remains correct: `NOT_ESTABLISHED_BY_INSPECTED_SURFACE`.

### Ephemeral expiry / usage retention

Current repository evidence includes many expiry/lease constructs for credentials, sessions, and continuity records, but no directly matching PAT-001 micro-node lifecycle implementation proving default node expiry with retention only through externally evidenced ongoing usage. `default_expiry` and `usage_only_delayed_expiry_or_lease` therefore remain unresolved.

### HeartBeat non-authority

This is directly corroborated at the software-architecture level. `stegos/heartbeat_protocol_sample.py` requires `observation_is_causal=false`, `authority_effect=NONE`, `heartbeat_grants_execution_authority=false`, TV/TVC credential authority, and a transition packet that excludes HeartBeat payload. This advances HeartBeat non-authority corroboration but does **not** establish the separate proposition that a micro-node cannot self-retain based only on HeartBeat.

### Prior-art verification

The prior-art identifier record is advanced with bounded, stable patent publication identifiers for moving-target defense and zero-trust/workload identity. These references are collision-zone evidence only; no novelty, obviousness, freedom-to-operate, or patentability conclusion is made. The broader PAT-001 prior-art gate remains open pending complete limitation mapping, combination analysis, and practitioner review.

## Ingestion rule

Future proof processing is mechanical: populate the pre-registered evidence fields, validate hashes and identities, evaluate the predicate, and update the evidence posture. Do not rewrite `P1-L17` through `P1-L21` after observing the result merely to obtain a favorable support mapping.
