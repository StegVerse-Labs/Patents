# Filing Packet Specification — filing-packet:v1

## Purpose

Automate the USPTO provisional filing pipeline up to and after the submission act, while keeping the submission itself a human-gated boundary crossing. The architecture is static emit → governed transport → human commit → receipt written back to the ledger.

This preserves the repository doctrine: **No automatic filing with USPTO or any jurisdiction.**

## Pipeline

```text
watcher (tools/patent_ai.py v2)
  positive trigger gate: T1 [PATENT] tag | T2 patent_candidates/** | T3 PR label
  → queue/<id>.trigger.json
  → disclosures/<id>.md
  → provisionals/<id>_provisional.md
  → deadlines ledger item, status=drafting; filed date remains null

human/AI drafting pass
  populate provisional sections + claims/<id>_claims.md

emitter (tools/filing_packet_emitter.py)
  → filing_packets/<id>/specification.docx
  → filing_packets/<id>/cover_sheet_data.json
  → filing_packets/<id>/fee_estimate.json
  → filing_packets/<id>/FILING_CHECKLIST.md
  → filing_packets/<id>/PACKET_MANIFEST.json
  ledger status → packet-emitted

HUMAN BOUNDARY CROSSING
  upload DOCX, complete cover data, certify entity status, pay fee
  → save uspto_filing_receipt.pdf into packet directory
  → record application number and actual filing date
  → calculate nonprovisional and PCT due dates from the actual filing date
  → commit = completion receipt
```

## Invariants

1. **No automated USPTO submission.** The emitter is filesystem-in/filesystem-out only.
2. **Filed dates are human-recorded after filing.** Draft creation never starts a fictional 365-day clock.
3. **Every admitted candidate has a positive-trigger receipt.**
4. **Every packet is hash-pinned in `PACKET_MANIFEST.json`.**
5. **Warnings prevent silent degradation.** Placeholder claims, abstract text, or cover fields produce `ready-with-warnings`.
6. **The human filing act is not delegated to StegFin or another executor.** Financial providers may prepare or record authorized payment state, but cannot cross the USPTO submission boundary.

## StegFin registry boundary

The patent engine may reference StegFin services through explicit governed interfaces:

| Repository | Permitted patent-engine use |
|---|---|
| `StegVerse-Labs/stegfin-governance` | authorize filing expenditure, vendor engagement, assignment, licensing, or acquisition transitions |
| `StegVerse-Labs/stegfin-provider-banking` | prepare and reconcile fee-payment records after human authorization |
| `StegVerse-Labs/stegfin-provider-token-ledger` | register patent-family asset identifiers, ownership events, costs, and licensing records |
| `StegVerse-Labs/stegfin-provider-vendor-payment` | govern payments to counsel, search providers, illustrators, translators, and other vendors |
| `StegVerse-Labs/stegfin-provider-acquisition-close` | govern patent purchases, portfolio sales, assignments, escrow, and closing evidence |
| `StegVerse-Labs/stegfin-provider-token-ledger-executor` | execute only admitted ledger transitions; never file with a patent office |

The dependency is one-way: the patent registry may consume governed StegFin services, while StegFin runtimes must not require claim-sensitive patent documents to operate.

## Legal and review boundary

The tools generate first-party preparation artifacts. Human and patent-counsel review remain required before filing. The engine must not represent itself as legal counsel or file applications for third parties.

## Core-Lite compliance

Both Python files are tools invoked through existing dispatch. They add no workflow files. Workflow consolidation remains a separate repository-standard remediation task.
