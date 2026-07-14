# PAT-005 Negative and Failure Path Evidence

**Family:** PAT-005 — Governed Device Continuity and Destination-Bound Hardware Abstraction  
**Status:** technical evidence matrix; not a legal conclusion

## Purpose

This record preserves the failure behavior that distinguishes governed continuity from ordinary device discovery or onboarding. A complete embodiment must show not only successful identification and packaging, but also what happens when identity, destination, evidence, authority, or publication cannot be established.

## Failure Matrix

| Failure condition | Required system result | Authority effect | Evidence required |
|---|---|---|---|
| observation lacks stable identity data | preserve distinct unresolved observation | no destination operation | observation record and unresolved fingerprint state |
| two fingerprints collide ambiguously | do not merge automatically | review required | both source fingerprints, collision reason, merge refusal receipt |
| destination capability is unsupported | retain unsupported item | no destination operation | classification result and unsupported reason |
| destination classification is generic | assign review-required state | no destination operation | generic destination record and constrained response options |
| package item destination differs from package destination | validation failure | package rejected | validator output and failed package fixture |
| destination receives package but does not accept it | preserve pending or denied disposition | no reliance or operation | destination receipt or timeout record |
| destination accepts observation only | record `accepted_observe_only` | observation permitted; operation withheld | destination receipt with `non_authorizing: true` |
| guardian policy rejects or cannot verify | retain review or refusal state | operation blocked | guardian record and refusal reason |
| release descriptor is malformed | release gate fails | no tag or release | descriptor validator result |
| release artifact is missing or hash changes | manifest generation or verification fails | no publication | missing-artifact or digest-mismatch record |
| tag exists at an unexpected commit | publication verification fails | release not confirmed | observed tag target and expected source commit |
| hosted release is absent | publication receipt remains unconfirmed | publication not claimed | release query result |
| documentation mirror succeeds without destination acceptance | mirror recorded only | no activation inferred | mirror receipt and absent destination activation receipt |
| evidence chain is incomplete | non-inference result | no final continuity claim | missing-link report |

## Required Negative Fixtures

The source implementation should retain or add fixtures for:

1. ambiguous fingerprint collision;
2. unsupported destination;
3. generic destination requiring review;
4. package destination mismatch;
5. denied destination response;
6. missing release artifact;
7. tag-target mismatch;
8. absent hosted release;
9. incomplete cross-repository receipt chain.

## Patent Relevance

Failure behavior may support the technical distinction between:

- discovering a device and reconstructing a defensible identity;
- preparing a destination package and authorizing operation;
- accepting observation and accepting reliance;
- documenting a transition and proving activation;
- publishing software and reconstructing the publication state.

No failure behavior should be treated as novel merely because it is documented. The relevant review question is whether the ordered failure-preserving architecture, in combination with source-linked identity reconstruction and non-authorizing destination packages, is supported and distinguishable over the prior art.
