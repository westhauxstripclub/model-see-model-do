# Contributing

This repository prioritizes reproducibility and claim hygiene over feature velocity.

## Research changes

A change that affects a scientific claim should include:

1. the motivating claim ID from `replication/claim_ledger.csv` or a new claim entry;
2. the data partition used;
3. whether the analysis was registered, exploratory, or a robustness check;
4. the exact model/SAE/code revisions when applicable;
5. updated tests for statistical or audit logic;
6. updated limitations if the interpretation changes.

Do not delete nulls, failed selections, or falsifications simply because a later approach works better.

## Code changes

Run:

```bash
python -m pip install -e '.[dev]'
python scripts/verify_artifacts.py
pytest
```

Keep model-execution code separate from dependency-light analysis/audit code where possible so core statistical logic remains independently testable.
