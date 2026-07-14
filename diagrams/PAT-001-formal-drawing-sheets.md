# PAT-001 Formal Drawing Sheets — Working Source

**Patent family:** PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing

**Status:** provisional drawing source for technical and counsel review; not USPTO-formatted drawings and not evidence of filing.

## Drawing conventions

- Solid arrows represent verified data, decision, receipt, or reconstruction flow.
- Dashed arrows represent proposed, conditional, or not-yet-corroborated transitions.
- Double-bordered nodes represent independently governed systems or durable witness stores.
- Reference numerals in the 100 series identify request and intake components.
- Reference numerals in the 200 series identify transition-role components.
- Reference numerals in the 300 series identify decision, receipt, return, and reconstruction components.
- Reference numerals in the 400 series identify proposed capability-resolution, construction, expiry, and retention components that require further corroboration.

## FIG. 1 — Governed micro-node system overview

```mermaid
flowchart LR
    R100[100 Governed request or manifest] --> I110[110 Intake and request normalization]
    I110 --> H120[120 Request hash formation]
    H120 --> T200[200 Transition-role evaluator]
    T200 --> D300{300 Terminal decision}
    D300 -->|ALLOW| A310[310 Bounded allowed result]
    D300 -->|DENY| N320[320 Denied result]
    D300 -->|FAIL_CLOSED| F330[330 Failed-closed result]
    A310 --> C340[340 Receipt issuer]
    N320 --> C340
    F330 --> C340
    C340 --> P350[350 Governed return-path carrier]
    P350 --> W360[[360 Reconstruction witness store]]
```

**Support posture:** verified by the July 2 runtime implementation for request hashing, ordered role execution, terminal decisions, receipt generation, governed return, and reconstruction witness production.

## FIG. 2 — Ordered transition-role sequence

```mermaid
flowchart TB
    O210[210 Observer] --> I220[220 Interpreter]
    I220 --> A230[230 Authority checker]
    A230 --> G240[240 Admissibility gate]
    G240 --> D250[250 Decision role]
    D250 --> R260[260 Receipt issuer]
    R260 --> P270[270 Return-path carrier]
    P270 --> W280[280 Reconstruction witness]
```

**Support posture:** verified by the required-role declarations and runtime coverage checks.

## FIG. 3 — Authority and admissibility decision boundary

```mermaid
flowchart TB
    Q100[100 Complete governed request] --> M205{205 Required fields present?}
    M205 -->|no| FC330[330 FAIL_CLOSED]
    M205 -->|yes| A230{230 Authority standing valid?}
    A230 -->|no| DN320[320 DENY]
    A230 -->|yes| G240{240 Admissibility standing valid?}
    G240 -->|no| DN320
    G240 -->|yes| AL310[310 ALLOW]
```

**Support posture:** verified by distinct delegation/authority and policy/admissibility checks in the runtime evaluator.

## FIG. 4 — Receipt binding structure

```mermaid
flowchart LR
    Q100[100 Governed request] --> H120[120 Request hash]
    E290[290 Ordered role evidence] --> H295[295 Role-evidence hash]
    D300[300 Terminal decision] --> R340[340 Receipt record]
    H120 --> R340
    H295 --> R340
    P345[345 Optional previous receipt hash] --> R340
    R340 --> RH346[346 Receipt hash]
```

**Support posture:** verified by deterministic receipt generation and receipt-determinism validation.

## FIG. 5 — Governed return and reconstruction witness

```mermaid
flowchart LR
    D300[300 Decision] --> P350[350 Governed return payload]
    R346[346 Receipt hash] --> P350
    RP355[355 Declared return path] --> P350
    P350 --> PH356[356 Return-payload hash]
    QH120[120 Request hash] --> W360[360 Reconstruction witness]
    EH295[295 Role-evidence hash] --> W360
    R346 --> W360
    PH356 --> W360
    W360 --> WH365[365 Reconstruction hash]
```

**Support posture:** verified by runtime return-path and reconstruction-witness components.

## FIG. 6 — Required-role completeness enforcement

```mermaid
flowchart TB
    S200[200 Runtime role results] --> C205{205 All required role identifiers present?}
    C205 -->|yes| O300[300 Return governed decision object]
    C205 -->|no| E335[335 Runtime coverage error]
```

