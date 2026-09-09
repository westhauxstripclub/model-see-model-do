<p align="center">
  <img src="docs/assets/banner.svg" alt="Attention Is Not All You Need — causal sparse-feature interpretability" width="100%" />
</p>

<p align="center">
  <strong>Separate what a representation correlates with from what it causally controls.</strong>
</p>

<p align="center">
  <a href="paper/Manuscript.md">Manuscript</a> ·
  <a href="docs/METHODS.md">Methods</a> ·
  <a href="docs/CLAIMS.md">Claim ledger guide</a> ·
  <a href="docs/REPRODUCING.md">Reproduction</a> ·
  <a href="STATUS.md">Live research status</a>
</p>

<p align="center">
  <img alt="study exploratory" src="https://img.shields.io/badge/study-exploratory-C9AC79?style=flat-square&labelColor=17242B" />
  <img alt="reference model Gemma 2 2B" src="https://img.shields.io/badge/reference-Gemma%202%202B-B5CED0?style=flat-square&labelColor=17242B" />
  <img alt="primary precision FP32" src="https://img.shields.io/badge/primary%20precision-FP32-B5CED0?style=flat-square&labelColor=17242B" />
  <img alt="cross model replication in progress" src="https://img.shields.io/badge/replication-in%20progress-C9AC79?style=flat-square&labelColor=17242B" />
  <a href="https://github.com/westhauxstripclub/attention-is-not-all-you-need/actions"><img alt="validation" src="https://img.shields.io/github/actions/workflow/status/westhauxstripclub/attention-is-not-all-you-need/validate.yml?branch=main&style=flat-square&label=artifact%20checks&labelColor=17242B" /></a>
</p>

---

# Attention Is Not All You Need

**A causal study of sparse autoencoder features, lexical constraints, and model-internal computation.**

English article choice provides a compact experimental system: *a university* but *an hour*. The visible orthography can conflict with the sound class that governs the article, which makes the domain useful for separating surface cues from latent constraints.

This project asks four deliberately different questions:

1. **Activation** — when does an SAE feature fire naturally?
2. **Prediction** — what information can be decoded from the representation without leakage?
3. **Causation** — does intervening on the feature change sound-compatible continuation probabilities while the prompt stays fixed?
4. **Mechanism** — through which positions, MLPs, and attention pathways does the effect propagate?

The central methodological lesson is simple: **feature interpretation should survive causal intervention, negative controls, alternative dictionaries, and independent-model replication—not just activation examples.**

> **Status — 8 September 2026.** The Gemma 2 exploratory intervention grids have been completed and reaggregated. Same-model alternate-dictionary robustness is available. The candidate set has not yet passed independent human adjudication, and the confirmatory cross-model program is not complete. A Llama replication pilot has generated a 41,808-trial intervention schedule; those trials are not presented as completed evidence. See [`STATUS.md`](STATUS.md).

## Headline result

The reference experiment studies **Gemma Scope feature 12010** at layer 24 of Gemma 2 2B (16k residual-stream dictionary). A first phonology probe was invalid because the article in the prompt leaked the target label. That inference is retired.

The revised intervention keeps the visible prompt fixed and asks whether removing the naturally active feature changes the log-probability contrast between vowel-sound and consonant-sound continuations.

| Dictionary | Neutral context, after **an** | Cued context, after **an** |
| :--- | ---: | ---: |
| Original | **−14.4515 nats** | **−3.4118 nats** |
| Alternate same-layer dictionary | **−12.8354 nats** | **−3.2845 nats** |

Negative values mean feature removal lowers vowel-sound continuation scores relative to consonant-sound continuations. These are paired effects on summed continuation log probabilities—not classification accuracy, not a universal feature label, and not evidence that attention is unnecessary.

For the original dictionary, the corresponding **a** estimates are approximately `7.75e-7` and `1.02e-8` nats. They are practically tiny in this saved grid, but the current study does **not** claim formal equivalence.

## Evidence available now

| Component | Current evidence | Interpretation |
| :--- | :--- | :--- |
| Original Gemma 2 dictionary | **30,576 / 30,576** intervention records | Complete exploratory grid |
| Alternate Gemma 2 dictionary | **30,576 / 30,576** intervention records | Same-model dictionary robustness |
| Intervention schedule | **26 conditions** | Includes 8 random and 4 matched SAE directions |
| Numerical no-op audit | Exact **0.0 nats** differences | Implementation check only |
| Llama extension | **41,808 scheduled trial IDs** in current pilot | Running / not yet a result |
| Gemma 3 + Gemma Scope 2 | Prospective protocol | Not yet confirmatory evidence |
| Qwen + Qwen-Scope | Prospective protocol | Not yet confirmatory evidence |

The package records both positive and negative evidence in [`replication/claim_ledger.csv`](replication/claim_ledger.csv).

## Why this is interesting

Sparse autoencoders can produce features that look semantically clean, but interpretability requires more than a feature visualization. This project is designed around the gaps between **association, decodability, intervention, and mechanism**.

The research program therefore layers increasingly difficult tests:

