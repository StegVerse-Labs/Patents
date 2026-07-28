#!/usr/bin/env python3
"""Validate portfolio filing-state invariants without performing any filing.

This validator rejects any family that claims a filed, patent-pending, or
calculated-deadline state unless the repository record contains an actual
filing date, application number, and filing-receipt path. It validates records;
it does not submit, certify, pay, authorize, or provide legal conclusions.

Usage:
    python tools/validate_portfolio_filing_state.py --root .

Exit codes:
    0  PORTFOLIO_FILING_STATE_VALID
    2  FAIL_CLOSED_FILING_STATE
    3  INVALID_PORTFOLIO_RECORD
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

SIG = "portfolio-filing-state-validation:v1"
ACTIVE_FILED_STATES = {"filed", "provisional_filed", "nonprovisional_filed"}
PATENT_PENDING_TRUE = {True, "true", "yes", "authorized"}


@dataclass(frozen=True)
class CheckResult:
    family_id: str
    check_id: str
    status: str
    detail: str


def _is_nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_true(value: Any) -> bool:
    return value in PATENT_PENDING_TRUE


def _parse_iso_date(value: Any) -> bool:
    if not _is_nonempty(value):
        return False
    try:
        date.fromisoformat(str(value)[:10])
    except ValueError:
        return False
    return True


def _receipt_exists(root: pathlib.Path, value: Any) -> bool:
    if not _is_nonempty(value):
        return False
    path = pathlib.Path(value)
    if path.is_absolute():
        return False
    return (root / path).is_file()


def _validate_family(root: pathlib.Path, family: dict[str, Any]) -> list[CheckResult]:
    family_id = str(family.get("family_id") or family.get("family_key") or "UNKNOWN")
    checks: list[CheckResult] = []

    status = str(family.get("status") or "").lower()
    filed_value = family.get("filed")
    filed_claimed = filed_value is True or status in ACTIVE_FILED_STATES or str(family.get("human_filing") or "").lower() in ACTIVE_FILED_STATES
    patent_pending_claimed = _is_true(family.get("patent_pending_authorized")) or _is_true(family.get("patent_pending"))

    receipt = family.get("filing_receipt")
    application_number = family.get("application_number")
    filing_date = family.get("filing_date") or family.get("provisional_filed_utc") or family.get("actual_filing_date")
    deadline = family.get("nonprovisional_deadline")

    if filed_claimed:
        missing = []
        if not _receipt_exists(root, receipt):
            missing.append("existing repository filing_receipt")
        if not _is_nonempty(application_number):
            missing.append("application_number")
        if not _parse_iso_date(filing_date):
            missing.append("actual filing_date")
        checks.append(CheckResult(
            family_id,
            "filed-state-evidence",
            "PASS" if not missing else "FAIL",
            "filed state supported" if not missing else "missing " + ", ".join(missing),
        ))
    else:
        checks.append(CheckResult(family_id, "filed-state-evidence", "PASS", "no filed state claimed"))

    if patent_pending_claimed:
        supported = filed_claimed and _receipt_exists(root, receipt) and _is_nonempty(application_number) and _parse_iso_date(filing_date)
        checks.append(CheckResult(
            family_id,
            "patent-pending-boundary",
            "PASS" if supported else "FAIL",
            "patent-pending state supported by actual filing evidence" if supported else "patent-pending claimed without complete actual filing evidence",
        ))
    else:
        checks.append(CheckResult(family_id, "patent-pending-boundary", "PASS", "patent-pending state not claimed"))

    if deadline is not None:
        supported = filed_claimed and _parse_iso_date(filing_date) and _parse_iso_date(deadline)
        checks.append(CheckResult(
            family_id,
            "deadline-basis",
            "PASS" if supported else "FAIL",
            "deadline has an actual filing-date basis" if supported else "deadline present without a valid actual filing-date basis",
        ))
    else:
        checks.append(CheckResult(family_id, "deadline-basis", "PASS", "no filing deadline calculated"))

    if receipt is not None and not _receipt_exists(root, receipt):
        checks.append(CheckResult(family_id, "receipt-path", "FAIL", f"filing receipt path does not exist: {receipt}"))
    else:
        checks.append(CheckResult(family_id, "receipt-path", "PASS", "receipt absent as expected or existing path verified"))

    return checks


def validate(root: pathlib.Path) -> tuple[dict[str, Any], int]:
    ledger_path = root / "data" / "portfolio-completion-status.json"
    if not ledger_path.is_file():
        return {
            "sig": SIG,
            "decision": "INVALID_PORTFOLIO_RECORD",
            "checks": [asdict(CheckResult("PORTFOLIO", "portfolio-ledger", "FAIL", f"missing {ledger_path}"))],
        }, 3

    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {
            "sig": SIG,
            "decision": "INVALID_PORTFOLIO_RECORD",
            "checks": [asdict(CheckResult("PORTFOLIO", "portfolio-ledger", "FAIL", f"cannot parse ledger: {exc}"))],
        }, 3

    families = ledger.get("numbered_families")
    if not isinstance(families, list) or not families:
        return {
            "sig": SIG,
            "decision": "INVALID_PORTFOLIO_RECORD",
            "checks": [asdict(CheckResult("PORTFOLIO", "numbered-families", "FAIL", "numbered_families must be a non-empty list"))],
        }, 3

    checks: list[CheckResult] = []
    for family in families:
        if not isinstance(family, dict):
            checks.append(CheckResult("UNKNOWN", "family-record", "FAIL", "family record is not an object"))
            continue
        checks.extend(_validate_family(root, family))

    failed = [check for check in checks if check.status == "FAIL"]
    decision = "FAIL_CLOSED_FILING_STATE" if failed else "PORTFOLIO_FILING_STATE_VALID"
    report = {
        "sig": SIG,
        "decision": decision,
        "portfolio_ledger": str(ledger_path.relative_to(root)),
        "schema_version": ledger.get("schema_version"),
        "family_count": len(families),
        "checks": [asdict(check) for check in checks],
        "failures": [asdict(check) for check in failed],
        "boundary": {
            "external_submission_performed": False,
            "fee_payment_performed": False,
            "legal_conclusion_generated": False,
        },
    }
    return report, 2 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    report, exit_code = validate(root)
    encoded = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        output = pathlib.Path(args.output)
        if not output.is_absolute():
            output = root / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
