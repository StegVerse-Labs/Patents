# PAT-005 ChatGPT Correspondence Intake Contract

## Purpose

All ChatGPT-created correspondence that is pertinent to PAT-005 Steps 1–4 must be eligible for governed intake into the pre-owner packet. Correspondence is preserved as attributed source material, not silently converted into verified fact, legal judgment, inventorship, ownership, prior-art conclusions, drawing approval, or filing authority.

## Intake scope

Pertinent correspondence includes user messages, assistant responses, attached-image discussions, generated drafts, corrections, objections, confirmations, and chronology statements relating to:

- conception and contribution history;
- claim limitations and combinations;
- implementation descriptions and repository anchors;
- disclosure chronology and public-accessibility leads;
- prior-art collision questions and distinction hypotheses;
- specification, abstract, claims, embodiments, and drawings;
- contributor identity or role questions;
- counsel questions and proposed dispositions;
- corrections, uncertainties, contradictions, and warnings.

## Required provenance

Each intake item must retain:

```text
intake_id
family_id
conversation_id or stable export identifier
message_id or stable message ordinal
message_timestamp when available
author_role: USER | ASSISTANT | TOOL | ATTACHMENT_CONTEXT
source_type: CHATGPT_CORRESPONDENCE
verbatim_source_path or export reference
content_sha256
category tags
status classification
related claim, limitation, figure, evidence, or chronology identifiers
supersedes or contradicts references
review notes
```

## Status classifications

```text
UNREVIEWED_CORRESPONDENCE
USER_FACTUAL_ASSERTION_UNCORROBORATED
USER_FACTUAL_ASSERTION_CORROBORATED
ASSISTANT_SYNTHESIS_NOT_EVIDENCE
DRAFT_LANGUAGE
QUESTION_FOR_CONTRIBUTOR
QUESTION_FOR_COUNSEL
DISCLOSURE_LEAD_UNVERIFIED
IMPLEMENTATION_LEAD_UNVERIFIED
CONTRADICTION_REQUIRES_REVIEW
SUPERSEDED
EXCLUDED_NOT_PERTINENT
```

Assistant-generated text is never treated as independent corroboration merely because it appears in a ChatGPT transcript. A user confirmation may be recorded as testimony or an assertion, but corroboration status requires an identified supporting record.

## Category routing

| Category | Pipeline destination |
|---|---|
| contribution or conception | Stage A contribution capture |
| disclosure, publication, URL, post, paper, or commit | Stage B disclosure audit |
| prior art, support, enablement, claim scope, or legal question | Stage C counsel packet |
| figure, diagram, embodiment, numbering, or drawing correction | Stage D drawing review |
| owner preference or proposed disposition | Step 5 owner-decision inputs, never authorization by itself |

An item may route to more than one category while retaining a single immutable intake identity.

## Required manifest

The normalized intake manifest is:

```text
intake/chatgpt/PAT-005-correspondence-manifest.json
```

The manifest must contain only records derived from preserved correspondence or an attributable export. Missing timestamps, IDs, or source paths remain null and generate warnings; they must not be invented.

## Deduplication and succession

Deduplication uses the content hash plus source identity. Similar wording is not automatically merged. Corrections and later confirmations must point to the earlier item through `supersedes`, `confirms`, or `contradicts` relationships so chronology remains reconstructable.

## Privacy and privilege boundary

The intake process must support exclusion or restricted handling of personal, health, family, security-sensitive, privileged, or unrelated material. Only pertinent excerpts should enter counsel-facing packets. Full conversation exports should remain in a restricted source location when broader context must be retained.

## Fail-closed rules

The pre-owner pipeline must warn or stop when:

- a relied-upon item lacks a stable source reference or content hash;
- assistant synthesis is represented as factual corroboration;
- a legal conclusion is attributed to non-counsel correspondence;
- an owner preference is represented as filing authorization;
- a contradiction affecting conception, disclosure, inventorship, support, or drawings is unresolved;
- correspondence is cited without preserving the pertinent source text or attributable export.

## Human and counsel boundary

The system may classify, extract, cross-reference, deduplicate, and present correspondence. Contributors confirm factual statements. Patent counsel determines legal inventorship, disclosure consequences, patentability-related conclusions, and filing recommendations. The owner makes the explicit Step 5 disposition.
