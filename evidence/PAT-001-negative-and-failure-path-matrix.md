# PAT-001 Negative and Failure Path Matrix

**Status:** working executable-evidence plan; not a patentability or filing conclusion

## Purpose

This matrix preserves the negative, refusal, and fail-closed behaviors that distinguish the governed micro-node architecture from a permissive worker or agent runtime. A positive-path demonstration alone is insufficient to establish the claimed transition boundary.

## Verified Core Paths

| Path ID | Input condition | Required result | Existing evidence | Status |
|---|---|---|---|---|
| NF-001 | required request field missing | `FAIL_CLOSED` | `micro_node/runtime.py` required-field evaluation | verified implementation |
| NF-002 | delegation reference missing or invalid | `DENY` | authority checker role | verified implementation |
| NF-003 | policy reference missing | `DENY` | admissibility gate role | verified implementation |
| NF-004 | required role absent from execution | runtime error / no governed result | required-role coverage check | verified implementation |
| NF-005 | identical admitted request replayed | deterministic receipt hash | receipt determinism verifier | verified implementation |
| NF-006 | return path present | governed result includes return-path evidence | return-path carrier role | verified implementation |
| NF-007 | reconstruction inputs present | witness binds request, roles, receipt, and return payload | reconstruction witness | verified implementation |

## High-Value Unverified Paths

| Path ID | Input condition | Required result | Evidence needed | Current posture |
|---|---|---|---|---|
| NF-101 | capable admissible node already active | reuse admitted node; do not construct duplicate | capability registry query fixture and receipt | open |
| NF-102 | no admissible capable node exists | construct only minimum manifest-required node | constructor fixture, build manifest, receipt | open |
| NF-103 | proposed build exceeds manifest scope | deny or reduce build before activation | addressability comparison test | open |
| NF-104 | undeclared construction method proposed | fail closed | constructor allowlist test | open |
| NF-105 | task completes with no external usage evidence | expire node and preserve receipt | expiry fixture and disposal receipt | open |
| NF-106 | node heartbeat continues without external usage | heartbeat must not renew persistence | retention-policy test | open |
| NF-107 | valid conversation/stream lease exists | delayed expiry with bounded context | usage-lease fixture and receipt | open |
| NF-108 | retained context requests broader authority | deny authority expansion while permitting bounded reuse | context-boundary test | open |
| NF-109 | lease expires or external use ends | terminate retained node | lease-expiry test and receipt | open |
| NF-110 | reconstruction hash differs on replay | report mismatch and fail verification | tamper fixture | open |

## Fixture Requirements

Each preserved negative fixture should include:

1. canonical input JSON;
2. policy and delegation references;
3. expected decision;
4. expected reason code;
5. expected receipt fields;
6. actual output;
7. stable hashes;
8. source repository, path, and commit;
9. execution timestamp;
10. verifier result.

## Claim-Support Rule

A limitation must not be promoted from proposed to verified solely because this matrix describes the expected behavior. Promotion requires committed executable evidence or independently corroborated documentary evidence.

## Filing Boundary

This matrix supports technical review only. It does not determine novelty, non-obviousness, inventorship, enablement, or filing readiness.