# PAT-005 Destination and Guardian Evidence Anchors

**Status:** verified repository evidence map  
**Legal status:** technical preservation record only; not filed; not a patentability opinion

## StegTalk Destination Receipt

Repository: `StegVerse-Labs/StegTalk`

Path:

- `receipts/device-continuity/stegtalk-device-continuity-receipt.json`

Commit:

- `0e7b153faba53adc2bac7277e33c50c9f8075343`

Recorded technical facts:

- receipt id: `stegtalk-device-continuity-receipt-v0.1.0`
- payload id: `device-continuity-stegtalk-handoff-v0.1.0`
- decision: `accepted_observe_only`
- non-authorizing: `true`
- reconstructable: `true`

This is direct destination-side evidence that receipt acceptance did not independently authorize device operation.

## StegMusic Destination Receipt

Repository: `StegVerse-Labs/StegMusic`

Path:

- `receipts/device-continuity/stegmusic-device-continuity-receipt.json`

Commit:

- `87d1e7ec2151d6dcc416f9246b003c288c2853c1`

Recorded technical facts:

- receipt id: `stegmusic-device-continuity-receipt-v0.1.0`
- payload id: `device-continuity-stegmusic-handoff-v0.1.0`
- decision: `accepted_observe_only`
- non-authorizing: `true`
- reconstructable: `true`

This is direct destination-side evidence that media-device continuity intake remained distinct from playback, routing, or control authority.

## Guardian Boundary Page

Repository: `StegVerse-002/stegguardian-wiki`

Path:

- `pages/device-continuity-guardian-boundary.md`

Commit:

- `dc7d7891552de0f93229296b896a48031f1459b8`

Recorded technical boundary:

- Device Continuity output is a handoff candidate.
- It is not operator approval.
- It is not active device trust.
- It is not destination behavior authority.
- unknown devices remain review-only until destination policy accepts them;
- destination repositories must issue their own receipts;
- observations must remain reconstructable.

## Guardian Receipt

Repository: `StegVerse-002/stegguardian-wiki`

Path:

- `receipts/device-continuity-receipt.json`

Commit:

- `ad6d123a750a8dcf521137c2dfdf6d0913c5235d`

Recorded technical facts:

- receipt id: `guardian-device-continuity-v0.1.0`
- decision: `recorded`
- reconstructable: `true`

The guardian receipt records propagation of the boundary. It does not establish destination activation or operational authority.

## Additional Destination Commit Chains

### StegTalk

- docs installation: `28d84cf202dc948889d444fb6c3ac52865115041`
- contract installation: `0acc2835220966686dcfd3ebe96c572182784edd`
- handoff payload installation: `1c1675f962cb9f3856168ec06f165937830846a5`
- sample receipt installation: `79762bb6b53d6ae0f19c47233510b58e40bab2cd`
- destination receipt installation: `0e7b153faba53adc2bac7277e33c50c9f8075343`
- receipt validator: `4f328f0332016a8ac08f7cc8cf1963a57a506ad5`
- receipt test: `699114621bfb9ae5f686d642ffb2926cdc0ed4dc`
- validation workflow: `5db5d83dadc93ff419245b31e48e4ffb3fc5266a`

### StegMusic

- docs installation: `f749c59759d2d81806dc45075f32af32f440b63f`
- contract installation: `c271e2041e5e191e49e50f4b4ed6ea41d883661d`
- handoff payload installation: `ec6002ed372f38aaf697e274f2ad322a23369653`
- sample receipt installation: `b23e358207e43a993a46dc0964580cd88163bfcb`
- destination receipt installation: `87d1e7ec2151d6dcc416f9246b003c288c2853c1`
- receipt validator: `73650898a6d847d9c48416642e8fe3cda31709b1`
- receipt test: `7e6960c1532173156942fbe25eaf0194ed245a10`
- validation workflow: `0ea1ff406fde89ec9c2ca019697c3ded83ff0e5e`

## Claim Relevance

These anchors support candidate limitations concerning:

1. destination-side receipt issuance;
2. observation-only acceptance;
3. explicit non-authorization;
4. independent destination validation;
5. reconstructability across repository boundaries;
6. guardian preservation of refusal and review-only states;
7. separation of technical handoff, trust, behavior authority, and activation.
