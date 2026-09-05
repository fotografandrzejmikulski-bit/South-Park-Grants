import pytest

from neurosteer.steering import (
    add_scaled,
    angular_distance,
    cosine_similarity,
    l2_norm,
    pairwise_mean_max_angular_distance,
)


def test_l2_norm():
    assert l2_norm([3.0, 4.0]) == pytest.approx(5.0)


def test_cosine_similarity():
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == pytest.approx(1.0)
    assert cosine_similarity([1.0, 0.0], [0.0, 1.0]) == pytest.approx(0.0)


def test_zero_vector_rejected():
    with pytest.raises(ValueError):
        cosine_similarity([0.0, 0.0], [1.0, 0.0])


def test_angular_distance():
    assert angular_distance([1.0, 0.0], [1.0, 0.0]) == pytest.approx(0.0)
    assert angular_distance([1.0, 0.0], [-1.0, 0.0]) == pytest.approx(1.0)


def test_add_scaled():
    assert add_scaled([1.0, 2.0], [0.5, -1.0], 2.0) == pytest.approx([2.0, 0.0])


def test_dimension_mismatch():
    with pytest.raises(ValueError):
        add_scaled([1.0], [1.0, 2.0], 1.0)


def test_group_metric_singleton():
    assert pairwise_mean_max_angular_distance([[1.0, 0.0]]) == 0.0
