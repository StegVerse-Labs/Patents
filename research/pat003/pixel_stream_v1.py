"""Bounded-memory PAT-003 research replay, separate authorization of reuse.

Source-only experiment: no authentic StegVerse runtime authorization asserted.
A frame iterable of grayscale 8-bit integer rows is supplied by a caller.
"""
from dataclasses import dataclass
from hashlib import sha256
from json import dumps
from time import perf_counter_ns

ALLOW, DENY, FAIL_CLOSED = "ALLOW", "DENY", "FAIL_CLOSED"


def digest(value):
    return sha256(dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class FrameResult:
    index: int
    allow: int
    deny: int
    fail_closed: int
    reuse_allow: int
    reconstruction_equal: bool
    receipt_root: str


def replay(frames, *, source_sha256, dependencies_verified=True,
           reuse_authorized=True, expected_frames=None):
    """Yield one frame summary at a time; never retain whole video or pixel receipts.

    Full pixel scan is required here. Hash chaining commits every operation
    disposition, including reuse authorization, but is not a Merkle membership
    proof. Source SHA is caller-supplied and must be independently verified.
    """
    if not isinstance(source_sha256, str) or len(source_sha256) != 64 or any(
        c not in "0123456789abcdef" for c in source_sha256
    ):
        raise ValueError("invalid source SHA-256")
    previous = None
    root = "0" * 64
    count = 0
    for index, frame in enumerate(frames):
        frame = tuple(tuple(row) for row in frame)
        if not frame or not frame[0] or any(len(row) != len(frame[0]) for row in frame):
            raise ValueError("invalid frame geometry")
        if previous is not None and (len(frame), len(frame[0])) != (len(previous), len(previous[0])):
            raise ValueError("frame dimensions changed")
        allow = deny = fail = reuse_allow = 0
        reconstructed = []
        for y, row in enumerate(frame):
            out = []
            for x, pixel in enumerate(row):
                old = previous[y][x] if previous is not None else None
                valid = type(pixel) is int and 0 <= pixel <= 255
                if not valid or not dependencies_verified:
                    disposition, predicate, value = FAIL_CLOSED, "INVALID_OR_UNVERIFIED", None
                    reuse = "NOT_REQUESTED"
                    fail += 1
                elif old is None or pixel != old:
                    disposition, predicate, value = ALLOW, "INITIAL_OR_CHANGED", pixel
                    reuse = "NOT_REQUESTED"
                    allow += 1
                else:
                    disposition, predicate = DENY, "UNCHANGED_RECOMPUTATION"
                    deny += 1
                    reuse = ALLOW if reuse_authorized else FAIL_CLOSED
                    value = old if reuse == ALLOW else None
                    if reuse == ALLOW:
                        reuse_allow += 1
                    else:
                        fail += 1
                root = digest(["pat003-stream-v1", source_sha256, root, index, x, y,
                               old, pixel, "RECOMPUTE_PIXEL", disposition,
                               predicate, "REUSE_PIXEL", reuse])
                out.append(value)
            reconstructed.append(tuple(out))
        equal = tuple(reconstructed) == frame
        yield FrameResult(index, allow, deny, fail, reuse_allow, equal, root)
        previous = frame
        count += 1
    if count == 0:
        raise ValueError("no frames")
    if expected_frames is not None and count != expected_frames:
        raise ValueError("missing or excess frames")


def benchmark(frames, *, source_sha256):
    """Replay a bounded in-memory sample; report measured wall time, no speedup claim."""
    frames = tuple(tuple(tuple(row) for row in frame) for frame in frames)
    start = perf_counter_ns()
    baseline = tuple(tuple(tuple(row) for row in frame) for frame in frames)
    baseline_ns = perf_counter_ns() - start
    start = perf_counter_ns()
    summaries = tuple(replay(frames, source_sha256=source_sha256))
    governed_ns = perf_counter_ns() - start
    return {"frames": len(frames), "baseline_ns": baseline_ns,
            "governed_ns": governed_ns,
            "reconstruction_equal": all(s.reconstruction_equal for s in summaries),
            "allow": sum(s.allow for s in summaries),
            "deny": sum(s.deny for s in summaries),
            "fail_closed": sum(s.fail_closed for s in summaries),
            "last_receipt_root": summaries[-1].receipt_root if summaries else None,
            "baseline_reference_equal": baseline == frames}
