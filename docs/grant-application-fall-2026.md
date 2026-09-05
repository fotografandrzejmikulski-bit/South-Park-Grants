# South Park Commons Founder Fellowship — Fall 2026

## Applicant

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337

## Project

# NeuroSteer

### Interpretable, controllable inference for open-weight language models

## 1. What are you building?

I am exploring a new inference-control layer for open-weight language models.

The technical question is simple to state and difficult to solve: **can we identify interpretable features inside a language model and use those features to make targeted, measurable behavioral interventions during inference—without retraining the base model for every change?**

NeuroSteer combines two research directions with strong prior evidence: Sparse Autoencoders (SAEs) for discovering interpretable activation features, and activation engineering for steering model behavior at inference time. The new work is to investigate whether the representation layer itself can be made cheaper, more stable, and more operationally useful through cross-layer grouping and subsequent causal steering.

This is an early-stage research project. I deliberately distinguish established results from NeuroSteer's hypotheses in the repository.

## 2. Why now?

Mechanistic interpretability has progressed from a qualitative research idea toward a practical engineering discipline. Prior work has shown that SAEs can expose more interpretable features in language-model activations, while activation engineering has shown that intermediate activations can be modified to steer behavior during a forward pass.

The remaining opportunity I want to investigate is the engineering layer between those research results and a dependable inference-control system: representation cost, feature stability, causal validation, latency, and deployment constraints.

## 3. What is the key insight?

The initial hypothesis is that neighboring layers may contain sufficiently related structure that a carefully designed grouped representation can share learned feature dictionaries across layers rather than requiring an entirely independent SAE for every layer.

This may reduce training and serving cost, but I do **not** claim a 50% reduction as an established result. The repository defines the experiment needed to test that claim.

A second hypothesis is that useful, causally identified features can be converted into controllable steering directions. The research goal is to measure whether a target behavior can be changed predictably while preserving off-target capabilities.

## 4. What have you built?

The public repository currently contains the project thesis, evaluation protocol, references, a dependency-free steering primitive, tests, configuration, and CI. The first vertical slice is:

**activations → representation baseline → grouped-layer experiment → feature analysis → steering intervention → behavioral evaluation → latency measurement**

The present implementation is intentionally small. It makes the scientific loop explicit and reproducible before introducing large model dependencies.

Repository: https://github.com/fotografandrzejmikulski-bit/South-Park-Grants

## 5. What remains to be proven?

There are three core validation gates:

**Representation:** grouped SAE must demonstrate a meaningful systems advantage without unacceptable degradation in reconstruction and feature quality.

**Causality:** candidate features must produce repeatable behavioral interventions, not correlations that disappear under controlled evaluation.

**Operations:** the intervention must satisfy a predefined latency budget on a realistic open-weight serving stack.

Only after these gates pass would I treat an enterprise design-partner product as justified.

## 6. Who is the initial customer?

The initial commercial hypothesis is organizations that need greater control over self-hosted or open-weight language models and cannot depend exclusively on prompt-level controls.

Potential early users include teams operating regulated or security-sensitive AI systems where they need observable, testable controls over model behavior and an audit trail of interventions.

I would start with a narrow workflow rather than attempting to sell a generic “AI safety” platform.

## 7. Why South Park Commons?

This project is unusually well matched to SPC's -1 to 0 model. The problem spans research, systems engineering, product discovery, and founder-market fit, and I expect the highest-leverage progress to come from testing the thesis with exceptional technical peers and iterating quickly on evidence.

SPC's current Founder Fellowship offers $400K for 7% upfront on a standard SAFE plus a $600K guarantee in the next external venture round. SPC also states that Founder Fellows receive up to $1M in credits and perks. My use of the program would therefore be centered on rapid empirical validation, not on assuming that a large infrastructure budget automatically proves the thesis.

## 8. What would I do with the first $400K?

The capital would be used conservatively around four objectives:

- full-time founder runway and eventual technical co-founder recruitment;
- model experimentation and compute for reproducible representation studies;
- customer discovery and design-partner validation after the technical gates pass;
- legal, incorporation, security, and operating infrastructure.

I would not commit to large-scale compute consumption before the experiments establish that the method is worth scaling.

## 9. What is the 6–12 month plan?

**Phase 1 — Research validation:** establish the baseline, grouped representation experiment, feature-stability measurements, and causal steering benchmarks.

**Phase 2 — Systems validation:** integrate the strongest intervention into an open-weight inference stack and measure p50/p95/p99 latency, throughput, memory, and failure modes.

**Phase 3 — Customer discovery:** test one narrowly defined enterprise workflow with design partners and determine whether the technical advantage maps to a sufficiently painful business problem.

**Phase 4 — Company formation / financing:** once technical and customer evidence is strong, formalize the company structure and prepare for an external seed process.

## 10. What could make this fail?

The most important risk is that grouped representations do not preserve the properties needed for causal intervention. In that case the project should narrow the method rather than manufacture a product narrative around weak results.

A second risk is closed-weight model access. The initial product thesis therefore targets open-weight and self-hosted models, where internal activations can actually be instrumented.

A third risk is that steering is effective in benchmarks but too fragile for production. The evaluation protocol therefore treats stability, off-target effects, adversarial conditions, and tail latency as first-class measurements.

## 11. Why me?

I am approaching this as a builder-founder problem rather than as a claim that the research is already solved. My current work emphasizes turning an ambitious thesis into a falsifiable technical artifact, documenting what is known versus hypothesized, and using empirical evidence to decide where the company should go next.

SPC is particularly attractive because it can help pressure-test the thesis, identify the strongest version of the problem, and connect the research to the right technical collaborators and eventual customers.

## 12. North Star

**Make internal model behavior measurable and controllable enough that inference-time intervention becomes an engineering primitive rather than a research demo.**

The immediate objective is not to promise a universal solution. It is to determine, rigorously, whether there is a commercially valuable and technically defensible control layer hidden inside this research direction—and, if so, build it.
