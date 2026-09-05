# NeuroSteer

### Interpretable, controllable inference for open-weight language models

**Founder:** Andrzej Mikulski  
**Contact:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Repository:** `fotografandrzejmikulski-bit/South-Park-Grants`

> Research-stage project. The repository is designed to make the thesis falsifiable, reproducible, and measurable rather than presenting hypotheses as established results.

## Thesis

NeuroSteer investigates whether interpretable features learned from language-model activations can be used as a low-latency control layer during inference. The initial research program combines Sparse Autoencoders (SAEs), cross-layer feature grouping, and activation steering.

The core product hypothesis is a middleware layer that allows an operator to inspect and selectively intervene on model behavior for open-weight / self-hosted models without retraining the base model for every behavioral change.

## What is proven vs. proposed

| Claim | Status |
|---|---|
| SAEs can expose more interpretable directions in LM activations | Supported by prior research |
| Activation addition can steer model behavior at inference time | Supported by prior research |
| Cross-layer Group-SAE can reduce training/computation cost without unacceptable loss of fidelity | **Research hypothesis — not yet proven here** |
| SAE-NO improves feature stability / reduces redundancy | **Research hypothesis — not yet proven here** |
| NeuroSteer can provide production-grade steering with <50 ms overhead | **Target — not yet demonstrated** |
| Enterprise PII / safety intervention can be reliably enforced by latent steering alone | **Target / research question — requires rigorous evaluation** |

## Research questions

1. Can neighboring transformer layers share a useful feature dictionary without materially degrading reconstruction fidelity or causal usefulness?
2. Does an angular-similarity grouping criterion identify stable layer clusters across seeds, prompts, and model families?
3. Can shared SAE representations reduce training cost and memory footprint relative to independently trained per-layer SAEs?
4. Which learned features causally control targeted behaviors, rather than merely correlating with them?
5. Can steering vectors derived from interpretable features achieve measurable behavioral changes while preserving off-target capability?
6. What latency, reliability, and failure modes arise when this control plane is placed directly in the inference path?

## Repository roadmap

- `docs/` — research thesis, methodology, evaluation protocol, product and grant material
- `src/neurosteer/` — reference implementation
- `experiments/` — reproducible experiment entry points
- `configs/` — model and experiment configuration
- `tests/` — unit and smoke tests
- `results/` — generated result schema and benchmark summaries
- `.github/workflows/` — continuous integration

## Initial vertical slice

The first reproducible vertical slice is intentionally narrow:

**model activations → baseline SAE → grouped-layer experiment → feature inspection → steering vector → controlled generation → behavioral evaluation → latency measurement**

The objective is not to claim a finished enterprise product. It is to demonstrate a complete causal research loop and identify the first quantitative evidence for or against the central hypothesis.

## Evaluation principles

We will report at minimum:

- reconstruction MSE / explained variance
- L0 sparsity
- dead-feature rate
- feature consistency across random seeds
- feature overlap / similarity across grouped layers
- causal intervention effect size
- off-target capability retention
- steering success rate
- inference latency overhead (p50 / p95 / p99)
- memory and compute consumption
- reproducibility across repeated runs

Negative results are retained. A hypothesis is considered validated only when the measured results justify the stated claim.

## Non-goals of the first prototype

The initial prototype does not claim to solve general AI safety, guarantee removal of hallucinations, prevent all PII extraction, or control closed-weight proprietary APIs that do not expose internal activations. These are longer-term product and research questions.

## Research basis

The project builds on established research into:

- polysemanticity and superposition in neural networks;
- Sparse Autoencoders as a method for discovering interpretable features;
- inference-time activation engineering / steering.

Primary references are listed in [`docs/references.md`](docs/references.md).

## Reproducibility

Experiments should record model identifier, layer, activation source, seed, dataset/configuration, SAE hyperparameters, checkpoint identifier, software version, hardware, and evaluation metrics. No result should be considered final unless it can be regenerated from a committed configuration.

## Research status

**Stage:** early research / prototype  
**Commercialization hypothesis:** B2B inference-control infrastructure for open-weight models  
**Current priority:** establish empirical evidence before expanding the product surface
