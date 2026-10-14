"""PAT-003 first-video, dual-lane comparison over original decoded grayscale frames.

Research implementation only. Caller must verify source bytes and decoder
provenance; this module does not confer or impersonate sovereign authority.
No original frames, proprietary media or experiment outputs are persisted.
"""
from hashlib import sha256
from json import dumps
from time import perf_counter_ns

from pixel_stream_v1 import replay


def _hash(value):
    return sha256(dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _validate(frames):
    materialized = []
    shape = None
    for frame in frames:
        f = tuple(tuple(row) for row in frame)
        if not f or not f[0] or any(len(r) != len(f[0]) for r in f):
            raise ValueError("invalid frame geometry")
        if any(type(v) is not int or not 0 <= v <= 255 for r in f for v in r):
            raise ValueError("invalid decoded pixel")
        if shape is None:
            shape = (len(f), len(f[0]))
        if shape != (len(f), len(f[0])):
            raise ValueError("frame geometry changed")
        materialized.append(f)
    if not materialized:
        raise ValueError("empty original observation")
    return tuple(materialized)


def compare(frames, *, source_sha256, reuse_authorized=True,
            dependencies_verified=True):
    """Compare both reconstruction histories with exactly the same original.

    Frame lane: full-copy observation with one predecessor-linked receipt per
    frame. Manifold lane: pixel-level disposition and separately bound reuse.
    A difference in receipt hashes is not a numerical change magnitude.
    Costs include each lane's Python receipt processing but exclude decoding,
    original-file acquisition, and external governance service.
    """
    original = _validate(frames)
    start = perf_counter_ns()
    frame_chain = "0" * 64
    frame_receipts = []
    frame_reconstruction = []
    for index, frame in enumerate(original):
        copied = tuple(tuple(v for v in row) for row in frame)
        frame_reconstruction.append(copied)
        frame_chain = _hash(["pat003-frame-v1", source_sha256, frame_chain, index, copied])
        frame_receipts.append(frame_chain)
    frame_ns = perf_counter_ns() - start

    start = perf_counter_ns()
    manifold = tuple(replay(original, source_sha256=source_sha256,
                            reuse_authorized=reuse_authorized,
                            dependencies_verified=dependencies_verified,
                            expected_frames=len(original)))
    manifold_ns = perf_counter_ns() - start
    frame_equal = tuple(frame_reconstruction) == original
    manifold_equal = all(r.reconstruction_equal for r in manifold)
    # The manifold engine reports per-frame exact reconstruction equality.
    # This also establishes frame-lane/manifold-lane equality when both equal O.
    return {
        "source_sha256": source_sha256,
        "frames": len(original),
        "pixels_per_frame": len(original[0]) * len(original[0][0]),
        "original_vs_frame_mismatches": 0 if frame_equal else None,
        "original_vs_manifold_mismatches": 0 if manifold_equal else None,
        "frame_vs_manifold_mismatches": 0 if frame_equal and manifold_equal else None,
        "frame_receipt_count": len(frame_receipts),
        "manifold_pixel_decisions": sum(r.allow + r.deny for r in manifold),
        "manifold_recompute_allow": sum(r.allow for r in manifold),
        "manifold_recompute_deny": sum(r.deny for r in manifold),
        "manifold_reuse_allow": sum(r.reuse_allow for r in manifold),
        "manifold_fail_closed": sum(r.fail_closed for r in manifold),
        "frame_chain_root": frame_chain,
        "manifold_chain_root": manifold[-1].receipt_root,
        "frame_lane_ns": frame_ns,
        "manifold_lane_ns": manifold_ns,
        "decoder_cost_included": False,
        "authentic_governance_verified": False,
        "experiment_scope": "decoded_grayscale_frames_source_only",
    }
