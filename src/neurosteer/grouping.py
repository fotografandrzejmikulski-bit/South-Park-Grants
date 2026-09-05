"""Layer grouping primitives for the NeuroSteer research program."""

from __future__ import annotations

from typing import Sequence

from .steering import angular_distance


def mean_cross_angular_distance(a: Sequence[Sequence[float]], b: Sequence[Sequence[float]]) -> float:
    """Return the mean angular distance across all vector pairs."""
    if not a or not b:
        raise ValueError("both groups must contain at least one vector")
    distances = [angular_distance(x, y) for x in a for y in b]
    return sum(distances) / len(distances)


def greedy_layer_groups(
    layer_vectors: Sequence[Sequence[float]],
    threshold: float,
) -> list[list[int]]:
    """Greedily group layers whose representative vectors are within threshold.

    This is an intentionally transparent baseline for experiments. It is not
    claimed to be the final NeuroSteer grouping algorithm.
    """
    if threshold < 0:
        raise ValueError("threshold must be non-negative")

    groups: list[list[int]] = []
    representatives: list[tuple[float, ...]] = []
    for idx, vector in enumerate(layer_vectors):
        candidate = tuple(float(x) for x in vector)
        if not candidate:
            raise ValueError("layer vectors must not be empty")
        placed = False
        for group_idx, representative in enumerate(representatives):
            if angular_distance(candidate, representative) <= threshold:
                groups[group_idx].append(idx)
                placed = True
                break
        if not placed:
            groups.append([idx])
            representatives.append(candidate)
    return groups
