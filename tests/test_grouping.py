import pytest

from neurosteer.grouping import greedy_layer_groups, mean_cross_angular_distance


def test_mean_cross_angular_distance():
    assert mean_cross_angular_distance([[1.0, 0.0]], [[1.0, 0.0]]) == pytest.approx(0.0)


def test_greedy_groups_similar_layers():
    groups = greedy_layer_groups([[1.0, 0.0], [0.999, 0.001], [0.0, 1.0]], threshold=0.05)
    assert groups == [[0, 1], [2]]


def test_negative_threshold_rejected():
    with pytest.raises(ValueError):
        greedy_layer_groups([[1.0, 0.0]], threshold=-0.1)
