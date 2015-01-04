import pytest
from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci():
    test_fib_vals = [0, 1, 1, 2, 3, 5]

    for n in range(5):
        assert fibonacci(n + 1) == test_fib_vals[n]


def test_lucas():
    test_lucas_vals = [2, 1, 3, 4, 7, 11]

    for n in range(5):
        assert lucas(n + 1) == test_lucas_vals[n]


def test_sum_series():
    test_sum_series_vals = ([[5, 0, 1, 3], [5, 2, 1, 7], [5, 3, 10, 36]])

    for n in range(3):
        assert (sum_series(*test_sum_series_vals[n][0:3]) ==
                test_sum_series_vals[n][3])
