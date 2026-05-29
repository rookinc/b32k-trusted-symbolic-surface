#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ANCHORS = [
    ("A01", "Physical/Foundation"),
    ("A02", "Information/Signal"),
    ("A03", "Language/Symbolic"),
    ("A04", "Mathematical/Structural"),
    ("A05", "Logical/Algorithmic"),
    ("A06", "Biological/Adaptive"),
    ("A07", "Conscious/Observational"),
    ("A08", "Eidronic/Reflective"),
    ("A09", "Cultural/Linguistic"),
    ("A10", "Technological/Synthetic"),
    ("A11", "Matricial/Geometric"),
    ("A12", "Ethical/Normative"),
    ("A13", "Mythic/Narrative"),
    ("A14", "Planetary/Ecological"),
    ("A15", "Transcendent/Coherent"),
]

def entry(index):
    zero = index - 1
    plane = zero // 1024
    within = zero % 1024
    r = within // 32
    c = within % 32
    anchor_domain, anchor_label = ANCHORS[zero % 15]
    return {
        "index": index,
        "hex": f"0x{index:04X}",
        "unicode_point": f"U+{index:04X}",
        "plane": plane,
        "r": r,
        "c": c,
        "anchor_domain": anchor_domain,
        "anchor_label": anchor_label,
    }

def main():
    entries = [entry(i) for i in range(1, 32768)]

    (ROOT / "artifacts/json").mkdir(parents=True, exist_ok=True)
    (ROOT / "artifacts/csv").mkdir(parents=True, exist_ok=True)

    payload = {
        "registry": "B32K Canonical Alphabet",
        "version": "1.0-generated",
        "count": len(entries),
        "index_min": 1,
        "index_max": 32767,
        "plane_size": 1024,
        "row_size": 32,
        "column_size": 32,
        "anchors": [
            {"anchor_domain": a, "anchor_label": b}
            for a, b in ANCHORS
        ],
        "entries": entries,
    }

    json_path = ROOT / "artifacts/json/b32k_canonical_alphabet.json"
    csv_path = ROOT / "artifacts/csv/b32k_canonical_alphabet.csv"

    json_path.write_text(json.dumps(payload, indent=2) + "\n")

    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(entries[0].keys()))
        writer.writeheader()
        writer.writerows(entries)

    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    print(f"entries: {len(entries)}")

if __name__ == "__main__":
    main()
