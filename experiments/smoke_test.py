"""Deterministic smoke test demonstrating the causal steering primitive.

Run with: python experiments/smoke_test.py
"""

from neurosteer.steering import add_scaled, cosine_similarity, angular_distance


BASE = [0.2, 0.4, 0.6, 0.8]
DIRECTION = [1.0, 0.0, -1.0, 0.0]


if __name__ == "__main__":
    steered = add_scaled(BASE, DIRECTION, 0.5)
    print("base:", BASE)
    print("direction:", DIRECTION)
    print("steered:", steered)
    print("cosine(base, direction):", round(cosine_similarity(BASE, DIRECTION), 6))
    print("angular_distance(base, direction):", round(angular_distance(BASE, DIRECTION), 6))
    assert steered == [0.7, 0.4, 0.09999999999999998, 0.8]
    print("smoke_test: PASS")
