#!/usr/bin/env python
from safe_input import safe_input
import codecs
import os


def thanks(donor_dict):
    """full name. list of names, quit, or add name"""
    while True:
        name = u'' + safe_input("Input name of donor for letter, \
            'list' for listing of all donors or 'quit' to exit")
        if donor_name.lower() == u'list':
            for donor_name in donor_dict.keys():
                print donor_name
        elif name == u'quit':
            return donor_dict
        else:
            donor_dict.setdefault(name, [])
            break

    amount = u'' + safe_input("Enter donation amount for \
        %s. Type 'quit' to exit " % name)
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

    donor_dict[name].append(amount)
    try:
        os.mkdir('./mail')
        print './folder created'
    except OSError:
        print './folder exists'

    letter_folder = "./mail/{}_ty.txt".format(name)
    letter = codecs.open(letter_folder, 'w')
    letter.write("Dear {}, \n\n\
        \t Thank you for your generous donation and support \
        to our organization. \n\n\
        Sincerely, \n Alicija Bulota".format(name, amount))
    letter.close()
    print "letter saved in " + letter_folder
    return donor_dict


def report(rep_list):
    """create report of donations"""
    donation_rep = []
    n_long = 10  #extra space for longer names in forma
    for donor in donations.keys():
        if len(donor) > n_long:
            n_long = len(donor)
        if count == 0:
            avg = 0
        else:
            avg = total/count
        #sort list by total amount starting with greatest
    print (# the list of donors with ordered amounts)

