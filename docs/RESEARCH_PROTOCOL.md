# NeuroSteer Research Protocol

## Objective

Determine whether cross-layer grouping of sparse activation features can reduce redundant representation-learning work while maintaining feature quality and causal usefulness.

## Experimental discipline

Each experiment must define before execution:

- model and exact checkpoint;
- layers and activation tensor location;
- activation dataset and sample count;
- random seeds;
- SAE architecture and dictionary expansion;
- sparsity mechanism and k/top-k settings;
- optimizer, learning rate, batch size, training steps;
- grouping rule and similarity threshold;
- steering intervention definition;
- target and off-target evaluation tasks;
- hardware and software versions.

## Comparisons

At minimum, compare:

1. independent per-layer SAE baseline;
2. grouped-layer SAE candidate;
3. ablation with grouping disabled;
4. multiple random seeds.

The same evaluation budget should be used wherever feasible. Any deviation must be documented.

## Primary metrics

### Representation quality

- reconstruction MSE;
- explained variance;
- sparsity / L0;
- dead-feature rate.

### Stability

- feature similarity across seeds;
- feature similarity across neighboring layers;
- cluster stability under bootstrap or resampling.

### Causal usefulness

- target behavior effect size;
- success rate at predefined steering strength;
- dose-response curve;
- off-target capability retention;
- regressions on unrelated tasks.

### Systems

- training wall-clock time;
- peak memory;
- estimated accelerator-hours;
- inference p50/p95/p99 overhead.

## Acceptance logic

No single threshold is treated as universally sufficient. A grouping method advances only if the total evidence supports the intended trade-off between computational savings, representation fidelity, feature stability, and causal usefulness.

The 50% cost-reduction figure from earlier concept documents is a target hypothesis, not an established result. The repository must not report it as achieved without benchmark evidence.

Similarly, a sub-50 ms latency target is an operational target, not a demonstrated property.

## Reproducibility artifact

Each completed experiment should add a machine-readable record under `results/` containing:

- experiment ID;
- commit SHA;
- configuration path;
- seed;
- model/checkpoint;
- metrics;
- environment metadata;
- notes and known limitations.

## Negative results

Failed experiments, null effects, instability, and regressions should be retained with an explanation. The project optimizes for decision quality, not selective reporting.
