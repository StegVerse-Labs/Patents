"""PAT-003 source-only pixel computation governance research fixture.

No authentic StegVerse runtime authority is asserted. A decision applies to a
specific operation, pixel and source-bound predecessor observation. Raw observations
are supplied by the caller; this module does not authenticate camera capture.
"""
from dataclasses import dataclass
from hashlib import sha256
from json import dumps

ALLOW = "ALLOW"
DENY = "DENY"
FAIL_CLOSED = "FAIL_CLOSED"


@dataclass(frozen=True)
class Decision:
    frame: int
    x: int
    y: int
    operation: str
    disposition: str
    predicate: str
    predecessor_digest: str
    observation_digest: str
    receipt_digest: str


def _digest(obj):
    return sha256(dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def execute(frames, *, source_sha256, dependencies_verified=True, policy_version="pat003-pixel-v1"):
    """Replay rectangular arrays of integer grayscale pixel values.

    This deliberately simple full-scan implementation tests authorization,
    not a claim of accelerated change detection. Reconstructed output and
    per-operation dispositions are deterministic. Invalid evidence FAILS CLOSED.
    """
    if not isinstance(source_sha256, str) or len(source_sha256) != 64 or any(
        c not in "0123456789abcdef" for c in source_sha256
    ):
        raise ValueError("source digest required")
    if not frames:
        raise ValueError("frames required")
    previous = None
    receipts = []
    reconstructed = []
    prior_receipt = "0" * 64
    for t, frame in enumerate(frames):
        if not frame or not frame[0] or any(len(row) != len(frame[0]) for row in frame):
            raise ValueError("nonrectangular observation")
        if previous is not None and (len(frame) != len(previous) or len(frame[0]) != len(previous[0])):
            raise ValueError("frame dimensions changed")
        output = []
        for y, row in enumerate(frame):
            outrow = []
            for x, value in enumerate(row):
                valid = type(value) is int and 0 <= value <= 255
                predecessor = previous[y][x] if previous is not None else None
                observation_digest = _digest([source_sha256, t, x, y, value])
                predecessor_digest = _digest([source_sha256, t - 1, x, y, predecessor])
                if not dependencies_verified or not valid:
                    disposition, predicate = FAIL_CLOSED, "UNVERIFIED_DEPENDENCY_OR_PIXEL"
                    result = None
                elif predecessor is None or value != predecessor:
                    disposition, predicate = ALLOW, "INITIAL_OR_CHANGED_PIXEL"
                    result = value
                else:
                    disposition, predicate = DENY, "UNCHANGED_RECOMPUTATION"
                    result = predecessor
                record = [policy_version, source_sha256, prior_receipt, t, x, y,
                          "RECOMPUTE_PIXEL", disposition, predicate,
                          predecessor_digest, observation_digest]
                receipt_digest = _digest(record)
                receipts.append(Decision(t, x, y, "RECOMPUTE_PIXEL", disposition,
                                         predicate, predecessor_digest,
                                         observation_digest, receipt_digest))
                prior_receipt = receipt_digest
                outrow.append(result)
            output.append(tuple(outrow))
        reconstructed.append(tuple(output))
        previous = frame
    return tuple(reconstructed), tuple(receipts)


def summarize(receipts):
    return {state: sum(r.disposition == state for r in receipts)
            for state in (ALLOW, DENY, FAIL_CLOSED)}
