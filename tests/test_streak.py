import pytest
from streak import longest_positive_streak

def test_empty_input():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 0, 1]) == 3

def test_zeros_and_negatives():
    assert longest_positive_streak([-1, -2, 0, -4, -5, -6]) == 0
    assert longest_positive_streak([1, 2, -1, 3, 4, 0, 5]) == 2
