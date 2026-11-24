
import pytest
from modelexplain.metrics import calculate_accuracy, calculate_precision, calculate_recall


def test_perfect_accuracy():
    actual = [1, 0, 1, 1]
    predicted = [1, 0, 1, 1]
    assert calculate_accuracy(actual, predicted) == 1.0


def test_partial_accuracy():
    actual = [1, 0, 1, 0]
    predicted = [1, 1, 1, 0]
    assert calculate_accuracy(actual, predicted) == 0.75


def test_zero_accuracy():
    actual = [1, 1, 1]
    predicted = [0, 0, 0]
    assert calculate_accuracy(actual, predicted) == 0.0


def test_empty_lists():
    assert calculate_accuracy([], []) == 0.0


def test_different_lengths():
    with pytest.raises(ValueError):
        calculate_accuracy([1, 0], [1])


def test_precision():
    actual = [1, 0, 1, 0]
    predicted = [1, 1, 1, 0]
    assert calculate_precision(actual, predicted) == 0.6666666666666666


def test_recall():
    actual = [1, 0, 1, 0]
    predicted = [1, 1, 1, 0]
    assert calculate_recall(actual, predicted) == 1.0