# NeuroSteer Evaluation Protocol

This protocol defines the minimum evidence required before making performance claims.

## A. Representation benchmark

For each selected model and layer set:

- collect a fixed activation corpus;
- train independent per-layer SAE baseline;
- train grouped-layer SAE;
- hold architecture and optimizer family constant where possible;
- repeat at least 3 seeds for stability analysis.

Record reconstruction error, explained variance, L0, dead features, training time, peak memory, and accelerator-hours.

## B. Grouping benchmark

Compute pairwise layer similarity using a precisely defined angular-distance statistic. Record:

- layer pairs;
- similarity distribution;
- chosen grouping threshold;
- resulting groups;
- within-group and between-group statistics.

The grouping method must be deterministic for a fixed input corpus and configuration.

## C. Feature matching

Match features between independently trained systems using cosine similarity and activation-response agreement over a held-out corpus. Report distributions rather than only a single best match.

## D. Causal steering benchmark

For each candidate feature or steering direction:

1. establish a no-intervention baseline;
2. define a target behavior metric before running the intervention;
3. sweep steering coefficient over a pre-registered range;
4. evaluate target effect and off-target capability;
5. repeat over multiple prompt sets and random seeds.

A steering effect must be directional, repeatable, and distinguishable from prompt-only effects.

## E. Latency benchmark

Measure the same serving stack with and without steering. Warm the system before measurement and report p50, p95, and p99 end-to-end latency plus the incremental steering overhead.

Benchmark at the intended batch/concurrency setting and record hardware, model quantization, sequence length, and runtime configuration.

## F. Safety / reliability boundary

The prototype must not be described as a complete safety mechanism. Evaluate failure cases including:

- prompt distribution shift;
- adversarially chosen prompts;
- weakly activated or polysemantic features;
- intervention sign reversal;
- excessive steering coefficients;
- cross-model transfer failure;
- closed-weight deployment constraints.

## G. Reporting template

Every experiment should generate a machine-readable result containing:

```json
{
  "model": "",
  "revision": "",
  "layers": [],
  "activation_source": "",
  "dataset": "",
  "seed": 0,
  "sae": {},
  "grouping": {},
  "steering": {},
  "metrics": {},
  "hardware": {},
  "runtime": {},
  "status": ""
}
```

## H. Decision gates

**Gate 1 — Representation:** grouped method must provide a measurable systems advantage while retaining acceptable representation metrics.

**Gate 2 — Causality:** selected features must produce repeatable behavioral interventions.

**Gate 3 — Operations:** the intervention must meet the defined latency budget in a realistic serving environment.

**Gate 4 — Product:** only after Gates 1–3 should enterprise design-partner pilots be proposed around a specific high-value use case.
