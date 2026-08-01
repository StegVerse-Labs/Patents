# AI Output-to-Action Boundary — Source Inventory

## Family

`AI Output-to-Action Boundary`

## Current decision

```text
PARTIAL_VERIFIED_REQUEST_TO_EXECUTION_CANDIDATE_SUPPORT
```

## Verified executable sources

### Publisher bounded import anchor

```text
repository: GCAT-BCAT-Engine/Publisher
path: scripts/import_ecosystem_chat_activation.py
blob: a2186f2634f5acf5253f9f26b28b673c2afc2b8a
evidence type: executable
```

This source validates upstream state, propagation, custody, reconstruction, stage-chain, supersession, destination, and authority-boundary records while keeping publication, release, custody, and execution authorization false.

### TVC service-request router

```text
repository: StegVerse-Labs/TVC
path: scripts/route_ecosystem_service_request.py
blob: 5139f935362967906fdbb318f4444fa453b70c9a
evidence type: executable
```

This source validates a provider-neutral service request, binds it to a deterministic hash, resolves an enabled provider, emits a hash-bound route, and requires later service estimate, authority evidence, CGE admissibility, service receipt or refusal, service actual, ledger receipt, and requester return receipt records. The route explicitly records `authority_granted: false`, `admissibility_granted: false`, and `execution_authorized: false`.

### TVC authority and admissibility binder

```text
repository: StegVerse-Labs/TVC
path: scripts/bind_service_admissibility.py
blob: 570eaa2db77379fd5f093c2ba721357e25c7c914
evidence type: executable
```

This source binds the route to authority evidence and an externally produced CGE decision. It verifies request, route, provider, service, authority-evidence hash, decision hash, expiry, admissibility state, and execution scope. It rejects invalid authority, mismatched records, expired decisions, and out-of-scope service requests. A passing record emits an `execution_candidate` while preserving `execution_authorized_by_tvc: false`.

## Supported technical behavior

The combined bounded chain now supports:

1. receipt of an upstream informational state or packet;
2. canonical hashing and cross-record binding;
3. explicit separation of informational admission from action authority;
4. a provider-neutral service-request object;
5. deterministic routing without authority or admissibility;
6. a required later authority-evidence record;
7. external CGE admissibility binding;
8. scoped service admission;
9. expiry-based refusal;
10. emission of an execution candidate without execution authorization.

## Candidate limitation leads

```text
output or state packet received
provenance and integrity validated
service request represented and hashed
request routed without authority
authority evidence independently supplied and hash-bound
admissibility decision independently supplied and hash-bound
scope and expiration validated
execution candidate emitted
execution authority remains false
separate tool-specific authorization and execution transition required
```

## Remaining unsupported elements

No verified source yet establishes:

```text
a general AI model output schema
a canonical generalized action-request object
a mechanism that creates the authority evidence
a tool-specific execution grant
grant revocation behavior
grant one-time consumption behavior
a complete execution transition and service actual
a retained positive execution output
retained revoked, consumed, and tool-out-of-scope outputs
combination-level operation across arbitrary AI agents and tools
```

## Bounded source-search observations

The connected repository index was first searched for combined action-request, authority-grant, execution-grant, revocation, expiration, and consumption terminology. No combined indexed result was returned. A later targeted search for `execution_authorized` returned the TVC routing and admissibility-binding executables above, among other bounded authority-preserving sources.

These are bounded connector observations only. They do not prove that no additional qualifying source exists in repository history, unindexed paths, artifacts, workflow outputs, other first-party repositories, or retained runtime evidence.

## Family overlap questions

Non-legal technical comparison remains required against:

```text
Commit-Time Admissibility Gate
Publisher Governed Disclosure Pipeline
Receipt-Based State Transition Validation
PAT-002 heartbeat and reflected-state family
TVC service admissibility and execution-candidate mechanisms
```

This inventory does not merge those families or determine claim scope.

## Approval state

```text
owner approval required now: false
```

The family is not ready for an owner filing or disposition decision.
