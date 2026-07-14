# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because PAT-001 and PAT-005 still contain authorized machine tasks.

## Canonical automation

Run:

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration and negative source-search receipts, PAT-005 four-repository implementation anchors, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- Four monochrome SVG review drawings and a SHA-256 manifest remain under `rendered/PAT-001/`.
- Capability resolution, minimum construction, expiry, usage leases, bounded context, and heartbeat non-self-retention still require executable evidence or explicit negative evidence.

## PAT-005 four-repository anchors

`data/PAT-005-implementation-anchors.json` binds eleven exact artifacts across four repositories.

### Source implementation

`StegVerse-Labs/device-continuity-layer@d12e8790b7d426cda0594cd817833d0b76db15ac`

- destination package builder;
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

### StegGuardian boundary

`StegVerse-002/stegguardian-wiki@8cfa27cae30c314da4cedab5dcd8af0ef2e02977`

- guardian boundary page — blob `777a9aa6f0786c1ac5740f63ff6f9589c512fd53`;
- reconstructable guardian receipt — blob `37d0e769fbe9aacfa646d66562eaffb0e72deafc`.

The Guardian page states that a handoff candidate is not operator approval, active device trust, or destination behavior authority; unknown devices remain review-only until destination policy accepts them. The validator explicitly prevents Guardian documentation from being classified as executable authority.

## Current next machine work

1. Execute the canonical runner through the authoritative execution path.
2. Preserve PAT-005 executable cross-repository negative fixtures and outputs beyond the already anchored denial, review-only, and non-authority outcomes.
3. Preserve PAT-001 executable or explicit negative lifecycle evidence.
4. Populate stable prior-art identifiers only from verified patent and non-patent sources.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The four-repository anchor record, Guardian-aware validator, regression tests, completion-state binding, and this handoff are committed. No attached workflow run has yet supplied an authoritative execution receipt.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, both queues, corroboration controls, source-search receipts, PAT-005 four-repository anchor controls, and synchronized continuation state.
