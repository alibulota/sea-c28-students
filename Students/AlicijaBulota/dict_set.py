#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create dictionary.
d = {"name": u"Chris",
    u"city": "Seattle",
    u"cake": "chocolate"}


# display dictionary.
print d


# delete entry for "cake".
del d["cake"]


# display dictionary.
print d


# Add an entry for “fruit” with “Mango” and display the dictionary.
d[u'fruit'] = 'Mango'

print d


# -Display the dictionary keys.
print d.keys()


# -Display the dictionary values.
print d.values()


# -Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print 'cake' in d


# -Display whether or not “Mango” is a value in the dictionary.
print "Mango" in d.values()


# use dict contructor and zip: dict of numbers 0-15, hexadecimal.
num = range(16)  # 16 values total including 0.
hd = []
for n in num:
    hd.append(hex(n))

hd_dict = dict(zip(num, hd))
print hd_dict


# use original dict: make dict use same keys, diff number of 'a's.


# create s2, s3, s4 with 0-20 only divisible by 2, 3, 4.

# display sets.

# display if s3 is a subset of s2 (False).

# display if s4 is a subset of s2 (True).

# create set with letters in 'Python' + i.

# create frozenset with letters in 'marathon'.

# display union and intersection of the two sets.
