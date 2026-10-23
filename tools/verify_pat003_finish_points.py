#!/usr/bin/env python3
"""CLI entrypoint for the PAT-003 finish-point structural verifier (E0, stdlib only).

The implementation is research/pat003/finish_point_verifier_v1.py. Output is evidence input
only: not truth, not legal determination, not execution authority.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research", "pat003"))
from finish_point_verifier_v1 import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
