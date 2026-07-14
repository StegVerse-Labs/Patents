# PAT-005 Cross-Repository Source Map

**Family:** PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction  
**Status:** working evidence map; not filed; not a patentability opinion

## Purpose

This map identifies every repository presently involved in the conception, implementation, destination integration, publication, governance interpretation, and patent intake of PAT-005. It is intended to prevent a provisional or later application from describing only the source repository while omitting destination-side, governance, publication, or reconstructability aspects.

## Repository Roles

### 1. `StegVerse-Labs/device-continuity-layer`

Primary executable implementation and source of truth for the continuity pipeline.

Material aspects include:

- BLE, LAN, audio, and manual discovery adapters;
- heterogeneous observation fixtures and validators;
- fingerprint generation and stable fingerprint records;
- deterministic inventory construction and duplicate merge behavior;
- retained source fingerprint paths;
- destination classification with explicit generic, unsupported, and manual-review outcomes;
- recovery-plan generation separating package preparation from device-operation authority;
- deterministic destination bundle grouping;
- destination-bound package generation;
- package response options and review posture;
- package and receipt validation;
- StegTalk and StegMusic contracts and integration payloads;
- release request, status, manifest, and publication-receipt artifacts;
- two-workflow validation and publication architecture.

High-value paths include:

- `adapters/`
- `tools/build_inventory.py`
- `tools/classify_inventory.py`
- `tools/build_recovery_plan.py`
- `tools/build_destination_bundles.py`
- `tools/build_destination_packages.py`
- `tools/validate_inventory.py`
- `tools/validate_inventory_pipeline.py`
- `tools/validate_destination_bundles.py`
- `tools/validate_destination_packages.py`
- `contracts/stegtalk-device-adapter.contract.md`
- `contracts/stegmusic-device-adapter.contract.md`
- `integrations/stegtalk-consumption-task.md`
- `integrations/stegmusic-consumption-task.md`
- `integrations/payloads/stegtalk-device-continuity-handoff.json`
- `integrations/payloads/stegmusic-device-continuity-handoff.json`
- `fixtures/acceptance/stegtalk-package.json`
- `fixtures/acceptance/stegmusic-package.json`
- `receipts/`
- `releases/current.json`
- `tools/build_release_manifest.py`
- `tools/build_publication_receipt.py`
- `.github/workflows/check.yml`
- `.github/workflows/tag-release.yml`

### 2. `StegVerse-Labs/StegTalk`

Communication-destination implementation context.

Material aspects to preserve:

- destination-side contract intake;
- device-continuity payload validation;
- observation-only acceptance semantics;
- explicit non-authorization of microphone, speaker, button, sensor, radio, or communication operation;
- destination receipt generation;
- separation of entity recognition, reliance, readiness, commitment, transition, discovery, revocation, and operational authority;
- interaction between recovered hardware identity and StegTalk entity/runtime boundaries.

The StegTalk entity-runtime work is relevant because it represents commitment and transition as separate records rather than treating recognition or discovery as execution authority.

### 3. `StegVerse-Labs/StegMusic`

Media-destination implementation context.

Material aspects to preserve:

- destination-side contract intake;
- device-continuity payload validation;
- observation-only acceptance semantics;
- media renderer, receiver, controller, speaker, amplifier, and transport handling;
- unsupported and ambiguous media capability preservation;
- separation between identifying or preparing a media device and authorizing playback, routing, control, or persistent reliance;
- destination receipt generation.

Because this repository is private, exported legal-review evidence should preserve repository path, commit, hash, and access status without making confidential material public.

### 4. `StegVerse-Labs/Site`

Public ecosystem status and mirror evidence.

Known relevant paths include:

- `data/device-continuity-layer.json`
- `data/device-continuity-layer-receipt.json`

Material aspects include:

- public-facing representation of the implementation state;
- mirror receipt and source-to-site propagation evidence;
- distinction between installed documentation and verified production deployment;
- possible earlier public-disclosure dates that must be audited.

### 5. `GCAT-BCAT-Engine/Publisher`

Publication and distribution evidence.

Known relevant paths include:

