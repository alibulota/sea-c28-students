#!/usr/bin/env python


import pytest
from lambda_magic import lamb


def test_lamb():
    test_vals = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

    n = 3
    val_list = lamb(n)

    for i, f in enumerate(val_list):
        for j in range(3):
            f(j) == test_vals[i][j]
