#!/usr/bin/env bash
# Update versions.json manifest for multi-version documentation.
#
# Usage:
#   ./scripts/update-versions-json.sh --version 1.0.0 --url /docs/1.0.0/ [--stable] [--file versions.json]
#   ./scripts/update-versions-json.sh --version dev --url /docs/dev/ --dev [--file versions.json]
#
# Requires: python3 (for JSON manipulation)

set -euo pipefail

VERSION=""
URL=""
STABLE=false
DEV=false
FILE="versions.json"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --version) VERSION="$2"; shift 2 ;;
        --url)     URL="$2"; shift 2 ;;
        --stable)  STABLE=true; shift ;;
        --dev)     DEV=true; shift ;;
        --file)    FILE="$2"; shift 2 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

if [[ -z "$VERSION" || -z "$URL" ]]; then
    echo "Usage: $0 --version VERSION --url URL [--stable] [--dev] [--file FILE]" >&2
    exit 1
fi

DATE=$(date -u +%Y-%m-%d)

python3 - "$FILE" "$VERSION" "$URL" "$STABLE" "$DEV" "$DATE" <<'PYTHON'
import json
import sys

file_path = sys.argv[1]
version = sys.argv[2]
url = sys.argv[3]
stable = sys.argv[4] == "true"
dev = sys.argv[5] == "true"
date = sys.argv[6]

# Read existing versions.json or start empty
try:
    with open(file_path, 'r') as f:
        versions = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    versions = []

# Remove existing entry for this version (if updating)
versions = [v for v in versions if v.get('version') != version]

# Build new entry
entry = {"version": version, "url": url, "date": date}
if stable:
    entry["stable"] = True
if dev:
    entry["dev"] = True

# If this is a stable release, remove stable flag from all others
if stable:
    for v in versions:
        v.pop("stable", None)

versions.append(entry)

# Sort: stable first, then by version descending (simple string sort), dev last
def sort_key(v):
    if v.get("dev"):
        return (2, "")
    if v.get("stable"):
        return (0, v["version"])
    return (1, v["version"])

versions.sort(key=sort_key)

# Write back
with open(file_path, 'w') as f:
    json.dump(versions, f, indent=2)
    f.write('\n')

print(f"Updated {file_path}: {version} -> {url}" +
      (" [stable]" if stable else "") +
      (" [dev]" if dev else ""))
PYTHON
