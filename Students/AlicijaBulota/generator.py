#!/usr/bin/env python
"""generators: sum of int, doubler, fib, prime"""


def sum_int():
    i = 0
    n = 0
    while True:
        yield i
        n += 1
        i = i + n
