"""StegPatent-AI-001 — Patent Entity (v2)

Runs inside GitHub Actions.

v2 change (doctrine alignment): the candidate gate is now POSITIVE-TRIGGER
ONLY, matching canon/docs/PATENT_DOCTRINE.md exactly. A commit becomes a
patent candidate if and only if at least one of:

  T1  commit message contains "[PATENT]"
  T2  a file added/changed under patent_candidates/**
  T3  an associated PR carries the label "patent-candidate"

v1 used a negative filter (anything not chore/docs/merge) which drifted
from doctrine and would emit disclosures for every substantive commit
across both orgs. That gate is removed. Every admitted candidate now gets
a trigger receipt in /queue recording which trigger fired and the
evidence, so greens trace to executed predicate outcomes (dead-basis
doctrine).

Safety unchanged: v2 only generates drafts, never files externally.
"""

from __future__ import annotations

import os, json, fnmatch, datetime as dt, pathlib
from typing import List, Optional, Tuple
import requests

API = "https://api.github.com"
CANDIDATE_PATH_PREFIX = "patent_candidates/"
CANDIDATE_PR_LABEL = "patent-candidate"
COMMIT_TAG = "[PATENT]"


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def utc_iso(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


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


# ---------------------------------------------------------------------------
# Candidate gate — doctrine triggers, cheapest check first
# ---------------------------------------------------------------------------

def check_triggers(token: str, full_name: str, commit: dict) -> Optional[Tuple[str, str]]:
    """Return (trigger_id, evidence) if the commit is a patent candidate
    under doctrine, else None. Checks are ordered by API cost:
    T1 needs no extra call, T2 needs one, T3 needs one."""
    owner, repo = full_name.split("/")
    sha = commit["sha"]
    msg = commit["commit"]["message"]

    if COMMIT_TAG.lower() in msg.lower():
        return ("T1-commit-tag", f"message contains {COMMIT_TAG}: {msg.splitlines()[0][:120]}")

    try:
        detail = gh_get(token, f"/repos/{owner}/{repo}/commits/{sha}")
        for f in detail.get("files", []):
            name = f.get("filename", "")
            if name.startswith(CANDIDATE_PATH_PREFIX):
                return ("T2-candidate-path", f"touched {name}")
    except RuntimeError as e:
        log(f"WARN: commit detail fetch failed for {full_name}@{sha[:7]}: {e}")

    try:
        prs = gh_get(token, f"/repos/{owner}/{repo}/commits/{sha}/pulls")
        for pr in prs:
            labels = [lb.get("name", "") for lb in pr.get("labels", [])]
            if CANDIDATE_PR_LABEL in labels:
                return ("T3-pr-label", f"PR #{pr.get('number')} labeled {CANDIDATE_PR_LABEL}")
    except RuntimeError as e:
        log(f"WARN: PR lookup failed for {full_name}@{sha[:7]}: {e}")

    return None


def write_trigger_receipt(root: pathlib.Path, inv_id: str, full_name: str,
                          sha: str, trigger: str, evidence: str):
    path = root / "queue" / f"{inv_id}.trigger.json"
    if path.exists():
        return False
    path.write_text(json.dumps({
        "sig": "patent-trigger-receipt:v1",
        "invention_id": inv_id,
        "source": f"{full_name}@{sha}",
        "trigger": trigger,
        "evidence": evidence,
        "admitted_utc": utc_iso(utc_now()),
    }, indent=2), encoding="utf-8")
    log(f"ADMIT {inv_id} via {trigger} — {evidence}")
    return True


def infer_invention_id(full_name: str, sha: str) -> str:
    return f"{full_name.split('/')[1]}-{sha[:7]}"


def ensure_dirs(root: pathlib.Path):
    for d in ["disclosures", "provisionals", "claims", "diagrams", "deadlines",
              "queue", "filing_packets"]:
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
        "date_utc": utc_iso(utc_now()),
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
        "date_utc": utc_iso(utc_now()),
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
    now = utc_now()
    data["items"].append({
        "invention_id": inv_id,
        "provisional_filed_utc": None,
        "candidate_admitted_utc": utc_iso(now),
        "nonprovisional_due_utc": None,
        "pct_due_utc": None,
        "status": "drafting",
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
    since = utc_iso(utc_now() - dt.timedelta(days=since_days))

    ensure_dirs(root)
    scanned = admitted = 0

    for org in manifest["allow_orgs"]:
        log(f"Scanning org: {org} since {since} …")
        for r in list_org_repos(token, org):
            full = r["full_name"]
            if glob_any(full, manifest.get("exclude_repos_glob", [])):
                continue
            if not glob_any(full, manifest.get("allow_repos_glob", [])):
                continue

            for c in recent_commits(token, full, since):
                scanned += 1
                sha = c["sha"]
                hit = check_triggers(token, full, c)
                if hit is None:
                    continue
                trigger, evidence = hit
                inv_id = infer_invention_id(full, sha)

                if write_trigger_receipt(root, inv_id, full, sha, trigger, evidence):
                    admitted += 1
                title = f"{full} — {c['commit']['message'].splitlines()[0][:80]}"
                sources = f"{full}@{sha} (trigger: {trigger})"

                write_disclosure(root, inv_id, title, sources)
                write_provisional(root, inv_id, title)
                update_deadlines(root, inv_id)

    log(f"Patent watch run complete. scanned={scanned} admitted={admitted}")


if __name__ == "__main__":
    main()
