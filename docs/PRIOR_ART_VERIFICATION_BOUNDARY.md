# Prior-Art Verification Boundary

The active-family prior-art record is intentionally split into two states:

1. **Verified non-patent identifiers** — persistent identifiers and publication dates have been confirmed.
2. **Unverified patent leads** — titles, categories, or search leads are not promoted until a patent publication number, priority date, family information, and relevant claim or paragraph can be confirmed through USPTO, WIPO, or Espacenet records.

Absence from a search is not novelty evidence. A verified identifier is not a patentability, validity, infringement, freedom-to-operate, or inventorship conclusion. Machine validation cannot authorize filing or patent-pending language.

Canonical controls:

- `data/active-family-prior-art-identifiers.json`
- `tools/validate_prior_art_identifiers.py`
- `tests/test_prior_art_identifiers.py`

The record may change from `PRIOR_ART_IDENTIFIERS_PARTIALLY_VERIFIED` to `PRIOR_ART_IDENTIFIERS_VERIFIED` only after at least one patent publication has been independently verified and preserved with sufficient metadata for practitioner review.