- leakage-resistant feature selection;
- paired causal ablation and steering;
- random-direction and matched-SAE controls;
- alternate-dictionary robustness;
- family-level resampling rather than treating lexical derivatives as independent;
- position-specific causal tracing;
- path-specific MLP mediation;
- grouped-attention tests;
- natural-text activation mapping;
- independent feature selection in Gemma 3, Llama, and Qwen.

This structure is intentionally falsifiable: a feature can be interpretable without being causal, causal without being unique, and model-specific without generalizing.

## Research integrity decisions

The repository keeps failed and incomplete hypotheses visible.

| Claim | Current disposition |
| :--- | :--- |
| “The original probe shows phonology is encoded” | **Retired** — label leakage |
| “Feature 12010 causally affects the held-out *an* contrast in Gemma 2” | **Supported narrowly** by the saved exploratory grids |
| “The feature is a universal phonology neuron” | **Not supported** |
| “The same semantic coordinate exists in every model” | **Not assumed** |
| “MLPs form a proven serial causal circuit” | **Pending mechanistic tests** |
| “Attention is unnecessary” | **Not claimed**; title is intentionally provocative |
| “Population-level lexical generalization is established” | **Not established**; only four independent ordinary silent-h root families are currently available |

See [`docs/CLAIMS.md`](docs/CLAIMS.md) for the exact standards of evidence.

## 2026 replication context

The replication program is built around three public interpretability ecosystems:

- **Gemma Scope 2**: SAEs and transcoders across Gemma 3, including Matryoshka-trained SAEs and cross-layer/skip transcoders.
- **Llama Scope**: layer- and sublayer-level SAE dictionaries for Llama-3.1-8B-Base.
- **Qwen-Scope**: 2026 SAE releases for Qwen3/Qwen3.5 spanning dense and MoE models, with demonstrations of feature steering and model-development workflows.

Every model selects its **own** candidate coordinate using discovery and selection partitions. Cross-model replication means replication of an experimental relationship, not forcing feature IDs to correspond.

## Repository tour

| Path | Contents |
| :--- | :--- |
| [`paper/Manuscript.md`](paper/Manuscript.md) | Current manuscript-style research narrative |
| [`STATUS.md`](STATUS.md) | Completed, running, blocked, and planned work |
| [`docs/METHODS.md`](docs/METHODS.md) | Experimental design and estimands |
| [`docs/CLAIMS.md`](docs/CLAIMS.md) | Interpretation boundaries and evidence standards |
| [`docs/LITERATURE.md`](docs/LITERATURE.md) | Current SAE / mechanistic-interpretability context |
| [`docs/REPRODUCING.md`](docs/REPRODUCING.md) | How to validate and reproduce the package |
| [`replication/protocol/PROTOCOL.md`](replication/protocol/PROTOCOL.md) | Prospective cross-model protocol |
| [`replication/models/registry.json`](replication/models/registry.json) | Model/resource registry and empirical status |
| [`replication/claim_ledger.csv`](replication/claim_ledger.csv) | Supported, null, retired, pending claims |
| [`src/attention_not_all/`](src/attention_not_all/) | Small dependency-light analysis utilities |
| [`tests/`](tests/) | Unit tests for family bootstrap, Holm correction, and audits |
| [`publication/`](publication/) | Artifact inventory and publication gates |

## Validate locally

The repository includes dependency-light checks that do not download model weights:

```bash
python -m pip install -e .
python scripts/verify_artifacts.py
pytest -q
```

The analysis utilities intentionally operate on ordinary records/CSV-like data so statistical logic can be tested separately from GPU execution.

## Reproduce or extend

The GPU notebooks and raw evidence generated in Kaggle/RunPod are larger research artifacts and are **not fabricated here**. Before publication, they should be copied into the paths specified in [`publication/ARTIFACTS.md`](publication/ARTIFACTS.md), checksummed, and frozen. The exact remaining steps are tracked in [`publication/CHECKLIST.md`](publication/CHECKLIST.md).

For a fresh replication, start from [`replication/protocol/PROTOCOL.md`](replication/protocol/PROTOCOL.md). Do not use a pilot-selected feature as confirmatory evidence; discovery, selection, intervention, and analysis boundaries are explicit.

## Limitations that matter

- The completed Gemma 2 results are exploratory and within-model.
- Alternate-dictionary robustness is not independent-model replication.
- The rare orthography/phonology conflict cells impose a small number of independent lexical families.
- SAE features are learned dictionary coordinates, not guaranteed ontological atoms.
- Ablation can create off-manifold states; random and matched-feature controls reduce but do not eliminate this concern.
- Near-zero effects are not equivalence tests.
- A causal effect on continuation probabilities does not imply a unique circuit or a human-like phonological representation.

## Citation

Until a public paper identifier or DOI exists, cite the repository with the exact commit hash and access date. Metadata is provided in [`CITATION.cff`](CITATION.cff).

---

<p align="center"><sub><strong>Measure the association. Test the intervention. Keep the falsification.</strong></sub></p>