- `Papers/device-continuity-layer-governed-hardware-abstraction.md`
- `data/device-continuity-layer.json`
- `data/device-continuity-receipt.json`

Material aspects include:

- public written description of the architecture;
- publication-receipt and propagation evidence;
- boundary statements preventing publication from being treated as activation or deployment;
- known public-disclosure commit `661521388485f275a9231394dd2308bb52db68d3`.

### 6. `StegVerse-Labs/admissibility-wiki`

Governance and admissibility interpretation.

Known relevant paths include:

- `pages/device-continuity-admissibility.md`
- `receipts/device-continuity-admissibility-receipt.json`

Material aspects include:

- formal separation among discovery, compatibility, admissibility, and authority;
- treatment of ambiguous or unsupported devices;
- fail-closed and review-required states;
- public governance explanation and receipt evidence;
- possible public-disclosure dates for claim limitations.

### 7. `StegVerse-002/stegguardian-wiki`

Guardian and operational-boundary interpretation.

Material aspects to preserve:

- guardian-side explanation of observation, review, refusal, and authority boundaries;
- treatment of destination packages as non-authorizing evidence;
- distinction between technical reachability and permission to operate;
- propagation receipts and page history when located and verified.

Any absent or unverified path must remain marked as pending rather than inferred.

### 8. `StegVerse-Labs/Patents`

Portfolio, claim, evidence, and deadline management.

Material aspects include:

- `disclosures/PAT-005-governed-device-continuity.md`
- `claims/PAT-005-claim-architecture.md`
- `evidence/PAT-005-evidence-ledger.md`
- `evidence/PAT-005-cross-repository-source-map.md`
- `triage/PAT-005-public-disclosure-and-filing-triage.md`
- repository-wide claim and evidence rules;
- inventorship uncertainty and contributor analysis;
- disclosure-date audit and practitioner-review status.

## Cross-Repository Transition Chain

The complete candidate invention should be evaluated as a linked chain:

```text
Device observation
→ source fingerprint
→ canonical inventory
→ destination classification
→ recovery plan
→ destination bundle
→ non-authorizing destination package
→ destination-side validation
→ observation / review / denial posture
→ separate authority transition, if any
→ source and destination receipts
→ Site mirror evidence
→ Publisher paper and publication receipt
→ admissibility and guardian interpretation
→ patent evidence and claim mapping
```

A patent draft that omits the destination repos risks losing the non-authorizing destination-response aspect. A draft that omits Site, Publisher, or wiki evidence risks losing the reconstructable propagation and publication-boundary aspect. A draft that omits source implementation risks becoming an abstract approval or recordkeeping description.

## Claim-Support Categories

### Physical-device and machine-operation support

Primarily from `device-continuity-layer`, StegTalk, and StegMusic:

- concrete observations;
- machine-generated fingerprints and inventories;
- package generation and validation;
- destination-specific handling;
- operational-authority separation.

### Governance and fail-closed support

Primarily from `admissibility-wiki`, `stegguardian-wiki`, destination receipts, and source contracts:

- review-required outcomes;
- unsupported-device retention;
- refusal and denial states;
- no inference from reachability to authority.

### Reconstruction and publication support

Primarily from source receipts, Site, Publisher, and release workflows:

- source-to-destination evidence chain;
- mirror receipts;
- artifact hashes;
- release descriptors and manifests;
- publication receipts;
- public-disclosure history.

## Required Evidence Completion

1. Resolve exact StegTalk destination-side paths and commits.
2. Resolve exact StegMusic destination-side paths and commits while preserving confidentiality.
3. Locate the StegGuardian page and receipt paths or mark them absent.
4. Record exact commits for Site and admissibility-wiki artifacts.
5. Capture negative and failure fixtures across source and destination repos.
6. Export a claim-by-claim evidence bundle with hashes.
7. Audit all public disclosure dates across Publisher, Site, wikis, repository README files, and external posts.
8. Obtain human conception statements for each claimed cross-repository limitation.

## Boundary

Repository relationships and implementation evidence do not establish patentability, inventorship, ownership, priority, or filing status. They provide technical support for qualified legal review.
