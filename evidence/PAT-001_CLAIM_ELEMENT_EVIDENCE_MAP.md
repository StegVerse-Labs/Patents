# PAT-001 Claim-Element Evidence Map

**Patent family:** PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing

**Status:** Initial claim-level evidence map. Verified entries identify concrete repository evidence; unresolved entries require further corroboration. This document is not a legal conclusion and does not determine inventorship, novelty, or priority.

## Evidence posture labels

- **CONCEPTION** — documentary evidence describing the architecture or limitation.
- **REDUCTION TO PRACTICE** — executable implementation, schema, test, or verified runtime behavior.
- **CORROBORATION REQUIRED** — recollection or session evidence exists, but canonical source/commit has not yet been verified.
- **CLAIM REFINEMENT** — limitation was articulated after the earliest implementation and may require separate priority analysis.
- **VERIFIED SOFTWARE ARCHITECTURE** — immutable source/commit evidence verifies the stated software-side architecture but does not establish any still-pending physical/runtime predicate.
- **PARTIAL REDUCTION** — executable source/tests establish part of a candidate limitation while the complete physical/runtime proposition remains unproved.

## Candidate independent-claim limitations

| ID | Candidate limitation | Evidence | Date | Posture | Notes |
|---|---|---|---|---|---|
| P1-L01 | Receive or resolve a machine-readable manifest or governed request defining an addressable scope outside the manifest/request itself. | `StegVerse-Micro-Node-Agency.md`; June 6 system-map precursor; `MicroNodeRequest` fields in runtime evaluator. | 2026-06-06 / 2026-06-16 / 2026-07-02 | CONCEPTION + PARTIAL REDUCTION | Canonical repository and commit for the June documents still required. Runtime requires transition, origin, return path, action, actor, target, and scope. |
| P1-L02 | Bind the work request to a transition-table-native set of processing roles and obligations. | `transition_table/role_obligations.json`, commit `548e969ab5218772d08a00b73dce058d42a273b0`. | 2026-07-02 | REDUCTION TO PRACTICE | Defines observer, interpreter, authority checker, admissibility gate, decision role, receipt issuer, return carrier, and reconstruction witness obligations. |
| P1-L03 | Evaluate authority and admissibility as distinct required conditions before an ALLOW result. | `micro_node/runtime.py`, commit `53c5045babae5f3bb3f63430500a4939bf8364b8`. | 2026-07-02 | REDUCTION TO PRACTICE | Runtime separately checks delegation/authority and policy/admissibility, returning DENY or FAIL_CLOSED when standing is absent. |
| P1-L04 | Fail closed when required request fields or role evidence are missing or unknown. | `micro_node/runtime.py`, commit `53c5045babae5f3bb3f63430500a4939bf8364b8`; role obligations commit `548e969...`. | 2026-07-02 | REDUCTION TO PRACTICE | Explicit `FAIL_CLOSED` terminal decision and `default_unknown_decision`. |
| P1-L05 | Generate a bounded processing result from ordered role evaluations. | `micro_node/runtime.py`, commit `53c5045babae5f3bb3f63430500a4939bf8364b8`. | 2026-07-02 | REDUCTION TO PRACTICE | Produces a decision, reasons, role results, receipt, governed return, and reconstruction witness. |
| P1-L06 | Generate a cryptographically linked or hash-bound receipt identifying request and role evidence. | `micro_node/runtime.py`, commit `53c5045...`; receipt determinism verifier commit `515ec3e776cb6564f2d9d58078a893bf51b47024`. | 2026-07-02 | REDUCTION TO PRACTICE | Receipt binds request hash, decision, role-evidence hash, and optional previous receipt hash; verifier confirms repeated evaluation yields the same receipt hash. |
| P1-L07 | Produce a governed return path carrying the bounded decision back to an origin or declared destination. | `micro_node/runtime.py`, commit `53c5045...`; role obligation `return_path_carrier`. | 2026-07-02 | REDUCTION TO PRACTICE | Return payload includes return path, transition ID, decision, and receipt hash. |
| P1-L08 | Produce reconstruction evidence sufficient to compare a repeated execution against prior hashes. | `micro_node/reconstruction.py`, commit `4c65bb5e025635bf5c1ae318fe6d8ee801725249`; runtime integration commit `53c5045...`. | 2026-07-02 | REDUCTION TO PRACTICE | Witness binds request, role-result, receipt, and return-payload hashes and provides a replay hint. |
| P1-L09 | Require complete role coverage before a runtime result is accepted. | `micro_node/runtime.py`, commit `53c5045...`; role obligations commit `548e969...`; verifier commit `5424d1cbd95214899f6c9f6b520bbec89e7675b3`. | 2026-07-02 | REDUCTION TO PRACTICE | Runtime raises an error if required roles are absent; separate verifier was added. |
| P1-L10 | Determine whether an already active node possesses the manifest-required capability and construct a node only when no admissible capable node exists. | July 13–14 architecture discussion; prior micro-node minimalism rationale. | 2026-07-13–14 | CLAIM REFINEMENT / CORROBORATION REQUIRED | No canonical executable registry/query/construction commit has yet been mapped. This is a central candidate claim and requires careful priority treatment. |
| P1-L11 | Construct no more capability, authority, addressability, context, or tooling than the admitted manifest requires. | June 16 micro-node agency architecture; July 13–14 minimum-node formulation. | 2026-06-16 / 2026-07-13–14 | CONCEPTION + CLAIM REFINEMENT | Earlier document appears to support scoped authority and declared function; exact minimum-construction limitation needs canonical text and commit. |
| P1-L12 | Permit no unconceded alternative construction path outside manifest and transition-table derivation. | July 13–14 architecture discussion. | 2026-07-13–14 | CLAIM REFINEMENT | Strong portfolio distinction but not yet tied to executable enforcement evidence. |
| P1-L13 | Expire the processing node after completion by default while retaining durable receipts and reconstruction evidence. | June 28–29 ephemeral runtime discussion; micro-node reconstruction and receipt implementation. | 2026-06-28–29 / 2026-07-02 | CONCEPTION + PARTIAL REDUCTION | Runtime evidence proves durable evidence generation; actual process destruction/expiry implementation still requires canonical commit evidence. |
| P1-L14 | Delay expiry only when externally evidenced ongoing usage requires continued operation. | July 13–14 discussion. | 2026-07-13–14 | CLAIM REFINEMENT | Candidate dependent or continuation claim. Requires usage-lease implementation evidence. |
| P1-L15 | Preserve bounded prior context during delayed expiry without expanding authority or addressability. | July 13–14 discussion. | 2026-07-13–14 | CLAIM REFINEMENT | Candidate conversational/stream embodiment; no canonical implementation mapped yet. |
| P1-L16 | Prevent a node's own heartbeat from independently justifying persistence. | July 13–14 discussion. | 2026-07-13–14 | CLAIM REFINEMENT | Important anti-self-preservation limitation; likely dependent claim. |
| P1-L17 | Treat ephemeral network membership as resulting from an admitted, receipt-bound Node/Interlock/local-head relationship rather than from connectivity, addressability, heartbeat observation, or execution capability alone. | StegOS PR #32 merge `0758a31ac61d9ec19f65d5a40de683cac5a6a380`; PR #35 merge `47da2996d9442f6c7b359f6ee61ea7e949f793bd`; `docs/STEGOS_NODE_MANIFOLD_MIRROR_HANDOFF.md`. | No conception/RTP date assigned by this refinement | CLAIM REFINEMENT + PARTIAL REDUCTION + CORROBORATION REQUIRED | Software-side admission/binding exists; authentic retained physical network membership and second-node evidence remain pending. |
| P1-L18 | Derive current Network Manifold topology from each Node's latest accepted governed relationship while retaining historical observations only for reconstruction. | StegOS PR #29 merge `5bf75a2744aa7d4c688dc621a855bc7a6c5675a5`; PR #33 merge `9a7c521dd468ed404148fdec1ef6e58948cf470d`; StegOS manifold handoff. | No conception/RTP date assigned by this refinement | CLAIM REFINEMENT + PARTIAL REDUCTION + CORROBORATION REQUIRED | `NETWORK_PRESENT` and authentic multi-node resultant-manifold evidence remain pending. |
| P1-L19 | Keep observation/synchronization, credentials/routes, transition admissibility, execution capability, and reconstruction/reality authority distinct so evidence from one plane cannot self-promote into another. | StegOS PR #25 merge `14f3acddd61260c54ba8b3cbc6826d5fc4c6467d`; PR #35 merge `47da2996d9442f6c7b359f6ee61ea7e949f793bd`; canonical `STEGOS-NODE-MANIFOLD-001` task authority model. | No conception date assigned by this refinement | VERIFIED SOFTWARE ARCHITECTURE + CLAIM REFINEMENT | Verified as software/source authority separation only; does not imply completion of physical manifold predicates. |
| P1-L20 | Permit ephemeral execution substrates to disappear, expire, or be replaced while durable receipt lineage and reconstruction evidence preserve governed causal state independently of continued node existence. | Existing P1-L13 evidence; StegOS PR #28 merge `942adfe9dd3f7768c09f4e979938d5aa9db99b09`; PR #30 merge `3d48eb6ab4b11ce7b0013141e40cb8e3209f2474`; PR #34 merge `40c3b165c0eadd79dcda75315924be24d3bff784`. | No conception/RTP date assigned by this refinement | CLAIM REFINEMENT + PARTIAL REDUCTION + CORROBORATION REQUIRED | Durable evidence is implemented; actual PAT-001 expiry/destruction and real fragmentation/reformation remain unresolved. |
| P1-L21 | Accept a reformed Network Manifold as governed continuation only when replay/reconstruction of the retained causal transition sequence satisfies equality requirements, rather than on renewed reachability alone. | StegOS PR #30 merge `3d48eb6ab4b11ce7b0013141e40cb8e3209f2474`; StegOS manifold handoff; existing P1-L08 reconstruction witness evidence. | No conception/RTP date assigned by this refinement | CLAIM REFINEMENT + PARTIAL REDUCTION + CORROBORATION REQUIRED | Authentic fragmentation/reformation and exact multi-node replay equality remain pending. |

