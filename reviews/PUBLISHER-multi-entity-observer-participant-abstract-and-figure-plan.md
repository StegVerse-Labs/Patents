# Multi-Entity Observer-Participant Admissibility — Working Abstract and Figure Plan

## Working abstract

A governed transition-evaluation system represents multiple bounded entities affected by a proposed transition and binds each entity to available local state, declared role, authority relation, observation timing, recoverability condition, and receipt references. Local coherence is evaluated separately from global coherence. Participant and observer evidence is used to attempt reconstruction of a candidate shared post-transition state while observation is prevented from automatically conferring execution authority. The transition is admitted only when required authority, receipts, timing, coherence, and recoverability conditions can be reconciled. Otherwise, the system returns a bounded refusal, hold, or quarantine disposition and preserves evidence sufficient to reconstruct the decision boundary.

## Abstract boundary

The abstract is a working technical summary derived from verified formal sources. It does not assert a completed implementation, novelty, patentability, inventorship, ownership, priority, or filing authorization.

## Figure plan

### Figure 1 — Multi-entity transition boundary

Show one proposed transition intersecting multiple bounded entities. Each entity has a local state, role, authority reference, observation timestamp, receipt chain, and recoverability state.

### Figure 2 — Local versus global coherence

Show separate local evaluations for affected entities followed by a distinct global-coherence and global-recoverability evaluation. Include a local-pass/global-fail branch.

### Figure 3 — Participant and observer evidence flow

Show proposal, performance, observation, and review as possible roles rather than a mandatory fixed triad. Separate observation evidence from execution authority.

### Figure 4 — Shared post-transition reconstruction

Show participant records and observer returns entering a reconciliation stage that attempts to construct a candidate shared post-transition state.

### Figure 5 — Fail-closed disposition

Show branches for `ALLOW`, `DENY`, `HOLD`, and `QUARANTINE`, with refusal conditions for conflicting receipts, authority drift, stale observation, incompatible local states, and insufficient global recoverability.

### Figure 6 — Reconstruction record

Show preserved inputs, per-entity evaluations, reconciliation result, disposition, and evidence references sufficient to reconstruct the decision boundary.

## Drawing status

```text
figure concepts: complete
formal drawings: not created
implementation-specific field names: unresolved
drawing approval: not authorized
```
