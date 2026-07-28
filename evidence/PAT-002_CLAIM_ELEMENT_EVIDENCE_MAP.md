# PAT-002 Claim-Element Evidence Map

## Status

Internal evidence-collection template for `PAT-002 — Heartbeat-Governed Entity and Reflected-State Computing`.

This file does not establish inventorship, ownership, priority, novelty, patentability, enablement, filing authority, or filing status.

## Source of Truth

```text
PATENTS_MIRROR_HANDOFF.md
data/master_claims.json
data/PAT-002-completion-status.json
```

## Evidence Classification

Use only these support states:

```text
VERIFIED_EXECUTABLE
VERIFIED_WRITTEN_DESCRIPTION
CANDIDATE_SOURCE_UNVERIFIED
PROPOSED_ONLY
UNSUPPORTED
```

Do not upgrade a state without an exact repository, path, commit or immutable identifier, date, and supporting excerpt or test/receipt.

## Candidate Source Repositories

```text
StegVerse-Labs/StegEntity
Data-Continuation/core-lite
```

Exact paths and commits remain unresolved.

## Limitation Map

### PAT-002-L1 — Composite State-Bearing Heartbeat

Working description:

```text
Forming a heartbeat from current system state, prior subsystem information, context, and routing intent.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- repository and exact path;
- immutable commit or blob identifier;
- dated written description or executable implementation;
- fields showing state, prior information, context, and routing intent;
- test, example, or receipt showing the heartbeat object in use.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L2 — Preflight Health and Admissibility Evaluation

Working description:

```text
Evaluating health and admissibility of the heartbeat before subsystem interaction.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- exact pre-interaction evaluation path;
- decision rules or policy references;
- allow, deny, defer, fail-closed, or equivalent outcome;
- proof that evaluation occurs before interaction or consequence;
- retained result or receipt.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L3 — Returned Subsystem Signal

Working description:

```text
Receiving one or more signals returned after subsystem interaction.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- source heartbeat or request identifier;
- target subsystem or interaction boundary;
- returned object, event, response, error, refusal, or acknowledgement;
- linkage between source and return;
- integrity or correlation mechanism.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L4 — Multidimensional Source-to-Return Delta

Working description:

```text
Determining a multidimensional delta between a source heartbeat and one or more returned subsystem signals.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- exact comparison implementation or specification;
- dimensions compared;
- source and returned values;
- deterministic or bounded evaluation method;
- output used by a later transition.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L5 — Whole-System State or Routing Update

Working description:

```text
Updating system state and later routing according to evaluated fresh subsystem data rather than merely reflecting the signal to its origin.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- pre-state and post-state;
- returned-data reference;
- update or routing decision;
- proof the update affects a wider system state or later route;
- receipt, event, or reconstruction record.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L6 — Reconstructable Witness Record

Working description:

```text
Providing a reconstructable representation of source, return, delta, and resulting state transitions to a witness record system.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- source-state reference;
- return-signal reference;
- delta record;
- resulting transition or disposition;
- integrity hash, event linkage, or reconstruction method;
- retained test or replay output.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

### PAT-002-L7 — Receipt

Working description:

```text
Generating a receipt identifying the relevant state-bearing heartbeat, interaction, returned evidence, evaluated result, and disposition.
```

Current support state: `CANDIDATE_SOURCE_UNVERIFIED`

Required evidence:

- receipt schema or implementation;
- exact fields linked to PAT-002 behavior;
- deterministic hash or signature behavior, if any;
- validator, test, or replay result;
- retained example output.

Evidence records:

| Repository | Path | Commit/blob | Date | Evidence type | Support state | Notes |
|---|---|---|---|---|---|---|
| TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | TO_VERIFY | CANDIDATE_SOURCE_UNVERIFIED | No exact anchor recorded |

## Combination-Level Evidence

The following combinations require separate support and must not be inferred merely because individual components exist:

1. composite heartbeat + preflight evaluation;
2. source heartbeat + returned signal + multidimensional delta;
3. evaluated delta + whole-system state or routing update;
4. source + return + delta + resulting transition witness;
5. complete combination with receipt-backed reconstruction.

## Human Fact Development Needed

- Identify contributors to each limitation and combination.
- Record earliest conception and corroboration evidence.
- Identify earliest written description and executable implementation.
- Audit enabling public disclosures.
- Separate factual contribution records from counsel's legal inventorship determination.

## Automation Resumption

After exact anchors are entered, automation may:

1. validate repository paths and immutable identifiers;
2. classify support states;
3. produce a source-anchor manifest;
4. refresh `data/PAT-002-completion-status.json`;
5. draft a bounded technical disclosure from verified material;
6. prepare a practitioner review packet.

## Current Decision

```text
FAIL_CLOSED_BLOCKERS
```