## Verified implementation evidence

### Transition-table role obligations

Commit: `548e969ab5218772d08a00b73dce058d42a273b0`

File: `transition_table/role_obligations.json`

Verified behavior:

- declares terminal decisions `ALLOW`, `DENY`, and `FAIL_CLOSED`;
- declares unknown/default behavior as fail closed;
- enumerates mandatory evidence fields for each runtime role;
- separates observation, interpretation, authority, admissibility, decision, receipt, return, and reconstruction.

### Runtime evaluator

Commit: `53c5045babae5f3bb3f63430500a4939bf8364b8`

File: `micro_node/runtime.py`

Verified behavior:

- hashes the request;
- validates required request fields;
- evaluates interpreter, authority, and admissibility conditions;
- issues ALLOW, DENY, or FAIL_CLOSED;
- generates a receipt;
- produces a governed return;
- builds reconstruction evidence;
- rejects incomplete role coverage.

### Deterministic receipt verification

Commit: `515ec3e776cb6564f2d9d58078a893bf51b47024`

File: `tools/verify_receipt_determinism.py`

Verified behavior:

- executes the same request twice;
- compares resulting receipt hashes;
- fails verification when hashes differ.

### Reconstruction witness

Commit: `4c65bb5e025635bf5c1ae318fe6d8ee801725249`

