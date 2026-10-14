"""PAT-003 source-only double-pendulum alignment adapter v1.0.

No dataset bundled. This adapter validates externally supplied, calibrated
time-series; it does not establish authentic synchronization or physical truth.
Frozen optical v0.7 is not imported or modified.
"""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from math import isfinite
from typing import Sequence


class EvidenceRejected(ValueError):
    pass


@dataclass(frozen=True)
class Series:
    trial: str
    source_sha256: str
    times: tuple[float, ...]
    values: tuple[float, ...]
    clock: str
    calibration: str

    def validate(self) -> None:
        if not self.trial or not self.clock or not self.calibration:
            raise EvidenceRejected("missing trial, clock or calibration")
        if len(self.source_sha256) != 64 or any(c not in "0123456789abcdef" for c in self.source_sha256):
            raise EvidenceRejected("invalid source digest")
        if len(self.times) != len(self.values) or len(self.times) < 3:
            raise EvidenceRejected("insufficient or unequal samples")
        if any(not isfinite(x) for x in self.times + self.values):
            raise EvidenceRejected("non-finite sample")
        if any(b <= a for a, b in zip(self.times, self.times[1:])):
            raise EvidenceRejected("non-monotonic or repeated timestamp")


def hash_source(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def align(a: Series, b: Series, *, tolerance: float, clock_mapping_verified: bool = False) -> list[tuple[float, float, float]]:
    a.validate()
    b.validate()
    if a.trial != b.trial:
        raise EvidenceRejected("trial mismatch")
    if not clock_mapping_verified:
        raise EvidenceRejected("clock mapping unverified")
    if a.clock != b.clock:
        raise EvidenceRejected("different clock domains without an explicit mapping")
    if tolerance <= 0 or not isfinite(tolerance):
        raise EvidenceRejected("invalid tolerance")
    result = []
    j = 0
    for t, value in zip(a.times, a.values):
        while j + 1 < len(b.times) and abs(b.times[j + 1] - t) < abs(b.times[j] - t):
            j += 1
        if abs(b.times[j] - t) <= tolerance:
            result.append((t, value, b.values[j]))
    if not result:
        raise EvidenceRejected("no aligned observations")
    return result
