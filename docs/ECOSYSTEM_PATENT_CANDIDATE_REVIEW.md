# Ecosystem Patent Candidate Review Transition

## Purpose

This policy defines when the Patents system should begin reviewing the wider StegVerse ecosystem for additional patent candidates while preserving active-family filing priority.

## Activation Rule

Candidate review activates when every higher-priority active family is in at least one of these states:

1. **submission-ready** — the family has passed technical, evidence, inventorship, prior-art, drawing, practitioner, and owner-authorization gates; or
2. **externally blocked** — no authorized machine task can materially advance the family because the next transition is owned by a contributor, qualified practitioner, external search/review process, dispatcher, or owner filing decision.

Repository incompleteness alone does not activate candidate review if authorized machine work remains.

## Non-Abandonment Rule

Activation of ecosystem review does not close, deprioritize, or abandon an active patent family. New evidence, practitioner feedback, authorization, validation results, or filing events immediately return the affected family to the active queue.

## Candidate Admission Signals

A repository change may enter candidate triage only when at least one positive signal is present:

- commit message contains `[PATENT]`;
- path under `patent_candidates/**` changed;
- associated pull request carries `patent-candidate`;
- a durable architecture record identifies a new technical mechanism, not merely a business objective;
- a cross-repository implementation combines technical elements in a way not already represented by an active family;
- a public disclosure creates a time-sensitive review requirement.

## Candidate Evaluation Dimensions

Each candidate receives a working, non-legal assessment of:

1. technical problem;
2. technical mechanism;
3. measurable or reconstructable technical effect;
4. novelty-risk collision zones;
5. distinction from existing PAT families;
6. implementation and conception evidence;
7. likely human contributors;
8. earliest known disclosure;
9. public-disclosure urgency;
10. enablement gaps;
11. claim-family relationship;
12. recommended disposition.

## Dispositions

- `OPEN_DISCLOSURE` — create a new working family record.
- `DEPENDENT_FAMILY_REVIEW` — evaluate as continuation or related family.
- `MERGE_INTO_EXISTING_FAMILY` — preserve evidence under an existing PAT record.
- `HOLD_FOR_EVIDENCE` — technical concept exists but evidence or enablement is insufficient.
- `NOT_PATENT_CANDIDATE` — ordinary implementation, documentation, policy, business method, or known mechanism without an identified technical distinction.
- `URGENT_DISCLOSURE_TRIAGE` — public disclosure may affect filing strategy and requires prompt practitioner review.

## Required Durable Output

Every review cycle must emit:

- cycle identifier and timestamp;
- activation basis;
- active-family status snapshot;
- repositories and commits examined;
- candidate records and dispositions;
- evidence references;
- unresolved questions;
- next owner;
- explicit statement that no inventorship or patentability determination was made.

## Authority Boundary

Candidate review may identify and organize potential inventions. It may not:

- declare inventorship;
- conclude patentability or freedom to operate;
- expose nonpublic enabling details outside authorized records;
- file an application;
- authorize payment, signature, certification, or `patent pending` language.

## Current Transition

PAT-001 and PAT-005 have substantial technical packages but remain blocked on human/practitioner/search/rendering/dispatcher gates. Once remaining authorized machine tasks are exhausted, ecosystem candidate review may run in parallel while those external gates remain pending.