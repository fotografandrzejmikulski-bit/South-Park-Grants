# NeuroSteer — One-Page Founder Pitch

**Andrzej Mikulski**  
mojealterego21@gmail.com · +48 455 575 337

## The problem

Language models are increasingly deployed as critical infrastructure, but their internal representations remain difficult to inspect and control. Prompting and fine-tuning are useful, but neither provides a general, measurable control plane for model behavior during inference.

## The insight

NeuroSteer is testing whether sparse, interpretable activation features can become a practical control surface for open-weight models. The key research direction combines Sparse Autoencoders, cross-layer similarity analysis, and causal activation steering.

## The wedge

Build the smallest system that can answer one question convincingly:

**Can we identify a behavior-relevant latent feature, intervene on it during inference, measurably change the target behavior, and preserve unrelated capability at acceptable latency?**

## Why now

Open-weight models and self-hosted inference give operators direct access to model internals. This creates a growing surface for tooling that sits below the prompt layer and above raw model weights.

## 90-day proof plan

1. Establish a reproducible SAE baseline.
2. Compare independent per-layer training with grouped-layer variants.
3. Measure feature consistency across seeds and layers.
4. Validate causal steering and off-target preservation.
5. Benchmark latency, memory, and compute.
6. Use results to select one customer-critical workflow.

## Long-term product

A control plane for customer-operated models: inspect features, define bounded interventions, test them against regression suites, deploy versioned policies, and monitor latency and behavior.

## Why SPC

The project is at the stage where the highest-leverage work is reducing uncertainty. SPC's Founder Fellowship is explicitly designed for the -1 to 0 phase, provides direct partner involvement, allows solo founders, and combines funding with a dense technical community. That environment matches the project's current needs: challenge the research, find the market, and build conviction before scaling the company.

## Current status

The public repository contains the research thesis, reference primitives, tests, CI, evaluation protocol, and grant materials. It deliberately does not claim benchmark results that have not yet been run.

**Core repository:** https://github.com/fotografandrzejmikulski-bit/South-Park-Grants
