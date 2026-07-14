# PAT-005 Claim Architecture

**Family:** PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction  
**Status:** working claim concepts; not filed; requires patent-practitioner review

## Independent Method Concept

A computer-implemented method comprising:

1. receiving heterogeneous observation records associated with one or more physical devices, the observation records originating from different discovery transports or manual observation paths;
2. generating respective fingerprint records from the observation records;
3. deterministically merging fingerprint records satisfying a canonical identity relationship into an inventory record while retaining evidence identifying the source fingerprint records;
4. classifying the inventory record relative to one or more destination capability boundaries;
5. generating a recovery-plan record that distinguishes preparation of a destination artifact from authority to operate the physical device;
6. generating a destination-bound package containing the inventory identity, destination identity, one or more fingerprint-bound item records, a proposed action, and a review posture;
7. validating consistency between each item destination and the package destination;
8. emitting a receipt from which the inventory, classification, recovery plan, package, validation result, and disposition can be reconstructed.

## Independent System Concept

A system comprising:

- one or more discovery adapters configured to produce heterogeneous device observations;
- a fingerprinting component;
- a deterministic inventory builder;
- a destination classifier;
- a recovery-plan builder;
- a destination-package builder;
- a package validator;
- a receipt generator;
- a data store retaining linked evidence sufficient to reconstruct each transition.

The destination package does not independently grant operational authority to the physical device.

## Independent Publication-Provenance Concept

A computer-implemented publication method comprising:

1. reading a machine-readable release descriptor identifying a release tag, title, request artifact, status artifact, and release assets;
2. validating the descriptor and identified artifacts;
3. generating a release manifest containing hashes and sizes of the identified artifacts;
4. creating or verifying a source-control tag corresponding to the descriptor;
5. creating or verifying a hosted release corresponding to the tag;
6. obtaining observed tag and release state from the hosting system;
7. generating a publication receipt binding the source commit, tag, release URL, observed state, and release artifacts.

This concept should be evaluated separately because generic automated release publication and software-supply-chain attestation create substantial prior-art and obviousness risk.

## Dependent Claim Candidates

1. The method wherein the heterogeneous observations comprise at least two of BLE, LAN, audio, manual, model, label, service, or transport observations.
2. The method wherein canonical identity is based on a model observation when present and a normalized operator label when the model observation is absent.
3. The method wherein source fingerprint paths are retained in the inventory record.
4. The method wherein a generic destination automatically requires review.
5. The method wherein an unsupported item is preserved rather than omitted or automatically assigned.
6. The method wherein response options are constrained to an observation-only acceptance state, a review-required state, and a denial state.
7. The method wherein the destination package is non-authorizing and requires a separate authority decision before device operation.
8. The method wherein the receipt records both origin and destination artifacts.
9. The method wherein package preparation and device activation are represented as separate governed transitions.
10. The method wherein successful publication does not establish successful destination activation.
11. The method wherein release validation and release publication are limited to no more than two repository workflows.
12. The method wherein a current-release descriptor changes between releases without modifying the publication workflow.
13. The method wherein a publication receipt is attached to the hosted release after the release is independently queried.

## Highest-Value Claim Distinctions

The strongest candidate distinctions appear to be:

- canonical multi-transport identity reconstruction linked to source evidence;
- preservation of ambiguity and unsupported states throughout destination planning;
- a destination package that proposes continuity while explicitly withholding operational authority;
- receipt-linked reconstruction across discovery, classification, packaging, destination response, and publication;
- separation of technical reachability, destination compatibility, admissibility, and authority.

## Likely Weak or Crowded Elements

The following elements should not be relied upon alone:

- discovering Bluetooth or network devices;
- generating a hardware fingerprint;
- maintaining an inventory;
- classifying devices by capability;
- producing JSON packages;
- validating schemas;
- creating source-control tags or hosted releases;
- hashing release artifacts;
- using two CI workflows.

## Section 101 Framing

Claims should be grounded in concrete device observations, machine-generated fingerprint and inventory records, destination-bound package structures, validation of physical-device continuity relationships, and measurable effects on duplicate identity, unsupported-device handling, and unauthorized device operation. Avoid framing the invention merely as approval, recordkeeping, or organizing human activity.

## Enablement Checklist

Before provisional drafting, confirm support for:

- canonical identity rules and collision handling;
- duplicate merge examples;
- ambiguous-device examples;
- multiple destination classes;
- unsupported destination behavior;
- review-required behavior;
- package schema and validation rules;
- receipt linkage and reconstruction procedure;
- destination response and authority separation;
- publication verification and failure behavior;
- diagrams showing state transitions and data structures.
