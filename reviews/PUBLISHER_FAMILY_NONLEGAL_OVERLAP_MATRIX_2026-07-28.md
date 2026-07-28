# Publisher Family Non-Legal Overlap Matrix

## Purpose

This matrix records technical adjacency among Publisher-origin invention candidates. It is not a legal family determination, claim-construction analysis, inventorship conclusion, patentability opinion, continuation recommendation, or filing strategy.

No row authorizes merging, splitting, abandoning, publishing, or treating one family as covered by another.

## Relationship labels

- `SHARED_INPUT` — both families may consume the same evidence or state material.
- `SHARED_RECEIPT` — both may rely on receipts, hashes, provenance, or reconstruction records.
- `UPSTREAM_OF` — one technical process may precede another.
- `DOWNSTREAM_OF` — one technical process may consume another's result.
- `BOUNDARY_REFINEMENT` — one candidate may refine a narrower technical boundary of another.
- `IMPLEMENTATION_ADJACENCY` — current repository artifacts place the candidates near each other without establishing one combination.
- `FORMALISM_ADJACENCY` — they share mathematical or governance vocabulary.
- `DISTINCT_CONTROL_POINT` — available evidence places the principal control decisions at different stages.
- `UNRESOLVED` — evidence is insufficient to classify the relationship more specifically.

## Pairwise matrix

| Family A | Family B | Non-legal relationship | Current technical basis | Unresolved question |
|---|---|---|---|---|
| Commit-Time Admissibility Gate | Receipt-Based State Transition Validation | `SHARED_RECEIPT`, `UPSTREAM_OF`, `IMPLEMENTATION_ADJACENCY` | Commit-time decisions may emit receipts later used to validate state transitions. | Is receipt validation an element, dependent embodiment, or separate system? |
| Commit-Time Admissibility Gate | Publisher Governed Disclosure Pipeline | `DISTINCT_CONTROL_POINT`, `IMPLEMENTATION_ADJACENCY` | One concerns execution admission; the other concerns governed intake, validation, and publication-awareness workflow. | Does any claimed combination require both control points? |
| Commit-Time Admissibility Gate | Application Correction Gate | `UNRESOLVED` | No authoritative technical Application Correction source has been identified. | What technical object is corrected, and at what stage? |
| Commit-Time Admissibility Gate | AI Output-to-Action Boundary | `BOUNDARY_REFINEMENT`, `UPSTREAM_OF` | AI output may remain informational until a later authority-bearing commit decision. | Is the output-to-action separation broader than commit-time admissibility or a use case of it? |
| Commit-Time Admissibility Gate | Recoverability-Aware Execution Boundary | `BOUNDARY_REFINEMENT`, `FORMALISM_ADJACENCY` | Recoverability, consequence horizon, and calibrated fail-closed regions can constrain commit-time execution. | Is recoverability a required gate element, optional policy dimension, or separate family? |
| Commit-Time Admissibility Gate | Master-Records Reconstruction and Verification | `DOWNSTREAM_OF`, `SHARED_RECEIPT` | Master-record custody and reconstruction may verify the evidence and receipts of a prior gate decision. | Does reconstruction merely audit the gate or participate in admission? |
| Commit-Time Admissibility Gate | Multi-Entity Observer-Participant Admissibility | `FORMALISM_ADJACENCY`, `BOUNDARY_REFINEMENT` | Multi-entity roles and observer state may change the evidence evaluated at commit time. | Are observer/participant roles essential to a distinct combination? |
| Receipt-Based State Transition Validation | Publisher Governed Disclosure Pipeline | `SHARED_RECEIPT`, `IMPLEMENTATION_ADJACENCY` | Publisher workflow artifacts use validation results and bounded status records. | Are those receipts generic workflow evidence or the claimed transition-validation mechanism? |
| Receipt-Based State Transition Validation | Application Correction Gate | `UNRESOLVED` | No technical correction source establishes whether correction operates through replacement receipts or state repair. | Does correction create a superseding transition receipt? |
| Receipt-Based State Transition Validation | AI Output-to-Action Boundary | `SHARED_RECEIPT`, `DOWNSTREAM_OF` | A validated output packet can remain non-authorizing while producing a bounded status record. | Is receipt validation required before every output-to-action transition? |
| Receipt-Based State Transition Validation | Recoverability-Aware Execution Boundary | `SHARED_RECEIPT`, `FORMALISM_ADJACENCY` | Recoverability decisions may require retained decision traces and reconstruction residue. | Is validation post-transition, pre-transition, or both? |
| Receipt-Based State Transition Validation | Master-Records Reconstruction and Verification | `SHARED_RECEIPT`, `UPSTREAM_OF`, `DOWNSTREAM_OF` | Transition receipts may be ingested into custody; reconstruction can later validate receipt chains. | Which component owns canonical truth versus verification? |
| Receipt-Based State Transition Validation | Multi-Entity Observer-Participant Admissibility | `SHARED_RECEIPT`, `FORMALISM_ADJACENCY` | Observer and participant entities may emit conflicting or lagged receipts requiring reconciliation. | Is multi-party receipt reconciliation a distinct implementation? |
| Publisher Governed Disclosure Pipeline | Application Correction Gate | `UNRESOLVED` | A governed disclosure pipeline could contain correction or supersession stages, but no source proves this candidate. | Is correction an intake repair step, publication correction, or unrelated application-state gate? |
| Publisher Governed Disclosure Pipeline | AI Output-to-Action Boundary | `DISTINCT_CONTROL_POINT`, `IMPLEMENTATION_ADJACENCY` | Publisher accepts informational projections without granting execution authority. | Is this merely a pipeline safety property or a standalone execution-boundary family? |
| Publisher Governed Disclosure Pipeline | Recoverability-Aware Execution Boundary | `DISTINCT_CONTROL_POINT`, `FORMALISM_ADJACENCY` | Disclosure/publication workflow and execution recoverability govern different consequences. | Are they technically combined anywhere beyond common governance vocabulary? |
| Publisher Governed Disclosure Pipeline | Master-Records Reconstruction and Verification | `UPSTREAM_OF`, `SHARED_RECEIPT` | Publisher may consume custody and reconstruction evidence while retaining publication-awareness limits. | Is master-record verification a prerequisite, downstream audit, or independent service? |
| Publisher Governed Disclosure Pipeline | Multi-Entity Observer-Participant Admissibility | `IMPLEMENTATION_ADJACENCY` | Publisher workflow preserves workload ownership and may observe upstream entities without inheriting authority. | Does the pipeline instantiate the proposer/performer/observer triad? |
| Application Correction Gate | AI Output-to-Action Boundary | `UNRESOLVED` | No authoritative Application Correction source has resolved its technical meaning. | Does correction occur before an output becomes actionable? |
| Application Correction Gate | Recoverability-Aware Execution Boundary | `UNRESOLVED` | No source establishes correction as rollback, repair, or recoverability restoration. | Is correction an alternative to denial or quarantine? |
| Application Correction Gate | Master-Records Reconstruction and Verification | `UNRESOLVED` | Master records could preserve supersession, but no correction protocol is verified. | Does correction require immutable original and superseding records? |
| Application Correction Gate | Multi-Entity Observer-Participant Admissibility | `UNRESOLVED` | No source identifies who proposes, approves, performs, or observes a correction. | Is correction authority multi-party? |
| AI Output-to-Action Boundary | Recoverability-Aware Execution Boundary | `BOUNDARY_REFINEMENT`, `UPSTREAM_OF` | An AI output can remain non-authorizing; later action may additionally require recoverability-aware admission. | Are these sequential gates or alternative descriptions of one boundary? |
| AI Output-to-Action Boundary | Master-Records Reconstruction and Verification | `SHARED_RECEIPT`, `DOWNSTREAM_OF` | Output validation status and action authority records can be retained and reconstructed. | Does master-record custody contribute authority or only evidence? |
| AI Output-to-Action Boundary | Multi-Entity Observer-Participant Admissibility | `FORMALISM_ADJACENCY`, `IMPLEMENTATION_ADJACENCY` | Different entities may generate output, authorize action, perform action, and observe consequence. | Is the separated-role architecture required for the output-to-action family? |
| Recoverability-Aware Execution Boundary | Master-Records Reconstruction and Verification | `SHARED_RECEIPT`, `DOWNSTREAM_OF` | Recoverability decisions require calibration provenance, traces, residue, and later reconstruction. | Is retained reconstruction evidence an element of execution admission or an audit layer? |
| Recoverability-Aware Execution Boundary | Multi-Entity Observer-Participant Admissibility | `FORMALISM_ADJACENCY`, `BOUNDARY_REFINEMENT` | Recoverability and observability may differ across coupled entities with lagged authority and state knowledge. | Does multi-entity geometry create a separate recoverability invention center? |
| Master-Records Reconstruction and Verification | Multi-Entity Observer-Participant Admissibility | `SHARED_RECEIPT`, `FORMALISM_ADJACENCY` | Distributed entities may hold conflicting receipts requiring custody, reconciliation, and reconstruction. | Is multi-ledger reconciliation part of Master-Records or a separate observer-participant protocol? |

