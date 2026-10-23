#!/usr/bin/env python3
"""PAT-003 finish-point structural verifier, v1 (stdlib only; operating mode E0, no LLM).

This verifier checks the structure of the PAT-003 finish points FE-1..3, FC-1..2 and
FP-1..2. Their text was adopted in StegVerse-Labs/.github#3331 @397e00f5, in
tests/fixtures/canonical_task_registration/pat-003-lane-a/PAT-003-{EVIDENCE,CHRONOLOGY,
PRIOR-ART}.request.json at sealed_scope.scope.finish_point.predicate. It checks them at
a repository tree (--root) or at a commit (--git-dir/--rev).

Every status is one of MET, NOT_MET or UNKNOWN. UNKNOWN never counts as MET.

Exit codes:
- 0 only if every requested finish point is MET;
- 2 if any requested point is NOT_MET or UNKNOWN;
- 3 on bad input, with a sealed six-field FAIL_CLOSED.

Owner and practitioner check-offs (index L73, L75, L77, L78, L79, L82) are reported as
HUMAN_ACTION dependencies (class C). They are never evaluated as met.

The output is evidence input only. It is not truth, not a legal determination and not
execution authority. It never states that a family may be filed. The furthest any result
reaches is evidence-complete inputs to READY_FOR_FILING_REVIEW.

The field lists are read from the existing templates at the tree being checked:
- chronology fields: evidence/PAT-003_DISCLOSURE_CHRONOLOGY.md, block under
  "## Chronology records required" (L16-L31 @cf30104d);
- event classes: the "### " headings under "## Event classes" (L36-L86 @cf30104d);
- search-record fields: reviews/PAT-003_TECHNICAL_COMPARISON_RESEARCH_LEDGER.md, block
  under "## Search record fields" (L78-L92 @cf30104d);
- classification vocabulary: filing-readiness/PAT-003_LIMITATION_EVIDENCE_CHART.md L7
  @cf30104d (from data/PAT-003-completion-status.json L81);
- limitations: data/master_claims.json, claims CLM-PAT-003-METHOD-001 (L229) and
  CLM-PAT-003-SYSTEM-001 (L251) @cf30104d;
- evidence-map columns and the three evidence classes: the FE-1 predicate, plus the
  section header appended in StegVerse-Labs/Patents#21 @63be4ccf, chart L82;
- implementation-anchor fields: data/PAT-005-implementation-anchors.json, checked by
  tools/validate_pat005_implementation_anchors.py L52-L83 @cf30104d; the "test and
  retained output" requirement is from the index L75;
- disclosure-register columns: evidence/PAT-005-public-disclosure-audit.md L52
  @cf30104d, with the family named PAT-003; the path follows
  data/PAT-005-completion-status.json L61.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

SCHEMA = "stegverse.patents.pat003-finish-point-verifier/v1"
FAIL_SCHEMA = "stegverse.patents.pat003-finish-point-verifier.fail-closed/v1"
POINTS = ("FE-1", "FE-2", "FE-3", "FC-1", "FC-2", "FP-1", "FP-2")
TASK_OF = {"FE-1": "PAT-003-EVIDENCE", "FE-2": "PAT-003-EVIDENCE", "FE-3": "PAT-003-EVIDENCE",
           "FC-1": "PAT-003-CHRONOLOGY", "FC-2": "PAT-003-CHRONOLOGY",
           "FP-1": "PAT-003-PRIOR-ART", "FP-2": "PAT-003-PRIOR-ART"}
PREDICATE_SOURCE = ("StegVerse-Labs/.github#3331 @397e00f52a980adf49bcf085f31636301b0e9118 "
                    "tests/fixtures/canonical_task_registration/pat-003-lane-a/"
                    "PAT-003-{EVIDENCE,CHRONOLOGY,PRIOR-ART}.request.json "
                    "sealed_scope.scope.finish_point.predicate")
MET, NOT_MET, UNKNOWN = "MET", "NOT_MET", "UNKNOWN"
OWNING_GOAL = "StegVerse-org/.github#165"
RETRY = "research/pat003/finish_point_verifier_v1.py::main"

CHART = "filing-readiness/PAT-003_LIMITATION_EVIDENCE_CHART.md"
CHRONO = "evidence/PAT-003_DISCLOSURE_CHRONOLOGY.md"
CHRONO_DIR = "evidence/PAT-003-chronology-evidence/"
LEDGER = "reviews/PAT-003_TECHNICAL_COMPARISON_RESEARCH_LEDGER.md"
INDEX = "filing-readiness/PAT-003_FILING_READINESS_INDEX.md"
CLAIMS = "data/master_claims.json"
PA_IDS = "data/active-family-prior-art-identifiers.json"
ANCHORS = "data/PAT-003-implementation-anchors.json"
AUDIT = "evidence/PAT-003-public-disclosure-audit.md"
PAT005_AUDIT = "evidence/PAT-005-public-disclosure-audit.md"
REQUIRED_TEMPLATES = (CHART, CHRONO, LEDGER, INDEX, CLAIMS, PAT005_AUDIT)
THIS_REPO = "StegVerse-Labs/Patents"
CLAIM_IDS = ("CLM-PAT-003-METHOD-001", "CLM-PAT-003-SYSTEM-001")
EVIDENCE_CLASSES = ("proofs", "software tests", "physical measurements")
MAP_COLUMNS = ["Lim.", "Evidence class", "Locator", "Hash", "Conditions", "Status"]
POINTER_COLUMNS = ["Pointer", "Kind", "Drive file id", "SHA-256 (retrieved copy)", "Note"]
# Rows proposed as implemented-partial per the FE-3 predicate.
FE3_ROWS = (("CLM-PAT-003-METHOD-001", "L3"), ("CLM-PAT-003-SYSTEM-001", "L4"))
ANCHOR_TYPES = {"executable_builder", "executable_validator", "acceptance_fixture",
                "contract", "receipt", "boundary_document"}
EXECUTABLE_TYPES = {"executable_builder", "executable_validator", "acceptance_fixture"}
OVERLAP_COLUMNS = ["reference_id", "family_id", "mapped_limitations", "candidate_overlap"]
# Human check-offs: (index label prefix, finish points it follows, citation)
HUMAN = (("Verified implementation anchors", ("FE-3",), "index L75"),
         ("Every row of `PAT-003_LIMITATION_EVIDENCE_CHART.md` classified", ("FE-1", "FE-2"), "index L77"),
         ("Factual conception and public/private disclosure chronology", ("FC-1",), "index L78"),
         ("Disclosure-risk audit of already-public source", ("FC-2",), "index L79"),
         ("Dated, reproducible prior-art search ledger", ("FP-1", "FP-2"), "index L82"))

HEX40 = re.compile(r"\b[0-9a-f]{40}\b")
HEX64 = re.compile(r"\b[0-9a-f]{64}\b")
HEXPFX = re.compile(r"\b[0-9a-f]{7,64}\b")
DRIVE_ID = re.compile(r"^[A-Za-z0-9_-]{25,64}$")
POINTER_ID = re.compile(r"\b(?:PRIV|KV)-\d+\b")
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?$")
ISO_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})")
REPO_NAME = re.compile(r"\b(StegVerse-[A-Za-z0-9-]+/[A-Za-z0-9_.-]+?)(?=[\s`,;)]|$)")
BACKTICK = re.compile(r"`([^`]*)`")


class BadInput(Exception):
    def __init__(self, code: str, predicate: str, repair: str):
        super().__init__(code)
        self.code, self.predicate, self.repair = code, predicate, repair


def fail_closed(exc: BadInput) -> dict:
    six = {"failure_code": exc.code, "failed_predicate": exc.predicate,
           "required_evidence_or_repair": exc.repair, "retry_entrypoint": RETRY,
           "owning_existing_goal": OWNING_GOAL,
           "next_attempt": "rerun with corrected input; nothing was evaluated"}
    seal = hashlib.sha256(json.dumps(six, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"schema": FAIL_SCHEMA, "disposition": "FAIL_CLOSED", **six, "seal_sha256": seal,
            "authority_effect": "NONE_EVIDENCE_INPUT_ONLY"}


# ---------------------------------------------------------------- tree / stores
def _git(gitdir: str, *args: str) -> Tuple[int, bytes]:
    p = subprocess.run(["git", "-C", gitdir, *args], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return p.returncode, p.stdout


class Store:
    """Offline local git object store for one repository."""

    def __init__(self, path: Optional[str]):
        self.path = path
        self.usable = bool(path) and _git(path, "rev-parse", "--git-dir")[0] == 0
        self.shallow = self.usable and _git(path, "rev-parse", "--is-shallow-repository")[1].strip() == b"true"

    def obj_type(self, sha: str) -> Optional[str]:
        if not self.usable:
            return None
        rc, out = _git(self.path, "cat-file", "-t", sha)
        return out.decode().strip() if rc == 0 else None

    def blob_at(self, commit: str, path: str) -> Optional[str]:
        if not self.usable:
            return None
        rc, out = _git(self.path, "rev-parse", "--verify", "-q", f"{commit}:{path}")
        return out.decode().strip() if rc == 0 else None

    def first_add_date(self, rev: str, path: str) -> Optional[str]:
        if not self.usable or self.shallow:
            return None
        rc, out = _git(self.path, "log", "--diff-filter=A", "--format=%cI", rev, "--", path)
        lines = out.decode().split()
        return lines[-1][:10] if rc == 0 and lines else None


class Tree:
    def __init__(self, root: Optional[str], gitdir: Optional[str], rev: Optional[str]):
        self.root, self.gitdir = root, gitdir
        self.reads: Dict[str, Optional[str]] = {}
        if gitdir:
            rc, out = _git(gitdir, "rev-parse", "--verify", "-q", f"{rev}^{{commit}}")
            if rc != 0:
                raise BadInput("REV_NOT_RESOLVABLE", "REV_RESOLVES_TO_A_COMMIT_IN_GIT_DIR",
                               f"--rev {rev!r} does not resolve to a commit in --git-dir {gitdir!r}")
            self.rev = out.decode().strip()
            self.store = Store(gitdir)
            self.identity = {"mode": "git_rev", "commit": self.rev}
        else:
            if not root or not os.path.isdir(root):
                raise BadInput("ROOT_NOT_A_DIRECTORY", "ROOT_IS_AN_EXISTING_DIRECTORY",
                               f"--root {root!r} is not an existing directory")
            self.rev = None
            self.store = Store(root)
            head = None
            if self.store.usable:
                rc, out = _git(root, "rev-parse", "HEAD")
                head = out.decode().strip() if rc == 0 else None
            self.identity = {"mode": "working_tree", "head_commit_if_git": head}
            self.rev = head

    def read(self, path: str) -> Optional[str]:
        if path in self.reads:
            return self.reads[path]
        text = None
        if self.gitdir:
            rc, out = _git(self.gitdir, "show", f"{self.identity['commit']}:{path}")
            if rc == 0:
                text = out.decode("utf-8", "replace")
        else:
            full = os.path.join(self.root, path)
            if os.path.isfile(full):
                with open(full, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
        self.reads[path] = text
        return text

    def files(self) -> List[str]:
        if self.gitdir:
            rc, out = _git(self.gitdir, "ls-tree", "-r", "--name-only", self.identity["commit"])
            return sorted(out.decode().split("\n")[:-1]) if rc == 0 else []
        if self.store.usable:
            rc, out = _git(self.root, "ls-files", "--cached", "--others", "--exclude-standard")
            if rc == 0:
                return sorted(x for x in out.decode().split("\n") if x)
        acc = []
        for d, dirs, fs in os.walk(self.root):
            dirs[:] = [x for x in dirs if x != ".git"]
            for f in fs:
                acc.append(os.path.relpath(os.path.join(d, f), self.root).replace(os.sep, "/"))
        return sorted(acc)

    def read_manifest(self) -> List[dict]:
        out = []
        for p in sorted(self.reads):
            t = self.reads[p]
            out.append({"path": p, "present": t is not None,
                        "sha256": hashlib.sha256(t.encode()).hexdigest() if t is not None else None})
        return out


# ---------------------------------------------------------------- markdown helpers
def section(lines: List[str], prefix: str, level: int = 2) -> List[Tuple[int, List[Tuple[int, str]]]]:
    """All sections whose heading starts with '#'*level + ' ' + prefix; (heading line no, body)."""
    mark = "#" * level + " "
    found, cur, start = [], None, 0
    for i, ln in enumerate(lines, 1):
        is_head = re.match(r"^(#{1,%d}) " % level, ln)
        if is_head and cur is not None:
            found.append((start, cur))
            cur = None
        if ln.startswith(mark + prefix):
            cur, start = [], i
        elif cur is not None:
            cur.append((i, ln))
    if cur is not None:
        found.append((start, cur))
    return found


def fenced_blocks(body: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
    blocks, cur = [], None
    for i, ln in body:
        if ln.strip().startswith("```"):
            if cur is None:
                cur = []
            else:
                blocks.append(cur)
                cur = None
        elif cur is not None:
            cur.append((i, ln))
    return blocks


def cells(line: str) -> List[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tables(body: List[Tuple[int, str]]) -> List[Tuple[int, List[str], List[Tuple[int, List[str]]]]]:
    out, i = [], 0
    while i < len(body):
        n, ln = body[i]
        if ln.strip().startswith("|") and i + 1 < len(body) and re.match(r"^\s*\|[\s:|-]+\|\s*$", body[i + 1][1]):
            head, rows, j = cells(ln), [], i + 2
            while j < len(body) and body[j][1].strip().startswith("|"):
                rows.append((body[j][0], cells(body[j][1])))
                j += 1
            out.append((n, head, rows))
            i = j
        else:
            i += 1
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("*", "").replace("`", "")).strip().lower()


def chk(cid: str, status: str, detail: str, **kw) -> dict:
    d = {"check_id": cid, "status": status, "detail": detail}
    d.update(kw)
    return d


def rollup(checks: List[dict]) -> str:
    sts = {c["status"] for c in checks}
    if not checks or NOT_MET in sts:
        return NOT_MET
    return UNKNOWN if UNKNOWN in sts else MET


def kv_records(blocks: List[List[Tuple[int, str]]], first_key: str) -> List[Tuple[int, Dict[str, str]]]:
    recs = []
    for blk in blocks:
        content = [(i, l) for i, l in blk if l.strip()]
        if not content or not content[0][1].strip().startswith(first_key + ":"):
            continue
        rec: Dict[str, str] = {}
        for _, l in content:
            if ":" in l:
                k, v = l.split(":", 1)
                rec.setdefault(k.strip(), v.strip())
        recs.append((content[0][0], rec))
    return recs


# ---------------------------------------------------------------- templates (field provenance)
def field_block(tree: Tree, path: str, heading: str) -> Tuple[List[str], dict]:
    text = tree.read(path)
    secs = section(text.splitlines(), heading) if text is not None else []
    blocks = fenced_blocks(secs[0][1]) if secs else []
    if not blocks:
        raise BadInput("TEMPLATE_FIELD_BLOCK_ABSENT", "FIELD_LIST_READ_FROM_EXISTING_TEMPLATE",
                       f"{path}: no fenced field list under '## {heading}'")
    fields = [l.strip() for _, l in blocks[0] if l.strip()]
    lines = [i for i, l in blocks[0] if l.strip()]
    return fields, {"file": path, "lines": f"L{lines[0]}-L{lines[-1]}", "count": len(fields)}


def load_templates(tree: Tree) -> dict:
    for p in REQUIRED_TEMPLATES:
        if tree.read(p) is None:
            raise BadInput("REQUIRED_TEMPLATE_ABSENT", "EXISTING_TEMPLATES_PRESENT_AT_TREE",
                           f"required existing file {p} is absent at the tree")
    t: dict = {"sources": {}}
    t["chrono_fields"], t["sources"]["chronology_fields"] = field_block(tree, CHRONO, "Chronology records required")
    t["search_fields"], t["sources"]["search_record_fields"] = field_block(tree, LEDGER, "Search record fields")
    lines = tree.read(CHRONO).splitlines()
    ev = section(lines, "Event classes")
    classes = [(i, l[4:].strip()) for i, l in (ev[0][1] if ev else []) if l.startswith("### ")]
    if not classes:
        raise BadInput("TEMPLATE_EVENT_CLASSES_ABSENT", "FIELD_LIST_READ_FROM_EXISTING_TEMPLATE",
                       f"{CHRONO}: no '### ' event classes under '## Event classes'")
    t["event_classes"] = [c for _, c in classes]
    t["sources"]["event_classes"] = {"file": CHRONO, "lines": f"L{classes[0][0]}-L{classes[-1][0]}",
                                     "count": len(classes)}
    vocab, vline = None, None
    for i, l in enumerate(tree.read(CHART).splitlines(), 1):
        if l.startswith("- Classification vocabulary"):
            vocab = [x for x in BACKTICK.findall(l) if re.fullmatch(r"[a-z_]+", x)]
            vline = i
            break
    if not vocab:
        raise BadInput("TEMPLATE_VOCABULARY_ABSENT", "FIELD_LIST_READ_FROM_EXISTING_TEMPLATE",
                       f"{CHART}: no '- Classification vocabulary' line")
    t["vocab"] = vocab
    t["sources"]["classification_vocabulary"] = {"file": CHART, "lines": f"L{vline}", "count": len(vocab)}
    try:
        claims = json.loads(tree.read(CLAIMS))
    except ValueError as exc:
        raise BadInput("CLAIMS_JSON_INVALID", "MASTER_CLAIMS_IS_JSON", f"{CLAIMS}: {exc}")
    lims, cl_lines = {}, {}
    raw_lines = tree.read(CLAIMS).splitlines()
    for c in claims.get("claims", []):
        if c.get("claim_id") in CLAIM_IDS:
            lims[c["claim_id"]] = [x.get("limitation_id") for x in c.get("limitations", [])]
            cl_lines[c["claim_id"]] = next((i for i, l in enumerate(raw_lines, 1)
                                            if f'"claim_id": "{c["claim_id"]}"' in l), None)
    if set(lims) != set(CLAIM_IDS) or not all(lims.values()):
        raise BadInput("CLAIM_LIMITATIONS_ABSENT", "PAT003_CLAIM_LIMITATIONS_IN_MASTER_CLAIMS",
                       f"{CLAIMS}: limitations for {', '.join(CLAIM_IDS)} not found")
    t["limitations"] = lims
    t["sources"]["limitations"] = {"file": CLAIMS, "lines": ", ".join(f"{k} L{v}" for k, v in sorted(cl_lines.items())),
                                   "count": sum(len(v) for v in lims.values())}
    fam = {f.get("family_id") for f in claims.get("families", []) if f.get("family_id")}
    pa = tree.read(PA_IDS)
    if pa:
        try:
            fam |= set(json.loads(pa).get("families", {}).keys())
        except ValueError:
            pass
    t["family_ids"] = sorted(fam)
    t["sources"]["family_ids"] = {"file": f"{CLAIMS} families[].family_id; {PA_IDS} families", "count": len(fam)}
    head = None
    for i, l in enumerate(tree.read(PAT005_AUDIT).splitlines(), 1):
        if l.startswith("| Event ID |"):
            head = (i, [c.replace("PAT-005", "PAT-003") for c in cells(l)])
            break
    if not head:
        raise BadInput("TEMPLATE_REGISTER_HEADER_ABSENT", "FIELD_LIST_READ_FROM_EXISTING_TEMPLATE",
                       f"{PAT005_AUDIT}: no '| Event ID |' disclosure register header")
    t["register_columns"] = head[1]
    t["sources"]["disclosure_register_columns"] = {"file": PAT005_AUDIT, "lines": f"L{head[0]}",
                                                   "count": len(head[1]), "family_substitution": "PAT-005->PAT-003"}
    t["sources"]["anchor_fields"] = {"file": "tools/validate_pat005_implementation_anchors.py", "lines": "L52-L83",
                                     "fields": ["repository", "commit", "path", "blob_sha", "anchor_type", "supports"]}
    t["sources"]["evidence_map_columns"] = {"file": "FE-1 predicate; StegVerse-Labs/Patents#21 @63be4ccf " + CHART,
                                           "lines": "L82", "fields": MAP_COLUMNS}
    return t


# ---------------------------------------------------------------- FE
def evidence_map(tree: Tree) -> Optional[dict]:
    text = tree.read(CHART)
    lines = text.splitlines()
    secs = section(lines, "Evidence map")
    if not secs:
        return None
    start, body = secs[-1]
    sub = {}
    cur = None
    for i, l in body:
        if l.startswith("### "):
            cur = l[4:].strip()
            sub[cur] = []
        elif cur is not None:
            sub[cur].append((i, l))
    return {"heading_line": start, "section_count": len(secs), "body": body, "sub": sub, "all_lines": lines}


def public_labels(em: dict) -> Dict[str, dict]:
    out = {}
    for name, body in em["sub"].items():
        if not name.lower().startswith("public locators"):
            continue
        for i, l in body:
            m = re.match(r"^- \*\*([A-Za-z0-9 ]+?):\*\*\s*(.*)$", l)
            if m:
                label, rest = m.group(1).strip(), m.group(2)
                lab = label.split()[0]
                out[lab] = {"line": i, "label": label, "text": rest}
    return out


def pointer_rows(em: dict) -> Tuple[Optional[List[str]], List[Tuple[int, List[str]]]]:
    for name, body in em["sub"].items():
        if name.lower().startswith("private pointers"):
            tb = tables(body)
            if tb:
                return tb[0][1], tb[0][2]
            return None, []
    return None, []


def classify_hash(h: str, loc: str, labels: Dict[str, dict], ptrs: set) -> Optional[str]:
    hn = norm(h)
    if HEX40.search(h) or HEX64.search(h) or re.search(r"\b[0-9a-f]{7,}…", h):
        return "DIGEST"
    if hn in {"not computed", "not_computed"}:
        return "NOT_COMPUTED"
    if hn in {"—", "-", "–"} and norm(loc).startswith("none"):
        return "NONE_LOCATED"
    if re.fullmatch(r"see pointers?", hn):
        return "POINTER" if POINTER_ID.search(loc) else None
    if hn == "as above":
        segs = [s.strip() for s in loc.split(";") if s.strip()]
        ok = segs and all((s.split()[0] in labels) or POINTER_ID.fullmatch(s.split()[0]) for s in segs)
        return "LOCATOR_REFERENCE" if ok else None
    parts = [p.strip() for p in re.split(r";", h) if p.strip()]
    if parts:
        ok = True
        for p in parts:
            m = re.fullmatch(r"([A-Za-z0-9/]+) (hash|blob|commit|commits) above", p)
            if m:
                if not all(x in labels for x in m.group(1).split("/")):
                    ok = False
            elif not (HEX40.search(p) or HEX64.search(p) or re.search(r"[0-9a-f]{7,}…", p)):
                ok = False
        if ok:
            return "LOCATOR_REFERENCE"
    return None


def fe1(tree: Tree, t: dict, em: Optional[dict]) -> dict:
    if em is None:
        return {"status": NOT_MET, "checks": [chk("FE-1.section", NOT_MET,
                f"{CHART} has no '## Evidence map' section at this tree")]}
    checks = []
    labels = public_labels(em)
    _, prow = pointer_rows(em)
    ptrs = {r[0] for _, r in prow if r}
    lines_found = 0
    vocab = set(t["vocab"])
    for claim in CLAIM_IDS:
        sub = next((b for n, b in em["sub"].items() if claim in n), None)
        if sub is None:
            checks.append(chk(f"FE-1.{claim}.table", NOT_MET, f"no '### ... {claim}' subsection"))
            continue
        tb = [x for x in tables(sub) if [norm(c) for c in x[1]] == [norm(c) for c in MAP_COLUMNS]]
        if len(tb) != 1:
            checks.append(chk(f"FE-1.{claim}.table", NOT_MET,
                              f"expected exactly one table with columns {MAP_COLUMNS}, found {len(tb)}"))
            continue
        rows = tb[0][2]
        by_lim: Dict[str, Dict[str, List[Tuple[int, List[str]]]]] = {}
        for ln, r in rows:
            if len(r) != len(MAP_COLUMNS):
                checks.append(chk(f"FE-1.{claim}.L{ln}", NOT_MET, f"line has {len(r)} cells, expected 6", line=ln))
                continue
            by_lim.setdefault(r[0], {}).setdefault(norm(r[1]), []).append((ln, r))
        expected = t["limitations"][claim]
        extra = sorted(set(by_lim) - set(expected))
        if extra:
            checks.append(chk(f"FE-1.{claim}.extra", NOT_MET, f"limitations not in {CLAIMS}: {extra}"))
        for lim in expected:
            got = by_lim.get(lim, {})
            for cls in EVIDENCE_CLASSES + ("proposed class",):
                cid = f"FE-1.{claim}.{lim}.{cls.replace(' ', '_')}"
                entries = got.get(cls, [])
                if len(entries) != 1:
                    checks.append(chk(cid, NOT_MET, f"expected exactly 1 line, found {len(entries)}"))
                    continue
                ln, r = entries[0]
                _, _, loc, h, cond, status = r
                problems = []
                if cls == "proposed class":
                    terms = BACKTICK.findall(status)
                    if not terms or not all(x in vocab for x in terms):
                        problems.append(f"proposed class terms {terms} not all in {sorted(vocab)}")
                    if "CANDIDATE_NOT_ADMITTED" not in status:
                        problems.append("proposed class line does not carry CANDIDATE_NOT_ADMITTED")
                else:
                    lines_found += 1
                    if norm(loc) in {"", "—", "-"}:
                        problems.append("empty locator")
                    if classify_hash(h, loc, labels, ptrs) is None:
                        problems.append(f"hash cell {h!r} is not a digest, pointer, locator reference, NOT_COMPUTED or none-located")
                    absent = norm(status).startswith("absent")
                    if norm(cond) in {"", "—", "-"} and not absent:
                        problems.append("empty conditions (allowed only when status is ABSENT)")
                    if norm(status) in {"", "—", "-"}:
                        problems.append("empty status")
                if re.search(r"(?<!NOT_)\bADMITTED\b", status):
                    problems.append("status claims ADMITTED")
                checks.append(chk(cid, NOT_MET if problems else MET, "; ".join(problems) or "structurally complete", line=ln))
    # original chart rows stay CANDIDATE_NOT_ADMITTED
    bad = []
    pre = [(i, l) for i, l in enumerate(em["all_lines"], 1) if i < em["heading_line"]]
    for _, head, rows in tables(pre):
        if head and norm(head[-1]) == "classification":
            bad += [ln for ln, r in rows if r[-1] != "CANDIDATE_NOT_ADMITTED"]
    checks.append(chk("FE-1.original_rows_not_admitted", NOT_MET if bad else MET,
                      f"rows not CANDIDATE_NOT_ADMITTED at lines {bad}" if bad else "all original rows CANDIDATE_NOT_ADMITTED"))
    want = 3 * sum(len(v) for v in t["limitations"].values())
    checks.append(chk("FE-1.line_count", MET if lines_found == want else NOT_MET,
                      f"{lines_found} evidence-class lines parsed; expected {want}"))
    return {"status": rollup(checks), "checks": checks, "section_heading_line": em["heading_line"],
            "evidence_map_section_count": em["section_count"]}


def resolve_obj(stores: Dict[str, Store], repo: str, sha: str, kind: str) -> Tuple[str, str]:
    st = stores.get(repo)
    if st is None or not st.usable:
        return UNKNOWN, f"no local object store for {repo}"
    typ = st.obj_type(sha)
    if typ is None:
        return (UNKNOWN, f"{sha[:12]} absent from shallow store for {repo}") if st.shallow else \
               (NOT_MET, f"{sha[:12]} not found in local store for {repo}")
    if kind and typ != kind:
        return NOT_MET, f"{sha[:12]} is a {typ}, expected {kind}"
    return MET, f"{sha[:12]} resolves as {typ} in {repo}"


def fe2(tree: Tree, t: dict, em: Optional[dict], stores: Dict[str, Store]) -> dict:
    if em is None:
        return {"status": NOT_MET, "checks": [chk("FE-2.section", NOT_MET, f"{CHART} has no evidence-map section")]}
    checks = []
    labels = public_labels(em)
    if not labels:
        checks.append(chk("FE-2.public_locators", NOT_MET, "no '### Public locators' bullet list"))
    attributed = set()
    for lab, info in sorted(labels.items()):
        txt = info["text"]
        if "this repository" in txt:
            repo = THIS_REPO
        else:
            m = REPO_NAME.search(txt)
            repo = m.group(1) if m else None
        hexes = HEX40.findall(txt)
        if not hexes:
            continue
        if repo is None:
            checks.append(chk(f"FE-2.{lab}", NOT_MET, "40-hex identifier without a named repository", line=info["line"]))
            continue
        blobs = set(re.findall(r"blob `([0-9a-f]{40})`", txt))
        commits = [h for h in hexes if h not in blobs]
        for h in hexes:
            attributed.add(h)
            st, d = resolve_obj(stores, repo, h, "blob" if h in blobs else "commit")
            checks.append(chk(f"FE-2.{lab}.{h[:12]}", st, d, line=info["line"], repository=repo))
        paths = [p for p in BACKTICK.findall(txt) if "/" in p and "*" not in p and not HEX40.fullmatch(p)]
        for p in paths:
            for c in commits:
                s = stores.get(repo)
                if s is None or not s.usable:
                    checks.append(chk(f"FE-2.{lab}.path", UNKNOWN, f"no local store for {repo} to resolve {p}", line=info["line"]))
                    continue
                b = s.blob_at(c, p)
                if b is None:
                    checks.append(chk(f"FE-2.{lab}.path", UNKNOWN if s.shallow else NOT_MET,
                                      f"{p} not found at {c[:12]}", line=info["line"]))
                elif blobs and b not in blobs:
                    checks.append(chk(f"FE-2.{lab}.path", NOT_MET, f"{p}@{c[:12]} is blob {b[:12]}, not the named blob", line=info["line"]))
                else:
                    checks.append(chk(f"FE-2.{lab}.path", MET, f"{p}@{c[:12]} resolves" + (" to the named blob" if blobs else ""), line=info["line"]))
    for i, l in em["body"]:
        for h in HEX40.findall(l):
            if h not in attributed and not HEX64.search(l[max(0, l.find(h) - 24):l.find(h) + 64]):
                checks.append(chk(f"FE-2.unattributed.{h[:12]}", UNKNOWN, "40-hex identifier not tied to a public-locator bullet", line=i))
                attributed.add(h)
    head, prow = pointer_rows(em)
    if head is None or [norm(c) for c in head] != [norm(c) for c in POINTER_COLUMNS]:
        checks.append(chk("FE-2.private_pointer_table", NOT_MET, f"no private-pointer table with columns {POINTER_COLUMNS}"))
        prow = []
    defined = set()
    for ln, r in prow:
        if len(r) != len(POINTER_COLUMNS):
            checks.append(chk(f"FE-2.pointer.L{ln}", NOT_MET, "wrong cell count", line=ln))
            continue
        pid, kind, ids, sha, note = r
        defined.add(pid)
        problems = []
        if not re.fullmatch(r"(?:PRIV|KV)-\d+", pid):
            problems.append(f"pointer id {pid!r} not PRIV-n/KV-n")
        dids = BACKTICK.findall(ids)
        if not dids or not all(DRIVE_ID.fullmatch(x) for x in dids):
            problems.append("Drive file id cell is not one or more backticked Drive ids")
        shas = BACKTICK.findall(sha)
        if not (shas and len(shas) == len(dids) and all(re.fullmatch(r"[0-9a-f]{64}", x) for x in shas)):
            problems.append("SHA-256 cell is not one 64-hex digest per Drive id" +
                            (" (explicit NOT COMPUTED)" if "not computed" in sha.lower() else ""))
        if len(kind) > 120 or len(note) > 200 or "```" in kind + note:
            problems.append("kind/note exceed the opaque-pointer length bound (possible content)")
        checks.append(chk(f"FE-2.pointer.{pid}", NOT_MET if problems else MET,
                          "; ".join(problems) or "Drive id plus 64-hex SHA-256 only", line=ln))
    used = set()
    for n, body in em["sub"].items():
        if any(c in n for c in CLAIM_IDS):
            for i, l in body:
                used |= set(POINTER_ID.findall(l))
    undefined = sorted(used - defined)
    checks.append(chk("FE-2.pointers_defined", NOT_MET if undefined else MET,
                      f"pointers used but not defined: {undefined}" if undefined else f"{len(used)} pointers used, all defined"))
    return {"status": rollup(checks), "checks": checks}


def fe3(tree: Tree, t: dict, em: Optional[dict], stores: Dict[str, Store]) -> dict:
    rows = set(FE3_ROWS)
    if em is not None:
        for claim in CLAIM_IDS:
            sub = next((b for n, b in em["sub"].items() if claim in n), [])
            for _, head, trows in tables(sub):
                for _, r in trows:
                    if len(r) == 6 and norm(r[1]) == "proposed class" and "implemented" in BACKTICK.findall(r[5]):
                        rows.add((claim, r[0]))
    raw = tree.read(ANCHORS)
    if raw is None:
        return {"status": NOT_MET, "target_rows": sorted(f"{c}:{l}" for c, l in rows),
                "checks": [chk("FE-3.anchors_file", NOT_MET, f"{ANCHORS} absent at this tree")]}
    try:
        data = json.loads(raw)
    except ValueError as exc:
        return {"status": NOT_MET, "checks": [chk("FE-3.anchors_file", NOT_MET, f"{ANCHORS} is not JSON: {exc}")]}
    checks = []
    anchors = data.get("anchors") if isinstance(data, dict) else None
    if data.get("family_id") != "PAT-003" if isinstance(data, dict) else True:
        checks.append(chk("FE-3.family_id", NOT_MET, "family_id must be PAT-003"))
    if not isinstance(anchors, list) or not anchors:
        checks.append(chk("FE-3.anchors", NOT_MET, "anchors must be a non-empty array"))
        anchors = []
    cover: Dict[Tuple[str, str], set] = {r: set() for r in rows}
    for k, a in enumerate(anchors):
        cid = f"FE-3.anchor[{k}]"
        problems = []
        if not isinstance(a, dict):
            checks.append(chk(cid, NOT_MET, "anchor must be an object"))
            continue
        repo, commit, path, blob = a.get("repository"), str(a.get("commit", "")), a.get("path"), str(a.get("blob_sha", ""))
        if not isinstance(repo, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            problems.append("repository invalid")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            problems.append("commit is not an immutable 40-hex commit")
        if not isinstance(path, str) or not path:
            problems.append("path missing")
        if not re.fullmatch(r"[0-9a-f]{40}", blob):
            problems.append("blob_sha invalid")
        if a.get("anchor_type") not in ANCHOR_TYPES:
            problems.append("anchor_type invalid")
        sup = a.get("supports")
        if not isinstance(sup, list) or not sup:
            problems.append("supports missing")
            sup = []
        status = NOT_MET if problems else MET
        detail = "; ".join(problems)
        if not problems:
            s = stores.get(repo)
            if s is None or not s.usable:
                status, detail = UNKNOWN, f"no local object store for {repo}"
            else:
                b = s.blob_at(commit, path)
                if b is None:
                    status, detail = (UNKNOWN if s.shallow else NOT_MET), f"{path} not found at {commit[:12]}"
                elif b != blob:
                    status, detail = NOT_MET, f"{path}@{commit[:12]} is blob {b[:12]}, not {blob[:12]}"
                else:
                    detail = f"{path}@{commit[:12]} resolves to blob_sha"
        checks.append(chk(cid, status, detail or "ok"))
        for r in rows:
            if f"{r[0]}:{r[1]}" in sup:
                cover[r].add((status, a.get("anchor_type")))
    for r, got in sorted(cover.items()):
        cid = f"FE-3.{r[0]}.{r[1]}"
        good = {ty for st, ty in got if st == MET}
        unk = {ty for st, ty in got if st == UNKNOWN}
        if good & EXECUTABLE_TYPES and "receipt" in good:
            checks.append(chk(cid, MET, "resolved test/executable anchor and retained-output receipt anchor"))
        elif (good | unk) & EXECUTABLE_TYPES and "receipt" in (good | unk):
            checks.append(chk(cid, UNKNOWN, "anchors present but not all resolvable offline"))
        else:
            checks.append(chk(cid, NOT_MET, f"needs an executable/test anchor and a receipt anchor whose supports lists '{r[0]}:{r[1]}' (index L75: test and retained output)"))
    return {"status": rollup(checks), "checks": checks, "target_rows": sorted(f"{c}:{l}" for c, l in rows),
            "row_binding": "supports[] entry '<claim_id>:<limitation_id>'"}


# ---------------------------------------------------------------- FC
def chrono_sources(tree: Tree) -> List[str]:
    return [CHRONO] + [p for p in tree.files() if p.startswith(CHRONO_DIR) and p.endswith(".md")]


def fc1(tree: Tree, t: dict) -> dict:
    fields = t["chrono_fields"]
    classes = {norm(c): c for c in t["event_classes"]}
    checks, covered, n = [], set(), 0
    for src in chrono_sources(tree):
        text = tree.read(src) or ""
        body = list(enumerate(text.splitlines(), 1))
        for ln, rec in kv_records(fenced_blocks(body), fields[0]):
            n += 1
            problems = []
            missing = [f for f in fields if not rec.get(f)]
            if missing:
                problems.append(f"missing fields {missing}")
            rtype = norm(rec.get("record_type", "")).replace("_", " ")
            if rtype not in classes:
                problems.append(f"record_type {rec.get('record_type')!r} is not one of {t['event_classes']}")
            unverified = rec.get("verification_status", "").strip().upper() == "UNVERIFIED"
            date = rec.get("exact_date_or_datetime", "")
            if date.lower() == "unknown":
                if not unverified:
                    problems.append("date unknown but verification_status is not UNVERIFIED")
            elif not ISO.fullmatch(date):
                problems.append(f"exact_date_or_datetime {date!r} not ISO-8601")
            for f in ("source_repository_or_location", "exact_path_or_document_identifier"):
                if rec.get(f, "").lower() == "unknown" and not unverified:
                    problems.append(f"{f} unknown but not UNVERIFIED")
            h = rec.get("commit_blob_or_content_hash", "")
            if h.lower() == "unknown":
                if not unverified:
                    problems.append("hash unknown but not UNVERIFIED")
            elif not re.fullmatch(r"(?:sha256:)?[0-9a-f]{7,64}", h):
                problems.append("commit_blob_or_content_hash not a commit, blob or hash")
            if not problems and rtype in classes:
                covered.add(rtype)
            checks.append(chk(f"FC-1.{src}:L{ln}", NOT_MET if problems else MET, "; ".join(problems) or "record complete", line=ln))
    missing_classes = [classes[c] for c in classes if c not in covered]
    checks.append(chk("FC-1.event_class_coverage", NOT_MET if missing_classes else MET,
                      f"{n} records; event classes without a valid record: {missing_classes}" if missing_classes else f"{n} records; all {len(classes)} event classes covered"))
    return {"status": rollup(checks), "checks": checks, "record_count": n}


def fc2(tree: Tree, t: dict) -> dict:
    text = tree.read(AUDIT)
    if text is None:
        return {"status": NOT_MET, "checks": [chk("FC-2.audit_file", NOT_MET, f"{AUDIT} absent at this tree")]}
    body = list(enumerate(text.splitlines(), 1))
    want = [norm(c) for c in t["register_columns"]]
    tb = [x for x in tables(body) if [norm(c) for c in x[1]] == want]
    if not tb:
        return {"status": NOT_MET, "checks": [chk("FC-2.register", NOT_MET, f"no disclosure register with columns {t['register_columns']}")]}
    checks, named = [], []
    cols = t["register_columns"]
    ix = {norm(c): k for k, c in enumerate(cols)}
    rows = [r for x in tb for r in x[2]]
    if not rows:
        checks.append(chk("FC-2.rows", NOT_MET, "register has no rows"))
    for ln, r in rows:
        if len(r) != len(cols):
            checks.append(chk(f"FC-2.L{ln}", NOT_MET, "wrong cell count", line=ln))
            continue
        problems = []
        date = r[ix["date and exact time"]]
        m = ISO_PREFIX.match(date)
        if not m:
            problems.append("date does not start with an ISO-8601 date")
        ident = r[ix["immutable identifier"]] + " " + r[ix["platform or location"]]
        commits = HEX40.findall(ident)
        if not commits and "https://" not in ident:
            problems.append("no 40-hex commit or URL")
        paths = [p for p in BACKTICK.findall(r[ix["immutable identifier"]]) if "/" in p or "." in p]
        local = THIS_REPO in r[ix["platform or location"]]
        status = NOT_MET if problems else MET
        detail = "; ".join(problems) or "row well-formed"
        if not problems and local:
            named += paths
            for c in commits:
                if tree.store.obj_type(c) is None:
                    status, detail = (UNKNOWN if (not tree.store.usable or tree.store.shallow) else NOT_MET), f"commit {c[:12]} not resolvable locally"
            for p in paths:
                fd = tree.store.first_add_date(tree.rev or "HEAD", p.rstrip("/"))
                if fd is None:
                    status, detail = (UNKNOWN if status != NOT_MET else status), f"first-add date of {p} not computable offline"
                elif m and fd != m.group(1) and status != NOT_MET:
                    status, detail = NOT_MET, f"{p} first added {fd}, row says {m.group(1)}"
        checks.append(chk(f"FC-2.{r[0] or ln}", status, detail, line=ln))
    surfaces = [p for p in tree.files() if re.search(r"pat-?003", p, re.I) and p != AUDIT]
    uncovered = [p for p in surfaces if not any(p == q or (q.endswith("/") and p.startswith(q)) for q in named)]
    checks.append(chk("FC-2.local_surface_coverage", NOT_MET if uncovered else MET,
                      f"{len(uncovered)} of {len(surfaces)} PAT-003 paths in this repository not named: {uncovered[:20]}" if uncovered
                      else f"all {len(surfaces)} PAT-003 paths in this repository named"))
    return {"status": rollup(checks), "checks": checks}


# ---------------------------------------------------------------- FP
def ledger_records(tree: Tree, t: dict) -> Tuple[List[Tuple[int, Dict[str, str]]], bool]:
    lines = tree.read(LEDGER).splitlines()
    secs = section(lines, "Current verified references")
    if not secs:
        return [], False
    return kv_records(fenced_blocks(secs[0][1]), t["search_fields"][0]), True


def fp1(tree: Tree, t: dict) -> dict:
    recs, present = ledger_records(tree, t)
    checks = []
    if not present:
        checks.append(chk("FP-1.section", NOT_MET, "no '## Current verified references' section"))
    for ln, rec in recs:
        problems = []
        missing = [f for f in t["search_fields"] if not rec.get(f)]
        if missing:
            problems.append(f"missing fields {missing}")
        for f in ("search_query", "source_url_or_database"):
            if rec.get(f, "").lower() in {"unknown", "none", "tbd"}:
                problems.append(f"{f} not recorded verbatim")
        if not ISO.fullmatch(rec.get("retrieval_date", "")):
            problems.append("retrieval_date not ISO-8601")
        if rec.get("legal_review_status") != "NOT_REVIEWED":
            problems.append("legal_review_status must be NOT_REVIEWED")
        checks.append(chk(f"FP-1.{rec.get('reference_id') or ln}", NOT_MET if problems else MET, "; ".join(problems) or "record complete", line=ln))
    checks.append(chk("FP-1.count", MET if recs else NOT_MET, f"N = {len(recs)} records (N >= 1 required)"))
    return {"status": rollup(checks), "checks": checks, "record_count": len(recs)}


def fp2(tree: Tree, t: dict) -> dict:
    recs, _ = ledger_records(tree, t)
    refs = {r.get("reference_id") for _, r in recs if r.get("reference_id")}
    body = list(enumerate(tree.read(LEDGER).splitlines(), 1))
    tb = [x for x in tables(body) if [norm(c) for c in x[1]] == OVERLAP_COLUMNS]
    if not tb:
        return {"status": NOT_MET, "checks": [chk("FP-2.overlap_map", NOT_MET, f"no overlap table with columns {OVERLAP_COLUMNS} in {LEDGER}")]}
    checks, seen = [], set()
    fams = set(t["family_ids"])
    for ln, r in [row for x in tb for row in x[2]]:
        problems = []
        if len(r) != len(OVERLAP_COLUMNS):
            checks.append(chk(f"FP-2.L{ln}", NOT_MET, "wrong cell count", line=ln))
            continue
        ref, fam = r[0].strip("`"), r[1].strip("`")
        if ref not in refs:
            problems.append(f"reference_id {ref!r} not an FP-1 record")
        if fam not in fams:
            problems.append(f"family_id {fam!r} not in {sorted(fams)}")
        if not problems:
            seen.add(ref)
        checks.append(chk(f"FP-2.L{ln}", NOT_MET if problems else MET, "; ".join(problems) or "row valid", line=ln))
    missing = sorted(refs - seen)
    checks.append(chk("FP-2.reference_coverage", NOT_MET if (missing or not refs) else MET,
                      f"references without an overlap row: {missing}" if refs else "no FP-1 references to map"))
    return {"status": rollup(checks), "checks": checks}


# ---------------------------------------------------------------- human dependencies
def human_actions(tree: Tree, requested: List[str]) -> List[dict]:
    lines = tree.read(INDEX).splitlines()
    rule = next((i for i, l in enumerate(lines, 1) if "Only the owning human or practitioner can check off" in l), None)
    out = []
    for prefix, pts, cite in HUMAN:
        if not set(pts) & set(requested):
            continue
        ln = next((i for i, l in enumerate(lines, 1) if re.match(r"^\s*- \[[ xX]\]\s+" + re.escape(prefix), l)), None)
        out.append({"dependency": cite, "index_line": ln, "rule_line": rule, "finish_points": list(pts),
                    "class": "C", "status": "HUMAN_ACTION_REQUIRED",
                    "evaluated_by_tool": False,
                    "note": "owner/practitioner check-off; reported only, never evaluated as met"})
    if set(requested) & {"FC-1", "FC-2"}:
        out.append({"dependency": f"{CHRONO} Public disclosure: enablement assessment and foreign-filing consequence (requires counsel)",
                    "index_line": None, "rule_line": rule, "finish_points": ["FC-1", "FC-2"], "class": "C",
                    "status": "HUMAN_ACTION_REQUIRED", "evaluated_by_tool": False, "note": "counsel"})
    if set(requested) & {"FP-1", "FP-2"}:
        out.append({"dependency": "practitioner evaluation (PAT-003-FILING-PACKET)", "index_line": None, "rule_line": rule,
                    "finish_points": ["FP-1", "FP-2"], "class": "C", "status": "HUMAN_ACTION_REQUIRED",
                    "evaluated_by_tool": False, "note": "practitioner"})
    return out


# ---------------------------------------------------------------- main
def verify(tree: Tree, requested: List[str], stores: Dict[str, Store]) -> dict:
    t = load_templates(tree)
    em = evidence_map(tree)
    fn = {"FE-1": lambda: fe1(tree, t, em), "FE-2": lambda: fe2(tree, t, em, stores),
          "FE-3": lambda: fe3(tree, t, em, stores), "FC-1": lambda: fc1(tree, t),
          "FC-2": lambda: fc2(tree, t), "FP-1": lambda: fp1(tree, t), "FP-2": lambda: fp2(tree, t)}
    results = {}
    for p in requested:
        r = fn[p]()
        r["task"] = TASK_OF[p]
        results[p] = r
    all_met = all(results[p]["status"] == MET for p in requested)
    return {
        "schema": SCHEMA,
        "operating_mode": "E0",
        "llm_used": False,
        "authority_effect": "NONE_EVIDENCE_INPUT_ONLY",
        "boundary": "not truth, not legal determination, not execution authority",
        "furthest_reachable_state": "EVIDENCE_COMPLETE_INPUTS_TO_READY_FOR_FILING_REVIEW",
        "rows_admission_state": "CANDIDATE_NOT_ADMITTED",
        "predicate_source": PREDICATE_SOURCE,
        "tree": tree.identity,
        "requested_points": requested,
        "disposition": "ALL_REQUESTED_POINTS_MET" if all_met else "REQUESTED_POINTS_NOT_ALL_MET",
        "summary": {p: results[p]["status"] for p in requested},
        "results": results,
        "human_action_dependencies": human_actions(tree, requested),
        "field_sources": t["sources"],
        "object_stores": {k: {"usable": v.usable, "shallow": v.shallow} for k, v in sorted(stores.items())},
        "files_read": tree.read_manifest(),
    }


def parse_args(argv: List[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", help="repository working tree to check")
    ap.add_argument("--git-dir", help="local git repository to read --rev from")
    ap.add_argument("--rev", help="commit/ref to check (with --git-dir)")
    ap.add_argument("--points", default=",".join(POINTS), help="comma-separated subset of " + ",".join(POINTS))
    ap.add_argument("--object-store", action="append", default=[], metavar="OWNER/REPO=PATH",
                    help="local git clone used to resolve objects of another repository (offline)")
    return ap.parse_args(argv)


def run(argv: List[str]) -> Tuple[dict, int]:
    try:
        try:
            a = parse_args(argv)
        except SystemExit:
            raise BadInput("ARGUMENTS_INVALID", "ARGUMENTS_PARSE", "see --help")
        if bool(a.git_dir) == bool(a.root) or (a.git_dir and not a.rev) or (a.rev and not a.git_dir):
            raise BadInput("TREE_SELECTOR_INVALID", "EXACTLY_ONE_OF_ROOT_OR_GIT_DIR_WITH_REV",
                           "pass either --root DIR, or --git-dir DIR --rev REV")
        req = [p.strip() for p in a.points.split(",") if p.strip()]
        bad = [p for p in req if p not in POINTS]
        if not req or bad or len(set(req)) != len(req):
            raise BadInput("FINISH_POINT_UNKNOWN", "REQUESTED_POINTS_ARE_KNOWN_AND_UNIQUE",
                           f"unknown/duplicate points {bad or req}; allowed {list(POINTS)}")
        req = [p for p in POINTS if p in req]
        tree = Tree(a.root, a.git_dir, a.rev)
        stores = {THIS_REPO: tree.store}
        for spec in a.object_store:
            if "=" not in spec:
                raise BadInput("OBJECT_STORE_SPEC_INVALID", "OBJECT_STORE_IS_OWNER_REPO_EQUALS_PATH", f"bad --object-store {spec!r}")
            k, v = spec.split("=", 1)
            if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", k) or not os.path.isdir(v):
                raise BadInput("OBJECT_STORE_SPEC_INVALID", "OBJECT_STORE_IS_OWNER_REPO_EQUALS_PATH", f"bad --object-store {spec!r}")
            stores[k] = Store(v)
        out = verify(tree, req, stores)
        return out, 0 if out["disposition"] == "ALL_REQUESTED_POINTS_MET" else 2
    except BadInput as exc:
        return fail_closed(exc), 3


def main(argv: Optional[List[str]] = None) -> int:
    out, code = run(sys.argv[1:] if argv is None else argv)
    sys.stdout.write(json.dumps(out, indent=2, sort_keys=True) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
