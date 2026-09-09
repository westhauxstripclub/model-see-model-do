from attention_not_all import audit_records, family_bootstrap_mean, holm_adjust


def test_holm_adjust_preserves_order_and_monotonicity():
    p = [0.04, 0.001, 0.03, 0.20]
    adjusted = holm_adjust(p)
    assert adjusted[1] == 0.004
    assert all(0.0 <= value <= 1.0 for value in adjusted)
    order = sorted(range(len(p)), key=lambda i: p[i])
    ordered_adj = [adjusted[i] for i in order]
    assert ordered_adj == sorted(ordered_adj)


def test_family_bootstrap_uses_family_means():
    rows = [
        {"family": "hour", "effect": -10.0},
        {"family": "hour", "effect": -6.0},
        {"family": "heir", "effect": -2.0},
    ]
    result = family_bootstrap_mean(rows, n_boot=500, seed=7)
    assert result["mean"] == -5.0  # mean of family means: (-8 + -2) / 2
    assert result["n_families"] == 2.0


def test_audit_records_detects_missing_and_duplicates():
    rows = [
        {"trial": 1, "condition": "natural", "score": 0.0},
        {"trial": 1, "condition": "natural", "score": 0.0},
    ]
    expected = {(1, "natural"), (1, "ablate")}
    audit = audit_records(rows, key_fields=("trial", "condition"), score_fields=("score",), expected_keys=expected)
    assert audit["complete"] is False
    assert audit["duplicate_keys"]
    assert audit["missing_keys"] == [(1, "ablate")]
