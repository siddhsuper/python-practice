
"""========================================
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list ( or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop()	Removes the element at the specified position
remove() Removes the item with the specified value
reverse() Reverses the order of the list
sort()	Sorts the list
========================================"""

import random

# Randomrange is int in between 2 nos
random_num = random.randrange(1, 30)
print(random_num)

# Random is float
random_float = random.random()
print(random_float)

head_tail = random.randint(0, 2)
if head_tail == 1:
    print("its head")
else:
    print("its tail")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])

# Print the last item of the list:
print(thislist[-1])

# Return the third, fourth, and fifth item:
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
print(thislist[:4])

# This example returns the items from "cherry" to the end:
print(thislist[2:])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

for x in thislist:
    print(x)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
