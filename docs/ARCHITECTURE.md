# NeuroSteer Technical Architecture

## Research architecture

```text
Open-weight model
      │
      ▼
Activation capture
      │
      ├── per-layer baseline
      │
      └── grouped-layer representation
                  │
                  ▼
             Sparse features
                  │
          ┌───────┴────────┐
          ▼                ▼
   feature analysis    causal tests
          │                │
          └───────┬────────┘
                  ▼
          steering direction
                  │
                  ▼
        inference-time control
                  │
                  ▼
     target / off-target evaluation
```

## Design principles

1. **Open-weight first.** The first implementation assumes access to model activations and does not depend on proprietary closed-weight APIs.
2. **Measurement before productization.** Every proposed optimization is benchmarked against a transparent baseline.
3. **Causal validation.** Correlation between a feature and a behavior is not sufficient to declare a feature controllable.
4. **Bounded interventions.** Steering strength and intervention location must be explicit, logged, and reproducible.
5. **Failure visibility.** The system must preserve failed experiments and regressions.

## Prototype boundaries

The current code provides framework-independent mathematical primitives. Full transformer activation extraction, SAE training, model execution, and large-scale benchmarking are intentionally separate layers so the research core remains testable without forcing a heavyweight runtime dependency.

## Product evolution

The research prototype can later become a service boundary with:

- model adapters;
- feature-store/checkpoint management;
- policy definitions;
- offline regression suites;
- runtime intervention middleware;
- observability and audit logs.

Those layers are future work and should not be represented as implemented functionality until committed code exists.
