#!/usr/bin/env python
from safe_input import safe_input
import codecs
import os


def thanks(donor_dict):
    """full name. list of names, quit, or add name"""
    while True:
        donor_name = u'' + safe_input("Input name of donor for letter, \
            'list' for listing of all donors or 'quit' to exit")
        if donor_name.lower() == u'list':
            for donor in donor_dict.keys():
                print donor
        elif donor_name == u'quit':
            return donor_dict
        else:
            donor_dict.setdefault(donor_name, [])
            break

    amount = u'' + safe_input("Enter donation amount for \
        %s. Type 'quit' to exit " % donor_name)
    if amount == u'quit':
        return donor_dict
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amount = u'' + safe_input("Invalid entry. Please input number. \
            Type 'exit' to quit.")
        if amount == u'quit':
            return donor_dict
    else:
        break

    donor_dict[donor_name].append(amount)
    try:
        os.mkdir('./mail')
        print './folder created'
    except OSError:
        print './folder exists'

    letter_folder = "./mail/{}_ty.txt".format(donor_name)
    letter = codecs.open(letter_folder, 'w')
    letter.write("Dear {}, \n\n\
        \t Thank you for your generous donation and support \
        to our organization. \n\n\
        Sincerely, \n Alicija Bulota".format(donor_name, amount))
    letter.close()
    print "letter saved in " + letter_folder
    return donor_dict


def report(donations):
    """create report of donations"""
    donation_rep = []
    spacing = 10
    for donor in donations.keys():
        if len(donor) > spacing:
            spacing = len(donor)
        total = sum(donations[donor])
        count = len(donations[donor])
        if count == 0:
            avg = 0
        else:
            avg = total / count
        donation_rep.append([donor, total, count, avg])
    donation_rep.sort(key=second, reverse=True)

    print "{name:<{n}} {total:>10} {count:>10} {average:>10}".\
        format(n=spacing, name="Name", total="Total",
               count="Count", average="Average")
    for donor in donation_rep:
        print "{name:<{n}} {total:>10} {count:>10} {average:>10}".\
            format(n=spacing, name=donor[0], total=donor[1], count=donor[2],
                   average=donor[3])
