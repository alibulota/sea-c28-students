#!/usr/bin/env python
"""generators: sum of int, doubler, fib, prime"""


def sum_int():
    i = 0
    n = 0
    while True:
        yield i
        n += 1
        i = i + n


def doubler():
    i = 1
    while True:
        yield i
        i = i * 2


def fib_seq():
    i = 1
    last = 0
    while True:
        yield i
        i = i + last
        last = i - last


def prime():
    i = 1
    inum = [1]
    while True:
        while inum != []:
            i += 1
            inum = [1 for x in range(2, i) if not i % x]
        yield i
        inum = [1]
