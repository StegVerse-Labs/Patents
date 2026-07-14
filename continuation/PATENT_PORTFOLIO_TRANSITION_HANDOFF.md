# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because PAT-001 and PAT-005 still contain authorized machine tasks.

## Canonical automation

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration and source-search receipts, PAT-005 four-repository anchors and negative-case replay, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- Four monochrome SVG review drawings and a SHA-256 manifest remain under `rendered/PAT-001/`.
- Capability resolution, minimum construction, expiry, usage leases, bounded context, and heartbeat non-self-retention still require executable evidence or explicit negative evidence.

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

Eight replayable rejection cases cover:

1. wrong destination repository;
2. unexpected authorizing handoff status;
3. unauthorized destination decision;
4. missing non-authority rule;
5. payload/receipt mismatch;
6. destination/receipt mismatch;
7. receipt decision outside the allowed set;
8. non-reconstructable receipt.

The replay surface derives from exact anchored validator behavior. It is deterministic technical evidence, not a production execution receipt and not a legal conclusion. Dispatcher schema `2.0` now runs this replay automatically.

## Current next machine work

1. Execute the canonical runner through the authoritative execution path.
2. Preserve PAT-001 executable or explicit negative lifecycle evidence.
3. Populate stable prior-art identifiers only from verified patent and non-patent sources.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The negative corpus, replay tool, regression tests, dispatcher integration, PAT-005 completion-state binding, and this handoff are committed. No attached workflow run has supplied an authoritative execution receipt, so execution success is not claimed.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, queues, corroboration controls, source-search receipts, PAT-005 four-repository anchors, negative replay controls, and synchronized continuation state.
