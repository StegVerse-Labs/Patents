"""PAT-003 E-WIFI-1 harness: synthetic 802.11 captures only (no third-party capture data)."""
import struct
import sys
import unittest
from hashlib import sha256
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "research" / "pat003"))
import wifi_trace_replay_v1 as w


def _beacon(seq, tsf, ta=b"\x02\x00\x00\x00\x00\x01"):
    hdr = struct.pack("<HH", 0x0080, 0) + b"\xff" * 6 + ta + ta + struct.pack("<H", seq << 4)
    return hdr + struct.pack("<QHH", tsf, 100, 0x0401) + b"\x00\x04test"


def _data(seq, retry=0):
    fc = 0x0008 | (0x0800 if retry else 0)
    return struct.pack("<HH", fc, 0) + b"\x02\x00\x00\x00\x00\x09" * 3 + struct.pack("<H", seq << 4) + b"payload"


def _radiotap(frame, tsft, rate=0x0c, extended=False):
    if extended:
        present = struct.pack("<II", 0x80000007, 0)
        hl = 8 + 4
    else:
        present = struct.pack("<I", 0x00000007)
        hl = 8
    pad = (-hl) % 8
    body = b"\x00" * pad + struct.pack("<QBB", tsft, 0, rate)
    rlen = hl + len(body)
    return struct.pack("<BBH", 0, 0, rlen) + present + body + frame


def _pcap(frames, linktype=127, t0=1_700_000_000_000_000):
    out = [struct.pack("<IHHiIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, linktype)]
    for i, f in enumerate(frames):
        t = t0 + i * 1024
        out.append(struct.pack("<IIII", t // 1_000_000, t % 1_000_000, len(f), len(f)) + f)
    return b"".join(out)


def _capture(n=12, extended=False):
    frames = []
    for i in range(n):
        f = _beacon(i, 5_000_000 + i * 102_400) if i % 3 == 0 else _data(i, retry=int(i % 5 == 0))
        frames.append(_radiotap(f, 9_000_000 + i * 1024, extended=extended))
    return _pcap(frames)


class EWifi1Tests(unittest.TestCase):
    def test_extract_fields(self):
        lt, s = w.extract_stream(_capture())
        self.assertEqual(lt, 127)
        self.assertEqual(len(s), 12)
        self.assertEqual(s[0]["beacon_tsf_us"], 5_000_000)
        self.assertEqual(s[0]["tsft_us"], 9_000_000)
        self.assertEqual(s[5]["retry"], 1)
        self.assertEqual(s[4]["seq"], 4)

    def test_extended_present_bitmap(self):
        _, s = w.extract_stream(_capture(extended=True))
        self.assertEqual(s[1]["tsft_us"], 9_000_000 + 1024)

    def test_linktype_105(self):
        lt, s = w.extract_stream(_pcap([_data(1), _beacon(2, 7)], linktype=105))
        self.assertEqual((lt, s[0]["tsft_us"], s[1]["beacon_tsf_us"]), (105, None, 7))

    def test_replay_deterministic(self):
        r = w.run_experiment(_capture())
        self.assertTrue(r["replay_identical"])
        self.assertEqual(r["c10"], "OPEN")

    def test_every_negative_control_rejected_at_index(self):
        r = w.run_experiment(_capture(), k=4)
        self.assertTrue(r["all_controls_rejected"])
        for name in ("drop", "reorder", "alter_byte", "shift_time"):
            self.assertEqual(r["controls"][name]["verdict"], w.REJECT, name)
            self.assertEqual(r["controls"][name]["first_divergent_index"], 4, name)

    def test_drop_last_frame_counts(self):
        data = _capture()
        _, s = w.extract_stream(data)
        m = w.replay(s, source_sha256=sha256(data).hexdigest())
        _, t = w.extract_stream(data)
        c = w.replay(t[:-1], source_sha256=sha256(data).hexdigest())
        self.assertEqual(w.compare(m, c)["reason"], "FRAME_COUNT_DIFFERS")

    def test_clock_observation(self):
        c = w.clock_consistency(w.extract_stream(_capture())[1])
        self.assertEqual(c["beacon_frames"], 4)
        self.assertEqual(c["beacon_tsf_nondecreasing_pairs"], c["beacon_tsf_pairs"])
        self.assertEqual(c["tsft_minus_host_spread_us"], 0)

    def test_fail_closed_inputs(self):
        for bad, code in ((b"\x00" * 10, "PCAP_TOO_SHORT"),
                          (b"\x00" * 24, "PCAP_MAGIC_UNSUPPORTED"),
                          (_pcap([_data(1)], linktype=1), "LINKTYPE_UNSUPPORTED"),
                          (_pcap([]), "NO_FRAMES"),
                          (_capture()[:-3], "PCAP_RECORD_TRUNCATED")):
            with self.assertRaises(w.TraceError) as cm:
                w.extract_stream(bad)
            self.assertEqual(str(cm.exception), code)
        with self.assertRaises(w.TraceError):
            w.replay([], source_sha256="x")

    def test_schema_mismatch_fails_closed(self):
        self.assertEqual(w.compare({"schema": "other"}, {"schema": w.SCHEMA})["verdict"], w.FAIL_CLOSED)


if __name__ == "__main__":
    unittest.main()
