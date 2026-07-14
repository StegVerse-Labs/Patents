# PAT-001 Conception and Disclosure Chronology

**Patent family:** PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing

**Status:** Working evidence chronology for inventorship, disclosure, and counsel review. This document is not a legal conclusion.

## 2026-06-06 — Core-micro kernel and manifest/receipt gate documented

A StegVerse system map recorded:

- an ephemeral-address schema issued only for ingestion;
- an address-plus-receipt two-part gate;
- a `core-micro kernel at every acting level`;
- receipt/manifest carriage of an admissibility predicate and outcome;
- the distinction between governance evidence and ordinary logging.

This is an early architecture precursor. It should be reviewed for whether it supports later PAT-001 limitations involving bounded execution units, manifest-defined scope, transition admissibility, and receipt-bearing action.

## 2026-06-16 — Micro-node agency architecture explicitly documented

`StegVerse-Micro-Node-Agency.md` was created on 2026-06-16.

The document states that micro-node agency is the newest refinement after governed multi-tier intellectual AI hierarchy and defines a micro-node as:

> a scoped, receipt-bearing, revocable AI work unit that may perform one declared function inside a governed system, but may not treat successful output or execution as authority.

It further identifies:

- a transition from one large autonomous agent to many small governed agency cells;
- identity, purpose, authority boundary, policy scope, allowed inputs and outputs, declared task IDs, receipt schema, review triggers, revocation triggers, and failure behavior as minimum node structure;
- declared route before tool use;
- receipts before binding;
- external review before authority expansion;
- revocation and reaccreditation paths;
- cost and governance advantages over recursive agent loops;
- state drift, compute use, tool ambiguity, and reconstruction difficulty as motivating problems.

This is currently the earliest recovered document that expressly names and defines the micro-node agency structure.

## 2026-06-28 through 2026-06-29 — Ephemeral runtime formulation

Later implementation discussions around `StegVerse-002/micro-node-runtime` refined the architecture toward:

- ephemeral micro-node instantiation from a manifest and receipt context;
- activation of only required governed capabilities;
- deterministic decision and receipt production;
- destruction of runtime state while preserving reconstructable evidence;
- stable hashes and explicit timing;
- minimization of retained runtime and transmitted state.

These discussions appear to move the concept from architecture into executable runtime design.

## 2026-06-29 — `StegGhost/entity-sandbox-runner` transition-driven processing

The sandbox runner was refined toward:

```text
manifest
→ ingestion
→ fingerprint
→ transition lookup
→ admissibility determination
→ routing decision
→ transition receipt
```

This supports the operational lineage in which the communication and execution package was reduced to the minimum governed transition unit rather than a generalized persistent runtime.

## 2026-07-02 — Runtime and demo separation

The relationship between:

- `StegVerse-002/micro-node-runtime`; and
- `StegVerse-org/core-node-runtime-demo`

was formalized so that the micro-node runtime served as the portable transition-table-native governance unit, while the larger demo runtime adapted around and validated against that contract.

The governing rule was that each role must be expressed as a transition-table role and each role action must produce or update transition evidence.

## 2026-07-13 through 2026-07-14 — Demand construction and usage retention clarified

The architecture was further clarified:

- an admitted manifest establishes required addressability;
- the ecosystem first queries for an existing admissible capable node;
- absence of such a node warrants construction;
- construction is limited to the minimum node capable of satisfying the manifest;
- no alternative unconceded construction method is permitted;
- nodes expire by default;
- delayed expiry is justified only by externally evidenced active usage, such as a conversation, stream, pending feedback, or coupled operation;
- retained nodes preserve bounded prior context;
- heartbeat proves coherence but does not independently justify persistence.

These refinements are central candidate limitations for PAT-001.

## Candidate conception milestones

| Date | Candidate milestone | Current posture |
|---|---|---|
| 2026-06-06 | Core-micro kernel, ephemeral addressing, and manifest/receipt gate | Precursor; requires source verification |
| 2026-06-16 | Explicit micro-node agency definition and architecture | Strong documented conception evidence |
| 2026-06-28–29 | Ephemeral manifest/receipt-driven runtime | Implementation refinement |
| 2026-06-29 | Transition-driven sandbox runner | Cross-repository operational refinement |
| 2026-07-02 | Portable micro-node contract separated from larger demo runtime | Formal runtime boundary |
| 2026-07-13–14 | Demand-only construction and usage-only retention | Claim refinement |

## Required corroboration work

1. Locate the canonical repository and commit for `StegVerse-Micro-Node-Agency.md`.
2. Locate the source and commit history for the 2026-06-06 system map.
3. Extract commits, files, tests, manifests, schemas, and receipts from:
   - `StegVerse-002/micro-node-runtime`
   - `StegGhost/entity-sandbox-runner`
   - `StegVerse-org/core-node-runtime-demo`
   - relevant StegVerse-001/core-lite repositories.
4. Identify each human contributor to conception of each claimed limitation.
5. Separate conception evidence from reduction-to-practice evidence.
6. Record every public repository, post, demonstration, or external disclosure date.
7. Preserve private supporting material for counsel review.

## Non-conclusions

This chronology does not establish:

- patentability;
- novelty;
- non-obviousness;
- inventorship;
- ownership;
- freedom to operate;
- entitlement to any particular priority date.

Those determinations require claim-level legal analysis and corroborated evidence.
