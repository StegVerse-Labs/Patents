# PAT-002 Source Identity Resolution

## Family

`PAT-002 — Heartbeat-Governed Entity and Reflected-State Computing`

## Resolution status

```text
PARTIALLY_RESOLVED_FORMAL_AUTHORITY_IDENTIFIED
```

## Authority clarification

The owner has clarified that the `Admissible-Existence` organization currently maintains the formal documentation for the relevant protocols and formalisms.

This clarification resolves the organizational home for formal PAT-002 source discovery. It does not establish inventorship, ownership, priority, patentability, public-disclosure consequences, or a succession relationship from any prior repository name.

## Existing repositories and bounded roles

### `Admissible-Existence/AE`

Role:

```text
root formal source for admissible existence and existence-level admissibility conditions
```

Relevant documented scope includes coherent persistence, transition capacity, recoverability, observability, compositional compatibility, receipt chains, state reconstruction, deterministic replay, and failure-closed execution.

Authority classification:

```text
FORMAL_SOURCE_AUTHORITY
```

### `Admissible-Existence/DC`

Role:

```text
formal source for distributed coherence across multiple changing entities, nodes, observers, systems, and authority domains
```

Relevant documented scope includes returned observations, lag, authority drift, conflicting receipts, reconciliation, global coherence, and recoverability across nodes.

Authority classification:

```text
FORMAL_SOURCE_AUTHORITY
```

Important identity distinction:

```text
DC = Distributed Coherence
DaCo = Data Continuity
```

`Admissible-Existence/DC` must not be described as Data Continuity.

### `Admissible-Existence/core-lite`

Role:

```text
minimal runtime and intake layer for consuming released formalism receipts and producing governed next-step receipts
```

Authority classification:

```text
IMPLEMENTATION_AND_INTEGRATION_EVIDENCE_CANDIDATE
```

Non-authority boundary:

```text
core-lite does not create formal source authority
core-lite does not commit execution by itself
core-lite does not establish final cross-repository validity
```

## Prior candidate identities

The prior PAT-002 record named:

```text
StegVerse-Labs/StegEntity
Data-Continuation/core-lite
```

Neither identity is currently accessible through the connected GitHub installation. No rename, transfer, replacement, or succession record has been located that would permit those names to be treated as identical to an existing `Admissible-Existence` repository.

Therefore:

```text
StegVerse-Labs/StegEntity = UNRESOLVED_PRIOR_CANDIDATE
Data-Continuation/core-lite = UNRESOLVED_PRIOR_CANDIDATE
Admissible-Existence/core-lite = CURRENT_IMPLEMENTATION_CANDIDATE, NOT ASSUMED SUCCESSOR
```

## Repository-creation decision

```text
NEW_REPOSITORY_REQUIRED: false
```

No new repository is required merely to continue PAT-002 evidence development. Existing repositories provide homes for:

```text
formal foundation                 -> Admissible-Existence/AE
multi-entity and observer relation -> Admissible-Existence/DC
runtime/intake evidence             -> Admissible-Existence/core-lite
```

A new repository should be considered only if a distinct executable entity/heartbeat implementation is intentionally established as an independent authority surface and cannot be coherently maintained in an existing repository. Patent workflow convenience alone is not sufficient reason to create it.

## Remaining source-verification work

Automation may now inspect the three existing repositories for exact PAT-002 limitation anchors, but it must still preserve these distinctions:

1. formal written-description support versus executable support;
2. individual limitation support versus combination-level support;
3. source authority versus runtime integration evidence;
4. current repository identity versus any historical repository identity;
5. supported embodiment versus proposed embodiment.

## Next automation

1. Locate exact paths and immutable blobs or commits in `Admissible-Existence/AE` for PAT-002 formal concepts.
2. Locate exact paths and immutable blobs or commits in `Admissible-Existence/DC` for multi-entity, observer, returned-signal, lag, reconciliation, and global-state concepts.
3. Locate exact paths and immutable blobs or commits in `Admissible-Existence/core-lite` for receipt-bound intake, validation, next-step receipts, and integration behavior.
4. Populate `evidence/PAT-002_CLAIM_ELEMENT_EVIDENCE_MAP.md` using only verified anchors.
5. Emit a source-anchor manifest distinguishing formal and executable support.
6. Leave historical succession unresolved unless documentary evidence is found.

## Legal and filing boundary

This resolution does not determine:

```text
inventorship
ownership
priority
novelty
patentability
enablement as a legal conclusion
filing strategy
filing authorization
filing status
application number
deadline
```
