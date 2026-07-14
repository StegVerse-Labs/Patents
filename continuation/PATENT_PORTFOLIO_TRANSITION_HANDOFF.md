# Patent Portfolio Transition Handoff

## Current decision

`CONTINUE_ACTIVE_PATENT_WORK`

The ecosystem-candidate review path is armed but not active because PAT-001 and PAT-005 still have authorized machine tasks. The durable controller and status record must determine future transitions; sessions must not activate candidate review merely because external blockers also exist.

## Active-family work completed

### PAT-001

- `evidence/PAT-001-negative-and-failure-path-matrix.md`
- `diagrams/PAT-001-drawing-production-spec.md`
- `tools/validate_completion_status.py`
- `tests/test_completion_status.py`
- `tools/lint_patent_drawings.py`
- `tests/test_patent_drawings.py`

The evidence and drawing records separate verified negative behavior from unverified construction, expiry, retention, and heartbeat paths. The validators now enforce completion-record consistency, prohibit patent-pending authorization before a recorded filing, detect missing declared artifacts, and lint Mermaid drawing sources before rendering.

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

1. Corroborate PAT-001 June 6 and June 16 source records and commits.
2. Preserve executable fixtures for PAT-001 negative and proposed paths where implementation exists.
3. Add artifact maps to PAT-001 and PAT-005 completion records, then validate them against repository state.
4. Render and hash PAT-001 verified-core drawings after source lint passes.
5. Run readiness, completion, drawing, and full tests through the authoritative dispatcher.
6. Complete PAT-005 machine tasks in its completion record.
7. Re-run `tools/select_patent_workstream.py` after each material family-status change.

## Validation state

The latest direct commits have no attached pull-request workflow run. Authoritative dispatcher receipts therefore remain required. Absence of a workflow run must not be interpreted as validation success.

## Ownership

Issue #1 remains the portfolio priority record. This handoff owns the workstream-transition rule and candidate-review activation boundary.
