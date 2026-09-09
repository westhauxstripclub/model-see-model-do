# Research context and selected literature

This is a concise map of literature most directly relevant to the project's design. It is not intended to be a comprehensive mechanistic-interpretability bibliography.

## Sparse autoencoders as interpretability tools

### Gemma Scope

Google DeepMind released Gemma Scope in 2024 as a large open suite of JumpReLU sparse autoencoders for Gemma 2 2B and 9B, spanning layers and sublayers. This project uses Gemma Scope as the reference dictionary ecosystem.

- Google DeepMind, **“Gemma Scope: helping the safety community shed light on the inner workings of language models”** (2024): https://deepmind.google/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/

### Gemma Scope 2

Gemma Scope 2 extends the ecosystem to Gemma 3 and adds transcoders, including skip- and cross-layer transcoders, alongside Matryoshka-trained SAEs. This makes it especially relevant to the project's planned path-specific and cross-layer analyses.

- Google DeepMind, **Gemma Scope / Gemma Scope 2**: https://deepmind.google/models/gemma/gemma-scope/
- Google DeepMind, **“Gemma Scope 2: helping the AI safety community deepen understanding of complex language model behavior”** (2025): https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/

### Llama Scope

Llama Scope provides 256 SAEs across layers/sublayers of Llama-3.1-8B-Base with 32k and 128k feature dictionaries. It is the project's independent-family Llama resource.

- He et al., **“Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders”** (2024), arXiv:2410.20526: https://arxiv.org/abs/2410.20526

### Qwen-Scope

Qwen-Scope, released in 2026, provides SAEs for Qwen3 and Qwen3.5 model variants and demonstrates feature steering, representation-level evaluation analysis, data workflows, and post-training uses. Its release strengthens the case for a modern cross-family replication rather than restricting conclusions to Gemma.

- Deng et al., **“Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models”** (2026), arXiv:2605.11887: https://arxiv.org/abs/2605.11887
- Qwen Team, **“Qwen-Scope: Decoding Intelligence, Unleashing Potential”** (2026): https://qwen.ai/blog?id=qwen-scope

## Why causal testing is necessary

SAE features are learned coordinates optimized for reconstruction/sparsity objectives. Even when a feature has interpretable top activations, several ambiguities remain:

- correlated but unused information;
- feature splitting or merging across dictionary widths;
- decoder directions that are not unique causal variables;
- off-manifold effects introduced by intervention;
- dictionary-specific decompositions of the same model state.

Accordingly, this project treats activation examples as hypothesis generators and uses paired interventions, alternate dictionaries, controls, and cross-model replication to test stronger claims.

## Relation to feature steering

Recent SAE work increasingly uses features not only for description but for steering or control. Steering demonstrates that a direction can influence behavior, but the causal interpretation still depends on prompt controls, dose response, side effects, matched directions, and the distinction between an artificial control interface and the model's naturally used computation.

The present project therefore prioritizes **natural activation + removal/restoration + controls** before stronger mechanistic language.

## Relation to circuit analysis

Gemma Scope 2's transcoders and the broader move toward feature-level circuit methods motivate the extension from “does this coordinate matter?” to “where and through what path does its effect propagate?” The planned position-specific, MLP, attention, and downstream-blocking tests are designed to bridge that gap.

## Research position

The project takes a middle position between two weak extremes:

- **feature essentialism:** assuming a sparse coordinate is a literal, unique concept because examples look coherent;
- **feature nihilism:** dismissing learned sparse coordinates because they are not canonical.

A coordinate can be scientifically useful if it supports reproducible predictions and causal interventions with clearly stated scope—even if the representation is distributed, redundant, or dictionary-dependent.
