# Reproducing the research package

This repository separates **artifact validation** from **GPU reproduction**.

## 1. Validate the repository without model weights

Requires Python 3.10+.

```bash
python -m pip install -e .
python scripts/verify_artifacts.py
pytest -q
```

These checks validate the claim ledger, model registry, required documentation, and the dependency-light statistical utilities.

## 2. Freeze an execution environment

For any GPU run, record at minimum:

- Python version;
- PyTorch version;
- CUDA and driver versions;
- GPU type/count;
- model repository and exact revision;
- SAE repository and exact revision;
- tokenizer revision;
- precision/dtype;
- random seeds;
- experiment contract hash;
- trial schedule hash;
- code commit hash.

Never replace a prior manifest when changing precision or model revision. Create a new run directory.

## 3. Smoke test before the full schedule

A smoke run should exercise:

1. model load;
2. SAE load;
3. hook/intervention insertion;
4. one natural trial;
5. one selected-feature intervention;
6. one random-direction control;
7. serialization;
8. resume logic;
9. analysis parsing.

Only then launch the full grid.

## 4. Resume safely

Long GPU jobs should be restartable from durable storage. The schedule is frozen before execution and each trial-condition key is idempotent. On resume:

- reload the same schedule;
- skip keys already present and valid;
- append only missing keys;
- preserve logs and failure records;
- re-run the coverage audit after completion.

Closing a local laptop does not stop a properly detached RunPod/Kaggle remote process, but instance lifecycle and storage persistence depend on the provider configuration. Always copy final manifests/results to durable storage before terminating a pod.

## 5. Gemma 2 exploratory reproduction

The historical Gemma 2 run used Gemma 2 2B with a Gemma Scope residual-stream SAE. The clean reproduction should preserve the original stimuli and intervention contract while rerunning in a fresh environment.

Recommended sequence:

1. run FP32 smoke test;
2. reproduce feature-selection inputs without using test effects;
3. execute the original-dictionary schedule;
4. execute alternate-dictionary robustness as a separate run;
5. audit expected keys and finiteness;
6. aggregate paired sound-contrast effects;
7. compare to the frozen historical tables;
8. investigate any discrepancy before updating claims.

## 6. Cross-model replication

Follow `replication/protocol/PROTOCOL.md`.

Each model must select its own coordinate. Do not use the Gemma feature ID or a presumed semantic match as the selection target. The replicated object is the **relationship between a selected sparse coordinate and the controlled behavior**.

## 7. Raw evidence layout before publication

Large evidence files should eventually be frozen under a structure like:

```text
replication/evidence/
  gemma2_original/
    manifest.json
    schedule.json
    records.jsonl
    logs/
  gemma2_alternate/
    manifest.json
    schedule.json
    records.jsonl
    logs/
  gemma3/
  llama/
  qwen/
```

For each directory, publish SHA-256 checksums in `publication/ARTIFACTS.md` or a generated manifest.

## 8. Do not fabricate missing artifacts

This repository currently contains the research narrative, protocol, status, audit/statistical utilities, and publication structure. Raw GPU evidence and executed notebooks should be copied from the actual completed runs. A placeholder is preferable to invented bytes, fake registration URLs, or reconstructed timestamps.
