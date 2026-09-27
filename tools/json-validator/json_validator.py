import json
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: python json_validator.py FILE")

with open(sys.argv[1], encoding="utf-8") as handle:
    json.load(handle)

print("Valid JSON.")
