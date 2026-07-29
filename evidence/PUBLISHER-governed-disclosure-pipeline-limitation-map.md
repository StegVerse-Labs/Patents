# Publisher Governed Disclosure Pipeline — Limitation Evidence Map

## Evidence decision

`PARTIAL_VERIFIED_EXECUTABLE_SUPPORT`

This map records bounded first-party support only. It does not determine novelty, inventorship, ownership, patentability, family boundaries, filing authority, or disclosure consequences.

## Immutable sources

1. `GCAT-BCAT-Engine/Publisher/tools/acquire_site_ecosystem_chat_propagation.py`
   - blob: `b55d7ed7ff83c5a90e3553a5a66d8598fb882d0e`
   - class: executable acquisition and bounded state emission
2. `GCAT-BCAT-Engine/Publisher/tools/check_site_ecosystem_chat_propagation.py`
   - blob: `7ab7a9d5150a1cbfbac96aa3c871671b90b03bfa`
   - class: executable fail-closed validation
3. `GCAT-BCAT-Engine/Publisher/tools/write_verification_run_receipt.py`
   - blob: `5668ede1678dd573dd132effbfa97610a439e454`
   - class: workflow receipt generation with explicit non-activation boundary
4. `GCAT-BCAT-Engine/Publisher/docs/PUBLISHER_MIRROR_HANDOFF.md`
   - blob: `f72c74af785973d8391323a47cdae973459958f7`
   - class: repository authority and workflow written description

## Limitation clusters and support

### Governed external packet acquisition
Supported by the acquisition script's fixed Site source, declared Publisher destination requirement, bounded timeout, and repository-local status output.

### Integrity and destination validation
Supported by canonical JSON hashing, declared-hash comparison, destination membership validation, source identity validation, and repository identity validation.

### Authority-escalation refusal
Supported by rejection when any incoming authority flag is true and by validation requiring publication, release, activation, admissibility, and execution authority flags to remain false.

### Separation of awareness from activation
Supported by the exclusive emitted states `PENDING_SITE_ACTIVATION` and `VERIFIED_INGESTION_READY`; ready status requires the upstream Site state `READY_FOR_DOWNSTREAM_INGESTION` and does not confer publication or execution authority.

### Exact blocker preservation
Supported by requiring a non-empty blocker list in pending state and forbidding blockers in ready state.

### Workflow verification receipt without activation conversion
Supported by the receipt writer's validation and dispatch fields, closure-evidence status, artifact references, and repeated non-claim that the receipt is not an activation receipt until a separate closure receipt exists.

### Ordered evidence and closure separation
Supported at written-description level by the Publisher handoff and receipt fields for Publisher receipt artifacts, Site evidence artifacts, age limits, ordering grace, pending probe, and closure receipt path.

## Unsupported or incomplete combination elements

The reviewed sources do not yet establish:

- a generalized disclosure-object schema independent of the Site propagation embodiment;
- a complete publication packet construction implementation;
- content-level redaction, secrecy classification, or claim-sensitive disclosure filtering;
- a production closure receipt writer and retained authoritative closure receipt;
- complete custody transfer or reconstruction behavior;
- a generalized downstream publication decision engine;
- retained authoritative traces covering denial, pending, ready, publication refusal, and publication authorization;
- conception chronology, contributors, inventorship, ownership, or legal disposition.

## Current boundary

The verified implementation supports a governed publication-awareness and packet-validation embodiment. It does not support treating the complete candidate family as implemented or filing-ready.
