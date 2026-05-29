#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "artifacts/json/b32k_canonical_alphabet.json"

data = json.loads(path.read_text())
entries = data["entries"]

assert len(entries) == 32767
assert entries[0]["index"] == 1
assert entries[-1]["index"] == 32767

seen = set()
for e in entries:
    idx = e["index"]
    assert 1 <= idx <= 32767
    assert idx not in seen
    seen.add(idx)

    z = idx - 1
    assert e["plane"] == z // 1024
    assert e["r"] == (z % 1024) // 32
    assert e["c"] == z % 32
    assert e["hex"] == f"0x{idx:04X}"
    assert e["unicode_point"] == f"U+{idx:04X}"

print("B32K alphabet verification passed")
print(f"entries: {len(entries)}")
print(f"planes touched: {min(e['plane'] for e in entries)}..{max(e['plane'] for e in entries)}")
