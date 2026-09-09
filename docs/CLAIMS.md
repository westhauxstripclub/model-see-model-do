# Claims and interpretation boundaries

This project uses a deliberately conservative hierarchy of evidence. Sparse-autoencoder features are useful experimental coordinates, but a clean activation pattern is not by itself a mechanistic explanation.

## Four standards of evidence

### 1. Activation

**Question:** When is the feature naturally active?

Evidence can include activation distributions, top examples, lexical family contrasts, and natural-text maps.

**Does not establish:** semantic completeness, causal importance, or uniqueness.

### 2. Prediction

**Question:** Can causally available information in the representation predict a target?

A valid probe must exclude variables that directly reveal the label. The original project violated this rule by including the article in the probe input; that result is retired.

**Does not establish:** that the decoded variable is used by the model.

### 3. Causation

**Question:** Does a controlled edit to the representation change the model's behavior while visible inputs remain fixed?

Primary evidence is paired within-prompt change in continuation log probabilities. Controls include no-op edits, random directions, matched SAE directions, and alternate-dictionary replication.

**Does not establish:** that the edited coordinate is the unique natural representation, or that every induced state lies on-manifold.

### 4. Mechanism

**Question:** Which positions and computational paths mediate the causal effect?

Planned evidence includes restoration/tracing, controlled MLP path tests, grouped-attention tests, and downstream blocking.

**Does not establish:** a unique circuit unless plausible alternatives have been ruled out.

## Current supported statement

The saved exploratory Gemma 2 grids support a narrow statement:

> In the tested held-out lexical families and prompt carriers, removing the selected Gemma Scope coordinate changes the spelling-balanced vowel-vs-consonant continuation contrast after **an**, with a similar sign and magnitude pattern in an alternate same-layer dictionary.

This is a within-model causal result. It is not yet a population-level or cross-model claim.

## Explicit non-claims

The repository does **not** currently claim:

- a universal “phonology neuron”;
- one-to-one semantic correspondence between SAE features and human concepts;
- that decoder cosine establishes semantic identity;
- that the selected feature is the only route by which the behavior is computed;
- a proven serial MLP circuit;
- that attention is absent or unnecessary;
- equivalence from near-zero estimates;
- independent replication from a second SAE trained on the same model;
- population generalization from lexical derivatives treated as independent samples;
- confirmation from any pilot-selected feature.

## Why the title is allowed to be provocative

“Attention Is Not All You Need” is a project title, not a scientific conclusion. The mechanistic program explicitly tests attention involvement. A negative grouped-attention result would be informative; a positive result would be equally compatible with the project's core thesis that causal feature analysis must go beyond surface activation examples.

## Claim promotion rule

A claim moves from `pending` to `supported` only when:

1. the relevant analysis was specified before examining its test effect;
2. the intended data partition was respected;
3. trial coverage and numerical validity pass audit;
4. the statistic is computed at the declared unit of independence;
5. required multiplicity correction is applied;
6. negative controls behave as expected or are discussed;
7. the result is recorded in the claim ledger together with scope and limitations.

A failure at any stage remains visible as `retired`, `null`, `failed_selection`, or `blocked` rather than being silently replaced.
