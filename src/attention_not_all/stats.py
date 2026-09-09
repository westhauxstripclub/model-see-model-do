"""Small statistical utilities kept separate from model execution code."""

from __future__ import annotations

from collections import defaultdict
import random
from typing import Iterable, Mapping, Sequence


def holm_adjust(p_values: Sequence[float]) -> list[float]:
    """Return Holm-adjusted p-values in the original order.

    The implementation is dependency-light so the multiplicity logic can be
    tested independently of the GPU environment.
    """
    n = len(p_values)
    if any((p < 0.0 or p > 1.0) for p in p_values):
        raise ValueError("p-values must lie in [0, 1]")
    order = sorted(range(n), key=lambda i: p_values[i])
    adjusted_sorted: list[float] = []
    running = 0.0
    for rank, idx in enumerate(order):
        raw = (n - rank) * p_values[idx]
        running = max(running, raw)
        adjusted_sorted.append(min(1.0, running))
    out = [0.0] * n
    for idx, value in zip(order, adjusted_sorted):
        out[idx] = value
    return out


def _family_means(records: Iterable[Mapping[str, object]], family_key: str, value_key: str) -> dict[str, float]:
    grouped: dict[str, list[float]] = defaultdict(list)
    for row in records:
        family = str(row[family_key])
        value = float(row[value_key])
        grouped[family].append(value)
    if not grouped:
        raise ValueError("no records supplied")
    return {family: sum(values) / len(values) for family, values in grouped.items()}


def family_bootstrap_mean(
    records: Iterable[Mapping[str, object]],
    *,
    family_key: str = "family",
    value_key: str = "effect",
    n_boot: int = 10_000,
    seed: int = 0,
    alpha: float = 0.05,
) -> dict[str, float]:
    """Bootstrap a mean by resampling independent families.

    Surface forms are first averaged within family; families are then sampled
    with replacement. This avoids treating lexical derivatives as independent
    observations.
    """
    if n_boot <= 0:
        raise ValueError("n_boot must be positive")
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0, 1)")

    means = _family_means(records, family_key, value_key)
    families = sorted(means)
    values = [means[f] for f in families]
    observed = sum(values) / len(values)

    rng = random.Random(seed)
    draws: list[float] = []
    for _ in range(n_boot):
        sample = [values[rng.randrange(len(values))] for _ in values]
        draws.append(sum(sample) / len(sample))
    draws.sort()

    def quantile(q: float) -> float:
        pos = q * (len(draws) - 1)
        lo = int(pos)
        hi = min(lo + 1, len(draws) - 1)
        frac = pos - lo
        return draws[lo] * (1.0 - frac) + draws[hi] * frac

    return {
        "mean": observed,
        "ci_low": quantile(alpha / 2.0),
        "ci_high": quantile(1.0 - alpha / 2.0),
        "n_families": float(len(families)),
        "n_boot": float(n_boot),
    }
