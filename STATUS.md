# Research status

**Snapshot:** 8 September 2026  
**Study stage:** exploratory evidence complete for the saved Gemma 2 grids; prospective replication in progress.

This file separates completed evidence from active compute and planned work. It is intentionally stricter than a progress log: only artifacts that have finished and passed the stated audit are treated as results.

## Completed evidence

### Gemma 2 reference dictionary

- Model: Gemma 2 2B.
- SAE resource: original Gemma Scope residual-stream dictionary.
- Candidate coordinate: feature 12010, layer 24, 16k dictionary.
- Saved intervention records: **30,576 / 30,576**.
- Primary precision: FP32.
- Intervention schedule: 26 conditions, including 8 random directions and 4 matched SAE directions.
- Main saved contrast after **an**:
  - neutral context: **−14.4515 nats**;
  - cued context: **−3.4118 nats**.
- Corresponding saved **a** contrasts are near zero in the current grid (`~7.75e-7`, `~1.02e-8` nats), but no equivalence claim is made.

### Alternate dictionary robustness

- Same model/layer/width; a different dictionary and closest positive decoder-cosine feature were selected without using test effects.
- Saved intervention records: **30,576 / 30,576**.
- Main saved contrast after **an**:
  - neutral context: **−12.8354 nats**;
  - cued context: **−3.2845 nats**.
- This is **not** an independent model replication.

### Falsifications retained

- The first phonology probe is retired because the article in the input leaked the target.
- The repository does not infer semantic identity from decoder cosine alone.
- Null / negligible effects are retained rather than filtered out.

## Running / recently prepared

### Llama replication pilot

A current RunPod extension has produced an intervention schedule containing **41,808 trial IDs** for the Llama branch. Treat this as an execution-state fact, not a result. Completion, coverage, selection validity, and analysis must all be checked before any empirical statement is promoted.

## Prospective extensions

| Model family | Interpretability resource | Status |
| :--- | :--- | :--- |
| Gemma 3 | Gemma Scope 2 | Protocol prepared; confirmatory run pending |
| Llama 3.1 | Llama Scope | Pilot / intervention execution in progress |
| Qwen3 / Qwen3.5 | Qwen-Scope | Protocol prepared; run pending |

Planned analyses include position-specific causal tracing, path-specific MLP mediation, grouped-attention tests, and natural-text activation mapping.

## Publication gates still open

1. Independent lexical-family adjudication.
2. Frozen discovery / selection / test partitions.
3. Public preregistration of the confirmatory protocol and primary estimands.
4. Cross-model replication with each model selecting its own coordinate.
5. Finalized power/scope statement given the small number of independent rare lexical roots.
6. Frozen raw evidence, manifests, model/SAE revisions, checksums, and environment metadata.
7. Full claim-ledger review separating supported, null, retired, and unrun claims.

## Important linguistic constraint

The ordinary consonant-spelling / vowel-sound cell currently has only four independent root families: **hour, honor, honest, heir**. Derivatives do not create new independent families. Any population-level inference must respect that effective sample size.
