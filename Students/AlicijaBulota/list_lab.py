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

# ask user to choose fruit to remove
print "Fruit Basket List:", fruit

del_ans = raw_input("Select a fruit to remove from list: ")
while del_ans in fruit:
    fruit.remove(del_ans)
print "Updated fruit list:", fruit

# if list multiplied by two, ???
#dub_fruit = fruit * 2
#print "List of Fruits:", fruit
#rem_fruit = raw_input("Select a fruit to remove from list: ")
#while rem_fruit in dub_fruit:
    #dub_fruit.remove(rem_fruit)

#print "Remaining fruit:", dub_fruit

# ask user fruit preferences, remove dislikes, print
like_fruit = fruit[:]
for likes in fruit:
    choice = raw_input("Do you like: %s? " % fruit)
    if choice.lower() == 'no':
        while likes in fruit:
            fruit.remove(likes)
    elif choice.lower() == 'yes':
        pass
    else:
        print "Please answer with 'yes' or 'no'."
print "The remaining fruits are:", fruit

# copy of list, then reverse order
fruits = like_fruit[:]

rev_fruit = fruit[:]
for i, fruit in enumerate(rev_fruit):
    rev_fruit[i] = fruit[::-1]

print rev_fruit

# remove last item from list
del rev_fruit[len(rev_fruit) - 1]
print rev_fruit
