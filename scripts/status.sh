#!/usr/bin/env sh
set -eu

echo "B32K trusted symbolic surface status"
echo

python scripts/verify_b32k_alphabet.py

echo
echo "artifact sizes"
wc -c artifacts/json/b32k_canonical_alphabet.json
wc -l artifacts/csv/b32k_canonical_alphabet.csv

echo
echo "surface profile"
python - <<'PY'
import json
from pathlib import Path
p = Path("artifacts/json/surface_profile_000.json")
if p.exists():
    d = json.loads(p.read_text())
    print(d["profile_id"])
    print("symbols:", len(d["symbols"]))
    print("relations:", len(d["relations"]))
    print("claims:", len(d["claims"]))
    print("assertions:", len(d["assertions"]))
else:
    print("missing surface_profile_000.json")
PY

echo
echo "prompts"
find experiments/profile_000/prompts -maxdepth 1 -type f 2>/dev/null | sort

echo
echo "notes"
ls -1 notes
