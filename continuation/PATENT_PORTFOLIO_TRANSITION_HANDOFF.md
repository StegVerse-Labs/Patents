# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but not active because PAT-001 and PAT-005 still have authorized machine tasks. The durable controller and synchronized status record determine future transitions; sessions must not activate candidate review merely because external blockers also exist.

## Manual-task elimination baseline

All repeatable repository-local validation, task selection, evidence-task normalization, receipt creation, continuation-state synchronization, concurrency protection, operator summarization, and source-corroboration validation are consolidated behind:

- `tools/patent_portfolio.py`
- `tests/test_patent_portfolio_runner.py`
- `docs/PATENT_AUTOMATION_ENTRYPOINT.md`
- `tools/run_patent_portfolio_dispatcher.py`
- `tests/test_patent_portfolio_dispatcher.py`
- `tools/build_patent_machine_queue.py`
- `tests/test_patent_machine_queue.py`
- `tools/build_patent_evidence_queue.py`
- `tools/validate_patent_evidence_queue.py`
- `tests/test_patent_evidence_queue.py`
- `tools/synchronize_patent_portfolio_state.py`
- `tests/test_synchronize_patent_portfolio_state.py`
- `tools/validate_source_corroboration.py`
- `tests/test_source_corroboration.py`

The canonical command is:

```bash
python tools/patent_portfolio.py --repo-root .
```

One invocation now performs:

1. exclusive portfolio execution-lock acquisition;
2. PAT-001 and PAT-005 completion-record validation;
3. PAT-001 readiness and cross-repository corroboration validation;
4. PAT-001 drawing-source and rendered-drawing verification;
5. normalized evidence-acquisition queue generation and validation;
6. authorized machine-task queue generation;
7. active-work versus ecosystem-candidate workstream selection;
8. the complete pytest surface;
9. final consolidated JSON receipt creation;
10. automatic synchronization of workstream and continuation records;
11. concise output of the next authorized machine task;
12. guaranteed execution-lock cleanup.

Concurrent execution fails closed with `PORTFOLIO_EXECUTION_LOCKED`. The receipt is finalized before synchronization so stored SHA-256 values remain stable. Manual command sequencing, free-text evidence triage, queue selection, state inspection, source-anchor consistency checking, and handoff reconciliation are no longer required after a runner invocation.

The machine and evidence queues exclude human, practitioner, inventor, approval, authorization, signature, payment, submission, filing, and patent-pending tasks. Those transitions are legally or evidentially non-delegable authority boundaries.

## Active-family work completed

### PAT-001 and PAT-005 completion controls

- `data/PAT-001-completion-status.json`
- `data/PAT-005-completion-status.json`
- `tools/validate_completion_status.py`
- `tests/test_completion_status.py`

Every `completed: true` key is artifact-bound. Validation fails closed for missing maps, missing files, authority-state conflicts, and patent-pending authorization before filing.

### Automated evidence acquisition

- `tools/build_patent_evidence_queue.py`
- `tools/validate_patent_evidence_queue.py`
- `tests/test_patent_evidence_queue.py`
- `data/patent-evidence-acquisition-queue.json` after runner execution

The evidence queue converts active-family `next_machine_tasks` into stable task IDs, priorities, evidence classes, completion predicates, and external-verification flags. It distinguishes canonical source recovery, implementation anchors, executable fixtures, lifecycle evidence, verified prior-art identifiers, and authoritative execution. Queue entries explicitly claim no legal effect.

### PAT-001 source corroboration

- `data/PAT-001-source-corroboration.json`
- `tools/validate_source_corroboration.py`
- `tests/test_source_corroboration.py`

The corroboration record binds exact repository, commit, path, and blob identifiers for StegDB monitoring micro-node policy and schema sources and the Site publication micro-node workflow. These anchors support bounded scope, declared contracts and authority, role separation, lineage, lifecycle timestamps, receipt hashes, and fail-closed states. They do not establish the exact June 6 or June 16 source commit, inventorship, patentability, priority date, default expiry, usage-only retention, bounded context reuse, or heartbeat non-self-retention.

### PAT-001 rendered review drawings

Four monochrome SVG review drawings and a SHA-256 manifest are committed under `rendered/PAT-001/`. They are not approved filing drawings; practitioner approval remains unresolved.

## Portfolio transition infrastructure

- `docs/ECOSYSTEM_PATENT_CANDIDATE_REVIEW.md`
- `tools/select_patent_workstream.py`
- `tests/test_select_patent_workstream.py`
- `schemas/ecosystem-patent-candidate.schema.json`
- `data/patent-workstream-status.json`
- `continuation/patent-portfolio-machine-continuation.json` after runner execution

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is submission-ready or externally blocked with no authorized machine task remaining. The runner activates and reverses this state automatically from completion records.

## Current next machine work

1. Execute `tools/patent_portfolio.py` through the authoritative execution path; it will generate and validate both queues and preserve all synchronized outputs.
2. Process the generated evidence queue beginning with exact PAT-001 June 6/June 16 source recovery and PAT-005 implementation anchors.
3. Preserve executable fixtures for PAT-001 capability resolution, minimum construction, expiry, leases, bounded context, and heartbeat-retention paths where implementations exist.
4. Populate stable prior-art identifiers only from verified patent and non-patent sources.
5. Re-run the canonical entry point after each material family-status change; no manual queue, status, receipt, source-corroboration, or handoff reconciliation is required.

## Validation state

The new queue builder, validator, dispatcher integration, and regression tests are committed, but the latest direct commits have no attached pull-request workflow run. Authoritative execution receipts remain required; absence of a run is not validation success.

## Ownership

Issue #1 remains the authoritative filing-priority record. This handoff owns the workstream-transition rule, candidate-review activation boundary, concurrency-safe runner, unified dispatcher, machine queue, evidence-acquisition queue, source-corroboration controls, and synchronized continuation state.
