"""Evaluation metrics used by NeuroSteer experiments."""

from __future__ import annotations

from math import sqrt
from typing import Sequence


def mean_squared_error(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must have identical dimensions")
    if not a:
        raise ValueError("vectors must not be empty")
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


def explained_variance(original: Sequence[float], reconstruction: Sequence[float]) -> float:
    if len(original) != len(reconstruction):
        raise ValueError("vectors must have identical dimensions")
    if not original:
        raise ValueError("vectors must not be empty")
    mean = sum(original) / len(original)
    total = sum((x - mean) ** 2 for x in original)
    if total == 0.0:
        return 1.0 if mean_squared_error(original, reconstruction) == 0.0 else 0.0
    residual = sum((x - y) ** 2 for x, y in zip(original, reconstruction))
    return 1.0 - residual / total


def l0_count(values: Sequence[float], threshold: float = 0.0) -> int:
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    return sum(1 for value in values if abs(value) > threshold)


def relative_latency_overhead(baseline_ms: float, steered_ms: float) -> float:
    if baseline_ms <= 0 or steered_ms < 0:
        raise ValueError("latencies must be positive/non-negative")
    return (steered_ms - baseline_ms) / baseline_ms


def vector_rms(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sqrt(sum(value * value for value in values) / len(values))
