# PAT-001 Drawing Production Specification

**Status:** production specification for filing-review drawings; not approved filing drawings

## Scope

This specification governs conversion of PAT-001 working Mermaid sources and formal drawing sheets into monochrome filing-review outputs. It does not authorize submission.

## Source Classes

### Verified-core sources

- FIG. 1 — governed micro-node system overview
- FIG. 2 — ordered transition-table role sequence
- FIG. 3 — receipt and reconstruction binding
- FIG. 4 — ALLOW, DENY, and FAIL_CLOSED boundary
- FIG. 5 — governed return and reconstruction path
- FIG. 6 — request, role, receipt, and witness data relationships

These may be rendered for practitioner review because they correspond to mapped implementation evidence.

### Proposed-embodiment sources

- FIG. 7 — active-node capability resolution
- FIG. 8 — minimum manifest-derived construction
- FIG. 9 — expiry and externally evidenced retention
- FIG. 10 — bounded context reuse and heartbeat non-self-retention

These must remain visually marked `PROPOSED — SUPPORT REVIEW REQUIRED` until corroborated.

## Output Requirements

For each verified-core figure produce:

- editable source;
- monochrome SVG;
- print-ready PDF or combined drawing PDF;
- PNG preview for repository review;
- SHA-256 manifest entry;
- reference-numeral inventory;
- source commit and rendering-tool version.

## Drawing Conventions

- black lines and text on white background;
- no color-dependent meaning;
- no gradients, shadows, or decorative styling;
- consistent reference numerals across drawings and specification;
- solid arrows for verified data/evidence flow;
- dashed arrows only for proposed or optional transitions;
- terminal decisions shown distinctly as ALLOW, DENY, or FAIL_CLOSED;
- externally governed systems shown with double borders;
- no trademark or repository name where a broader functional label is supported.

## Reference Numeral Control

Every numeral must have:

1. one canonical component name;
2. one first-use definition in the specification;
3. consistent reuse across figures;
4. no conflicting component assignment;
5. a machine-readable mapping entry before packet authorization.

## Rendering Validation

A rendering pass is acceptable only when:

- all verified-core source files parse successfully;
- no node or label is clipped;
- arrows do not obscure numerals;
- page margins preserve all content;
- grayscale printing preserves all distinctions;
- the reference-numeral validator reports no duplicates or missing definitions;
- output hashes are recorded.

## Fail-Closed Conditions

Do not mark drawings approved when:

- any proposed embodiment is presented as verified;
- a reference numeral lacks specification support;
- output was manually altered without updating source and hash;
- a rendering tool/version is unknown;
- practitioner drawing review remains unresolved.

## Completion Event

This drawing task becomes complete only after rendered outputs, hashes, numeral validation, and practitioner approval are committed. Completion does not itself authorize filing.