# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but not active because PAT-001 and PAT-005 still have authorized machine tasks. The durable controller and status record must determine future transitions; sessions must not activate candidate review merely because external blockers also exist.

## Manual-task elimination baseline

All repeatable repository-local validation and task-selection steps are now consolidated behind:

- `tools/run_patent_portfolio_dispatcher.py`
- `tests/test_patent_portfolio_dispatcher.py`
- `tools/build_patent_machine_queue.py`
- `tests/test_patent_machine_queue.py`

A single dispatcher invocation now performs:

1. PAT-001 completion-record validation;
2. PAT-005 completion-record validation;
3. PAT-001 readiness validation, accepting the expected fail-closed blocker result as a valid machine outcome;
4. PAT-001 drawing-source linting;
5. PAT-001 rendered-drawing manifest, SHA-256, SVG, and reference-numeral verification;
6. automatic machine-task queue generation from active-family completion records;
7. active-work versus ecosystem-candidate workstream selection;
8. the complete pytest surface;
9. one consolidated JSON receipt.

The automatic queue excludes human, practitioner, inventor, approval, authorization, signature, payment, submission, filing, and patent-pending tasks. Those excluded transitions are not avoidable manual chores; they are legally or evidentially non-delegable authority boundaries.

## Active-family work completed

### PAT-001 and PAT-005 completion controls

- `data/PAT-001-completion-status.json`
- `data/PAT-005-completion-status.json`
- `tools/validate_completion_status.py`
- `tests/test_completion_status.py`

Both active-family completion records contain explicit `artifact_map` entries for every `completed: true` key. The validator fails closed for missing maps, unmapped completion claims, missing files, authority-state conflicts, and patent-pending authorization before filing.

### PAT-001 rendered review drawings

- `rendered/PAT-001/PAT-001-FIG-01-system-overview.svg`
- `rendered/PAT-001/PAT-001-FIG-02-role-sequence.svg`
- `rendered/PAT-001/PAT-001-FIG-03-receipt-binding.svg`
- `rendered/PAT-001/PAT-001-FIG-04-decision-boundary.svg`
- `rendered/PAT-001/manifest.json`
- `tools/verify_rendered_drawings.py`
- `tests/test_rendered_drawings.py`

The four verified-core drawings are monochrome SVG review artifacts with fixed reference numerals and SHA-256 values. They are not approved filing drawings. PAT-001 completion state records rendering as complete while the combined rendered-and-approved gate remains false pending practitioner approval.

### Existing PAT-001 machine controls

- `evidence/PAT-001-negative-and-failure-path-matrix.md`
- `diagrams/PAT-001-drawing-production-spec.md`
- `tools/lint_patent_drawings.py`
- `tests/test_patent_drawings.py`

These records separate verified negative behavior from unverified construction, expiry, retention, and heartbeat paths and lint Mermaid drawing sources before rendering.

## Portfolio transition infrastructure

- `docs/ECOSYSTEM_PATENT_CANDIDATE_REVIEW.md`
- `tools/select_patent_workstream.py`
- `tests/test_select_patent_workstream.py`
- `schemas/ecosystem-patent-candidate.schema.json`
- `data/patent-workstream-status.json`

## Activation event

Switch to `REVIEW_ECOSYSTEM_CANDIDATES` only when every higher-priority active family is either:

1. submission-ready; or
2. externally blocked with no authorized machine task remaining.

## Return event

Resume an active family immediately when new evidence, contributor facts, practitioner feedback, verified search results, drawing approval, dispatcher results, authorization, or a filing event arrives.

## Candidate review scope

A review cycle may inspect repositories and commits, identify technical mechanisms, preserve evidence, compare against existing families, and recommend a working disposition. It may not determine inventorship, patentability, freedom to operate, filing authority, or patent-pending status.

## Current next machine work

1. Execute the unified dispatcher and preserve its consolidated receipt through the authoritative execution path.
2. Corroborate PAT-001 June 6 and June 16 source records and commits.
3. Preserve executable fixtures for PAT-001 negative and proposed paths where implementation exists.
4. Complete PAT-005 source-anchor and executable-negative-fixture tasks.
5. Re-run the dispatcher after each material family-status change; it will rebuild the machine queue and workstream decision automatically.

## Validation state

The automation code and regression tests are committed, but the latest direct commits do not have an attached pull-request workflow run. Authoritative execution receipts therefore remain required. Absence of a workflow run must not be interpreted as validation success.

## Ownership

Issue #1 remains the portfolio priority record. This handoff owns the workstream-transition rule, candidate-review activation boundary, unified machine dispatcher, and automatic machine-task queue.
