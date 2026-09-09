#!/usr/bin/env python3
"""Fast repository-level integrity checks that require no model download."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "STATUS.md",
    "paper/Manuscript.md",
    "docs/METHODS.md",
    "docs/CLAIMS.md",
    "docs/REPRODUCING.md",
    "docs/LITERATURE.md",
    "replication/claim_ledger.csv",
    "replication/protocol/PROTOCOL.md",
    "replication/models/registry.json",
    "publication/ARTIFACTS.md",
    "publication/CHECKLIST.md",
]

ALLOWED_CLAIM_STATES = {
    "supported_exploratory",
    "retired",
    "not_supported",
    "not_claimed",
    "pending",
    "running",
    "blocked",
    "failed_selection",
    "null",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail("missing required paths: " + ", ".join(missing))

    registry = json.loads((ROOT / "replication/models/registry.json").read_text())
    if registry.get("schema_version") != 1:
        fail("unexpected model registry schema_version")
    ids = [item["id"] for item in registry.get("models", [])]
    if len(ids) != len(set(ids)):
        fail("duplicate model IDs in registry")

    with (ROOT / "replication/claim_ledger.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("claim ledger is empty")
    claim_ids = [row["claim_id"] for row in rows]
    if len(claim_ids) != len(set(claim_ids)):
        fail("duplicate claim IDs")
    bad_states = sorted({row["status"] for row in rows} - ALLOWED_CLAIM_STATES)
    if bad_states:
        fail("unknown claim states: " + ", ".join(bad_states))

    readme = (ROOT / "README.md").read_text()
    for phrase in ("30,576", "exploratory", "replication", "Limitations"):
        if phrase not in readme:
            fail(f"README is missing expected research framing: {phrase!r}")

    print(f"OK: {len(REQUIRED)} required paths")
    print(f"OK: {len(rows)} claim-ledger entries")
    print(f"OK: {len(ids)} model-registry entries")
    print("OK: repository research metadata is internally consistent")


if __name__ == "__main__":
    main()
