# Methods

## Experimental system

English indefinite-article choice is determined primarily by the initial **sound** of the following phrase, not its spelling. The rare conflict cases—such as words beginning with written `h` but a vowel sound, or written vowels with consonant onsets—create a compact test bed for representation-level causal analysis.

The design separates lexical identity, orthography, sound class, article, carrier template, contextual cue, and modifiers so that a feature can be tested under crossings rather than a single prompt template.

## Reference model and feature

The completed exploratory study uses:

- **model:** Gemma 2 2B;
- **resource:** Gemma Scope residual-stream SAE;
- **layer:** 24;
- **dictionary width:** 16k;
- **selected coordinate:** feature 12010.

The coordinate is treated as an experimental handle, not an ontological label.

## Feature-selection principle

Selection and causal testing must use disjoint information.

A valid confirmatory workflow is:

1. **Discovery:** identify candidates using activation/interpretation criteria on discovery items only.
2. **Selection:** choose a model-specific coordinate using a frozen selection partition and predeclared score.
3. **Lock:** serialize the selected feature, model revision, SAE revision, selection score, and contract hash.
4. **Intervention:** run the frozen test schedule without revisiting selection.
5. **Analysis:** compute the registered estimands on the declared independence units.

If selection fails, the model replication fails. The pipeline must not hand-pick a replacement from the test results.

## Intervention design

For each prompt/trial, the model is evaluated under paired interventions. The current saved schedule contains 26 conditions, including:

- natural/no intervention;
- selected-feature removal;
- selected-feature steering at declared strengths;
- random directions;
- matched SAE directions;
- numerical/no-op checks;
- control contexts and factual controls.

The main behavioral quantity is a continuation log-probability contrast, not a generated-text label. Using summed token log probabilities allows paired comparisons while keeping the visible prompt identical across the intervention pair.

## Primary contrast

For a trial `i`, let

`S_vowel(i, c)` = summed log probability assigned to the vowel-sound continuation under condition `c`, and

`S_cons(i, c)` = summed log probability assigned to the consonant-sound continuation under condition `c`.

Define the sound contrast

`D(i, c) = S_vowel(i, c) - S_cons(i, c)`.

For an intervention `z`, the paired causal effect is

`tau_i(z) = D(i, z) - D(i, natural)`.

Reported condition effects aggregate `tau_i` at the predeclared unit of independence.

## Independence and resampling

Lexical derivatives are not independent root families. The confirmatory analysis therefore resamples at the **family** level rather than the individual surface-form level. This is especially important for the rare consonant-spelling/vowel-sound cell, where only four ordinary root families are currently available.

The package includes a dependency-light family bootstrap implementation in `src/attention_not_all/stats.py`.

## Multiple testing

The proposed primary confirmatory family contains four declared tests. Holm's step-down procedure controls the family-wise error rate. Exploratory contrasts remain labeled exploratory rather than being mixed into the confirmatory family post hoc.

## Alternate-dictionary robustness

A second dictionary at the same model layer/width can test whether a result is tied to one SAE factorization. The alternate coordinate is chosen using dictionary geometry and selection information without access to test effects.

This is useful robustness evidence but **not** independent-model replication because both dictionaries decompose the same underlying model.

## Position-specific causal tracing

The planned extension localizes when the effect becomes causally available:

1. run a corrupted or feature-ablated reference;
2. restore the natural activation/state at one token position and layer at a time;
3. measure recovery of the primary continuation contrast;
4. compare recovery against position-matched controls.

The causal unit is restoration of model state, not correlation between activation and outcome.

## Path-specific MLP mediation

The planned MLP analysis compares natural, ablated, restored, and downstream-blocked computations. Group tests and leave-one-out tests are retained. A mediator is only promoted if restoration changes the target effect and the path survives relevant blocking/control logic.

## Grouped attention tests

Attention is tested rather than assumed away. The extension scans grouped heads, compares restoration/blocking effects, and retains head-level multiplicity controls. A result that finds attention involvement is not a failure of the project.

## Natural-text activation mapping

Frozen natural documents provide an external-distribution diagnostic:

- activation frequency and magnitude;
- top contexts;
- lexical-family enrichment;
- false-positive semantic regions;
- model/dictionary differences.

Natural-text mapping is interpretation evidence; it does not substitute for causal tests.

## Precision and compute

The reference inference target is FP32 where feasible. Lower precision may be used for smoke tests or memory-limited cross-model pilots, but precision changes must be recorded as separate runs rather than silently combined.

## Audit requirements

A result is analyzable only after verifying:

- expected trial IDs are present;
- no duplicate trial-condition keys exist;
- scores are finite;
- all required conditions are represented;
- model/SAE revisions and contract hashes match;
- worker completion is interpreted correctly;
- resumption did not alter the frozen schedule.

The previous `complete: false` report arose from a checker that treated worker log files as directories; coverage must therefore be audited from records and declared keys, not a single convenience flag.
