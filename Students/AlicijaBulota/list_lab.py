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

# add fruit to beginning of list (+), print.
fruit = ["Strawberrys"] + fruit

print "New fruit at top of list:", fruit

# add fruit to beginning of list (insert), print.
fruit.insert(0, "Blueberrys")

print "New fruit at top of list:", fruit

# display all fruits that begin with "P", for loop
print "All fruits that start with 'P' are listed below."
for first_letter in fruit:
    if first_letter[0] == 'P':
        print first_letter

# remove last fruit from list
print "The fruit basket now contains:", fruit

del fruit[len(fruit) - 1]

print "Last item removed from list:", fruit