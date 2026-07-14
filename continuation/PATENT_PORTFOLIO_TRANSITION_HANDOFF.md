# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because PAT-001 and PAT-005 still contain authorized machine tasks.

## Canonical automation

Run:

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration and negative source-search receipts, PAT-005 multi-repository implementation anchors, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- Four monochrome SVG review drawings and a SHA-256 manifest remain under `rendered/PAT-001/`.
- Capability resolution, minimum construction, expiry, usage leases, bounded context, and heartbeat non-self-retention still require executable evidence or explicit negative evidence.

## PAT-005 multi-repository implementation anchors

`data/PAT-005-implementation-anchors.json` now binds nine exact artifacts across three repositories.

### Source implementation

`StegVerse-Labs/device-continuity-layer@d12e8790b7d426cda0594cd817833d0b76db15ac`

- package builder;
- package validator;
- StegTalk acceptance fixture with observe-only, review-required, and denied outcomes.

### StegTalk destination

`StegVerse-Labs/StegTalk@0888572be55b5045643fa373bf2e17d829c8dbb4`

- handoff validator — blob `11d905fdb5b962bac3978503474e2632e227507a`;
- receipt validator — blob `6f79043d457348a65efd895238340340e325178d`;
- non-authorizing reconstructable receipt — blob `9ec4e41da35ec2cb11a8a52245bf1f974bae24ef`.

### StegMusic destination

`StegVerse-Labs/StegMusic@a7b1ebb37dd92b9dfef36096c4f414d4f9bab5bc`

- handoff validator — blob `3bccc370edc0964ec850f20e8094eab08e9a3fc1`;
- receipt validator — blob `bb129fd31c004c10b0f64d525a5bc7d7878b5f02`;
- non-authorizing reconstructable receipt — blob `c7fa05835c29362086f97499b145931499cac638`.

The record now supports source-to-destination package creation, installed non-authorizing handoffs, bounded destination decisions, payload and destination receipt binding, accepted observe-only posture, and reconstructability. It does not establish inventorship, patentability, filing authority, or patent-pending status.

## Current next machine work

1. Execute the canonical runner through the authoritative execution path.
2. Locate and verify StegGuardian page and receipt paths, or preserve an explicit absence receipt.
3. Preserve PAT-005 executable cross-repository negative fixtures and outputs beyond the already anchored denial and manual-review outcomes.
4. Preserve PAT-001 executable or explicit negative lifecycle evidence.
5. Populate stable prior-art identifiers only from verified patent and non-patent sources.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The multi-repository anchor record, validator, tests, dispatcher integration, completion-state binding, and this handoff are committed. No attached workflow run has yet supplied an authoritative execution receipt.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, both queues, corroboration controls, source-search receipts, PAT-005 multi-repository implementation-anchor controls, and synchronized continuation state.
