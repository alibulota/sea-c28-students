#!/usr/bin/env python

# create list, print.
print "Welcome to the Fruit Basket List!"

fruit = ["Apples", "Pears", "Oranges", "Peaches"]

print "There are", fruit, "in the basket."

# add user intput to end of list, print
new_fruit = raw_input("Please input a type of fruit: ")

fruit.append(new_fruit)

print "There are", fruit, "in the basket."

# ask user for number. display number and corresponding fruit.
ind = int(raw_input("Provide a number for a corresponding fruit: "))

print "The number %i corresponds to %s" % (ind, fruit[ind - 1])

print "The basket contains", fruit, "."