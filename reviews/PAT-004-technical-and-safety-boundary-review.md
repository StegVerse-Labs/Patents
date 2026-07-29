# PAT-004 Technical and Safety Boundary Review

## Status

```text
BOUNDED_REVIEW_SURFACE_COMPLETE
IMPLEMENTATION_AND_SPECIALIST_EVIDENCE_PENDING
```

## Purpose

This document separates candidate technical functions and authority boundaries for `PAT-004 — Manifest-Governed Bidirectional Neural Communication`. It is not a medical, clinical, regulatory, ethical, human-subject, product-safety, patentability, or legal conclusion.

## Required functional separation

Any future disclosure, specification, claim theme, diagram, implementation map, or test report must distinguish at least these operations:

```text
1. passive signal observation
2. signal preprocessing
3. state interpretation or classification
4. inferred communication content
5. communication authorization
6. coupled-state authorization
7. stimulation proposal
8. stimulation authorization
9. stimulation execution
10. disengagement
11. recovery to autonomous operation
12. receipt generation and verification
```

Evidence that supports one operation must not be silently reused as proof of another.

## Candidate operating states

The structured family record supports investigation of, but does not prove implementation of:

```text
ISOLATED_UNCALIBRATED
ISOLATED_CALIBRATING
ISOLATED_CALIBRATED
COUPLING_PROPOSED
COUPLING_AUTHORIZED
COUPLED_OBSERVATION
COUPLED_COMMUNICATION
STIMULATION_PROPOSED
STIMULATION_AUTHORIZED
DISENGAGING
AUTONOMOUS_RECOVERY
FAIL_CLOSED
QUARANTINED
```

A future implementation must identify which states actually exist, who may transition them, required evidence, expiry behavior, and retained receipts.

## Authority matrix intake

For each operation preserve:

```text
operation:
proposer:
observer:
authorizer:
executor:
revoker:
required evidence:
minimum confidence or calibration basis:
expiry:
fail-closed condition:
receipt fields:
recovery behavior:
```

Unknown roles must remain unknown. A classifier output, manifest, operator request, or model recommendation is not automatically execution authority.

## Technical safety questions

### Signal and calibration integrity

```text
How is source identity established?
How is signal quality measured?
How is calibration scoped to person, device, session, task, and time?
How is drift detected?
What state follows calibration failure or expiry?
```

### Ambiguity and non-inference

```text
What uncertainty blocks interpretation?
What uncertainty blocks communication?
What uncertainty blocks coupling or stimulation?
How are ambiguous states retained without being treated as intent?
```

### Coupling and disengagement

```text
Is coupling bilateral, unilateral, or externally authorized?
Can each participant independently revoke coupling?
What happens on lost heartbeat, disagreement, lag, or partial failure?
How is autonomous recovery demonstrated?
```

### Stimulation boundary

```text
What technical artifact proposes stimulation?
What distinct artifact authorizes stimulation?
What limits are enforced independently of the proposing component?
What conditions force denial, stop, disengagement, or quarantine?
```

### Receipts and reconstruction

```text
Can calibration, authorization, execution, denial, disengagement, and recovery be reconstructed?
Are source, actor, device, model, policy, manifest, and state hashes retained?
Can a reviewer distinguish observation from intervention?
```

## Evidence classes required before drafting formal embodiments

```text
hardware identity and configuration
signal-acquisition schema
calibration procedure and outputs
classifier or interpretation implementation
manifest schema
state-transition schema
coupling authorization protocol
stimulation proposal and authorization protocol
technical interlocks
negative-path tests
runtime receipts
recovery and disengagement traces
specialist review records
```

## Unsupported assertions prohibited

Until supported by qualified evidence, drafts must not claim:

```text
clinical efficacy
medical benefit
diagnostic accuracy
treatment effect
human safety
regulatory compliance
validated intention detection
validated communication accuracy
safe stimulation limits
human-subject authorization
```

## Specialist review gates

Before any counsel-ready specification containing human neural observation or stimulation embodiments, preserve appropriate review inputs from qualified technical and, where applicable, medical, clinical, safety, regulatory, ethical, and human-subject specialists. The required specialist roles depend on the actual supported embodiment and must not be invented here.

## Current decision

```text
FAIL_CLOSED_IMPLEMENTATION_CALIBRATION_AUTHORITY_SAFETY_AND_SPECIALIST_BLOCKERS
```

## Resume condition

Automation may expand this review after immutable first-party implementation, test, calibration, authorization, interlock, receipt, and specialist-review records are committed.