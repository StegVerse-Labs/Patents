# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but not active because PAT-001 and PAT-005 still have authorized machine tasks. The durable controller and synchronized status record determine future transitions; sessions must not activate candidate review merely because external blockers also exist.

## Manual-task elimination baseline

All repeatable repository-local validation, task selection, evidence-task normalization, canonical-source search receipt validation, receipt creation, continuation-state synchronization, concurrency protection, operator summarization, and source-corroboration validation are consolidated behind:

- `tools/patent_portfolio.py`
- `tools/run_patent_portfolio_dispatcher.py`
- `tools/build_patent_machine_queue.py`
- `tools/build_patent_evidence_queue.py`
- `tools/validate_patent_evidence_queue.py`
- `tools/validate_source_corroboration.py`
- `tools/validate_canonical_source_search_receipt.py`
- associated regression tests under `tests/`

The canonical command remains:

```bash
python tools/patent_portfolio.py --repo-root .
```

One invocation validates completion and readiness records, corroboration and canonical-source search receipts, drawing sources and rendered outputs, both task queues, workstream selection, the full test surface, the consolidated receipt, and synchronized continuation state. Concurrent execution fails closed with `PORTFOLIO_EXECUTION_LOCKED`.

The machine and evidence queues exclude human, practitioner, inventor, approval, authorization, signature, payment, submission, filing, and patent-pending tasks. Those transitions remain non-delegable authority boundaries.

## Active-family work completed

### PAT-001 and PAT-005 completion controls

Every `completed: true` key is artifact-bound. Validation fails closed for missing maps, missing files, authority-state conflicts, and patent-pending authorization before filing.

### Automated evidence acquisition

`tools/build_patent_evidence_queue.py` and `tools/validate_patent_evidence_queue.py` convert active-family tasks into stable IDs, priorities, evidence classes, completion predicates, and external-verification requirements without claiming legal effect.

### PAT-001 source corroboration

`data/PAT-001-source-corroboration.json` binds exact adjacent StegDB and Site repository anchors supporting bounded scope, declared contracts and authority, role separation, lineage, lifecycle timestamps, receipt hashes, and fail-closed states. It does not establish the exact June 6 or June 16 source, conception date, inventorship, patentability, or priority.

### PAT-001 canonical-source search receipt

- `data/PAT-001-canonical-source-search-receipt.json`
- `tools/validate_canonical_source_search_receipt.py`
- `tests/test_canonical_source_search_receipt.py`

Exact-title, exact-phrase, organization-scoped code, and global commit searches were preserved. The accessible GitHub index returned later Patents references but did not recover the original June source. The receipt records `CANONICAL_SOURCE_NOT_RECOVERED`, preserves negative evidence, and permits retries only when a recorded trigger occurs, such as restored history, a supplied archive or commit, newly accessible repositories, or materially changed index coverage. Missing search results do not establish absence or any legal conclusion.

### PAT-001 rendered review drawings

Four monochrome SVG review drawings and a SHA-256 manifest remain committed under `rendered/PAT-001/`. They are not approved filing drawings.

## Portfolio transition infrastructure

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically from completion records.

## Current next machine work

1. Execute `tools/patent_portfolio.py` through the authoritative execution path.
2. Do not repeat PAT-001 June-source searches until a recorded retry trigger occurs.
3. Advance PAT-001 executable evidence for capability resolution, minimum construction, expiry, leases, bounded context, and heartbeat-retention paths.
4. Complete PAT-005 implementation-anchor and executable-negative-fixture collection.
5. Populate stable prior-art identifiers only from verified patent and non-patent sources.

## Validation state

The search receipt, validator, tests, dispatcher integration, and completion-state binding are committed. The latest direct commits have no attached pull-request workflow run, so authoritative execution remains unresolved.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns portfolio transition, the concurrency-safe runner, unified dispatcher, both queues, corroboration controls, canonical-source search receipts, and synchronized continuation state.
