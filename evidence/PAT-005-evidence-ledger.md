# PAT-005 Evidence Ledger

**Status:** cross-repository evidence preservation map  
**Legal status:** not filed; not a patentability opinion

## Evidence Rule

For each proposed limitation, preserve the earliest known human conception evidence, written description, executable implementation, public disclosure, repository path, commit, test, receipt, and destination-side result. Unknown dates or inventors must remain unknown until supported.

## Involved Repositories

1. `StegVerse-Labs/device-continuity-layer`
2. `StegVerse-Labs/StegTalk`
3. `StegVerse-Labs/StegMusic`
4. `StegVerse-Labs/Site`
5. `GCAT-BCAT-Engine/Publisher`
6. `StegVerse-Labs/admissibility-wiki`
7. `StegVerse-002/stegguardian-wiki`
8. `StegVerse-Labs/Patents`

The detailed repository role map is maintained in `evidence/PAT-005-cross-repository-source-map.md`.

## Source Implementation Evidence

Repository: `StegVerse-Labs/device-continuity-layer`

| Candidate limitation | Repository evidence | Current confidence | Required follow-up |
|---|---|---:|---|
| heterogeneous discovery observations | `adapters/`, discovery fixtures, discovery validators | high | record exact commits and first conception discussion |
| fingerprint generation | fingerprint tools, schemas, fixtures | high | identify earliest implementation commit |
| deterministic canonical inventory merge | `tools/build_inventory.py`, `tests/test_device_inventory.py` | high | preserve before/after duplicate examples |
| source fingerprint lineage | inventory output and related tests | medium | reconcile schema support with generated field |
| destination classification | `tools/classify_inventory.py` | high | document rule rationale and conception source |
| recovery plan separating preparation from operation | `tools/build_recovery_plan.py` | high | capture human conception evidence for authority distinction |
| destination bundle grouping | `tools/build_destination_bundles.py` | high | preserve deterministic output fixtures |
| destination-bound package | `tools/build_destination_packages.py`, package fixtures | high | capture destination response examples |
| explicit review posture | bundle/package item records and validators | high | document unsupported and ambiguous cases |
| package validation | destination bundle and package validators | high | preserve failure fixtures, not only passing fixtures |
| source-to-destination contract | StegTalk and StegMusic contracts, payloads, and consumption tasks | high | preserve exact commits and destination copies |
| reconstructable receipt chain | receipts for v0.3, v0.4, v0.5 | high | produce one complete end-to-end reconstruction example |
| descriptor-driven release publication | `releases/current.json`, manifest builder, workflows | high | preserve successful workflow run when available |
| post-publication verification receipt | publication receipt builder and release workflow | high as code; unconfirmed operationally | preserve first successful release URL and workflow evidence |

## Destination Evidence

### `StegVerse-Labs/StegTalk`

Required evidence:

- exact destination-side contract path and commit;
- exact payload fixture path and commit;
- destination validator and test results;
- destination receipt recording observation-only, review-required, refusal, or denial posture;
- proof that package intake does not authorize microphone, speaker, button, sensor, radio, messaging, or other communication operation;
- entity/runtime records distinguishing recognition, reliance, readiness, commitment, transition, discovery, revocation, and operation;
- earliest human conception evidence for those distinctions as applied to recovered hardware.

Current confidence: medium. Repository exists and related entity-runtime work is confirmed, but exact device-continuity destination paths and commits require collection.

### `StegVerse-Labs/StegMusic`

Required evidence:

- exact destination-side contract path and commit;
- exact payload fixture path and commit;
- destination validator and test results;
- destination receipt recording observation-only, review-required, refusal, or denial posture;
- unsupported or ambiguous renderer, receiver, controller, playback, routing, or media-control examples;
- proof that device identity or compatibility does not authorize playback or control;
- private evidence export hashes and access-status record.

Current confidence: medium. Repository existence and private status are confirmed; exact device-continuity paths and commits require collection without public disclosure.

## Mirror and Publication Evidence

### `StegVerse-Labs/Site`

Known paths:

- `data/device-continuity-layer.json`
- `data/device-continuity-layer-receipt.json`

Known search commit anchor: `be68d3fc3bfed3add912ebed77b2ca9eca850214`.

Required preservation:

- exact file commits and hashes;
- source-to-site receipt linkage;
- public-disclosure date;
- boundary text distinguishing public status from deployment or activation.

### `GCAT-BCAT-Engine/Publisher`

Known paths:

