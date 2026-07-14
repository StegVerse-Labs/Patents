# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because PAT-001 and PAT-005 still contain authorized machine tasks.

## Canonical automation

Run:

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration and negative source-search receipts, PAT-005 implementation anchors, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- Four monochrome SVG review drawings and a SHA-256 manifest remain under `rendered/PAT-001/`.
- Capability resolution, minimum construction, expiry, usage leases, bounded context, and heartbeat non-self-retention still require executable evidence or explicit negative evidence.

## PAT-005 exact implementation anchors

The primary source repository is now bound at:

`StegVerse-Labs/device-continuity-layer@d12e8790b7d426cda0594cd817833d0b76db15ac`

Exact anchors:

- `tools/build_destination_packages.py` — blob `123a6c2779f5d3bf8ef7433ef8ed85ed35d5722e`
- `tools/validate_destination_packages.py` — blob `498eef1c023d9f4b73c24ddae4b8033c4a8fed0a`
- `fixtures/acceptance/stegtalk-package.json` — blob `7ec16437b05c61b400c59be4ae89844a4c3d1f12`

Durable controls:

- `data/PAT-005-implementation-anchors.json`
- `tools/validate_pat005_implementation_anchors.py`
- `tests/test_pat005_implementation_anchors.py`

These anchors support destination-bound package construction, source/inventory binding, bounded response options, destination consistency validation, and executable `accepted_observe_only`, `manual_review_required`, and `denied` outcomes. They do not establish inventorship, patentability, filing authority, or patent-pending status.

## Current next machine work

1. Execute the canonical runner through the authoritative execution path.
2. Collect exact StegTalk, StegMusic, and StegGuardian destination-side validator and receipt anchors.
3. Preserve PAT-005 executable negative fixtures and outputs across source and destination repositories.
4. Preserve PAT-001 executable or explicit negative lifecycle evidence.
5. Populate stable prior-art identifiers only from verified patent and non-patent sources.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The new PAT-005 record, validator, tests, dispatcher integration, and completion-state binding are committed. No attached workflow run has yet supplied an authoritative execution receipt.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, both queues, corroboration controls, source-search receipts, PAT-005 implementation-anchor controls, and synchronized continuation state.
