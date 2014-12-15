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
a_val_dict = {}
for key, val in d.items():
    a_val_dict[key] = val.count('a')
print a_val_dict


# create s2, s3, s4 with 0-20 only divisible by 2, 3, 4.
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)


# display sets.
print s2
print s3
print s4


# display if s3 is a subset of s2 (False).
print s3.issubset(s2)


# display if s4 is a subset of s2 (True).
print s4.issubset(s2)


# create set with letters in 'Python' + i.
set_p = set(u'Python')
set_p.add('i')

print set_p


# create frozenset with letters in 'marathon'.
set_frozen = frozenset(u'marathon')


# display union and intersection of the two sets.
print "union:", set_p.union(set_frozen)
print "intersection:", set_p.intersection(set_frozen)
