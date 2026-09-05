# Research Status & Evidence Ledger

Updated: 2026-09-05

## Evidence levels

### E0 — Prior literature
Established by external research literature. These are not NeuroSteer results.

- Sparse Autoencoders can be used to discover comparatively interpretable features in language-model activations.
- Activation engineering / steering can modify model behavior at inference time.

Primary references: `docs/references.md`.

### E1 — Repository implementation
Implemented and tested in this repository.

- vector norms and cosine similarity;
- normalized angular distance;
- additive steering primitive;
- transparent cross-layer grouping baseline;
- deterministic smoke test;
- unit tests and CI workflow.

### E2 — Research result
**Not yet populated.** Requires a real-model experiment with committed configuration and measured output.

### E3 — Product validation
**Not yet populated.** Requires user interviews, concrete workflow evidence, and ideally design-partner validation.

## Current hypotheses

H1. Neighboring layers contain enough transferable structure for grouped SAE training to reduce redundant training work while preserving useful reconstruction and causal behavior.

H2. Angular-similarity grouping is a useful baseline for identifying candidate layer clusters.

H3. Feature-derived steering can create repeatable target behavior changes with acceptable off-target degradation.

H4. A production control plane can expose these interventions with operationally acceptable latency, memory use, observability, and failure handling.

## What would falsify the thesis

The project should pivot or narrow materially if:

- grouped SAEs offer no reproducible compute/memory advantage at matched quality;
- cross-layer features fail to transfer causally across seeds or prompts;
- steering works only with substantial off-target degradation;
- operational overhead is incompatible with the intended inference workloads;
- customers do not identify a recurring high-value workflow requiring latent intervention.

## Evidence rule

A result may be promoted from hypothesis to demonstrated result only when the repository includes:

1. source/configuration;
2. model and checkpoint identifier;
3. hardware/software environment;
4. fixed seed(s);
5. raw or machine-readable result;
6. evaluation script;
7. interpretation and limitations.
