"""Fail-closed private input gate; no private bytes included in repository."""
import hashlib
import json
import os
import sys
from pathlib import Path


def verify(root: Path, manifest: dict, *, require_complete: bool = True) -> dict:
    findings = []
    for item in manifest["expected_sources"]:
        p = root / item["name"]
        entry = {"name": item["name"], "status": "FAIL_CLOSED"}
        if not p.is_file():
            entry["reason"] = "MISSING_SOURCE"
        elif p.stat().st_size != item["size_bytes"]:
            entry["reason"] = "SIZE_MISMATCH"
        elif not item["sha256"]:
            entry["reason"] = "EXPECTED_DIGEST_UNVERIFIED"
        else:
            digest = hashlib.sha256()
            with p.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            if digest.hexdigest() == item["sha256"]:
                entry.update(status="PASS", reason="EXACT_BYTES_VERIFIED")
            else:
                entry["reason"] = "DIGEST_MISMATCH"
        findings.append(entry)
    success = all(e["status"] == "PASS" for e in findings)
    return {"disposition": "ALLOW_SOURCE_BYTES_ONLY" if success else "FAIL_CLOSED", "results": findings}


def main() -> int:
    manifest = json.loads((Path(__file__).parent / "input_manifest_v1.json").read_text())
    root = os.environ.get("PAT003_PRIVATE_INPUT_DIR")
    if not root:
        print(json.dumps({"disposition": "FAIL_CLOSED", "reason": "PAT003_PRIVATE_INPUT_DIR_NOT_PROVIDED"}))
        return 2
    result = verify(Path(root), manifest)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["disposition"] == "ALLOW_SOURCE_BYTES_ONLY" else 2


if __name__ == "__main__":
    sys.exit(main())
