"""Diagram Generator (v1)

Produces simple ASCII diagrams from disclosure stubs.
"""

from __future__ import annotations
import pathlib

def ascii_system_diagram(title: str) -> str:
    return f"""
# FIG. 1 — System Diagram (ASCII)

+---------------------------+
|  StegVerse SCW / ECL Core |   <-- policy + templates
+------------+--------------+
             |
             v
+---------------------------+       +----------------------+
|  Ephemeral Artifact Gen   | ----> |  Short‑lived Files   |
+------------+--------------+       +----------+-----------+
             |                                 |
             v                                 v
+---------------------------+       +----------------------+
|  Usage + Event Ledger     | <---- |   CI/CD Execution    |
+---------------------------+       +----------------------+
"""

def main():
    root = pathlib.Path(".")
    (root / "diagrams").mkdir(exist_ok=True)
    for disc in (root / "disclosures").glob("*.md"):
        inv_id = disc.stem
        out = root / "diagrams" / f"{inv_id}_diagrams.md"
        if out.exists():
            continue
        title = disc.read_text().splitlines()[0].strip("# ").strip()
        out.write_text(ascii_system_diagram(title), encoding="utf-8")
        print(f"[DIAGRAM] wrote {out}")

if __name__ == "__main__":
    main()
