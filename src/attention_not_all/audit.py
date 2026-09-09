"""Trial-record coverage checks."""

from __future__ import annotations

import math
from typing import Iterable, Mapping, Sequence


def audit_records(
    records: Iterable[Mapping[str, object]],
    *,
    key_fields: Sequence[str],
    score_fields: Sequence[str] = (),
    expected_keys: set[tuple[object, ...]] | None = None,
) -> dict[str, object]:
    """Audit uniqueness, finiteness, and optional expected-key coverage."""
    seen: set[tuple[object, ...]] = set()
    duplicates: list[tuple[object, ...]] = []
    nonfinite: list[tuple[tuple[object, ...], str]] = []
    count = 0

    for row in records:
        count += 1
        key = tuple(row[field] for field in key_fields)
        if key in seen:
            duplicates.append(key)
        seen.add(key)
        for field in score_fields:
            value = float(row[field])
            if not math.isfinite(value):
                nonfinite.append((key, field))

    missing = sorted(expected_keys - seen) if expected_keys is not None else []
    unexpected = sorted(seen - expected_keys) if expected_keys is not None else []

    return {
        "records": count,
        "unique_keys": len(seen),
        "duplicate_keys": duplicates,
        "nonfinite_scores": nonfinite,
        "missing_keys": missing,
        "unexpected_keys": unexpected,
        "complete": not duplicates and not nonfinite and not missing,
    }
