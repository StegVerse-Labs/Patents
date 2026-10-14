"""PAT-003 authentic governance return boundary, source-only contract.

This module never issues sovereign ALLOW itself. It verifies an externally
supplied, operation-bound decision envelope. Until a verified return is supplied,
all requested operations are FAIL_CLOSED. Do not substitute research policy
predictions for authenticated governance returns.
"""
from dataclasses import dataclass
from hashlib import sha256
from hmac import compare_digest
from json import dumps

STATES = frozenset(("ALLOW", "DENY", "FAIL_CLOSED"))


def digest(value):
    return sha256(dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class Request:
    source_sha256: str
    frame: int
    x: int
    y: int
    operation: str
    predecessor_digest: str
    observation_digest: str
    policy_digest: str
    task_id: str

    def validate(self):
        for name in ("source_sha256", "predecessor_digest",
                     "observation_digest", "policy_digest"):
            value = getattr(self, name)
            if not isinstance(value, str) or len(value) != 64 or any(
                c not in "0123456789abcdef" for c in value
            ):
                raise ValueError("invalid " + name)
        if any(type(v) is not int or v < 0 for v in (self.frame, self.x, self.y)):
            raise ValueError("invalid coordinate")
        if self.operation not in ("RECOMPUTE_PIXEL", "REUSE_PIXEL") or not self.task_id:
            raise ValueError("invalid operation or task")


@dataclass(frozen=True)
class Return:
    request_digest: str
    disposition: str
    predicate: str
    authority_reference: str
    evidence_reference: str
    authenticated: bool


def evaluate(request, governance_return=None):
    """Fail closed unless a bound, authenticated return exists.

    authenticated is a claim carried by the adapter; a production caller must
    independently establish cryptographic and sovereign ledger provenance.
    This research boundary never confers authority merely from that boolean.
    """
    request.validate()
    request_digest = digest(request.__dict__)
    if governance_return is None:
        return ("FAIL_CLOSED", "AUTHENTIC_GOVERNANCE_RETURN_NOT_PROVIDED", request_digest)
    if not isinstance(governance_return, Return):
        return ("FAIL_CLOSED", "MALFORMED_GOVERNANCE_RETURN", request_digest)
    if not compare_digest(governance_return.request_digest, request_digest):
        return ("FAIL_CLOSED", "RETURN_NOT_BOUND_TO_REQUEST", request_digest)
    if governance_return.disposition not in STATES:
        return ("FAIL_CLOSED", "INVALID_DISPOSITION", request_digest)
    if not governance_return.predicate or not governance_return.authority_reference or not governance_return.evidence_reference:
        return ("FAIL_CLOSED", "INCOMPLETE_AUTHORITY_EVIDENCE", request_digest)
    if not governance_return.authenticated:
        return ("FAIL_CLOSED", "AUTHENTICITY_NOT_ESTABLISHED", request_digest)
    # A caller-controlled flag cannot certify a sovereign return. Strict
    # source-only mode deliberately withholds ALLOW and DENY.
    return ("FAIL_CLOSED", "SOVEREIGN_RETURN_VERIFIER_NOT_INTEGRATED", request_digest)
