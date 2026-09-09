# Attention Is Not All You Need

## Causal sparse-feature analysis of phonological constraints in language models

**Working manuscript — exploratory study and prospective replication protocol**  
**Status:** 8 September 2026

## Abstract

Sparse autoencoders (SAEs) offer a practical way to decompose dense language-model activations into sparse coordinates, but interpreting those coordinates from activation examples alone risks conflating correlation, decodability, and causal use. We study a controlled lexical phenomenon in which English indefinite-article choice depends on the sound rather than the spelling of the following phrase. Using Gemma 2 2B and a Gemma Scope residual-stream SAE, we revisit a candidate feature initially associated with this distinction. We first document a failed probe whose input leaked the target article, and retire the corresponding inference. We then hold visible prompts fixed and intervene directly on the selected feature while measuring spelling-balanced continuation log-probability contrasts. In the saved exploratory grid, natural feature removal yields large negative effects after **an** in both neutral (−14.4515 nats) and cued (−3.4118 nats) contexts. An alternate same-layer dictionary produces the same qualitative pattern (−12.8354 and −3.2845 nats). The corresponding saved effects after **a** are near zero in the original dictionary, but we do not claim formal equivalence. These results support a narrow within-model causal role for the selected coordinate in the tested continuation contrast, while leaving open representation uniqueness, population-level lexical generalization, circuit identity, and cross-model universality. We therefore preregister a stronger program using Gemma Scope 2, Llama Scope, and Qwen-Scope with independent feature selection, family-level inference, position-specific tracing, MLP mediation, grouped-attention tests, and natural-text mapping. The study argues for a distinction that should be routine in SAE interpretability: what activates a feature, what a feature predicts, what editing it causes, and where that effect propagates are separate empirical questions.

## 1. Introduction

Mechanistic interpretability increasingly uses learned sparse dictionaries to make model activations more legible. Sparse autoencoders are attractive because they transform a dense activation vector into a high-dimensional sparse code whose active coordinates can often be associated with human-recognizable regularities. Yet semantic coherence in top-activating examples is only the beginning of an explanation. A feature may correlate with a variable without being used by the model, may admit multiple equally useful dictionary factorizations, and may support steering despite not being a unique natural computational variable.

This work develops a small causal case study around English indefinite articles. Article choice is normally governed by the following sound: *a university* but *an hour*. Orthography/sound conflicts permit controlled lexical families in which surface spelling and phonological onset can be dissociated. The phenomenon is narrow enough to support explicit stimulus crossing, yet rich enough to expose common interpretability failures.

Our first failure is methodological. An early probe attempted to predict a phonological class from representations that included the article itself. Because the article directly encodes the label, high probe performance could not establish that the internal representation independently carried the intended variable. We retain that analysis as a falsification and rebuild the main question causally.

The revised question is: **holding the visible prompt fixed, does editing a selected sparse coordinate change the model's preference for sound-compatible continuations?**

## 2. Contributions

This research package contributes:

1. a leakage-aware reinterpretation of an SAE feature hypothesis;
2. a paired causal intervention design with fixed visible prompts;
3. completed exploratory Gemma 2 intervention grids for an original and alternate dictionary;
4. random-direction, matched-feature, no-op, contextual, and factual controls;
5. a family-level analysis plan respecting lexical dependence;
6. a claim ledger that preserves nulls, failures, and retired inferences;
7. a prospective cross-model replication protocol spanning Gemma 3, Llama 3.1, and Qwen3/Qwen3.5 interpretability ecosystems;
8. planned localization through position, MLP, attention, and natural-text analyses.

## 3. Experimental setup

### 3.1 Reference model

The completed exploratory experiment uses Gemma 2 2B and Gemma Scope. The selected coordinate is feature 12010 at layer 24 in a 16k residual-stream dictionary.

We emphasize that the feature number is an address in one learned dictionary, not a semantic name.

### 3.2 Stimulus logic

Stimuli cross lexical sound class with visible spelling cues, carrier templates, contextual cues, modifiers, and article environments. The important unit for inferential resampling is the independent lexical **root family**, not every inflected or derived surface form.

The rare consonant-spelling/vowel-sound cell is particularly constrained: the ordinary roots currently reduce to *hour, honor, honest,* and *heir*. That limitation prevents broad population claims from the current candidate pool.

### 3.3 Behavioral score

For each prompt we score candidate continuations and define a vowel-vs-consonant sound contrast. For intervention condition `z`, the paired causal effect is the change in that contrast relative to the natural run. Because the prompt is identical across the pair, the intervention—not a visible wording change—is the manipulated variable.

### 3.4 Intervention controls

The saved schedule contains 26 conditions and includes eight random directions and four matched SAE directions. These controls test whether effects are specific to the selected coordinate rather than generic residual-stream disruption. Exact no-op differences of 0.0 nats in the saved audit provide a numerical implementation check, not a semantic control.

## 4. Results

### 4.1 Reference dictionary

The original saved grid contains **30,576 / 30,576** expected trial-condition records.

For natural feature removal after **an**:

