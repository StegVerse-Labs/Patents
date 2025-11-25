"""Claim Generator (v1)

Given an invention disclosure, produce a 3‑tier claims set.
"""

from __future__ import annotations
import pathlib, re

def generate_claims(disclosure_text: str) -> str:
    lines = [l.strip() for l in disclosure_text.splitlines() if l.strip()]
    anchors = []
    for l in lines:
        if l.lower().startswith("solution"):
            anchors.append(l)
    core = anchors[0] if anchors else "a system for autonomous ephemeral computation"

    return f"""# Claims Set

## Broad (Independent) Claims
1. A method comprising: providing {core}; generating a short‑lived configuration artifact immediately prior to execution; executing the artifact; and dissolving the artifact after execution.

## Intermediate Claims
2. The method of claim 1, wherein generation is triggered by predicted event adjacency derived from repository state signals.

3. The method of claim 1, wherein dissolved artifacts are re‑materialized on demand based on a file usage ledger.

## Narrow (Dependent) Claims
4. The method of claim 2, wherein predicted event adjacency includes token rotation windows and workflow runner deprecation windows.

5. The method of claim 3, further comprising maintaining a manifest of artifact build identifiers and hashes excluding metadata blocks.
"""

def main():
    root = pathlib.Path(".")
    (root / "claims").mkdir(exist_ok=True)
    for p in (root / "disclosures").glob("*.md"):
        inv_id = p.stem
        out = root / "claims" / f"{inv_id}_claims.md"
        if out.exists():
            continue
        out.write_text(generate_claims(p.read_text()), encoding="utf-8")
        print(f"[CLAIMS] wrote {out}")

if __name__ == "__main__":
    main()
