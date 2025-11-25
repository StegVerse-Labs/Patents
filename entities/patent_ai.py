"""StegPatent-AI-001 — Patent Entity (v1)

Runs inside GitHub Actions.

- Scans org repos for new patentable deltas
- Emits disclosure stubs + provisional skeletons
- Updates deadlines ledger

NOTE: v1 is conservative: it only generates drafts, never files externally.
"""

from __future__ import annotations

import os, json, fnmatch, datetime as dt, pathlib, re
from typing import List
import requests

API = "https://api.github.com"

def log(msg): 
    print(f"[PATENT_AI] {msg}", flush=True)

def gh_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "StegPatent-AI-001",
    }

def gh_get(token, path, params=None):
    r = requests.get(f"{API}{path}", headers=gh_headers(token), params=params, timeout=30)
    if r.status_code >= 300:
        raise RuntimeError(f"GitHub GET {path} failed: {r.status_code} {r.text[:200]}")
    return r.json()

def load_manifest(root: pathlib.Path) -> dict:
    return json.loads((root / "patent_manifest.json").read_text())

def glob_any(name: str, patterns: List[str]) -> bool:
    return any(fnmatch.fnmatch(name, pat) for pat in patterns)

def list_org_repos(token: str, org: str):
    repos, page = [], 1
    while True:
        batch = gh_get(token, f"/orgs/{org}/repos",
                       {"per_page": 100, "page": page, "type": "all"})
        if not batch:
            break
        repos.extend(batch)
        page += 1
        if page > 10:
            break
    return repos

def recent_commits(token: str, full_name: str, since_iso: str):
    owner, repo = full_name.split("/")
    return gh_get(token, f"/repos/{owner}/{repo}/commits",
                  {"since": since_iso, "per_page": 20})

def infer_invention_id(full_name: str, sha: str) -> str:
    short = sha[:7]
    repo = full_name.split("/")[1]
    return f"{repo}-{short}"

def ensure_dirs(root: pathlib.Path):
    for d in ["disclosures", "provisionals", "claims", "diagrams", "deadlines", "queue"]:
        (root / d).mkdir(parents=True, exist_ok=True)

def render_template(tmpl: str, kv: dict) -> str:
    out = tmpl
    for k, v in kv.items():
        out = out.replace("{{" + k + "}}", str(v))
    return out

def write_disclosure(root: pathlib.Path, inv_id: str, title: str, sources: str):
    tmpl = (root / "templates/disclosure.md").read_text()
    txt = render_template(tmpl, {
        "invention_id": inv_id,
        "title": title,
        "inventors": "Rigel Randolph et al.",
        "date_utc": dt.datetime.utcnow().isoformat() + "Z",
        "sources": sources,
    })
    path = root / "disclosures" / f"{inv_id}.md"
    if not path.exists():
        path.write_text(txt, encoding="utf-8")
        log(f"Wrote disclosure {path}")

def write_provisional(root: pathlib.Path, inv_id: str, title: str):
    tmpl = (root / "templates/provisional.md").read_text()
    txt = render_template(tmpl, {
        "invention_id": inv_id,
        "title": title,
        "inventors": "Rigel Randolph et al.",
        "date_utc": dt.datetime.utcnow().isoformat() + "Z",
        "fig1": "System overview",
        "fig2": "Method flow",
        "fig3": "Timing/event adjacency",
    })
    path = root / "provisionals" / f"{inv_id}_provisional.md"
    if not path.exists():
        path.write_text(txt, encoding="utf-8")
        log(f"Wrote provisional skeleton {path}")

def update_deadlines(root: pathlib.Path, inv_id: str):
    ledger = root / "deadlines" / "deadlines.json"
    data = {"sig": "deadlines:v1", "items": []}
    if ledger.exists():
        data = json.loads(ledger.read_text())
    if any(i["invention_id"] == inv_id for i in data["items"]):
        return
    now = dt.datetime.utcnow()
    data["items"].append({
        "invention_id": inv_id,
        "provisional_filed_utc": now.isoformat() + "Z",
        "nonprovisional_due_utc": (now + dt.timedelta(days=365)).isoformat() + "Z",
        "pct_due_utc": (now + dt.timedelta(days=365)).isoformat() + "Z",
        "status": "drafting"
    })
    ledger.write_text(json.dumps(data, indent=2))
    log(f"Updated deadlines ledger for {inv_id}")

def main():
    root = pathlib.Path(os.getenv("GITHUB_WORKSPACE", "."))
    token = (os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or "").strip()
    if not token:
        raise SystemExit("Missing GH_TOKEN")

    manifest = load_manifest(root)
    since_days = int(os.getenv("PATENT_SINCE_DAYS", "7"))
    since = (dt.datetime.utcnow() - dt.timedelta(days=since_days)).isoformat() + "Z"

    ensure_dirs(root)

    for org in manifest["allow_orgs"]:
        log(f"Scanning org: {org} since {since} …")
        for r in list_org_repos(token, org):
            full = r["full_name"]
            if glob_any(full, manifest.get("exclude_repos_glob", [])):
                continue
            if not glob_any(full, manifest.get("allow_repos_glob", [])):
                continue

            for c in recent_commits(token, full, since):
                sha = c["sha"]
                msg = c["commit"]["message"].splitlines()[0]
                inv_id = infer_invention_id(full, sha)

                if re.search(r"\b(chore|docs|readme|bump|merge)\b", msg.lower()):
                    continue

                title = f"{full} — {msg[:80]}"
                sources = f"{full}@{sha}"

                write_disclosure(root, inv_id, title, sources)
                write_provisional(root, inv_id, title)
                update_deadlines(root, inv_id)

    log("Patent watch run complete.")

if __name__ == "__main__":
    main()
