# Prospective cross-model replication protocol

## Purpose

Test whether the relationship observed in the exploratory Gemma 2 study—between a model-selected sparse coordinate and a controlled sound-compatible continuation contrast—replicates under independent model families and interpretability resources.

The target of replication is an **experimental relationship**, not a specific feature ID.

## Models

Primary prospective families:

1. Gemma 3 + Gemma Scope 2.
2. Llama 3.1 8B Base + Llama Scope.
3. Qwen3 / Qwen3.5 + Qwen-Scope.

Exact revisions must be frozen in `replication/models/registry.json` before confirmatory execution.

## Partitioning

The lexical/material pool is split before feature selection into:

- **discovery** — candidate generation and qualitative interpretation;
- **selection** — model-specific feature choice;
- **test** — intervention and primary estimation only.

No test effect may influence discovery or selection.

## Independent adjudication

Before confirmation, two independent reviewers classify lexical items/families for:

- spelling onset;
- pronunciation/sound onset;
- root-family identity;
- ambiguity or dialect sensitivity;
- proper-noun / abbreviation / foreign-word status;
- exclusion reason where applicable.

Disagreements are resolved under a predeclared rule and preserved in the review artifact.

## Feature discovery

Within each model independently:

1. measure SAE activation on discovery materials;
2. identify coordinates enriched for the target contrast under predeclared criteria;
3. record the top candidate set, not only the winner;
4. preserve null discovery outcomes.

## Feature selection

On the selection partition, compute the frozen selection score. The selected coordinate must pass minimum activation/support gates and must not be chosen using intervention effects.

Write a `feature_lock.json` containing:

- model revision;
- SAE revision;
- layer/sublayer;
- dictionary width;
- feature ID;
- selection metric/value;
- discovery/selection data hashes;
- code commit;
- protocol/contract hash;
- timestamp.

If no feature passes, write `selection_failure.json` and stop that model's confirmatory intervention stage.

## Primary intervention estimands

The confirmatory family contains four tests defined before execution. The exact factor crossings should be frozen during registration; the expected structure is article × context for selected-feature removal on the sound contrast.

For each trial, compute

`tau_i = [D_i(intervention) - D_i(natural)]`,

where `D` is the vowel-sound minus consonant-sound continuation score.

Aggregate at the independent lexical-family level.

## Controls

Required controls include:

- exact no-op;
- random residual directions;
- matched SAE directions selected without test effects;
- factual controls unrelated to article/sound choice;
- neutral and cued carriers;
- modifier crossings;
- both articles;
- dose-response where steering is used.

## Multiplicity

Apply Holm correction to the four registered primary tests. Secondary analyses are labeled exploratory unless separately registered.

## Alternate dictionary

When a second same-model dictionary exists, select the closest eligible coordinate using dictionary geometry/selection information only. Report this as **same-model dictionary robustness**.

## Position-specific causal tracing

Restore natural state at one token position/layer at a time against the feature-ablated run. Estimate recovery of the primary contrast. Predefine the token positions of interest and summarize full scans without selecting only the maximal cell.

## Path-specific MLP mediation

For candidate MLP stages:

- test group restoration;
- test leave-one-out effects;
- block downstream candidate paths;
- compare against matched module controls.

Do not call a module a mediator based solely on activation correlation.

## Grouped-attention tests

Scan attention heads/groups under a frozen strategy, then test candidate groups with restoration and blocking. Correct or clearly separate exploratory head scans from confirmatory group tests.

## Natural-text activation mapping

Run the selected coordinate on a frozen external corpus. Report activation frequency, magnitude, top contexts, lexical enrichment, and prominent false-positive regions. Do not use this corpus to retroactively redefine the primary feature.

## Stopping / failure rules

A model replication is reported as failed or inconclusive if any of the following occur:

- feature selection fails;
- required trial coverage is not achieved;
- model/SAE revision mismatch is detected;
- results depend on an unregistered test-set selection choice;
- numerical instability invalidates primary scores.

Failures remain in the claim ledger.

## Registration boundary

Before a non-pilot confirmation:

1. complete independent review sheets;
2. freeze approved data and exclusions;
3. rerun discovery/selection without pilot mode;
4. calibrate scope/power;
5. register the final protocol and all primary selection outcomes;
6. record the public registration URL and timestamp only after a real registration exists.

A pilot cannot be relabeled as registered confirmation.
