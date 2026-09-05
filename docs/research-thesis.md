# NeuroSteer Research Thesis

## 1. Problem

Modern language models expose behavior at the output layer while much of the computation that produces that behavior remains difficult to inspect and intervene on. Sparse Autoencoders (SAEs) provide one route toward decomposing activations into sparse features. Activation engineering provides a route to modify internal activations at inference time.

NeuroSteer asks whether those two ideas can be combined into a practical, measurable control plane for open-weight language models.

## 2. Core hypothesis

**H1:** A shared or grouped feature dictionary learned across selected neighboring layers can preserve sufficient reconstruction quality and causal usefulness while reducing the cost of training and serving separate per-layer SAEs.

**H2:** Interpretable features identified by the representation can be converted into steering interventions that produce predictable changes in target behavior with bounded off-target degradation.

**H3:** A production-oriented steering layer can operate within a defined latency budget on selected open-weight models.

None of these hypotheses are presented as proven by this repository before measurement.

## 3. Falsification criteria

H1 is rejected for a model/configuration if grouping causes a material degradation in reconstruction or causal metrics relative to independent per-layer baselines, or if savings are not statistically meaningful.

H2 is rejected if steering does not produce a repeatable target effect, has unstable directionality across prompts/seeds, or causes unacceptable off-target degradation.

H3 is rejected if the intervention cannot satisfy the predefined p50/p95/p99 latency budget under the chosen serving configuration.

## 4. Baselines

Every grouped experiment must be compared against:

1. no intervention;
2. independently trained per-layer SAE;
3. grouped SAE;
4. simple activation steering baseline where applicable.

## 5. Experimental controls

- fixed model checkpoint per experiment;
- fixed tokenizer and preprocessing;
- explicit random seeds;
- train/validation/test separation where applicable;
- repeated runs for variance estimation;
- hardware and software versions logged;
- configuration committed to the repository;
- generated results separated from source code.

## 6. Required metrics

### Representation quality

- reconstruction MSE;
- explained variance;
- activation sparsity (L0);
- dead-feature rate;
- feature activation frequency.

### Stability

- feature matching across seeds;
- cosine/angular similarity;
- cluster consistency across layers;
- variance of feature semantics under perturbations.

### Causal usefulness

- target behavior effect size;
- intervention success rate;
- dose-response / steering-strength curve;
- off-target task retention.

### Systems

- training wall-clock time;
- accelerator-hours;
- peak memory;
- inference latency p50/p95/p99;
- throughput;
- steering overhead relative to baseline.

## 7. Interpretation policy

A metric improvement on one benchmark is insufficient for a generalized claim. Claims will be scoped to the evaluated model, layer selection, dataset, and intervention family. Results that contradict the hypothesis will be preserved and documented.

## 8. Product bridge

The long-term product hypothesis is a middleware control layer for organizations deploying open-weight models. The research prototype is successful when it establishes a causal and operational link between interpretable latent features and controllable model behavior. Enterprise guarantees are a later validation phase, not assumptions of the research prototype.
