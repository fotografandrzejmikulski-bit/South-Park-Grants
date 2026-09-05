# South Park Commons Founder Fellowship — Application Draft

## NeuroSteer
### Interpretable, controllable inference for open-weight language models

**Founder:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Repository:** https://github.com/fotografandrzejmikulski-bit/South-Park-Grants

---

## Executive Summary

I am building NeuroSteer, a research-driven infrastructure company exploring whether interpretable representations learned from language-model activations can become a practical control layer for open-weight and self-hosted language models.

The immediate research question is deliberately narrow: can Sparse Autoencoders (SAEs), cross-layer representation analysis, and activation steering be combined into a reproducible system that identifies behavior-relevant features and intervenes on them during inference while preserving unrelated capabilities?

The long-term company thesis is a developer and enterprise control plane for models that customers can run themselves: inspect latent behavior, identify causally relevant features, apply bounded interventions, and measure the resulting trade-offs. The first product should be earned by experiments rather than assumed in advance.

I am applying as a solo founder. My goal in SPC is to compress the transition from technical hypothesis to strong evidence, while using the SPC community to pressure-test the market, recruit a technical co-founder if the work warrants one, and turn a validated research result into a venture-scale product.

## Why this problem

Modern language models are highly capable but difficult to inspect and control internally. Prompt-level controls operate outside the representation space, while retraining or fine-tuning can be costly and can change behavior more broadly than intended.

Prior research suggests that learned activation features and inference-time interventions can expose useful structure inside neural networks. The unresolved commercial question is whether those techniques can be made sufficiently stable, measurable, low-overhead, and operationally reliable for repeated use on customer-controlled open-weight models.

NeuroSteer focuses on that gap.

## The core hypothesis

The project has three linked hypotheses:

1. **Feature discovery:** Sparse Autoencoders can recover useful, behavior-relevant directions from transformer activations.
2. **Cross-layer sharing:** neighboring layers may share enough representational structure that grouped SAE training can reduce redundant computation without unacceptable loss of reconstruction or causal usefulness.
3. **Controlled intervention:** steering derived from validated features can change a target behavior while retaining off-target model capability within a measurable tolerance.

A proposed grouping metric based on angular similarity between layer representations will be tested rather than asserted. A proposed Neural-Operator formulation (SAE-NO) is also treated as a research hypothesis, not as an established performance improvement.

## Initial vertical slice

The first complete technical loop is:

`model activations → baseline SAE → layer grouping → feature inspection → causal steering vector → controlled generation → behavioral evaluation → latency measurement`

The vertical slice is intentionally narrow. Its purpose is to produce a falsifiable result with reproducible measurements, not to simulate a finished enterprise platform.

## What success looks like

The first milestone is not a vanity metric. It is a decision-quality dataset that answers:

- whether grouped training preserves useful representation quality;
- whether features remain consistent across seeds and prompts;
- whether selected features cause the intended behavior change;
- how much off-target capability moves;
- what latency and memory overhead the intervention introduces;
- which failure modes prevent production use.

A negative result is valuable if it clearly falsifies part of the thesis and identifies a better direction.

## Evaluation

Every experiment will record:

- model and checkpoint identifier;
- layer selection and activation extraction method;
- dataset/configuration;
- random seed;
- SAE architecture and hyperparameters;
- reconstruction error / explained variance;
- L0 sparsity and dead-feature rate;
- feature consistency across seeds;
- cross-layer similarity and overlap;
- intervention effect size;
- off-target capability retention;
- steering success rate;
- p50/p95/p99 inference overhead;
- memory and compute cost;
- software and hardware versions.

The repository is structured so that committed configurations are the source of truth for reproducibility.

## Product hypothesis

If the experiments demonstrate sufficient stability and causal control, NeuroSteer can evolve into middleware for organizations operating open-weight or self-hosted models.

A future product would expose:

- activation and feature inspection;
- versioned intervention policies;
- bounded steering vectors;
- evaluation gates before deployment;
- latency and regression telemetry;
- auditability of interventions;
- adapters for common open-weight inference stacks.

The product will explicitly avoid claiming that latent steering alone guarantees elimination of hallucinations, PII extraction, or all unsafe behavior. Those require application-level controls, model evaluation, and defense-in-depth.

## Why SPC

SPC is unusually well matched to this stage because the value of the next step is primarily in reducing uncertainty rather than maximizing short-term feature output. The Founder Fellowship explicitly supports founders at the -1 to 0 stage, provides direct partner support, and allows open timelines around validation and fundraising. SPC also states that solo founders can apply and that co-founders can be found within the community.

The fit is therefore specific: I need an environment where technical assumptions, market assumptions, founder-market fit, and team composition can be challenged in parallel.

## Capital plan

The current SPC Fall 2026 public terms state:

- $400,000 upfront for 7% via a standard SAFE;
- $600,000 guaranteed in the next external funding round;
- up to $1M in credits and perks.

I would use the initial capital conservatively around three priorities: research and compute, founder runway, and customer discovery. I would not commit to large hiring or infrastructure contracts before experimental evidence supports them.

## 90-day plan

### Phase 1 — Establish baselines

Reproduce a small SAE baseline on a documented open-weight model, verify activation extraction, and establish evaluation harnesses.

**Exit criterion:** all baseline metrics and artifacts regenerate from a committed configuration.

### Phase 2 — Test grouping

Compare independently trained per-layer SAEs against grouped-layer variants using matched compute budgets and seeds.

**Exit criterion:** quantitative comparison of reconstruction, sparsity, feature consistency, and compute/memory cost.

### Phase 3 — Test causal steering

Select candidate features, derive steering vectors, run controlled interventions, and measure target effect versus off-target degradation.

**Exit criterion:** repeatable intervention results across multiple prompts/seeds with explicit failure analysis.

### Phase 4 — Product discovery

Interview technically sophisticated users of self-hosted/open-weight models. Identify the narrowest workflow for which the research result creates economic value.

**Exit criterion:** a clearly specified design-partner problem and a product wedge justified by evidence.

## Founder

**Andrzej Mikulski** is applying as a solo founder with the intention to build at the intersection of machine-learning research and practical AI infrastructure. The immediate objective is to demonstrate disciplined empirical progress. Team expansion will follow the technical and commercial evidence, not precede it.

## Risks

### Technical risk
The proposed grouping method may not preserve causal usefulness across layers or model families.

**Mitigation:** matched baselines, multiple seeds, causal tests, and explicit negative-result reporting.

### Stability risk
SAE feature dictionaries may vary significantly across training runs.

**Mitigation:** quantify feature consistency and treat instability as a first-class metric rather than hiding it behind aggregate scores.

### Product risk
A technically interesting steering mechanism may not map to a customer-critical workflow.

**Mitigation:** run customer discovery in parallel with technical validation and require a concrete design-partner problem before building a broad API.

### Access risk
Closed-weight APIs may not expose internal activations.

**Mitigation:** prioritize open-weight and self-hosted deployments where the operator controls the model and inference stack.

## Long-term ambition

The long-term ambition is to make model behavior more inspectable and controllable without requiring every behavioral change to become a new model-training cycle.

The first step, however, is much smaller: prove or disprove that a reproducible representation-and-steering loop can deliver enough causal control at an acceptable operational cost.

That is the mountain I want to climb with SPC.

---

## Application integrity note

This document intentionally distinguishes established prior research, current implementation, target outcomes, and unverified hypotheses. Performance figures are not presented as achieved unless backed by repository evidence. This is a research-stage application, not a claim of production readiness.
