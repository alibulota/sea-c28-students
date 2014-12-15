#!/usr/bin/env python
# reference: https://github.com/PythonCHB/
# PythonIntroClass/blob/master/week-04/code/trigram.py

from io import open
import sys
import string
import random

infilename = u'sherlock_small.txt'


# creating definitions of what to keep and what to remove
# in writing
keep = string.characters + "'"
all = ''.join([chr(i) for i in range(256)])
table = []
for c in all:
    if c in keep:
        table.append(c)
    else:
        table.append(' ')
table = ''.join(table)

infile = open(infilename, 'r')
for i in range(61):
    infile.readline()
in_data = infile.read()