File: `micro_node/reconstruction.py`

Verified behavior:

- binds request, role-result, receipt, and return-payload hashes;
- emits a reconstruction hash;
- specifies replay using the same role order and hash comparison.

## Evidence still required

### Earliest architecture sources

- canonical repository and commit for `StegVerse-Micro-Node-Agency.md`;
- canonical source and commit for the 2026-06-06 core-micro system map;
- any earlier private design notes, diagrams, drafts, or messages.

### Demand construction

Locate executable evidence for:

```text
manifest admitted
→ required capability/addressability resolved
→ active node registry queried
→ no admissible node found
→ minimum node build generated
```

Likely repositories:

- `StegVerse-002/capability-registry`
- `StegVerse-002/micro-node-runtime`
- `StegVerse-Labs/StegEntity`
- `StegVerse-Labs/StegAgents`
- `StegVerse-org/core-node-runtime-demo`

### Ephemeral expiry and usage retention

Locate evidence for:

- default node expiry or destruction;
- delayed-expiry reason codes;
- externally evidenced lease renewal;
- conversation/stream context retention;
- authority non-expansion during reuse;
- prohibition on heartbeat-only retention.

### StegOS/InTr physical manifold proof

Do not upgrade P1-L17 through P1-L21 beyond their current posture until authentic retained evidence resolves the applicable canonical predicates:

