#!/usr/bin/env python

import pytest
from ack import ack


def test_ack():
    test_values = ([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 5, 7, 9, 11], [5, 13, 29, 61, 125]])
    for m in range(4):  # 4 values... 0-3
        for n in range(5):  # 5 values... 0-4
            assert ack(m, n) == test_values[m][n]
