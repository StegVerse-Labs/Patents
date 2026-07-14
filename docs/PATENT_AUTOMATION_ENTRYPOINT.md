# Patent Portfolio Automation Entry Point

## Canonical command

```bash
python tools/patent_portfolio.py --repo-root .
```

This is the canonical repository-local entry point for all repeatable machine-owned patent work.

## Automatic actions

One invocation:

1. acquires an exclusive portfolio execution lock;
2. runs PAT-001 and PAT-005 completion validation;
3. evaluates PAT-001 filing-readiness records without treating expected blockers as runtime failure;
4. lints PAT-001 drawing sources;
5. verifies rendered SVG files, SHA-256 values, XML structure, figure labels, and reference numerals;
6. rebuilds the authorized machine-task queue;
7. selects active-family work or ecosystem-candidate review;
8. runs the complete test suite;
9. writes the consolidated dispatcher receipt;
10. synchronizes canonical workstream and continuation records;
11. emits a concise summary containing the next machine task.

## Durable outputs

- `receipts/patent-portfolio-dispatch.json`
- `data/patent-machine-queue.json`
- `data/patent-workstream-status.json`
- `continuation/patent-portfolio-machine-continuation.json`

## Concurrency behavior

The runner creates `receipts/.patent-portfolio.lock` using exclusive creation. A concurrent invocation fails with `PORTFOLIO_EXECUTION_LOCKED` rather than risking competing receipt or state writes. The lock is removed on success, validation failure, or exception.

## Exit decisions

- `0`: machine validation passed and synchronized state is readable;
- `2`: one or more dispatcher checks failed;
- `3`: synchronized state is missing or invalid;
- `4`: another portfolio execution owns the lock.

## Authority boundary

The entry point never:

- determines inventorship;
- supplies contributor testimony;
- makes legal or patentability determinations;
- approves drawings;
- authorizes a review or filing packet;
- signs an application;
- pays filing fees;
- submits an application;
- authorizes use of `patent pending`.

Those transitions remain explicit human or qualified-practitioner acts. All repeatable repository-local preparation, validation, queueing, state selection, receipt generation, and continuation synchronization are automated.