- `DISTINCT_SECOND_ACTIVE_NODE_OBSERVED`;
- `NETWORK_PRESENT_PROVEN`;
- `REAL_FRAGMENTATION_AND_REFORMATION_OBSERVED`;
- `EXACT_MULTI_NODE_REPLAY_RECONSTRUCTION_EQUALITY`.

Preserve exact repository/path/SHA, physical receipt identity, artifact digest, Node/Interlock identity, transition lineage, observation date, and reconstruction result for each future upgrade.

### Cross-repository implementation lineage

Map commits and files from:

- `StegGhost/entity-sandbox-runner`
- `StegVerse-org/core-node-runtime-demo`
- `StegVerse-002/micro-node-runtime`
- related StegVerse-001/core-lite and ingestion-engine repositories.

## Preliminary claim strategy

### Strongest presently evidenced independent-claim core

The strongest currently verified technical combination is:

1. receive a transition request containing origin, destination/return path, actor, target, action, and scope;
2. evaluate it through transition-table-defined roles;
3. separately verify authority and admissibility;
4. fail closed when required evidence is absent;
5. produce a bounded decision;
6. issue a deterministic hash-bound receipt;
7. return the result through a declared path; and
8. generate reconstruction evidence covering the request, role results, receipt, and return payload.

### High-value limitations needing corroboration

The strongest differentiating additions remain:

- manifest-defined addressability;
- construction only after capable-node absence;
- minimum-capability node construction;
- default ephemeral expiry;
- usage-only delayed expiry;
- retained context without authority expansion;
- heartbeat cannot establish its own right to persist;
- receipt-derived network membership;
- receipt-derived current Network Manifold topology;
- non-self-promoting separation of observation, credential, transition, execution, and reconstruction authorities;
- disposable execution substrate with durable causal state; and
- reformation acceptance conditioned on replay/reconstruction equality.

These should not be represented as sharing the July 2 evidence date or any earlier conception date unless immutable supporting material establishes that date.

## Dedicated StegOS/InTr refinement packet

See `evidence/PAT-001_STEGOS_INTR_NETWORK_MANIFOLD_CLAIM_REFINEMENT.md` for limitation-by-limitation software evidence, physical proof gates, and collision-zone scope.

## Inventorship worksheet placeholder

For each limitation, counsel review must identify the human contributor or contributors who conceived the complete operative idea. Repository authorship, prompting, implementation, review, and organizational ownership must be evaluated separately.

| Limitation | Candidate human inventor(s) | Conception evidence | Corroborator | Status |
|---|---|---|---|---|
| P1-L01–L09 | TBD | June architecture records and July runtime | TBD | OPEN |
| P1-L10–L16 | TBD | July 13–14 discussions and any earlier records | TBD | OPEN |
| P1-L17–L21 | TBD | Current StegOS/InTr sources plus any earlier conception records to be located | TBD | OPEN — NO DATE ASSIGNED BY REFINEMENT |
