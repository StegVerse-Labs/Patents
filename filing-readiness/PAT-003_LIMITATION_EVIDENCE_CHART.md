# PAT-003 — Limitation-Level Evidence Chart (skeleton, 2026-10-16)

**Disposition:** FAIL_CLOSED_NOT_READY_TO_FILE. This is a non-enabling status chart. It is not a patent application, not truth, not a legal determination and not execution authority. **Confidential invention details must not be added to this public repository.** Source locators, hashes and experimental details for private evidence belong in the private, disclosure-reviewed copy only.

- Limitation text: copied verbatim from `data/master_claims.json` (`CLM-PAT-003-METHOD-001`, `CLM-PAT-003-SYSTEM-001`, both `status: concept`). No limitation is added, removed or reworded.
- Candidate support / unverified requirement: copied from the preliminary mapping in Patents issue #16. That mapping is labelled "candidate evidence, NOT admitted".
- Classification vocabulary (from `data/PAT-003-completion-status.json`): `implemented`, `written_description_only`, `proposed`, `unsupported`. Until it is verified, every row is `CANDIDATE_NOT_ADMITTED`.
- `evidence_refs` in `data/master_claims.json` stays empty until a row is admitted.

## Method claim CLM-PAT-003-METHOD-001 — "A method for scanning an entity, comprising:"

| Lim. | Clause | Limitation text | Candidate support (issue #16) | Unverified requirement / missing element | Source locator + SHA-256 | Conditions / pos.-neg. result | Classification |
|---|---|---|---|---|---|---|---|
| L1 | — | acquiring a plurality of signals during temporally coordinated observation | Original video frames and playback/PTS temporal context | Independent synchronized signal plurality and capture-clock authenticity | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L2 | SCL-MINIMUM-NODE | dynamically constructing one or more signal-specific acquisition nodes according to normalized strength, noise, ambiguity, or confidence | Selective offline heavy analysis after cheap observations | Actual dynamic acquisition-node construction; camera acquisition not reduced | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L3 | — | constructing subsequent decoding or cross-signal comparison nodes according to attributes of acquired signals | Video decoding, ROI/global processing | Independent cross-signal comparative nodes | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L4 | SCL-RETURN-DELTA | determining functional condition from relationships among source-to-return transformations rather than solely from isolated thresholds | Observed motion deltas, immutable observation vs revised interpretation | Subsystem transformation comparison and functional-condition determination | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L5 | SCL-DYNAMIC-OBSERVATION | continuing observation until a manifest-relative complete signal is obtained or a minimum adverse-condition observation period is satisfied | Causal lookback, cooldown, context windows and episode coalescing | Manifest-relative completeness/adverse-condition observation controller | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L6 | SCL-NON-INFERENCE | producing non-inference when sufficient evidence is not obtained | Explicit research claim boundaries and unsupported classifications | Integrated operational non-inference output | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |

## System claim CLM-PAT-003-SYSTEM-001 — "An adaptive scanning system comprising:"

Issue #16 maps system L1–L4 as a group: support from "offline source, timestamp handling, reconstruction components"; unverified "plural modalities, authentic synchronization, governed node constructor, full comparative engine". The split per row below follows that same order and adds nothing.

| Lim. | Clause | Limitation text | Candidate support (issue #16) | Unverified requirement / missing element | Source locator + SHA-256 | Conditions / pos.-neg. result | Classification |
|---|---|---|---|---|---|---|---|
| L1 | — | a plurality of sensing modalities or channels | Offline source | Plural modalities | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L2 | — | a temporal synchronization component | Timestamp handling | Authentic synchronization | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L3 | SCL-MINIMUM-NODE | a transition-governed node constructor configured to allocate acquisition and analysis nodes according to detected signal conditions | (none specific in issue mapping) | Governed node constructor | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |
| L4 | — | a comparative state reconstruction engine | Reconstruction components | Full comparative engine | NOT VERIFIED | NOT RECORDED | CANDIDATE_NOT_ADMITTED |

## Previously reported results to verify (issue #16) — none admitted

Synthetic 120-frame replay (120 predecessor-linked observations); rights-cleared pendulum video, 422 frames; held-out ROI/global calibration; context-window and episode-coalescing tests; v0.13 independent-reference gate (**synthetic-only**). In-repo source-only modules (`research/pat003/*.py`, merged via PR #17 at `b39b588e`) are synthetic controls. They are not physical-trial evidence for any row.

## Manifest state-transition conformance findings (flag only)

Rule (StegVerse-Labs/.github README, organization-role deployment): every action is a manifest-bound state transition; an unavailable receiver yields `DURABLE_QUEUE_OR_EVENT_EPHEMERAL_MATERIALIZATION`; no external machine, always-on receiver or post-closure authentic-observer gate may be a transition predicate. Runtime observations belong to the original manifest-bound state transitions.

| Location | Finding | Action |
|---|---|---|
| `data/PAT-003-completion-status.json` `next_machine_tasks` | Said "when dispatcher execution is available", which waits on an external dispatcher | Reworded in this change as the output of the owning manifest-bound transition |
| `docs/FILING_PACKET_SPEC.md` pipeline | Begins with a "watcher (tools/patent_ai.py v2)"; a standing watcher is a receiver pattern | Flagged for the portfolio owner; not edited here (cross-family file) |
| Issue #16 open gate "independently authenticated manifest-bound transition/ledger readback" | Must not act as a post-closure observer predicate for document-readiness rows | Flagged for owner wording review; chart rows are not gated on it |

No new dependency, service, machine or workflow is introduced.
