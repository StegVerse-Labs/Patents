# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because PAT-001 and PAT-005 still contain authorized machine tasks.

## Canonical automation

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration, canonical-source search and lifecycle evidence, PAT-005 four-repository anchors and negative-case replay, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- `data/PAT-001-lifecycle-evidence.json` binds `StegVerse-002/micro-node-runtime@c2d5f89b239ff24cf7f40119ad79df526f24b2c4`.
- `micro_node/contracts.py` and `micro_node/runtime.py` support minimum request fields, authority and admissibility checks, fail-closed decisions, receipt chaining, governed return, and reconstruction.
- The same inspected surface explicitly does not implement default expiry, usage leases, bounded-context reuse, heartbeat non-self-retention, demand-only node construction, or full registry-based capability resolution.
- Retry those implementation searches only when a recorded trigger occurs.
- Four monochrome SVG review drawings and a SHA-256 manifest remain under `rendered/PAT-001/`.

## PAT-005 four-repository anchors

`data/PAT-005-implementation-anchors.json` binds eleven exact artifacts across:

- `StegVerse-Labs/device-continuity-layer@d12e8790b7d426cda0594cd817833d0b76db15ac`
- `StegVerse-Labs/StegTalk@0888572be55b5045643fa373bf2e17d829c8dbb4`
- `StegVerse-Labs/StegMusic@a7b1ebb37dd92b9dfef36096c4f414d4f9bab5bc`
- `StegVerse-002/stegguardian-wiki@8cfa27cae30c314da4cedab5dcd8af0ef2e02977`

The anchors preserve destination-bound package construction, bounded response options, non-authorizing destination handoffs, payload/destination receipt binding, accepted observe-only posture, reconstructability, Guardian review-only posture, and authority separation.

## PAT-005 executable negative evidence

- `fixtures/PAT-005-negative-cases.json`
- `tools/replay_pat005_negative_cases.py`
- `tests/test_pat005_negative_cases.py`

Eight replayable rejection cases cover wrong destination, authorizing status, unauthorized decisions, missing non-authority rules, payload and destination mismatches, disallowed receipt decisions, and non-reconstructable receipts.

## Current next machine work

1. Execute the canonical runner through the authoritative execution path.
2. Populate stable prior-art identifiers only from verified patent and non-patent sources.
3. Retry PAT-001 canonical-source or lifecycle searches only after a recorded trigger.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The PAT-001 lifecycle record, validator, tests, dispatcher schema `2.1`, completion-state binding, PAT-005 negative replay, and this handoff are committed. No attached workflow run has supplied an authoritative execution receipt, so execution success is not claimed.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, queues, corroboration controls, source-search and lifecycle receipts, PAT-005 four-repository anchors, negative replay controls, and synchronized continuation state.
