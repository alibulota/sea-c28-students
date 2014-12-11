#!/usr/bin/env python
# -*- coding: utf-8 -*-
# source:https://docs.python.org/2/library/codecs.html#standard-encodings


def rot13(text):
    """rot13 encoding:Returns the Caesar-cypher encryption of the operand"""
    return text.encode('rot13')

if __name__ == '__main__':
    code = "Python is AWESOME"
    rot13_code = "Clguba vf NJRFBZR"

    print rot13(code)

    assert rot13(rot13_code) == code

    cris = "Is AWESOME"
    assert rot13(rot13(cris)) == cris

# test another line of text by encoding it, reversing the
# encoding and then comparing it to the original text
