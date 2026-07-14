# PAT-005 Evidence Ledger

**Status:** initial evidence preservation map  
**Legal status:** not filed; not a patentability opinion

## Evidence Rule

For each proposed limitation, preserve the earliest known human conception evidence, written description, executable implementation, public disclosure, repository path, commit, test, and receipt. Unknown dates or inventors must remain unknown until supported.

## Source Repository

`StegVerse-Labs/device-continuity-layer`

## Implementation Evidence Map

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
| non-authorizing package semantics | destination integration receipts and Publisher paper | medium | add explicit destination-side proof and authority transition |
| package validation | `tools/validate_destination_bundles.py`, `tools/validate_destination_packages.py` | high | preserve failure fixtures, not only passing fixtures |
| reconstructable receipt chain | receipts for v0.3, v0.4, v0.5 | high | produce one complete end-to-end reconstruction example |
| descriptor-driven release publication | `releases/current.json`, `tools/build_release_manifest.py` | high | preserve successful workflow run when available |
| post-publication verification receipt | `tools/build_publication_receipt.py`, release workflow | high as code; unconfirmed operationally | preserve first successful release URL and workflow evidence |

## Related Destination Evidence

### StegTalk

Preserve destination-side contracts, fixtures, validation results, and receipts showing that package acceptance is observation-only and does not independently authorize operation.

### StegMusic

Preserve destination-side contracts, fixtures, validation results, and receipts showing destination-specific handling of media devices and unsupported capabilities.

### Publisher

Preserve:

- `GCAT-BCAT-Engine/Publisher/Papers/device-continuity-layer-governed-hardware-abstraction.md`
- commit `661521388485f275a9231394dd2308bb52db68d3`

This is a known public technical disclosure. It may not be the earliest public disclosure of every candidate limitation.

## Known Commit Anchors

- Publication paper installation: `661521388485f275a9231394dd2308bb52db68d3`
- PAT-005 disclosure opening: recorded in this repository history

Additional source commits must be collected from the Device Continuity Layer history and linked claim by claim.

## Missing Evidence

1. Earliest conception dates for each independent limitation.
2. Human contributor statements describing conception.
3. Earliest public disclosure across GitHub, LinkedIn, websites, and chat exports.
4. Complete negative/failure examples.
5. Successful hosted release and publication receipt.
6. Formal prior-art search results with claim charts.
7. Inventorship determination by claimed subject matter.

## Preservation Actions

- Do not rewrite or delete source commits containing candidate invention evidence.
- Preserve screenshots only as supplemental evidence; retain machine-readable commits and files as primary evidence.
- Record public disclosure URLs and dates when verified.
- Preserve test outputs and workflow artifacts associated with the first complete operational path.
- Hash exported evidence bundles before legal review.
