"""PAT-003 E-WIFI-1: deterministic replay of an 802.11 capture (stdlib only, source-only research).

Experiment harness for a candidate additional anchor (CA-4). It reads a classic libpcap
capture with link type 105 (IEEE 802.11) or 127 (radiotap + 802.11). It extracts a
per-frame stream (capture-host time, receiver TSFT, beacon TSF, frame type/subtype, retry
flag, sequence number, frame digest) and commits each frame into a hash chain.

The frame-level comparison against a recorded manifest localizes the first divergent
frame for drop, reorder, byte-alteration and re-timing controls.

Output is counts and hashes only. Transmitter addresses are reduced to a truncated digest
and never emitted. The harness does not authenticate a radio, a capture host or a
StegVerse runtime. It asserts no claim and is evidence input only: not truth, not legal
determination, not execution authority.
"""
from hashlib import sha256
from json import dumps
import struct

SCHEMA = "stegverse.patents.pat003-e-wifi-1/v1"
SUPPORTED_LINKTYPES = (105, 127)
ACCEPT, REJECT, FAIL_CLOSED = "ACCEPT", "REJECT", "FAIL_CLOSED"


class TraceError(ValueError):
    """Input cannot be evaluated; the caller must fail closed."""


def _digest(value):
    return sha256(dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read_pcap(data):
    """Return (linktype, [(ts_us, frame_bytes)]) for a classic pcap byte string."""
    if len(data) < 24:
        raise TraceError("PCAP_TOO_SHORT")
    magic = data[:4]
    if magic == b"\xd4\xc3\xb2\xa1":
        e, nano = "<", False
    elif magic == b"\xa1\xb2\xc3\xd4":
        e, nano = ">", False
    elif magic == b"\x4d\x3c\xb2\xa1":
        e, nano = "<", True
    elif magic == b"\xa1\xb2\x3c\x4d":
        e, nano = ">", True
    else:
        raise TraceError("PCAP_MAGIC_UNSUPPORTED")
    linktype = struct.unpack(e + "I", data[20:24])[0] & 0x0FFFFFFF
    if linktype not in SUPPORTED_LINKTYPES:
        raise TraceError("LINKTYPE_UNSUPPORTED")
    out, off = [], 24
    while off < len(data):
        if off + 16 > len(data):
            raise TraceError("PCAP_RECORD_HEADER_TRUNCATED")
        sec, frac, incl, _orig = struct.unpack(e + "IIII", data[off:off + 16])
        body = data[off + 16:off + 16 + incl]
        if len(body) != incl:
            raise TraceError("PCAP_RECORD_TRUNCATED")
        out.append((sec * 1_000_000 + (frac // 1000 if nano else frac), body))
        off += 16 + incl
    return linktype, out


def _radiotap(pkt):
    if len(pkt) < 8 or pkt[0] != 0:
        raise TraceError("RADIOTAP_HEADER_INVALID")
    rlen = struct.unpack("<H", pkt[2:4])[0]
    if rlen < 8 or rlen > len(pkt):
        raise TraceError("RADIOTAP_LENGTH_INVALID")
    present = [struct.unpack("<I", pkt[4:8])[0]]
    pos = 8
    while present[-1] & 0x80000000:
        if pos + 4 > rlen:
            raise TraceError("RADIOTAP_PRESENT_TRUNCATED")
        present.append(struct.unpack("<I", pkt[pos:pos + 4])[0])
        pos += 4
    first = present[0]
    tsft = flags = rate = None
    if first & 0x1:
        pos = (pos + 7) & ~7
        if pos + 8 > rlen:
            raise TraceError("RADIOTAP_TSFT_TRUNCATED")
        tsft = struct.unpack("<Q", pkt[pos:pos + 8])[0]
        pos += 8
    if first & 0x2:
        flags = pkt[pos] if pos < rlen else None
        pos += 1
    if first & 0x4:
        rate = pkt[pos] if pos < rlen else None
        pos += 1
    return tsft, flags, rate, pkt[rlen:]


def extract_stream(data):
    """Parse capture bytes into the per-frame stream used by replay and the controls."""
    linktype, records = read_pcap(data)
    stream = []
    for index, (ts_us, pkt) in enumerate(records):
        tsft = flags = rate = None
        frame = pkt
        if linktype == 127:
            tsft, flags, rate, frame = _radiotap(pkt)
        entry = {"index": index, "host_us": ts_us, "tsft_us": tsft, "rate_500kbps": rate,
                 "frame_sha256": sha256(frame).hexdigest(), "type": None, "subtype": None,
                 "retry": None, "seq": None, "beacon_tsf_us": None, "ta_tag": None}
        if len(frame) >= 2:
            fc = struct.unpack("<H", frame[:2])[0]
            entry["type"], entry["subtype"] = (fc >> 2) & 3, (fc >> 4) & 0xF
            entry["retry"] = (fc >> 11) & 1
            if entry["type"] in (0, 2) and len(frame) >= 24:
                entry["seq"] = struct.unpack("<H", frame[22:24])[0] >> 4
                entry["ta_tag"] = sha256(frame[10:16]).hexdigest()[:12]
                if entry["type"] == 0 and entry["subtype"] in (5, 8) and len(frame) >= 32:
                    entry["beacon_tsf_us"] = struct.unpack("<Q", frame[24:32])[0]
        stream.append(entry)
    if not stream:
        raise TraceError("NO_FRAMES")
    return linktype, stream


def replay(stream, *, source_sha256):
    """Commit every frame entry into a hash chain; return per-frame digests and roots."""
    if not isinstance(source_sha256, str) or len(source_sha256) != 64 or any(
            c not in "0123456789abcdef" for c in source_sha256):
        raise TraceError("SOURCE_SHA256_INVALID")
    root, entries, roots = "0" * 64, [], []
    for e in stream:
        d = _digest(e)
        root = _digest([SCHEMA, source_sha256, root, d])
        entries.append(d)
        roots.append(root)
    return {"schema": SCHEMA, "source_sha256": source_sha256, "count": len(entries),
            "entry_digests": entries, "roots": roots, "final_root": roots[-1] if roots else None}


def compare(manifest, candidate):
    """Compare a candidate replay to a recorded manifest. REJECT names the first divergent frame."""
    if manifest.get("schema") != SCHEMA or candidate.get("schema") != SCHEMA:
        return {"verdict": FAIL_CLOSED, "reason": "SCHEMA_MISMATCH", "first_divergent_index": None}
    a, b = manifest["entry_digests"], candidate["entry_digests"]
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return {"verdict": REJECT, "reason": "FRAME_ENTRY_DIVERGES", "first_divergent_index": i}
    if len(a) != len(b):
        return {"verdict": REJECT, "reason": "FRAME_COUNT_DIFFERS", "first_divergent_index": min(len(a), len(b))}
    if manifest["final_root"] != candidate["final_root"]:
        return {"verdict": REJECT, "reason": "CHAIN_ROOT_DIFFERS", "first_divergent_index": None}
    return {"verdict": ACCEPT, "reason": "IDENTICAL", "first_divergent_index": None}


def clock_consistency(stream):
    """Observe the three clocks: capture host, receiver TSFT, transmitter beacon TSF.

    These are counts only, with no pass threshold: an observation, not a verification
    of any claim.
    """
    host = [e["host_us"] for e in stream]
    tsft = [e["tsft_us"] for e in stream if e["tsft_us"] is not None]
    offs = [e["tsft_us"] - e["host_us"] for e in stream if e["tsft_us"] is not None]
    per_tx = {}
    for e in stream:
        if e["beacon_tsf_us"] is not None:
            per_tx.setdefault(e["ta_tag"], []).append(e["beacon_tsf_us"])
    pairs = lambda xs: sum(1 for x, y in zip(xs, xs[1:]) if y >= x)
    return {
        "frames": len(stream),
        "host_nondecreasing_pairs": pairs(host), "host_pairs": max(len(host) - 1, 0),
        "tsft_frames": len(tsft),
        "tsft_nondecreasing_pairs": pairs(tsft), "tsft_pairs": max(len(tsft) - 1, 0),
        "tsft_minus_host_spread_us": (max(offs) - min(offs)) if offs else None,
        "beacon_transmitters": len(per_tx),
        "beacon_frames": sum(len(v) for v in per_tx.values()),
        "beacon_tsf_nondecreasing_pairs": sum(pairs(v) for v in per_tx.values()),
        "beacon_tsf_pairs": sum(max(len(v) - 1, 0) for v in per_tx.values()),
    }


# ---------------------------------------------------------------- byte-level negative controls
def _records(data):
    e = "<" if data[:4] in (b"\xd4\xc3\xb2\xa1", b"\x4d\x3c\xb2\xa1") else ">"
    recs, off = [], 24
    while off + 16 <= len(data):
        incl = struct.unpack(e + "I", data[off + 8:off + 12])[0]
        recs.append(bytearray(data[off:off + 16 + incl]))
        off += 16 + incl
    return e, data[:24], recs


def control_drop(data, k):
    _, hdr, recs = _records(data)
    del recs[k]
    return hdr + b"".join(recs)


def control_reorder(data, k):
    _, hdr, recs = _records(data)
    recs[k], recs[k + 1] = recs[k + 1], recs[k]
    return hdr + b"".join(recs)


def control_alter_byte(data, k):
    """Flip the last byte of record k (a frame byte, never a radiotap header byte)."""
    _, hdr, recs = _records(data)
    recs[k][-1] ^= 0x01
    return hdr + b"".join(recs)


def control_shift_time(data, k, delta_us=1000):
    e, hdr, recs = _records(data)
    sec, frac = struct.unpack(e + "II", bytes(recs[k][:8]))
    total = sec * 1_000_000 + frac + delta_us
    recs[k][:8] = struct.pack(e + "II", total // 1_000_000, total % 1_000_000)
    return hdr + b"".join(recs)


def run_experiment(data, k=None):
    """E-WIFI-1 on one capture: replay twice, run four negative controls, observe the clocks."""
    src = sha256(data).hexdigest()
    _, s1 = extract_stream(data)
    _, s2 = extract_stream(data)
    m1, m2 = replay(s1, source_sha256=src), replay(s2, source_sha256=src)
    k = len(s1) // 2 if k is None else k
    if not 0 <= k < len(s1) - 1:
        raise TraceError("CONTROL_INDEX_OUT_OF_RANGE")
    controls = {}
    for name, fn in (("drop", control_drop), ("reorder", control_reorder),
                     ("alter_byte", control_alter_byte), ("shift_time", control_shift_time)):
        tampered = fn(data, k)
        _, ts = extract_stream(tampered)
        res = compare(m1, replay(ts, source_sha256=src))
        controls[name] = {"tampered_sha256": sha256(tampered).hexdigest(), **res,
                          "rejected": res["verdict"] == REJECT}
    return {"schema": SCHEMA, "source_sha256": src, "frames": len(s1), "control_index": k,
            "replay_identical": m1["final_root"] == m2["final_root"] and compare(m1, m2)["verdict"] == ACCEPT,
            "final_root": m1["final_root"], "controls": controls,
            "all_controls_rejected": all(c["rejected"] for c in controls.values()),
            "clocks": clock_consistency(s1),
            "c10": "OPEN", "authority_effect": "NONE_EVIDENCE_INPUT_ONLY"}
