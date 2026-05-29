#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "artifacts/json/b32k_canonical_alphabet.json"

def main():
    if len(sys.argv) != 2:
        print("usage: python scripts/lookup_b32k.py INDEX")
        raise SystemExit(2)

    idx = int(sys.argv[1])
    if idx == 0:
        print("index 0 is reserved / out-of-band / profile-controlled")
        return
    if not (1 <= idx <= 32767):
        print("index out of B32K 15-bit range")
        raise SystemExit(1)

    data = json.loads(path.read_text())
    e = data["entries"][idx - 1]

    print(f"index: {e['index']}")
    print(f"hex: {e['hex']}")
    print(f"unicode_point: {e['unicode_point']}")
    print(f"plane: {e['plane']}")
    print(f"r: {e['r']}")
    print(f"c: {e['c']}")
    print(f"anchor_domain: {e['anchor_domain']}")
    print(f"anchor_label: {e['anchor_label']}")

if __name__ == "__main__":
    main()