## Current technical clusters

### Cluster A — Admission and action boundary

- Commit-Time Admissibility Gate
- AI Output-to-Action Boundary
- Recoverability-Aware Execution Boundary

Shared surface: candidate action, authority separation, consequence assessment, fail-closed behavior, and a later authority-bearing transition.

Unresolved: whether these are independent families, dependent embodiments, continuation candidates, or one broader disclosure with multiple claim sets.

### Cluster B — Receipts, custody, and reconstruction

- Receipt-Based State Transition Validation
- Master-Records Reconstruction and Verification

Shared surface: state references, transition identity, receipts, parent linkage, hashes, provenance, custody, replay or reconstruction, explicit gaps, and supersession.

Unresolved: where validation ends and canonical custody/reconstruction begins.

### Cluster C — Governed workflow and correction

- Publisher Governed Disclosure Pipeline
- Application Correction Gate

Shared surface currently unproven beyond a possible workflow relationship. Application Correction Gate remains source-material blocked and must not be folded into the Publisher pipeline from title similarity.

### Cluster D — Multi-entity relational governance

- Multi-Entity Observer-Participant Admissibility
- Commit-Time Admissibility Gate
- Recoverability-Aware Execution Boundary
- Master-Records Reconstruction and Verification

Shared surface: multiple entities, partial observability, lag, authority relations, conflicting records, coupled consequence, and reconstruction.

Unresolved: whether the observer-participant architecture is a separate protocol, a generalized formal layer, or a dependent embodiment across several families.

## Counsel questions generated by this matrix

1. Which technical distinctions are sufficient to support separate independent families rather than dependent embodiments?
2. Which combinations have adequate written-description and enablement support today?
3. Which clusters should remain together to avoid unsupported new matter?
4. Which disclosures risk obviousness-type overlap or double-patenting concerns if filed separately?
5. Which subject matter is better retained as trade secret or defensive publication?
6. Does Application Correction Gate identify a real technical invention center once authoritative source material is supplied?
7. Should observer-participant roles be drafted as a generalized architecture or limited to verified implementations?

## Boundary

This matrix does not answer the counsel questions. It provides a bounded technical comparison surface for practitioner review.
