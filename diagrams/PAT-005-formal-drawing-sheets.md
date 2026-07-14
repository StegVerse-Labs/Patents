# PAT-005 Formal Drawing Sheets — Working Source

**Status:** provisional drawing source; not USPTO-formatted drawings

## Drawing Conventions

- Solid arrows represent data or evidence flow.
- Dashed arrows represent proposed or review-only transitions.
- Double borders represent independently governed repositories or destination systems.
- A stop marker represents a non-authorizing boundary.
- Receipt identifiers are shown adjacent to the transition they evidence.

## FIG. 1 — End-to-End Governed Device Continuity System

```mermaid
flowchart LR
    A[Physical device observations] --> B[Discovery adapters]
    B --> C[Fingerprint records]
    C --> D[Canonical inventory merge]
    D --> E[Destination classifier]
    E --> F[Recovery plan]
    F -. proposed .-> G[[Destination package]]
    G --> H{Destination review}
    H -->|observe only| I[Destination receipt]
    H -->|manual review| J[Review-required state]
    H -->|deny| K[Denied state]
    I --> L[Site mirror evidence]
    L --> M[Publisher evidence]
    M --> N[Admissibility boundary]
    N --> O[Guardian boundary]
    O --> P[Reverse reconstruction]
```

## FIG. 2 — Multi-Transport Observation and Fingerprint Formation

```mermaid
flowchart TB
    BLE[BLE observations] --> F[Fingerprint generator]
    LAN[LAN observations] --> F
    AUD[Audio observations] --> F
    MAN[Manual observations] --> F
    MOD[Model and label observations] --> F
    F --> R1[Fingerprint record 1]
    F --> R2[Fingerprint record 2]
    F --> RN[Fingerprint record N]
```

## FIG. 3 — Canonical Inventory Merge with Source Lineage

```mermaid
flowchart LR
    R1[Fingerprint 1] --> C{Canonical relationship}
    R2[Fingerprint 2] --> C
    R3[Fingerprint 3] --> C
    C -->|merge| I[Inventory identity]
    C -->|insufficient evidence| U[Unresolved identity]
    I --> L[Source fingerprint paths retained]
```

## FIG. 4 — Destination Classification with Preserved Ambiguity

```mermaid
flowchart LR
    I[Inventory record] --> C{Destination capability rules}
    C --> T[StegTalk candidate]
    C --> M[StegMusic candidate]
    C --> H[Home automation candidate]
    C --> G[Generic/manual review]
    C --> U[Unsupported]
```

## FIG. 5 — Recovery Plan and Authority Separation

```mermaid
flowchart LR
    C[Classification] --> R[Recovery plan]
    R -. prepare .-> P[Destination package]
    P --> S{{STOP: no operation authority}}
    S -. separate authority request .-> A[Commitment/operation decision]
```

## FIG. 6 — Destination Package Structure

```mermaid
classDiagram
    class DestinationPackage {
      package_id
      inventory_id
      destination
      source_repo
      items[]
      response_options[]
    }
    class PackageItem {
      fingerprint_id
      proposed_action
      review_required
      destination
    }
    DestinationPackage "1" --> "1..*" PackageItem
```

## FIG. 7 — Independent Destination Response

```mermaid
sequenceDiagram
    participant S as Source continuity layer
    participant D as Destination repository
    participant R as Receipt store
    S->>D: Non-authorizing destination package
    D->>D: Validate destination and review posture
    alt observation-only acceptance
        D->>R: accepted_observe_only receipt
    else review required
        D->>R: manual_review_required receipt
    else denied
        D->>R: denied receipt
    end
```

## FIG. 8 — Cross-Repository Evidence Propagation

```mermaid
flowchart LR
    SRC[[Device Continuity Layer]] --> ST[[StegTalk]]
    SRC --> SM[[StegMusic]]
    SRC --> SITE[[Site]]
    SITE --> PUB[[Publisher]]
    PUB --> AW[[Admissibility Wiki]]
    PUB --> GW[[Guardian Wiki]]
    ST --> E[Evidence graph]
    SM --> E
    SITE --> E
    PUB --> E
    AW --> E
    GW --> E
```

## FIG. 9 — Descriptor-Driven Release Publication

```mermaid
flowchart LR
    D[releases/current.json] --> V[Descriptor validator]
    V --> G[Release gate]
    G --> M[Artifact manifest and hashes]
    M --> T[Create or verify tag]
    T --> R[Create or verify hosted release]
    R --> Q[Query observed release state]
    Q --> P[Publication receipt]
```

## FIG. 10 — Reverse Reconstruction

```mermaid
flowchart RL
    P[Public paper or mirror receipt] --> M[Mirror source reference]
    M --> D[Destination receipt]
    D --> K[Destination package]
    K --> R[Recovery plan]
    R --> C[Classification]
    C --> I[Inventory]
    I --> F[Source fingerprints]
    F --> O[Original observations]
```

## FIG. 11 — Authority State Separation

```mermaid
stateDiagram-v2
    [*] --> Observed
    Observed --> Identified
    Identified --> Classified
    Classified --> Packaged
    Packaged --> DestinationReviewed
    DestinationReviewed --> ObservationAccepted
    DestinationReviewed --> ReviewRequired
    DestinationReviewed --> Denied
    ObservationAccepted --> AuthorityRequested
    AuthorityRequested --> OperationAuthorized
    AuthorityRequested --> AuthorityDenied
    OperationAuthorized --> Revoked
```

## FIG. 12 — Failure and Non-Inference States

```mermaid
flowchart TB
    A[Observation set] --> B{Sufficient identity evidence?}
    B -->|no| C[Unresolved/non-inference]
    B -->|yes| D{Destination supported?}
    D -->|no| E[Unsupported preserved]
    D -->|ambiguous| F[Manual review required]
    D -->|yes| G[Package prepared]
    G --> H{Destination validates?}
    H -->|no| I[Denied or failed closed]
    H -->|yes| J[Observation-only receipt]
```

## Drawing Completion Tasks

1. Convert each working sheet into monochrome line drawings with reference numerals.
2. Ensure every reference numeral is described in the specification.
3. Remove implementation-specific names from broad figures where broader support exists.
4. Add device, processor, memory, interface, and data-store components to system figures.
5. Add at least one concrete StegTalk and StegMusic embodiment sheet.
6. Obtain practitioner review before relying on these as filing drawings.