| Context | Effect on vowel-vs-consonant sound contrast |
| :--- | ---: |
| Neutral | **−14.4515 nats** |
| Cued | **−3.4118 nats** |

The negative sign means removal lowers the relative score of vowel-sound continuations.

For the corresponding **a** conditions, the original-dictionary saved estimates are approximately `7.75e-7` and `1.02e-8` nats. These small values are descriptively useful but do not support an equivalence claim without an equivalence margin and appropriate analysis.

### 4.2 Alternate dictionary

A different same-layer/width dictionary and a coordinate chosen without using test effects were used as a robustness check. That grid also contains **30,576 / 30,576** records.

| Context | Effect after **an** |
| :--- | ---: |
| Neutral | **−12.8354 nats** |
| Cued | **−3.2845 nats** |

The qualitative replication across dictionaries suggests the result is not solely an accident of one SAE factorization. Because both dictionaries analyze the same underlying language model, this remains same-model robustness rather than independent replication.

## 5. Interpretation

The strongest warranted statement is narrow: editing the selected sparse coordinate causally changes the tested sound-compatible continuation contrast in Gemma 2 under the held-out candidate prompts, and a second same-model dictionary yields a similar pattern.

Several stronger interpretations remain unproven.

First, the result does not establish a universal “phonology feature.” The selected coordinate may capture a mixture of contextual regularities useful for the intervention. Second, an SAE direction is not guaranteed to be a canonical natural variable; learned dictionaries can split, merge, or rotate structure. Third, a causal intervention can create states outside the model's natural activation manifold. Controls reduce this concern but cannot erase it. Fourth, a behavioral effect does not identify a unique computational route. The feature could influence multiple downstream pathways, including attention and MLP computation.

## 6. Failed inference as evidence

The original label-leaking probe is retained because it changes the epistemic status of the project. It demonstrates why probe accuracy is not sufficient when the probe input includes a direct cue to the target. Rather than discarding the failure, the revised study uses it to motivate the causal design.

This is important for interpretability research generally: a representation can appear to “encode” a variable under a permissive probe even when the evidence does not show the model computed or used that variable in the intended way.

## 7. Prospective replication

### 7.1 Gemma 3 / Gemma Scope 2

Gemma Scope 2 provides SAEs and transcoders across Gemma 3, making it suitable both for independent feature selection and for richer cross-layer path analysis.

### 7.2 Llama 3.1 / Llama Scope

Llama Scope provides a distinct model family and SAE training ecosystem. The current pilot has generated a 41,808-trial intervention schedule, but execution state must not be confused with completed evidence.

### 7.3 Qwen / Qwen-Scope

Qwen-Scope's 2026 release extends sparse-feature analysis to Qwen3/Qwen3.5 models, including dense and MoE variants. Replication here would test whether the experimental relationship survives both model-family and interpretability-tool changes.

### 7.4 Independent selection

Each model must select its own coordinate using frozen discovery and selection partitions. A failed selection is a valid outcome. We do not assume that decoder cosine to the Gemma coordinate identifies a semantically equivalent feature across models.

## 8. Mechanistic localization

The next stage decomposes the causal effect.

**Position-specific tracing** tests where restoring natural state recovers the effect. **MLP mediation** asks whether specific MLP outputs carry the intervention effect under controlled restoration and downstream blocking. **Grouped-attention tests** ask whether attention heads are necessary or sufficient for recovery. **Natural-text mapping** tests whether candidate semantics generalize outside the constructed lexical set.

These analyses are confirmatory only when selection and analysis choices are frozen before their test effects are inspected.

## 9. Statistical plan

The confirmatory unit of independence is the lexical family. Family bootstrap or equivalent family-level inference avoids pseudoreplication from derivatives. The primary confirmatory family contains four declared tests and uses Holm correction. Exploratory secondary analyses are reported separately.

The limited number of independent rare conflict families remains a fundamental constraint. No statistical technique can manufacture independent lexical roots; scope statements must reflect the support of the stimulus population.

## 10. Limitations

1. Completed evidence is exploratory and from one underlying model.
2. Alternate dictionaries do not constitute independent-model replication.
3. Candidate lexical families remain small in rare conflict cells.
4. The intervention may be off-manifold.
5. Near-zero estimates are not equivalence tests.
6. Sparse coordinates need not be canonical or unique.
7. A behavioral causal effect does not identify a unique circuit.
8. Cross-model and natural-text generalization remain pending.

## 11. Conclusion

The case study supports a methodological principle more general than the lexical phenomenon itself: **SAE interpretability should distinguish activation, prediction, causation, and mechanism.** A feature visualization can generate a hypothesis; a causal intervention can establish behavioral relevance within scope; pathway tests can localize computation; independent replications can determine whether the relationship survives changes in model and dictionary.

The project is therefore designed to keep the strongest causal result while preserving the failed probe, nulls, dictionary ambiguity, and replication gates. The intended contribution is not a claim that attention is unnecessary. It is a reproducible research program for deciding which sparse-feature interpretations deserve mechanistic confidence.
