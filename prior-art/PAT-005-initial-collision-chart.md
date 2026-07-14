# PAT-005 Initial Prior-Art Collision Chart

**Family:** PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction  
**Status:** search leads and technical comparison only; not a patentability opinion

## Review Rule

Each source below is a collision candidate, not a conclusion. A registered patent practitioner should verify publication numbers, priority dates, family members, claim scope, legal status, and applicability before relying on this chart.

## Initial Search Leads

### A. Sensor-based mobile-device fingerprinting

Source lead: *Mobile Device Identification via Sensor Fingerprinting* (Bojinov, Michalevsky, Nakibly, Boneh, 2014).

Potential overlap:

- hardware-derived device identity;
- multiple physical sensor characteristics;
- collision probability and identity confidence;
- remote device identification.

Apparent PAT-005 distinctions requiring claim review:

- heterogeneous observations are retained as source evidence rather than collapsed into a tracking identifier only;
- canonical inventory merge is part of a continuity pipeline;
- destination compatibility, review posture, and unsupported states are preserved;
- the resulting destination package expressly withholds operational authority;
- destination receipts and governance propagation are reconstructable.

### B. Behavioral IoT fingerprinting

Source lead: *IoTSense: Behavioral Fingerprinting of IoT Devices* (Bezawada et al., 2018).

Potential overlap:

- device type identification;
- network-traffic-derived features;
- device-category classification;
- operation with encrypted network traffic.

Apparent PAT-005 distinctions requiring claim review:

- merges multiple transport and manual observations into a canonical inventory identity;
- retains source fingerprint lineage;
- classifies relative to destination capability boundaries rather than device type alone;
- generates non-authorizing destination packages and receipts;
- preserves ambiguity and denial rather than forcing classification.

### C. Sovereign and secure IoT onboarding

Source lead: *ASOP: A Sovereign and Secure Device Onboarding Protocol for Cloud-based IoT Services* (Reaz and Wunder, 2024).

Potential overlap:

- sovereign onboarding;
- human-in-the-loop control;
- reduced dependence on manufacturer or supply-chain trust;
- secure device-to-service admission.

Apparent PAT-005 distinctions requiring claim review:

- concerns continuity reconstruction from heterogeneous observations before onboarding;
- separates package preparation, destination acceptance, admissibility, and operation authority;
- supports multiple destinations and unsupported states;
- produces cross-repository receipts and publication evidence;
- does not require cloud onboarding as the terminal state.

### D. Generic device fingerprinting and configuration inventory

Collision categories:

- browser and hardware fingerprinting;
- configuration-management databases;
- asset inventory systems;
- service discovery;
- driver matching;
- digital-twin registries.

Elements likely crowded when claimed alone:

- collecting device attributes;
- generating an identifier;
- storing an inventory record;
- classifying by capability;
- producing a JSON representation.

Candidate combined distinctions:

- deterministic source-linked merge;
- explicit unresolved and unsupported outcomes;
- destination-bound package preparation without authority grant;
- independent destination receipt;
- guardian and admissibility boundary propagation;
- reverse reconstruction from public or destination evidence to source observations.

### E. Software provenance and release attestations

Collision categories:

- software bill of materials;
- signed build provenance;
- source-control release automation;
- artifact hashing;
- deployment approvals;
- in-toto, SLSA, and related supply-chain attestations.

Elements likely crowded when claimed alone:

- release manifests;
- artifact hashes;
- source commit references;
- hosted-release creation;
- publication receipts.

Potential PAT-005 distinction:

Publication evidence is not the inventive center by itself. Its relevance is the use of publication and mirror receipts as the final reconstructable layers of a physical-device continuity path that still does not establish device activation or operational authority.

## Limitation-Level Collision Matrix

| PAT-005 limitation | Likely collision zone | Present differentiation hypothesis | Evidence needed |
|---|---|---|---|
| heterogeneous observation intake | discovery and fingerprinting | observations retained by source path and used in continuity reconstruction | adapter examples and lineage fixtures |
| deterministic canonical merge | entity resolution and CMDB deduplication | merge tied to physical-device evidence and downstream destination package | collision rules and negative examples |
| destination-relative classification | driver/service matching | preserves generic, unsupported, and manual-review states | rule history and failure fixtures |
| recovery plan distinct from authority | onboarding and deployment planning | preparation cannot imply operation or trust | conception evidence and destination receipts |
| non-authorizing destination package | access requests and deployment manifests | package carries explicit constrained response semantics | StegTalk and StegMusic receipts |
| independent destination response | distributed workflows | destination must emit its own reconstructable receipt | exact destination validators and receipts |
| guardian/admissibility propagation | policy engines and approval systems | reachability, compatibility, admissibility, and authority remain separate | wiki pages and receipts |
| reverse reconstruction | provenance systems | reconstructs from public/destination evidence back to physical observations | end-to-end reconstruction test |

## Search Expansion Plan

1. Search patents and non-patent literature separately for every independent limitation.
2. Search combinations, not only individual elements.
3. Capture exact patent publication numbers, priority dates, independent claims, and relevant figures.
4. Build element-by-element charts against the narrowest supported PAT-005 independent claim.
5. Preserve both adverse and favorable results.
6. Do not use absence from an initial search as evidence of novelty.
