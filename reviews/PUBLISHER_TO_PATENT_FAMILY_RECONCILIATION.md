# Publisher-to-Patent Family Reconciliation Review

## Status

Technical portfolio reconciliation draft. This is not a legal family determination, priority claim, inventorship determination, or filing instruction.

## Purpose

The Publisher counsel packet identifies eight invention families that are not yet represented as explicit numbered family records in the `PAT-001` through `PAT-005` registry. This review prevents those candidates from disappearing between Publisher capture and patent-portfolio execution.

## Current numbered families

1. `PAT-001` — Transition-Table-Native Dynamic Micro-Node Computing
2. `PAT-002` — Heartbeat-Governed Entity and Reflected-State Computing
3. `PAT-003` — Generalized Adaptive Scanner Using Dynamic Micro-Nodes
4. `PAT-004` — Manifest-Governed Bidirectional Neural Communication
5. `PAT-005` — Governed Device Continuity and Destination-Bound Hardware Abstraction

## Reconciliation table

| Publisher family | Potential technical relationship | Current disposition | Required decision |
|---|---|---|---|
| Commit-Time Admissibility Gate | Strong architectural overlap with PAT-001 transition-table role execution, authority/admissibility separation, fail-closed outcomes, receipts, and reconstruction | Unmapped umbrella/root candidate | Counsel and owner must decide whether this is the root of PAT-001, a broader separate provisional, or an umbrella disclosure supporting multiple families |
| Receipt-Based State Transition Validation | Cross-cutting receipt and reconstruction layer appearing in PAT-001 and potentially PAT-005 | Unregistered cross-cutting candidate | Determine whether dependent claims, separate family, or shared specification module best preserves scope |
| Publisher Governed Disclosure Pipeline | Application of commit-time governance to public release and invention capture | Unregistered application candidate | Decide whether separate provisional, dependent embodiment, trade secret, or defensive publication |
| Application Correction Gate | Application of commit-time validation to filing-package correction and submission readiness | Unregistered application candidate | Decide whether legal-document prior art warrants a separate narrow filing or only an embodiment |
| AI Output-to-Action Boundary | Consequence-boundary detection for AI-generated outputs becoming executable actions | Possible cross-cutting embodiment of Commit-Time Admissibility Gate | Decide independent versus dependent treatment and distinguish from tool permissions and output filters |
| Recoverability-Aware Execution Boundary | Denial or deferral where a transition would be non-reconstructable or non-recoverable | Strong overlap with PAT-001 and possible relationship to PAT-002 | Determine whether recoverability is mandatory in a root claim or a dependent family |
| Master-Records Reconstruction and Verification | Preservation and reconstruction of transition evidence and receipts | Cross-repository infrastructure candidate | Decide whether this is a separate family, receipt-family embodiment, or internal/trade-secret architecture |
| Multi-Entity Observer-Participant Admissibility | Coupled affected-entity and observer/participant evaluation at commit | Advanced formalism candidate not represented by a numbered family | Create separate capture packet before further public expansion; determine whether later continuation is preferable |

## Non-collapse rules

- Similarity does not establish that two invention families are legally the same invention.
- A cross-cutting technical feature may support multiple specifications without establishing priority entitlement.
- A numbered family must not silently absorb a Publisher family without an explicit scope decision.
- Public repository proximity does not establish inventorship, conception date, novelty, ownership, or filing rights.
- Claim-sensitive details remain controlled until filing or explicit publication authorization.

## Required portfolio decisions

For each Publisher family, record one of:

```text
MAP_TO_EXISTING_FAMILY
CREATE_NEW_NUMBERED_FAMILY
INCLUDE_AS_DEPENDENT_EMBODIMENT
RETAIN_AS_TRADE_SECRET
DEFENSIVE_PUBLICATION_REVIEW
DEFER_FOR_EVIDENCE
ABANDON
```

Each decision record must identify:

```text
publisher_family_key
selected_disposition
numbered_family_id_if_any
scope_summary
supporting_source_files
known_public_disclosures
inventorship_review_status
practitioner_or_owner_authority
conditions_and_unresolved_questions
```

## Next automatable work

1. Create structured completion records for PAT-002 through PAT-004.
2. Create a candidate-family registry for the eight Publisher families without assigning legal family identity.
3. Link existing counsel-packet files and public-disclosure controls as evidence pointers.
4. Add a validator that rejects any status of `filed`, `patent_pending`, or deadline-calculated without an actual filing receipt and filing date.
5. Update `data/portfolio-completion-status.json` after each disposition decision.

## Human and counsel boundary

The following cannot be inferred automatically:

- whether an invention is legally distinct;
- whether multiple disclosures support one provisional or several;
- inventorship for any proposed claim;
- novelty or obviousness conclusions;
- foreign-rights consequences;
- filing authorization;
- assignment or ownership;
- whether trade-secret protection is preferable.

Until those decisions are recorded, the eight Publisher families remain visible, controlled candidates rather than silently omitted work.
