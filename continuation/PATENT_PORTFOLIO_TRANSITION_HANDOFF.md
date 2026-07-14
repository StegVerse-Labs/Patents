# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but inactive because patent-publication verification, authoritative execution observation, and non-delegable legal gates remain unresolved.

## Canonical automation

```bash
python tools/patent_portfolio.py --repo-root .
```

The locked runner validates completion/readiness state, PAT-001 corroboration, canonical-source search and lifecycle evidence, PAT-005 four-repository anchors and negative-case replay, active-family prior-art identifiers, drawings, evidence and machine queues, workstream selection, pytest, consolidated receipts, and synchronized continuation state. It excludes inventorship, practitioner judgment, approval, filing, payment, submission, and patent-pending decisions.

## Authoritative execution path

The existing `.github/workflows/test-readiness.yml` executes the canonical runner on push, pull request, or explicit workflow dispatch. It retains read-only repository permissions and uploads the dispatcher receipt, synchronized status, both queues, and machine continuation record for 90 days. `tests/test_patent_execution_workflow.py` protects that workflow contract. No additional workflow was created.

## PAT-001 state

- `data/PAT-001-source-corroboration.json` preserves exact adjacent StegDB and Site anchors.
- `data/PAT-001-canonical-source-search-receipt.json` records `CANONICAL_SOURCE_NOT_RECOVERED` and suppresses repeated June-source searches until a retry trigger occurs.
- `data/PAT-001-lifecycle-evidence.json` binds `StegVerse-002/micro-node-runtime@c2d5f89b239ff24cf7f40119ad79df526f24b2c4` and separates implemented behavior from absent expiry, lease, bounded-context, heartbeat-retention, demand-construction, and full capability-resolution behavior.

## PAT-005 state

`data/PAT-005-implementation-anchors.json` binds eleven exact artifacts across the source implementation, StegTalk, StegMusic, and StegGuardian repositories. `fixtures/PAT-005-negative-cases.json` and `tools/replay_pat005_negative_cases.py` preserve eight deterministic rejection paths.

## Prior-art verification state

`data/active-family-prior-art-identifiers.json` currently preserves four verified non-patent identifiers:

- PAT-001: `arXiv:2204.07210`;
- PAT-005: `arXiv:1408.1416`, `arXiv:1804.03852`, and `arXiv:2403.13020`.

`tools/validate_prior_art_identifiers.py` and `tests/test_prior_art_identifiers.py` prevent the record from being promoted to complete without at least one verified patent publication and prevent novelty, patentability, FTO, inventorship, filing, or patent-pending authority claims. Patent publication numbers, priority dates, family members, and relevant claims remain unverified.

## Current next machine work

1. Observe and preserve the first completed canonical workflow execution artifact; do not claim success before a completed run is verified.
2. Verify patent publication identifiers through USPTO, WIPO, or Espacenet primary records.
3. Retry PAT-001 canonical-source or lifecycle searches only after a recorded trigger.

## Activation boundary

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically.

## Validation state

The partial prior-art record, validator, tests, dispatcher schema `2.2`, workflow wiring, and regression contract are committed. Authoritative execution success remains unclaimed until a completed workflow run and its artifacts are verified.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the canonical runner, the existing execution workflow, queues, corroboration controls, source-search and lifecycle records, PAT-005 anchors, negative replay controls, prior-art verification controls, and synchronized continuation state.
