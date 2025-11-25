"""Deadline AI (v1)

Reads deadlines ledger and emits warnings when within a threshold.
"""

from __future__ import annotations
import json, pathlib, datetime as dt

WARN_DAYS = 60

def main():
    ledger = pathlib.Path("deadlines/deadlines.json")
    if not ledger.exists():
        print("[DEADLINE] no ledger found")
        return
    data = json.loads(ledger.read_text())
    now = dt.datetime.utcnow()
    for item in data.get("items", []):
        due = dt.datetime.fromisoformat(item["nonprovisional_due_utc"].replace("Z", ""))
        days_left = (due - now).days
        if days_left <= WARN_DAYS:
            print(f"[DEADLINE] {item['invention_id']} non‑provisional due in {days_left} days")

if __name__ == "__main__":
    main()
