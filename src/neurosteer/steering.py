"""Small, dependency-free primitives used by the research prototype.

These functions intentionally operate on generic array-like objects so the core
logic can be tested without requiring a specific deep-learning framework.
"""

from __future__ import annotations

from math import sqrt
from typing import Iterable, Sequence


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must have identical dimensions")
    return sum(x * y for x, y in zip(a, b))


def l2_norm(v: Sequence[float]) -> float:
    """Return the Euclidean norm of a vector."""
    return sqrt(_dot(v, v))


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    """Return cosine similarity in [-1, 1]."""
    na, nb = l2_norm(a), l2_norm(b)
    if na == 0.0 or nb == 0.0:
        raise ValueError("cosine similarity is undefined for zero vectors")
    return _dot(a, b) / (na * nb)


def angular_distance(a: Sequence[float], b: Sequence[float]) -> float:
    """Return normalized angular distance, where 0 means identical direction."""
    sim = max(-1.0, min(1.0, cosine_similarity(a, b)))
    # Normalized angle: 0 for identical and 1 for opposite directions.
    from math import acos, pi

    return acos(sim) / pi


def add_scaled(base: Sequence[float], direction: Sequence[float], scale: float) -> list[float]:
    """Apply an additive steering intervention: base + scale * direction."""
    if len(base) != len(direction):
        raise ValueError("base and direction must have identical dimensions")
    return [x + scale * d for x, d in zip(base, direction)]


def pairwise_mean_max_angular_distance(groups: Iterable[Sequence[float]]) -> float:
    """Compute the mean of maximum pairwise angular distances to other vectors.

    This is a small building block for experimenting with layer/group similarity.
    It is not claimed to be a canonical definition of AMAD.
    """
    vectors = [tuple(v) for v in groups]
    if len(vectors) < 2:
        return 0.0

    maxima: list[float] = []
    for i, current in enumerate(vectors):
        distances = [angular_distance(current, other) for j, other in enumerate(vectors) if i != j]
        maxima.append(max(distances))
    return sum(maxima) / len(maxima)
