# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because verified prior-art identifiers and non-delegable legal gates remain unresolved.

## Canonical automation

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration, canonical-source search and lifecycle evidence, PAT-005 four-repository anchors and negative-case replay, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## Authoritative execution path

The existing `.github/workflows/test-readiness.yml` now executes the canonical runner on push, pull request, or explicit workflow dispatch. It retains read-only repository permissions and uploads these execution artifacts for 90 days:

- `receipts/patent-portfolio-dispatch.json`
- `data/patent-workstream-status.json`
- `data/patent-machine-queue.json`
- `data/patent-evidence-acquisition-queue.json`
- `continuation/patent-portfolio-machine-continuation.json`

`tests/test_patent_execution_workflow.py` protects that workflow contract. No additional workflow was created.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- `data/PAT-001-lifecycle-evidence.json` binds `StegVerse-002/micro-node-runtime@c2d5f89b239ff24cf7f40119ad79df526f24b2c4`.
- The inspected runtime supports minimum request fields, authority and admissibility checks, fail-closed decisions, receipt chaining, governed return, and reconstruction.
- It does not implement default expiry, usage leases, bounded-context reuse, heartbeat non-self-retention, demand-only construction, or full registry-based capability resolution.

## PAT-005 state

`data/PAT-005-implementation-anchors.json` binds eleven exact artifacts across the source implementation, StegTalk, StegMusic, and StegGuardian repositories. `fixtures/PAT-005-negative-cases.json` and `tools/replay_pat005_negative_cases.py` preserve eight deterministic rejection paths.

## Current next machine work

1. Observe and preserve the first completed canonical workflow execution artifact; do not claim success before a completed run is verified.
2. Populate stable prior-art identifiers only from verified patent and non-patent primary sources.
3. Retry PAT-001 canonical-source or lifecycle searches only after a recorded trigger.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The workflow wiring and its regression contract are committed. The connector has not yet exposed a completed run or status for the triggering commits, so authoritative execution success remains unclaimed.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the canonical runner, the existing execution workflow, queues, corroboration controls, source-search and lifecycle records, PAT-005 anchors, negative replay controls, and synchronized continuation state.
