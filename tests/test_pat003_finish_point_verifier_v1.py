"""Tests for the PAT-003 finish-point structural verifier (stdlib unittest, E0).

Fixtures copy the existing Patents templates (so field lists come from the real files) and
add synthetic, non-enabling placeholder records only. Mutation-negative cases check that
each predicate fails closed.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "research", "pat003"))
import finish_point_verifier_v1 as V  # noqa: E402

TEMPLATES = list(V.REQUIRED_TEMPLATES) + [V.PA_IDS]
GIT_ENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.invalid",
               GIT_AUTHOR_DATE="2026-01-02T03:04:05Z", GIT_COMMITTER_DATE="2026-01-02T03:04:05Z")
DRIVE = "1" + "A" * 32
SHA = "a" * 64


def git(d, *a):
    return subprocess.run(["git", "-C", d, *a], check=True, env=GIT_ENV,
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode().strip()


def run(*argv):
    out, code = V.run(list(argv))
    return out, code


class Fixture:
    def __init__(self):
        self.d = tempfile.mkdtemp(prefix="fpv-")
        for p in TEMPLATES:
            os.makedirs(os.path.dirname(os.path.join(self.d, p)), exist_ok=True)
            shutil.copy(os.path.join(ROOT, p), os.path.join(self.d, p))
        self._make_hermetic()
        git(self.d, "init", "-q")
        self.commit("templates")
        self.base = git(self.d, "rev-parse", "HEAD")

    def _make_hermetic(self):
        """Do not depend on records the live repository has since appended to the copied templates.

        The tests assume the pristine template state: no evidence-map section in the limitation
        chart and no verified references in the research ledger. Both files are normalised after
        copying, so merging evidence or ledger appends into the live files cannot change results.
        """
        chart = os.path.join(self.d, V.CHART)
        with open(chart, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        kept, skipping = [], False
        for line in lines:
            if line.startswith("## "):
                skipping = line.startswith("## Evidence map")
            if not skipping:
                kept.append(line)
        with open(chart, "w", encoding="utf-8") as fh:
            fh.write("\n".join(kept).rstrip("\n") + "\n")
        ledger = os.path.join(self.d, V.LEDGER)
        with open(ledger, encoding="utf-8") as fh:
            s = fh.read()
        start = s.index("## Current verified references")
        end = s.index("## Unsupported conclusions")
        with open(ledger, "w", encoding="utf-8") as fh:
            fh.write(s[:start] + "## Current verified references\n" + "\n```text\nnone\n```\n" + "\n" + s[end:])

    def commit(self, msg):
        git(self.d, "add", "-A")
        git(self.d, "commit", "-q", "--allow-empty", "-m", msg)
        return git(self.d, "rev-parse", "HEAD")

    def path(self, p):
        return os.path.join(self.d, p)

    def read(self, p):
        with open(self.path(p), encoding="utf-8") as fh:
            return fh.read()

    def write(self, p, text):
        os.makedirs(os.path.dirname(self.path(p)), exist_ok=True)
        with open(self.path(p), "w", encoding="utf-8") as fh:
            fh.write(text)

    def append(self, p, text):
        self.write(p, self.read(p) + text)

    def replace(self, p, old, new, count=1):
        s = self.read(p)
        assert old in s, old
        self.write(p, s.replace(old, new, count))

    def verify(self, *points, extra=()):
        return run("--root", self.d, "--points", ",".join(points), *extra)


def evidence_map(base_commit, pointer_sha=SHA):
    lims = {"CLM-PAT-003-METHOD-001": ["L1", "L2", "L3", "L4", "L5", "L6"],
            "CLM-PAT-003-SYSTEM-001": ["L1", "L2", "L3", "L4"]}
    out = ["", "## Evidence map, appended (synthetic fixture) — rows NOT admitted", "",
           "### Private pointers (content not reproduced)", "",
           "| Pointer | Kind | Drive file id | SHA-256 (retrieved copy) | Note |", "|---|---|---|---|---|",
           f"| PRIV-1 | placeholder | `{DRIVE}` | `{pointer_sha}` | placeholder |", "",
           "### Public locators used", "",
           f"- **AA:** this repository `README.md` at `{base_commit}`.", ""]
    for claim, ls in lims.items():
        out += [f"### Claim {claim}", "", "| Lim. | Evidence class | Locator | Hash | Conditions | Status |",
                "|---|---|---|---|---|---|"]
        for lim in ls:
            implemented = (claim, lim) in V.FE3_ROWS
            out += [f"| {lim} | proofs | PRIV-1 | see pointer | placeholder condition | UNVERIFIED |",
                    f"| {lim} | software tests | AA | AA commit above | placeholder condition | TESTED_SYNTHETIC |",
                    f"| {lim} | physical measurements | none located | — | — | ABSENT |",
                    f"| {lim} | **proposed class** | — | — | — | `{'implemented' if implemented else 'proposed'}` (CANDIDATE_NOT_ADMITTED) |"]
        out.append("")
    return "\n".join(out) + "\n"


def chrono_record(rtype, date="2026-01-02", status="VERIFIED", h="abcdef1"):
    fields = {"record_id": f"R-{rtype.replace(' ', '-')}", "record_type": rtype, "exact_date_or_datetime": date,
              "timezone": "UTC", "actor_or_contributor": "placeholder", "actor_role": "placeholder",
              "source_repository_or_location": "StegVerse-Labs/Patents", "exact_path_or_document_identifier": "README.md",
              "commit_blob_or_content_hash": h, "confidentiality_or_access_state": "public",
              "technical_subject_matter": "placeholder", "limitations_or_figures_supported": "none",
              "corroborating_witness_or_record": "none", "correction_or_supersession_relationship": "none",
              "verification_status": status, "review_notes": "synthetic fixture"}
    return fields


def block(rec):
    return "\n```text\n" + "\n".join(f"{k}: {v}" for k, v in rec.items()) + "\n```\n"


CLASSES = ["Conception", "Written description", "Implementation", "Private disclosure", "Public disclosure", "Contributors"]


def ledger_record(**over):
    r = {"reference_id": "REF-1", "title": "placeholder", "publication_or_patent_number": "X-1",
         "publication_date": "2020-01-01", "priority_date_if_verified": "unknown",
         "source_url_or_database": "https://example.invalid/db", "retrieval_date": "2026-01-02",
         "search_query": "placeholder query", "technical_cluster": "placeholder",
         "relevant_passages_or_figures": "placeholder", "candidate_overlap": "placeholder",
         "candidate_distinction": "placeholder", "verification_status": "IDENTIFIER_VERIFIED",
         "reviewer": "placeholder", "legal_review_status": "NOT_REVIEWED"}
    r.update(over)
    return r


class FieldProvenance(unittest.TestCase):
    def test_field_lists_come_from_existing_templates(self):
        tree = V.Tree(ROOT, None, None)
        t = V.load_templates(tree)
        self.assertEqual(len(t["chrono_fields"]), 16)
        self.assertEqual(t["chrono_fields"][0], "record_id")
        self.assertEqual(len(t["search_fields"]), 15)
        self.assertEqual(t["search_fields"][-1], "legal_review_status")
        self.assertEqual(t["vocab"], ["implemented", "written_description_only", "proposed", "unsupported"])
        self.assertEqual(t["event_classes"], CLASSES)
        self.assertEqual(sum(len(v) for v in t["limitations"].values()), 10)
        self.assertEqual(len(t["register_columns"]), 11)
        for k, src in t["sources"].items():
            self.assertIn("file", src, k)

    def test_real_tree_never_fail_closed_and_statuses_closed_set(self):
        out, code = run("--root", ROOT)
        self.assertNotEqual(out.get("disposition"), "FAIL_CLOSED", out)
        self.assertIn(code, (0, 2))
        for p, st in out["summary"].items():
            self.assertIn(st, ("MET", "NOT_MET", "UNKNOWN"))


class Envelope(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        shutil.rmtree(self.f.d, ignore_errors=True)

    def test_envelope_and_no_filing_token(self):
        out, code = self.f.verify(*V.POINTS)
        self.assertEqual(code, 2)
        self.assertEqual(out["operating_mode"], "E0")
        self.assertFalse(out["llm_used"])
        self.assertEqual(out["authority_effect"], "NONE_EVIDENCE_INPUT_ONLY")
        self.assertNotIn("READY_TO_FILE", json.dumps(out))
        self.assertEqual(set(out["summary"].values()), {"NOT_MET"})

    def test_deterministic(self):
        a, _ = self.f.verify(*V.POINTS)
        b, _ = self.f.verify(*V.POINTS)
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))

    def test_human_checkoffs_reported_never_evaluated_even_if_checked(self):
        s = self.f.read(V.INDEX).replace("- [ ] ", "- [x] ")
        self.f.write(V.INDEX, s)
        out, code = self.f.verify(*V.POINTS)
        deps = out["human_action_dependencies"]
        self.assertEqual({d["dependency"] for d in deps if d["index_line"]},
                         {"index L75", "index L77", "index L78", "index L79", "index L82"})
        for d in deps:
            self.assertEqual(d["status"], "HUMAN_ACTION_REQUIRED")
            self.assertFalse(d["evaluated_by_tool"])
            self.assertEqual(d["class"], "C")
        self.assertEqual(code, 2)


class FailClosed(unittest.TestCase):
    def check(self, out, code, failure):
        self.assertEqual(code, 3)
        self.assertEqual(out["disposition"], "FAIL_CLOSED")
        self.assertEqual(out["failure_code"], failure)
        for k in ("failure_code", "failed_predicate", "required_evidence_or_repair", "retry_entrypoint",
                  "owning_existing_goal", "next_attempt"):
            self.assertTrue(out[k], k)
        self.assertEqual(len(out["seal_sha256"]), 64)

    def test_missing_root(self):
        self.check(*run("--root", "/nonexistent-fpv-root"), "ROOT_NOT_A_DIRECTORY")

    def test_unknown_point(self):
        self.check(*run("--root", ROOT, "--points", "FE-9"), "FINISH_POINT_UNKNOWN")

    def test_both_selectors(self):
        self.check(*run("--root", ROOT, "--git-dir", ROOT, "--rev", "HEAD"), "TREE_SELECTOR_INVALID")

    def test_bad_rev(self):
        f = Fixture()
        try:
            self.check(*run("--git-dir", f.d, "--rev", "0" * 40), "REV_NOT_RESOLVABLE")
        finally:
            shutil.rmtree(f.d, ignore_errors=True)

    def test_missing_template(self):
        f = Fixture()
        try:
            os.remove(f.path(V.CHRONO))
            self.check(*f.verify("FC-1"), "REQUIRED_TEMPLATE_ABSENT")
        finally:
            shutil.rmtree(f.d, ignore_errors=True)

    def test_template_field_block_removed(self):
        f = Fixture()
        try:
            f.replace(V.LEDGER, "## Search record fields", "## Search record fieldz")
            self.check(*f.verify("FP-1"), "TEMPLATE_FIELD_BLOCK_ABSENT")
        finally:
            shutil.rmtree(f.d, ignore_errors=True)


class FE(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()
        self.f.write("README.md", "placeholder\n")
        self.readme_commit = self.f.commit("readme")
        self.f.append(V.CHART, evidence_map(self.readme_commit))

    def tearDown(self):
        shutil.rmtree(self.f.d, ignore_errors=True)

    def test_fe1_met_and_exit_zero_for_subset(self):
        out, code = self.f.verify("FE-1")
        self.assertEqual(out["summary"], {"FE-1": "MET"}, json.dumps(out["results"], indent=1)[:3000])
        self.assertEqual(code, 0)

    def test_fe1_not_met_without_section(self):
        f = Fixture()
        try:
            out, code = f.verify("FE-1")
            self.assertEqual(out["summary"]["FE-1"], "NOT_MET")
            self.assertEqual(code, 2)
        finally:
            shutil.rmtree(f.d, ignore_errors=True)

    def mutate(self, old, new):
        self.f.replace(V.CHART, old, new)
        out, code = self.f.verify("FE-1")
        self.assertEqual(out["summary"]["FE-1"], "NOT_MET")
        self.assertEqual(code, 2)

    def test_fe1_missing_line(self):
        self.mutate("| L2 | software tests | AA | AA commit above | placeholder condition | TESTED_SYNTHETIC |\n", "")

    def test_fe1_duplicate_class(self):
        self.mutate("| L2 | proofs |", "| L2 | software tests |")

    def test_fe1_bad_vocabulary(self):
        self.mutate("`proposed` (CANDIDATE_NOT_ADMITTED)", "`maybe` (CANDIDATE_NOT_ADMITTED)")

    def test_fe1_proposed_without_not_admitted(self):
        self.mutate("`proposed` (CANDIDATE_NOT_ADMITTED)", "`proposed`")

    def test_fe1_admitted_status(self):
        self.mutate("| placeholder condition | UNVERIFIED |", "| placeholder condition | ADMITTED |")

    def test_fe1_empty_locator(self):
        self.mutate("| L1 | proofs | PRIV-1 |", "| L1 | proofs |  |")

    def test_fe1_bad_hash(self):
        self.mutate("| PRIV-1 | see pointer |", "| PRIV-1 | trust me |")

    def test_fe1_reference_to_undefined_label(self):
        self.mutate("| AA | AA commit above |", "| AA | ZZ commit above |")

    def test_fe1_empty_conditions_when_not_absent(self):
        self.mutate("| none located | — | — | ABSENT |", "| none located | — | — | UNVERIFIED |")

    def test_fe1_extra_limitation(self):
        self.mutate("| L6 | proofs |", "| L9 | proofs |")

    def test_fe1_original_row_admitted(self):
        self.mutate("| NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |", "| NOT VERIFIED | NOT RECORDED | ADMITTED |")

    def test_fe2_met_with_local_store(self):
        self.f.commit("map")
        out, code = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "MET", json.dumps(out["results"], indent=1)[:3000])

    def test_fe2_not_computed_pointer_not_met(self):
        self.f.replace(V.CHART, f"| `{SHA}` |", "| NOT COMPUTED |")
        out, _ = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "NOT_MET")

    def test_fe2_bad_drive_id_not_met(self):
        self.f.replace(V.CHART, f"`{DRIVE}`", "`short`")
        out, _ = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "NOT_MET")

    def test_fe2_long_note_not_met(self):
        self.f.replace(V.CHART, "| placeholder |\n", "| " + "x" * 300 + " |\n")
        out, _ = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "NOT_MET")

    def test_fe2_missing_object_not_met(self):
        self.f.replace(V.CHART, self.readme_commit, "b" * 40)
        out, _ = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "NOT_MET")

    def test_fe2_foreign_repo_without_store_unknown_and_exit_2(self):
        self.f.replace(V.CHART, "this repository `README.md`", "StegVerse-Labs/other `README.md`")
        out, code = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "UNKNOWN")
        self.assertEqual(code, 2)
        out, code = self.f.verify("FE-2", extra=("--object-store", f"StegVerse-Labs/other={self.f.d}"))
        self.assertEqual(out["summary"]["FE-2"], "MET")
        self.assertEqual(code, 0)

    def test_fe2_undefined_pointer_not_met(self):
        self.f.replace(V.CHART, "| L3 | proofs | PRIV-1 | see pointer |", "| L3 | proofs | PRIV-9 | see pointer |")
        out, _ = self.f.verify("FE-2")
        self.assertEqual(out["summary"]["FE-2"], "NOT_MET")

    def write_anchors(self, blob=None, supports_row=True, commit=None):
        b = blob or git(self.f.d, "rev-parse", f"{self.readme_commit}:README.md")
        c = commit or self.readme_commit
        anchors = []
        for claim, lim in V.FE3_ROWS:
            sup = [f"{claim}:{lim}"] if supports_row else ["placeholder"]
            anchors += [{"repository": "StegVerse-Labs/Patents", "commit": c, "path": "README.md", "blob_sha": b,
                         "anchor_type": "executable_validator", "supports": sup},
                        {"repository": "StegVerse-Labs/Patents", "commit": c, "path": "README.md", "blob_sha": b,
                         "anchor_type": "receipt", "supports": sup}]
        self.f.write(V.ANCHORS, json.dumps({"family_id": "PAT-003", "anchors": anchors}))

    def test_fe3_met(self):
        self.write_anchors()
        out, _ = self.f.verify("FE-3")
        self.assertEqual(out["summary"]["FE-3"], "MET", json.dumps(out["results"], indent=1)[:3000])

    def test_fe3_absent_not_met(self):
        out, _ = self.f.verify("FE-3")
        self.assertEqual(out["summary"]["FE-3"], "NOT_MET")

    def test_fe3_wrong_blob_not_met(self):
        self.write_anchors(blob="c" * 40)
        out, _ = self.f.verify("FE-3")
        self.assertEqual(out["summary"]["FE-3"], "NOT_MET")

    def test_fe3_mutable_ref_not_met(self):
        self.write_anchors(commit="main")
        out, _ = self.f.verify("FE-3")
        self.assertEqual(out["summary"]["FE-3"], "NOT_MET")

    def test_fe3_unbound_row_not_met(self):
        self.write_anchors(supports_row=False)
        out, _ = self.f.verify("FE-3")
        self.assertEqual(out["summary"]["FE-3"], "NOT_MET")

    def test_rev_mode_matches_tree_mode(self):
        rev = self.f.commit("map")
        a, _ = self.f.verify("FE-1")
        b, _ = run("--git-dir", self.f.d, "--rev", rev, "--points", "FE-1")
        self.assertEqual(a["summary"], b["summary"])
        self.assertEqual(b["tree"], {"mode": "git_rev", "commit": rev})


class FC(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        shutil.rmtree(self.f.d, ignore_errors=True)

    def add_records(self, recs):
        self.f.write(V.CHRONO_DIR + "records.md", "# synthetic\n" + "".join(block(r) for r in recs))

    def test_fc1_not_met_today_shape(self):
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "NOT_MET")
        self.assertEqual(out["results"]["FC-1"]["record_count"], 0)

    def test_fc1_met(self):
        self.add_records([chrono_record(c) for c in CLASSES])
        out, code = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "MET", json.dumps(out["results"], indent=1)[:2000])
        self.assertEqual(code, 0)

    def test_fc1_unknown_stays_unverified_ok(self):
        recs = [chrono_record(c) for c in CLASSES]
        recs[0] = chrono_record("Conception", date="unknown", status="UNVERIFIED", h="unknown")
        self.add_records(recs)
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "MET")

    def test_fc1_unknown_date_marked_verified_not_met(self):
        recs = [chrono_record(c) for c in CLASSES]
        recs[0] = chrono_record("Conception", date="unknown", status="VERIFIED")
        self.add_records(recs)
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "NOT_MET")

    def test_fc1_missing_field_not_met(self):
        recs = [chrono_record(c) for c in CLASSES]
        del recs[2]["actor_role"]
        self.add_records(recs)
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "NOT_MET")

    def test_fc1_non_iso_date_not_met(self):
        recs = [chrono_record(c) for c in CLASSES]
        recs[1] = chrono_record("Written description", date="July 2026")
        self.add_records(recs)
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "NOT_MET")

    def test_fc1_missing_class_not_met(self):
        self.add_records([chrono_record(c) for c in CLASSES[:-1]])
        out, _ = self.f.verify("FC-1")
        self.assertEqual(out["summary"]["FC-1"], "NOT_MET")

    def audit(self, rows):
        cols = V.load_templates(V.Tree(self.f.d, None, None))["register_columns"]
        lines = ["# PAT-003 Public Disclosure Audit (synthetic)", "", "## Disclosure event register", "",
                 "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        lines += ["| " + " | ".join(r) + " |" for r in rows]
        self.f.write(V.AUDIT, "\n".join(lines) + "\n")

    def row(self, date, commit, paths):
        ident = f"commit `{commit}`; " + "; ".join(f"`{p}`" for p in paths)
        return ["EV-1", date, "UTC", "placeholder", "`StegVerse-Labs/Patents`", ident, "n/a", "public",
                "unresolved", "placeholder", "UNVERIFIED"]

    def test_fc2_absent_not_met(self):
        out, _ = self.f.verify("FC-2")
        self.assertEqual(out["summary"]["FC-2"], "NOT_MET")

    def test_fc2_met_with_coverage_and_first_add_date(self):
        surfaces = [p for p in V.Tree(self.f.d, None, None).files() if "pat-003" in p.lower() or "pat003" in p.lower()]
        self.audit([self.row("2026-01-02", self.f.base, surfaces)])
        self.f.commit("audit")
        out, code = self.f.verify("FC-2")
        self.assertEqual(out["summary"]["FC-2"], "MET", json.dumps(out["results"], indent=1)[:2500])

    def test_fc2_wrong_first_date_not_met(self):
        surfaces = [p for p in V.Tree(self.f.d, None, None).files() if "pat-003" in p.lower() or "pat003" in p.lower()]
        self.audit([self.row("2025-12-31", self.f.base, surfaces)])
        self.f.commit("audit")
        out, _ = self.f.verify("FC-2")
        self.assertEqual(out["summary"]["FC-2"], "NOT_MET")

    def test_fc2_uncovered_surface_not_met(self):
        self.audit([self.row("2026-01-02", self.f.base, [V.CHART])])
        self.f.commit("audit")
        out, _ = self.f.verify("FC-2")
        self.assertEqual(out["summary"]["FC-2"], "NOT_MET")

    def test_fc2_bad_date_not_met(self):
        surfaces = [p for p in V.Tree(self.f.d, None, None).files() if "pat-003" in p.lower() or "pat003" in p.lower()]
        self.audit([self.row("sometime", self.f.base, surfaces)])
        self.f.commit("audit")
        out, _ = self.f.verify("FC-2")
        self.assertEqual(out["summary"]["FC-2"], "NOT_MET")


class FP(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def tearDown(self):
        shutil.rmtree(self.f.d, ignore_errors=True)

    def set_refs(self, recs, overlap_rows=None):
        body = "".join(block(r) for r in recs) if recs else "\n```text\nnone\n```\n"
        s = self.f.read(V.LEDGER)
        start = s.index("## Current verified references")
        end = s.index("## Unsupported conclusions")
        s = s[:start] + "## Current verified references\n" + body + "\n" + s[end:]
        if overlap_rows is not None:
            s += "\n## Overlap map (synthetic)\n\n| reference_id | family_id | mapped_limitations | candidate_overlap |\n|---|---|---|---|\n"
            s += "".join("| " + " | ".join(r) + " |\n" for r in overlap_rows)
        self.f.write(V.LEDGER, s)

    def test_fp1_none_not_met(self):
        out, _ = self.f.verify("FP-1", "FP-2")
        self.assertEqual(out["summary"], {"FP-1": "NOT_MET", "FP-2": "NOT_MET"})
        self.assertEqual(out["results"]["FP-1"]["record_count"], 0)

    def test_fp1_fp2_met(self):
        self.set_refs([ledger_record()], [["REF-1", "PAT-003", "L1", "placeholder"]])
        out, code = self.f.verify("FP-1", "FP-2")
        self.assertEqual(out["summary"], {"FP-1": "MET", "FP-2": "MET"}, json.dumps(out["results"], indent=1)[:2500])
        self.assertEqual(code, 0)

    def test_fp1_reviewed_not_met(self):
        self.set_refs([ledger_record(legal_review_status="REVIEWED")])
        out, _ = self.f.verify("FP-1")
        self.assertEqual(out["summary"]["FP-1"], "NOT_MET")

    def test_fp1_missing_field_not_met(self):
        r = ledger_record()
        del r["search_query"]
        self.set_refs([r])
        out, _ = self.f.verify("FP-1")
        self.assertEqual(out["summary"]["FP-1"], "NOT_MET")

    def test_fp1_bad_retrieval_date_not_met(self):
        self.set_refs([ledger_record(retrieval_date="yesterday")])
        out, _ = self.f.verify("FP-1")
        self.assertEqual(out["summary"]["FP-1"], "NOT_MET")

    def test_fp2_unknown_family_not_met(self):
        self.set_refs([ledger_record()], [["REF-1", "PAT-999", "L1", "placeholder"]])
        out, _ = self.f.verify("FP-2")
        self.assertEqual(out["summary"]["FP-2"], "NOT_MET")

    def test_fp2_unmapped_reference_not_met(self):
        self.set_refs([ledger_record(), ledger_record(reference_id="REF-2")], [["REF-1", "PAT-003", "L1", "placeholder"]])
        out, _ = self.f.verify("FP-2")
        self.assertEqual(out["summary"]["FP-2"], "NOT_MET")


if __name__ == "__main__":
    unittest.main()