- `data/device-continuity-layer.json`
- `data/device-continuity-receipt.json`
- `Papers/device-continuity-layer-governed-hardware-abstraction.md`

Known paper commit: `661521388485f275a9231394dd2308bb52db68d3`.

Required preservation:

- publication data and receipt commits;
- paper content and commit;
- publication date and URL;
- boundary statements preventing publication from being treated as activation;
- any Publisher-to-wiki propagation records.

This is a known public technical disclosure. It may not be the earliest public disclosure of every candidate limitation.

## Governance Interpretation Evidence

### `StegVerse-Labs/admissibility-wiki`

Known paths:

- `pages/device-continuity-admissibility.md`
- `receipts/device-continuity-admissibility-receipt.json`

Known search commit anchor: `07880b9f31ad83850889d6a7f3b15bff083b1a5e`.

Required preservation:

- exact file commits and hashes;
- statements distinguishing reachability, compatibility, admissibility, and authority;
- review-required, unsupported, fail-closed, refusal, and denial behavior;
- public-disclosure dates.

### `StegVerse-002/stegguardian-wiki`

Required evidence:

- exact device-continuity page and receipt paths;
- guardian-side treatment of observation, review, refusal, and operational authority;
- distinction between technical reachability and permission to operate;
- exact commits, hashes, and disclosure dates.

Current confidence: pending verification. Do not infer paths or content not yet located.

## Patent-Process Evidence

Repository: `StegVerse-Labs/Patents`

Preserve:

- `disclosures/PAT-005-governed-device-continuity.md`;
- `claims/PAT-005-claim-architecture.md`;
- `evidence/PAT-005-evidence-ledger.md`;
- `evidence/PAT-005-cross-repository-source-map.md`;
- `triage/PAT-005-public-disclosure-and-filing-triage.md`;
- portfolio manifest history;
- human conception statements and inventorship review;
- practitioner comments and revisions.

## Cross-Repository Limitation Map

| Candidate limitation | Source repo | Destination / propagation support |
|---|---|---|
| canonical device identity | device-continuity-layer | destination receipts confirm referenced inventory |
| source fingerprint lineage | device-continuity-layer | destination package references preserve source identity |
| non-authorizing destination package | device-continuity-layer | StegTalk and StegMusic destination validation |
| observation-only or review-required response | package schema and source contracts | StegTalk / StegMusic receipts and validators |
| separate operational authority | source recovery plan and contracts | destination runtime or guardian authority records |
| mirror propagation without activation | source receipts | Site mirror artifacts and receipt |
| publication without activation | release and publication receipt tools | Publisher data, receipt, and paper |
| admissibility distinction | source package states | admissibility-wiki page and receipt |
| guardian refusal boundary | source non-authorizing semantics | stegguardian-wiki page and receipt, pending verification |
| end-to-end reconstruction | linked source receipts | destination, Site, Publisher, wiki, and patent evidence |

## Known Commit Anchors

- Publisher paper installation: `661521388485f275a9231394dd2308bb52db68d3`
- Site device-continuity search anchor: `be68d3fc3bfed3add912ebed77b2ca9eca850214`
- admissibility-wiki search anchor: `07880b9f31ad83850889d6a7f3b15bff083b1a5e`
- PAT-005 cross-repository source map: `fcdda81d308ebf76a71a5b31810a63e58d763ccc`

Additional source and destination commits must be collected and linked claim by claim.

## Missing Evidence

1. Earliest conception dates for every independent and dependent limitation.
2. Human contributor statements describing conception.
3. Exact StegTalk destination-side device-continuity paths and commits.
4. Exact StegMusic destination-side paths, commits, and confidential evidence hashes.
5. Exact StegGuardian page and receipt paths.
6. Earliest public disclosure across GitHub, LinkedIn, websites, papers, and chat exports.
7. Complete negative and failure examples across source and destination repos.
8. Successful hosted release and publication receipt.
9. One complete reconstruction from observation through destination response and public propagation.
10. Formal prior-art search results with claim charts.
11. Inventorship determination by claimed subject matter.

## Preservation Actions

- Do not rewrite or delete source commits containing candidate invention evidence.
- Preserve private destination evidence without making it public.
- Preserve screenshots only as supplemental evidence; retain machine-readable commits and files as primary evidence.
- Record public disclosure URLs and dates when verified.
- Preserve test outputs and workflow artifacts associated with the first complete operational path.
- Hash exported evidence bundles before legal review.
- Maintain repository-local boundaries: evidence aggregation does not authorize source, destination, Site, Publisher, or wiki mutation.
