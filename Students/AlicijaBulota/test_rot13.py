#!/usr/bin/env python


import pytest
from rot13 import rot13


def test_rot13():
    assert rot13(u'Python is AWESOME') == u'Clguba vf NJRFBZR'
