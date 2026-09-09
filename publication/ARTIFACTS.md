# Publication artifact inventory

This file distinguishes artifacts that exist in the repository now from evidence that must be copied from the actual compute environment before public release.

## Present now

- `README.md` — reviewer-facing project overview.
- `STATUS.md` — evidence / running / pending separation.
- `paper/Manuscript.md` — current working manuscript.
- `docs/METHODS.md` — methods and estimands.
- `docs/CLAIMS.md` — evidence hierarchy and non-claims.
- `docs/LITERATURE.md` — selected research context.
- `replication/protocol/PROTOCOL.md` — prospective confirmation protocol.
- `replication/claim_ledger.csv` — claim states.
- `replication/models/registry.json` — model/resource status.
- `src/attention_not_all/` and `tests/` — auditable statistical logic.

## Must be imported from real runs

Do not synthesize these files. Copy them from the completed Kaggle/RunPod outputs and preserve bytes.

### Gemma 2 original dictionary

- execution manifest;
- frozen schedule;
- raw trial records;
- worker logs;
- selection artifact;
- aggregate tables;
- environment metadata;
- executed notebook or launcher code.

### Gemma 2 alternate dictionary

Same categories as above plus the dictionary-match artifact.

### Cross-model extensions

For Gemma 3, Llama, and Qwen preserve discovery, selection, selection failure (if any), intervention, tracing, path, attention, natural-text, and analysis artifacts independently.

## Checksums

Before publication, generate SHA-256 checksums for every frozen evidence file and record:

- path;
- byte size;
- SHA-256;
- producing commit;
- model/SAE revision;
- run timestamp;
- execution environment identifier.

## Provenance rule

A publication table should be traceable backward:

`claim -> analysis output -> raw records -> schedule -> feature lock -> data hashes -> model/SAE revisions -> code commit`.

If any link is missing, treat the corresponding claim as not publication-ready.
