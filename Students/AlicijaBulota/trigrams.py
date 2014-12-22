#!/usr/bin/env python                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  #!/usr/bin/env python
# reference: https://github.com/PythonCHB/
# PythonIntroClass/blob/master/week-04/code/trigram.py

from io import open
import string
import random

infilename = u'sherlock.txt'

def strip_words(text):
    """formatting text, translating table for string."""

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
    data = infile.read()  # read file into memory


    # keys will be word pairs, values are list of words after each pair
    data_pair = {}


    # create format for data
    data = data.lower()
    data = data.translate(table)
    text = data.split()
    text = [texts for texts in text if texts != "'"]

    return text

#def read_text(infilename):
    #"""create loop to read through each word in text"""

    for i in range(len(text) - 2):
        text_pair = " ".join(text[i:i + 2])
        follower = text[i + 2]
        data_pair.setdefault(text_pair, []).append(follower)


    # new text
    new_data = []
    for i in range(50):
        sentence = list(random.choice(data_pair.keys()))

        for j in range(random.randint(2, 10)):
            text_pair = tuple(sentence[-2:])
            sentence.append(random.choice(data_pair[text_pair]))
        sentence[0] = sentence[0].capatalize()
        sentence[-1] += u"."
        new_data.extend(sentence)
    new_data = " ".join(new_data)
    print new_data
