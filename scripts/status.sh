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
echo "notes"
ls -1 notes
