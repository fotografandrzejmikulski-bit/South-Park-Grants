# NeuroSteer — Executive One-Pager

**Founder:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Repository:** https://github.com/fotografandrzejmikulski-bit/South-Park-Grants

## The thesis

NeuroSteer is a research-stage effort to make open-weight language models more **inspectable, controllable, and measurable at inference time**.

The initial wedge is narrow: determine whether Sparse Autoencoders (SAEs), cross-layer representation analysis, and activation steering can form a reproducible control loop that changes a targeted behavior while preserving unrelated capability.

## Why now

Inference-time model intervention is becoming more important as organizations deploy increasingly capable models inside workflows where retraining every behavioral change is too slow, expensive, or operationally undesirable. The opportunity is not to replace model providers; it is to build a control layer for organizations that operate models they can inspect and run themselves.

## What is differentiated

The proposed research combines three elements:

- interpretable feature discovery with SAEs;
- cross-layer grouping to test whether representational redundancy can be exploited;
- causal activation steering with explicit off-target regression measurement.

The cross-layer grouping and SAE-NO components are **hypotheses**, not claimed breakthroughs. The project is designed to prove or falsify them.

## First vertical slice

`activations → SAE baseline → grouped-layer comparison → feature validation → steering → controlled generation → behavioral evaluation → latency`

The first objective is a decision-quality benchmark, not a polished enterprise dashboard.

## Success criteria

A successful research milestone would demonstrate a favorable measured trade-off among:

- reconstruction / representation quality;
- sparsity and feature health;
- feature consistency across seeds;
- causal intervention effect;
- off-target capability retention;
- memory, compute, and latency overhead.

No fixed percentage or latency claim is treated as achieved until the repository contains reproducible evidence.

## Commercialization wedge

If the research validates sufficient stability and causal control, the product path is a middleware/control plane for open-weight and self-hosted inference stacks, including versioned intervention policies, evaluation gates, regression telemetry, and auditability.

## Why SPC

SPC's Founder Fellowship is explicitly designed for founders operating from -1 to 0: building conviction around frontier ideas before the final company shape is known. The program offers direct partner support, open timelines, and a community where technical collaborators and co-founders can be found.

## Current status

**Stage:** early research / prototype  
**Current proof:** reproducible reference primitives, tests, CI, methodology, and a defined vertical slice  
**Next proof:** benchmarked real-model experiments with committed configurations and measured results

## Application integrity

NeuroSteer deliberately separates prior research, current implementation, research hypotheses, targets, and achieved results. This prevents investor language from outrunning the evidence and makes the project easier to evaluate technically.
