# PAT-005 Limitation-Level Prior-Art Claim Chart

**Status:** working search and comparison artifact; not a patentability opinion

## Use Rule

Each reference must be reviewed against every limitation. A reference category, abstract, title, or search-result snippet is not enough to establish anticipation or obviousness. Record publication number, priority date, publication date, assignee or author, exact passages, figures, and the reviewer responsible.

## Independent Method Concept

| ID | Candidate limitation | Source support | Known collision zones | Reference mapping status | Distinguishing question |
|---|---|---|---|---|---|
| M1 | receive heterogeneous observations of a physical device through different transports or manual paths | Device Continuity adapters, fixtures, schemas | service discovery, CMDB ingestion, IoT onboarding | search required | does a reference preserve each source observation as reconstructable identity evidence? |
| M2 | generate fingerprint records from observations | fingerprint tools and schemas | browser, sensor, network, RF, behavioral fingerprinting | crowded | is the fingerprint tied to continuity reconstruction rather than authentication alone? |
| M3 | deterministically merge related fingerprints into a canonical inventory identity while retaining source lineage | inventory builder, tests, source paths | entity resolution, deduplication, digital twins | search required | does the reference retain the exact source-fingerprint path after canonical merge? |
| M4 | classify the inventory relative to destination capability boundaries while preserving unsupported and ambiguous results | classifier, fixtures, validators | policy routing, driver matching, capability negotiation | search required | are unresolved items preserved rather than coerced into a destination? |
| M5 | generate a recovery plan distinct from authority to operate the device | recovery-plan builder and governance records | migration plans, deployment plans, access-control approvals | high-value review | does the reference technically separate preparation from operational authority? |
| M6 | generate a destination-bound package carrying identity, destination, proposed action, and review posture | package builder and schema | onboarding packages, deployment bundles, device profiles | search required | is the package expressly non-authorizing and destination constrained? |
| M7 | constrain destination responses to observation-only acceptance, review, refusal, or denial | StegTalk and StegMusic receipts | approval workflows, zero-trust posture, admission controllers | high-value review | is observation acceptance technically distinct from reliance and operation? |
| M8 | independently validate destination/package consistency | validators and tests | schema validation, policy validation | crowded individually | is validation linked to physical-device continuity and authority state? |
| M9 | emit linked receipts reconstructing source observation through destination disposition | receipts, Site, Publisher, wiki records | audit logs, provenance systems, event sourcing | high-value review | can the complete cross-repository transition be reconstructed in reverse? |
| M10 | preserve non-inference when evidence or authority is incomplete | failure matrix and guardian boundary | fail-closed security, incomplete-data handling | search required | does the system preserve unresolved continuity without false activation? |

## Publication-Provenance Concept

| ID | Candidate limitation | Collision risk | Current treatment |
|---|---|---:|---|
| P1 | machine-readable current-release descriptor | high | dependent or separate claim candidate only |
| P2 | validate referenced release artifacts | high | do not rely on alone |
| P3 | generate artifact hashes and sizes | very high | do not rely on alone |
| P4 | create or verify tag and hosted release | very high | do not rely on alone |
| P5 | independently query observed publication state | medium | evaluate as part of ordered combination |
| P6 | bind source commit, tag, release URL, observed state, and artifacts into a publication receipt | medium | evaluate separately from core hardware-continuity claims |

## Search Buckets

A qualified search should include at least:

- device and browser fingerprinting;
- physical unclonable and RF fingerprinting;
- entity resolution and probabilistic record linkage;
- digital twins and device identity graphs;
- IoT commissioning and zero-touch onboarding;
- hardware abstraction and driver binding;
- configuration-management databases;
- device migration, backup, and recovery;
- policy admission controllers and zero-trust device posture;
- event sourcing and distributed provenance;
- software supply-chain attestations and release provenance;
- non-authorizing proposals, dry-run deployment, and approval separation.

## Completion Standard

This chart is complete only when each material reference includes:

1. stable publication identifier;
2. verified priority and publication dates;
3. exact mapped passages or figures;
4. limitation-by-limitation result;
5. single-reference anticipation assessment;
6. multi-reference combination rationale and counterargument;
7. reviewer identity and review date.
