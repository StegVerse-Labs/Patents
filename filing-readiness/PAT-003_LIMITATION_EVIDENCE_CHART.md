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

## Evidence map, appended 2026-10-23 (Lane A, session 19d95368) — rows NOT admitted

This section is appended. The rows above are not changed. Every row stays `CANDIDATE_NOT_ADMITTED`: no admission record exists. Nothing here is admitted, proven, ready, or a classification decision. The "proposed class" column uses the vocabulary of `data/PAT-003-completion-status.json` as a **proposal only**, for the claimed admission task (patent-registry#19 `PAT-003-EVIDENCE`, PROPOSED; claim pending). Not truth, not a legal determination, not execution authority. PAT-003 stays `FAIL_CLOSED_NOT_READY_TO_FILE`.

**Public non-enabling rule.** This map holds only identifiers, hashes, statuses and conditions that are already public. Private items appear only as an opaque pointer (`PRIV-n` or `KV-n`). Each pointer is a Google Drive file id plus the SHA-256 of the copy retrieved on 2026-10-23. They are a private, owner-authorized surface. Their content is not reproduced here and must not be added to this public repository. The three evidence classes are kept separate: **proofs** (mathematical / written-description candidates), **software tests** (synthetic or offline code checks), and **physical measurements** (on recorded physical media).

### Private pointers (content not reproduced)

| Pointer | Kind | Drive file id | SHA-256 (retrieved copy) | Note |
|---|---|---|---|---|
| PRIV-1 | proof / written-description candidate (outline v5) | `12gdUzB4ty_juBY_9K-JxDeW_kRLkufA5` | `2d3456d7ec42239a2760fd967ec69e7808be92612948e44e28df7337b6b7be20` | private, owner-authorized surface; unreviewed |
| PRIV-2 | proof candidates (derivations v2) | `1A3JVMFQAprTSNhfCGHJ-PGWIpknzEdeY` | `644e11af1af449c187af0baed7bb7af579a65862e01f9df70a79b7e51384a219` | private, owner-authorized surface; unreviewed |
| PRIV-3 | per-row gap matrix v1 | `17Y4hf-_dXVta4FNGL5tQjG3WLJYMeui2` | `06626fc0b365821028f99c54a51e4fe0334a1b4e91b79b33e594c0deb0941b3f` | private, owner-authorized surface |
| PRIV-4 | standards-alignment table v1 (71 rows) | `11qTDSur5SOLYOz8SzmrSJKmEUqCS0sXZ` | `3dafdc54359d74c848a246950898314647ebc7618a40b6b7936cdf43c9829a0c` | private, owner-authorized surface; 44/71 rows carry CONFLICT or UNDEFINED |
| PRIV-5 | runtime-observation audit (18 items) | `1G0Uv-fxj4Q0iUMeHD_7EsTleVoyiw6qj` | `0b12d0bd6737d5e3b144e5cb179a54036eb6237f2b9ea24fa1ae937db12aa1f0` | private, owner-authorized surface; 0 MEETS_STANDARD |
| PRIV-6 | source hash record + clock addendum (2026-10-16) | `1F2jT9kHEWOAtOpOj9qc7756XTWFCgaVe` | `68b39dd0b65de7e52df216bc468899713dd3b529db013c7a51a4e9c4bd50c041` | private, owner-authorized surface |
| KV-1 | experiment record, v0.8 | `1g4ECxNYILncMxOAz3siaH26q67PUDkSL` | `0d9f833a14dd051ee0e2b8cac2e1982b6632abe70fc4eac57474b749f6d141ab` | private, owner-authorized surface |
| KV-2 | experiment record, v0.9 | `1pdZEhgYT82M70UbytA5nAzchb4QrI9Mp` | `b3afa57320c65a2129e8af5949d08c2cdc57f7fe5e1559e558c8801041039967` | private, owner-authorized surface |
| KV-3 | experiment record, v0.12 + repeat result | `19RHMuPufE0ozgEvEMDYjGqi5YUA1ZUC4`, `1t4Jxb8wmfNLNho_f0mvuuv42v0OHRY2n` | `630f19dd6ce1f077cd16f4aa74062c5d8ccdbf257489c1e2dc23e4668de9ea24`, `b3150b2fecb21ac0c5b003ebdd0c9378daf15e71fda1a48d2a6cf14f1fa1884c` | private, owner-authorized surface |
| KV-4 | experiment record, v0.13 | `1JvItnCWl4HgCtDM7iHyyr0HKtkXd43kq` | `6a0f2cc20dc61d22cbc2e1aa32b5bccf98ba4aaa925e50058dba68893994bb79` | private, owner-authorized surface |
| KV-5 | experiment progression record (generation 266) | `1x3EImytgYnc9EPi0G8ZWEenlI-FPAEoe` | `e192d7bbb9ce7c14fca2ae089824efe2ddda644f2d29cd76b88d4b205e6d3055` | private, owner-authorized surface |
| KV-6 | v0.2 fixture record + evidence classification | `1OsabhfzFCt9OykYXFyKVZL51Mz2bX2hm`, `1k-H1tLOMKIV1U5YwMeyxE3-uTb3dFS6g` | `ccc0f02b128ee93a1ae62edf8a062f93b9434967770c6d521f96445dd5d3a142`, `4dcb040532a4a9a06446b1865b5111a31b4f6318c7a7b2d50b3a8f437a2724ba` | private, owner-authorized surface |
| KV-7 | third-party double-pendulum video file | `1h-UEEqCboivOJYa2qeEHNMhlEzn95Hlt` | NOT COMPUTED (7,271,648,696 bytes; `research/pat003/input_manifest_v1.json` declares 481,804,387) | private; rights HOLD; EXPECTED_ORIGINAL_NOT_LOCATED |

### Public locators used

- **LH:** StegVerse-Labs/.github `docs/OPTICAL_PHYSICAL_STATE_REPLAY_RESEARCH_MIRROR_HANDOFF.md`, main `86382e60da984fa02892fecfac2b9bdec0e64a5f`, blob `001808be2d5e93d0599b7702620bb66ba1969005`.
- **PEP:** StegVerse-Labs/.github `tests/patents/test_physical_emission_golden_vectors_2626.py`, blob `78c405ffe09b741b81b8544171bd11df50ee67c3`.
- **RP:** this repository, `research/pat003/*_v1.py` and `tests/test_pat003_*_v1.py` at `cf30104dd6a5b9e6b30ec3e15c4538a02f09e304`. These are synthetic controls (see the section above).
- **VE:** StegVerse-Labs/video-engine (private) branch `pat003-optical-execution` at `b11c1100c4544d4d81d0521e5c7e411c0c2dc186`. Identifiers only.
- **E1 source:** CC0 pendulum-clock recording, SHA-256 `069d9a266f584f14f009a2bc7d2e7fbc20cc87bdffebb8be87573ca939d2eb8b` (`reviews/PAT-003_TECHNICAL_COMPARISON_RESEARCH_LEDGER.md` L136; LH L151). Independently rehashed 2026-10-16 (PRIV-6): match.

### Method claim CLM-PAT-003-METHOD-001

| Lim. | Evidence class | Locator | Hash | Conditions | Status |
|---|---|---|---|---|---|
| L1 | proofs | PRIV-1 | see pointer | written-description only for the plurality; no supporting derivation | UNVERIFIED |
| L1 | software tests | PEP; VE comms R1; KV-2 sync gate | PEP blob above; VE commit above | synthetic paired streams only (LH L162) | TESTED_SYNTHETIC |
| L1 | physical measurements | E1 source; KV-7 | E1 hash above | single camera; decoder presentation timestamps, not authenticated capture time (LH L139–L142); second-instrument candidate KV-7 not ingested, rights HOLD (LH L160) | UNVERIFIED |
| L1 | **proposed class** | — | — | — | `proposed` (CANDIDATE_NOT_ADMITTED) |
| L2 | proofs | PRIV-1 | see pointer | interpretive mapping only; no derivation links it to node construction | INTERP |
| L2 | software tests | RP; VE scanner R2 | RP/VE commits above | synthetic only | TESTED_SYNTHETIC |
| L2 | physical measurements | LH L151–L152; KV-1; KV-2 | E1 hash above | on E1 under the recorded required-context policy, 421/422 frames still receive heavy analysis; adaptive-processing benefit **not demonstrated** | **CONFLICT** — recorded evidence currently cuts against this row's intent |
| L2 | **proposed class** | — | — | — | `proposed` (CONFLICT recorded; CANDIDATE_NOT_ADMITTED) |
| L3 | proofs | PRIV-2 | see pointer | candidate items; reviewer check not performed | CANDIDATE_UNREVIEWED |
| L3 | software tests | RP; VE scanner R2; PEP; KV-6 | as above | synthetic / offline | TESTED_SYNTHETIC |
| L3 | physical measurements | LH L140–L142; KV-5 | E1 hash above | all 422 frames of E1 decoded and recomputed exactly; no independently acquired second history, so cross-signal comparison is untested | PARTIAL (decoding only) |
| L3 | **proposed class** | — | — | — | `implemented` candidate for decoding only; cross-signal comparison `unsupported` (CANDIDATE_NOT_ADMITTED) |
| L4 | proofs | PRIV-1 | see pointer | row recorded as not addressed; key term undefined | ABSENT |
| L4 | software tests | none located | — | — | ABSENT |
| L4 | physical measurements | none located | — | independent physical reference absent | ABSENT |
| L4 | **proposed class** | — | — | owner scope decision pending | `unsupported` (CANDIDATE_NOT_ADMITTED) |
| L5 | proofs | PRIV-1 | see pointer | row recorded as not addressed | ABSENT |
| L5 | software tests | KV-3; RP | as above | synthetic; v0.12 coalescing saved 0 unique heavy frames | TESTED_SYNTHETIC |
| L5 | physical measurements | KV-3 | see pointer | same-video proxy only; original trigger rows not run | UNVERIFIED |
| L5 | **proposed class** | — | — | owner scope decision pending | `proposed` (CANDIDATE_NOT_ADMITTED) |
| L6 | proofs | PRIV-1; PRIV-2 | see pointers | candidate proof written; reviewer check not performed | CANDIDATE_UNREVIEWED |
| L6 | software tests | RP (`governance_boundary_v1`); PEP; KV-6 | as above | synthetic negative controls; source-only mode withholds ALLOW | TESTED_SYNTHETIC |
| L6 | physical measurements | none on E1 with exact receipts | — | negative controls not yet run on the physical recording | UNVERIFIED |
| L6 | **proposed class** | — | — | — | `written_description_only` (CANDIDATE_NOT_ADMITTED) |

### System claim CLM-PAT-003-SYSTEM-001

| Lim. | Evidence class | Locator | Hash | Conditions | Status |
|---|---|---|---|---|---|
| L1 | proofs | PRIV-1 | see pointer | written-description only | UNVERIFIED |
| L1 | software tests | VE comms R1 | VE commit above | synthetic; no physical channel | TESTED_SYNTHETIC |
| L1 | physical measurements | KV-7 | not computed | second modality absent; only candidate not ingested, rights HOLD | ABSENT |
| L1 | **proposed class** | — | — | — | `written_description_only` (CANDIDATE_NOT_ADMITTED) |
| L2 | proofs | PRIV-1 | see pointer | as method L1 | UNVERIFIED |
| L2 | software tests | KV-2 sync gate; PEP | as above | synthetic paired streams only | TESTED_SYNTHETIC |
| L2 | physical measurements | E1 source | E1 hash above | no authenticated capture clock | UNVERIFIED |
| L2 | **proposed class** | — | — | — | `proposed` (CANDIDATE_NOT_ADMITTED) |
| L3 | proofs | PRIV-1 | see pointer | interpretive mapping only | INTERP |
| L3 | software tests | VE scanner R2 | VE commit above | synthetic | TESTED_SYNTHETIC |
| L3 | physical measurements | LH L151–L152; KV-1; KV-2 | E1 hash above | same finding as method L2: benefit not demonstrated | **CONFLICT** |
| L3 | **proposed class** | — | — | — | `proposed` (CONFLICT recorded; CANDIDATE_NOT_ADMITTED) |
| L4 | proofs | PRIV-2 | see pointer | candidate items; reviewer check not performed | CANDIDATE_UNREVIEWED |
| L4 | software tests | LH L142 (64/64 offline, not exact-head); RP; KV-4 (synthetic reference gate) | as above | offline / synthetic | TESTED_OFFLINE |
| L4 | physical measurements | LH L142–L143; E1 source; PRIV-6 | E1 hash above; terminal receipt `fad1f946…` (LH L142) | replay and custody on E1 recorded; independent physical reference absent, so physical accuracy is not measured | PARTIAL (replay/custody only) |
| L4 | **proposed class** | — | — | — | `implemented` candidate for replay/custody only; physical accuracy `unsupported` (CANDIDATE_NOT_ADMITTED) |

### Open items recorded with this map (not resolved here)

1. Independent physical reference / second modality (method L1, L4; system L1, L4). The only located candidate (KV-7) is on rights HOLD and has a size mismatch.
2. Adaptive benefit under the required context (method L2; system L3). The recorded measurement conflicts with this.
3. Reviewer check of the PRIV-1 / PRIV-2 candidates.
4. Owner definitions of undefined terms, and the scope decision on method L4/L5.
5. Canonical specification and drawings.
6. patent-registry#19 claim/fence, admission and ledger readback.

`evidence_refs` in `data/master_claims.json` stays empty, and the readiness index checkbox at L77 stays unchecked, until rows are admitted.
