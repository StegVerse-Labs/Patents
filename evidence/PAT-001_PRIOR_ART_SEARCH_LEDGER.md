# PAT-001 Prior-Art Search Ledger

**Patent family:** PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing

**Status:** Search-control and evidence-recording ledger. No entry is a legal conclusion regarding novelty, obviousness, patentability, validity, or freedom to operate.

## Search discipline

Every search event must record:

- search date and researcher;
- database or corpus;
- exact query or classification;
- date restrictions;
- result identifiers and stable copies where permitted;
- mapped PAT-001 limitations;
- whether the reference teaches the element directly, implicitly, or not at all;
- whether multiple references would need to be combined;
- unresolved interpretation questions;
- counsel review posture.

Patentability searching and freedom-to-operate analysis must remain distinct. A reference may be relevant to one and not the other.

## Candidate collision zones

| Zone | Why relevant | PAT-001 limitations most exposed | Differentiating focus |
|---|---|---|---|
| Actor systems and actor-model runtimes | Dynamically create bounded workers with isolated state and message addressing. | P1-L01, L03, L05, L11, L13 | Manifest-derived minimum addressability, transition authority, receipts, and usage-only retention. |
| Microservices and service meshes | Scope services, route requests, issue telemetry, and manage lifecycle. | P1-L01, L03, L07, L13 | Construction only after admissible-capability absence and no unconceded construction path. |
| Serverless and function-as-a-service | Demand-triggered ephemeral execution and scaling. | P1-L03, L05, L13 | Transition-table role binding, separate authority/admissibility, deterministic governance receipts, bounded reuse. |
| Container and workload schedulers | Resolve capability/resources and instantiate workloads. | P1-L02, L03, L10, L11, L13 | Manifest-defined addressability and governance standing rather than resource availability alone. |
| Workflow and finite-state engines | Execute transitions under declared state machines. | P1-L02, L04, L05, L09 | Role evidence, authority/admissibility separation, return-path and reconstruction receipts. |
| Agent orchestration and tool routers | Select agents/tools according to task capability. | P1-L01, L10, L11, L12 | Minimum-addressability node construction, no authority expansion, default expiry. |
| Capability-based security | Grants narrow authorities and object capabilities. | P1-L01, L03, L11, L12 | Demand construction plus transition-bound lifecycle and receipt evidence. |
| Policy-as-code and authorization engines | Evaluate policy, identity, delegation, and deny decisions. | P1-L03, L04 | Integration into node construction, role coverage, return path, and reconstruction witness. |
| Event sourcing and tamper-evident logs | Preserve state transitions and replay evidence. | P1-L06, L08, L13 | Receipt binds node build/addressability/disposition and governs execution before consequence. |
| Lease-based distributed systems | Retain resources while leases or heartbeats remain valid. | P1-L14, L15, L16 | Externally evidenced usage rather than heartbeat-only self-retention; authority remains bounded. |
| Object pools and warm serverless instances | Reuse active instances to reduce startup cost. | P1-L10, L14, L15 | Reuse conditioned on admissibility and active usage, without scope or authority expansion. |
| Autonomic and self-healing systems | Monitor health and preserve or recreate components. | P1-L13, L14, L16 | Node cannot establish its own right to persist; external standing controls retention. |

## Search term matrix

### Core combination

- `manifest bounded processing node transition table receipt`
- `dynamic worker authority admissibility fail closed receipt`
- `ephemeral processing node deterministic receipt reconstruction`
- `minimum capability runtime manifest scope`
- `transition table role evidence governed execution`
- `request scoped actor cryptographic receipt lifecycle`

### Demand construction and active-node resolution

- `capability registry reuse existing worker before instantiate`
- `active service capability resolution dynamic creation`
- `task capability matching create agent only if absent`
- `manifest required capability workload constructor`
- `minimum privilege serverless function generation`

### Expiry and usage retention

- `ephemeral worker delayed expiration active usage lease`
- `conversation context worker retention lease`
- `heartbeat insufficient lease renewal external activity`
- `resource persistence external evidence not heartbeat`
- `bounded context reuse without privilege expansion`

### Receipt and reconstruction

- `execution receipt request hash role evidence`
- `tamper evident workflow decision receipt replay`
- `cryptographic proof policy authorization execution`
- `event sourced authorization decision reconstruction`

## Classification candidates

The following classifications are starting points only and must be confirmed in current USPTO, CPC, WIPO, and Espacenet classification tools:

- distributed processing and workload allocation;
- virtual machines, containers, and dynamic resource provisioning;
- access control, authorization, and policy enforcement;
- workflow and state-machine execution;
- cryptographic verification and tamper-evident records;
- event sourcing, replay, and state reconstruction;
- autonomous or agent-based computing;
- lifecycle, lease, and resource-retention control.

Record exact CPC/IPC symbols only after database verification.

## Search-event ledger

| Event ID | Date | Researcher | Database/corpus | Exact query/classification | Date limits | Results preserved | Limitation mapping | Status |
|---|---|---|---|---|---|---|---|---|
| PA-001 | TBD | TBD | USPTO Patent Public Search | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-002 | TBD | TBD | Google Patents | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-003 | TBD | TBD | WIPO Patentscope | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-004 | TBD | TBD | Espacenet | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-005 | TBD | TBD | IEEE Xplore / ACM Digital Library | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-006 | TBD | TBD | arXiv and technical literature | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |
| PA-007 | TBD | TBD | Open-source repositories and release history | TBD | Before earliest claimed priority | No | TBD | NOT STARTED |

## Reference analysis template

### Reference ID: TBD

- **Title:**
- **Patent/publication number or persistent identifier:**
- **Applicant/author:**
- **Priority date:**
- **Publication date:**
- **Source database:**
- **Stable copy or archive location:**
- **Relevant figures/claims/paragraphs:**
- **P1 limitation mapping:**
- **Direct teaching, implicit teaching, or missing:**
- **Single-reference concern or combination concern:**
- **Differences from PAT-001:**
- **Potential design-around relevance:**
- **Patentability relevance:**
- **Freedom-to-operate relevance:**
- **Counsel status:**

## Combination-analysis ledger

| Combination ID | References considered together | Motivation to combine | PAT-001 limitations potentially covered | Missing differentiators | Status |
|---|---|---|---|---|---|
| COMB-001 | TBD | TBD | TBD | TBD | NOT STARTED |

## Highest-value differentiators to test

Search and claim review should determine whether prior art teaches the complete combinations below rather than isolated pieces:

1. transition-table-native ordered roles **plus** distinct authority and admissibility checks **plus** fail-closed handling;
2. demand construction only after absence of an admissible active capable node;
3. construction limited to manifest-required capability, authority, addressability, context, and tools;
4. a deterministic receipt binding request, role evidence, decision, return path, reconstruction data, and node disposition;
5. default expiry with retention only through externally evidenced ongoing usage;
6. retained context without authority or addressability expansion;
7. prohibition on heartbeat-only self-justified persistence.

## Completion gate

The ledger is filing-review ready only when:

- searches cover patents and non-patent literature;
- exact queries and classifications are reproducible;
- references are preserved and mapped limitation by limitation;
- earliest dates are verified;
- combination risks are recorded;
- patentability and freedom-to-operate postures are separated;
- qualified counsel has reviewed the material references.