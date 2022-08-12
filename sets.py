# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print("set of integers: ", my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3), (2, 3, 4)}
print("set of mixed datatypes: ", my_set)

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2, 1}
print("set cannot have duplicates: ", my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print("we can make set from a list: ", my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

# my_set = {1, 2, [3, 4]}

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print("discard an element: ", my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print("remove an element: ", my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# my_set.remove(2)