**Support posture:** verified by the runtime role-coverage check that rejects incomplete role sets.

## FIG. 7 — Proposed active-node capability resolution

```mermaid
flowchart LR
    M100[100 Admitted manifest] -.-> C400[400 Required capability and addressability resolver]
    C400 -.-> Q410{410 Admissible active node available?}
    Q410 -. yes .-> U420[420 Reuse bounded active node]
    Q410 -. no .-> B430[430 Construct minimum node]
```

**Support posture:** claim refinement requiring canonical implementation evidence before it is treated as reduced to practice.

## FIG. 8 — Proposed minimum-addressability construction

```mermaid
flowchart TB
    S401[401 Manifest-defined scope] -.-> P402[402 Permitted policy and authority]
    P402 -.-> T403[403 Transition-role requirements]
    T403 -.-> C430[430 Minimum node constructor]
    C430 -.-> N440[440 Bounded node build]
    N440 -.-> X445{{445 No unconceded capability expansion}}
```

**Support posture:** conception and claim-refinement material; executable enforcement evidence remains required.

## FIG. 9 — Proposed expiry and usage-evidenced retention

```mermaid
stateDiagram-v2
    [*] --> Constructed: 430 node build
    Constructed --> Active: admitted operation
    Active --> Completed: terminal result
    Completed --> Expired: default disposition
    Completed --> Retained: external usage evidence
    Retained --> Active: bounded continued use
    Retained --> Expired: usage evidence ends
```

**Support posture:** default expiry and usage-only delayed retention require corroboration and executable evidence.

## FIG. 10 — Proposed bounded context reuse and anti-self-retention rule

```mermaid
flowchart LR
    U450[450 External continued-usage evidence] -.-> R460[460 Retention evaluator]
    C470[470 Prior bounded context] -.-> R460
    H480[480 Node heartbeat] -.-> R460
    R460 -.-> A490{490 Retention admissible?}
    A490 -. yes, external usage present .-> K495[495 Retain bounded context without authority expansion]
    A490 -. no, heartbeat only .-> E499[499 Expire node]
```

**Support posture:** claim refinement. Heartbeat non-self-retention and bounded-context reuse remain unsupported by a mapped executable implementation.

## Reference numeral index

| Numeral | Component |
|---|---|
| 100 | governed request or manifest |
| 110 | intake and request normalization |
| 120 | request hash formation or request hash |
| 200 | transition-role evaluator or role-result set |
| 205 | completeness decision |
| 210 | observer role |
| 220 | interpreter role |
| 230 | authority checker |
| 240 | admissibility gate |
| 250 | decision role |
| 260 | receipt issuer role |
| 270 | return-path carrier role |
| 280 | reconstruction witness role |
| 290 | ordered role evidence |
| 295 | role-evidence hash |
| 300 | terminal decision |
| 310 | ALLOW result |
| 320 | DENY result |
| 330 | FAIL_CLOSED result |
| 335 | role-coverage runtime error |
| 340 | receipt issuer or receipt record |
| 345 | previous receipt hash |
| 346 | receipt hash |
| 350 | governed return payload or return carrier |
| 355 | declared return path |
| 356 | return-payload hash |
| 360 | reconstruction witness |
| 365 | reconstruction hash |
| 400 | capability and addressability resolver |
| 401 | manifest-defined scope |
| 402 | permitted policy and authority |
| 403 | transition-role requirements |
| 410 | active-node availability decision |
| 420 | bounded active-node reuse |
| 430 | minimum node constructor or node build |
| 440 | bounded node build |
| 445 | no unconceded capability expansion boundary |
| 450 | external continued-usage evidence |
| 460 | retention evaluator |
| 470 | prior bounded context |
| 480 | node heartbeat |
| 490 | retention admissibility decision |
| 495 | bounded context retention without authority expansion |
| 499 | node expiry |

## Drawing completion requirements

1. Render FIGS. 1–6 as monochrome review drawings.
2. Do not rely on FIGS. 7–10 as reduction-to-practice evidence until their underlying implementations are mapped.
3. Ensure every reference numeral used in a filing version appears in the detailed description.
4. Remove repository-specific names from broad filing figures unless needed for a concrete embodiment.
5. Review line weight, page margins, legibility, and reference-numeral consistency before any filing packet is authorized.
6. Preserve the distinction between verified flow and proposed flow in every derivative format.
