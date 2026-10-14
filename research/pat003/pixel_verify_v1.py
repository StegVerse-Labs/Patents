"""PAT-003 streaming replay verification and bounded-sample comparative controls.

Source-only research. This does not authenticate a camera, external decoder,
or StegVerse runtime authorization.
"""
from hashlib import sha256
from json import dumps
from time import perf_counter_ns
from pixel_stream_v1 import replay


def _hash(obj):
    return sha256(dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify_replay(frames, *, source_sha256, dependencies_verified=True,
                  reuse_authorized=True, expected_frames=None):
    """Independent frame-count and output-equality audit of streaming summaries.

    This verifies repeatability and expected counts, not membership proofs for
    individual pixels: those require an authenticated runtime and evidence access.
    """
    results = list(replay(frames, source_sha256=source_sha256,
                          dependencies_verified=dependencies_verified,
                          reuse_authorized=reuse_authorized,
                          expected_frames=expected_frames))
    totals = {"ALLOW": sum(r.allow for r in results),
              "DENY": sum(r.deny for r in results),
              "FAIL_CLOSED": sum(r.fail_closed for r in results),
              "REUSE_ALLOW": sum(r.reuse_allow for r in results)}
    return {"frame_count": len(results), "totals": totals,
            "reconstruction_equal": all(r.reconstruction_equal for r in results),
            "last_root": results[-1].receipt_root,
            "per_frame": [r.__dict__ for r in results]}


def compare_bounded_sample(frames, *, source_sha256):
    """Compare full-copy baseline to governed replay, including hashing overhead.

    Decoding is excluded from both arms. No energy or physical-state accuracy
    is inferred. The supplied sample must fit in memory.
    """
    frames = tuple(tuple(tuple(row) for row in frame) for frame in frames)
    if not frames:
        raise ValueError("empty sample")
    start = perf_counter_ns()
    reference = tuple(tuple(tuple(row) for row in frame) for frame in frames)
    baseline_ns = perf_counter_ns() - start
    start = perf_counter_ns()
    result = verify_replay(frames, source_sha256=source_sha256,
                           expected_frames=len(frames))
    governed_ns = perf_counter_ns() - start
    result.update({"baseline_ns": baseline_ns, "governed_ns": governed_ns,
                   "baseline_equal": reference == frames,
                   "scope": "in_memory_decoded_grayscale_sample_only",
                   "decoder_cost_included": False,
                   "authentic_governance": False})
    return result


def adversarial_frame_commitment(frames):
    """Commit ordered decoded frame values; different order/value -> different hash."""
    chain = "0" * 64
    for i, frame in enumerate(frames):
        chain = _hash([chain, i, frame])
    return chain
