#!/usr/bin/env python
# -*- coding: utf-8 -*-
# source:https://docs.python.org/2/library/codecs.html#standard-encodings


def rot13(text):
    """rot13 encoding:Returns the Caesar-cypher encryption of the operand"""
    return text.encode('rot13')

if __name__ == '__main__':
    code = "Python is AWESOME"

    print rot13(code)
