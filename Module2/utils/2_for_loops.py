"""Training guide to using for loops"""

"""
Glossary:
for - the keyword for starting a for loop
< - check if the first value is less than the second
> - check if the first value is greather than the second
<= - check if the first value is less than or equal to the second
>= - check if the first value is greather than or equal to the second
== - check if the first value is equal to the second
!= - check if the first value is NOT equal to the second
and - logic operator to combine 2 or more checks. Only True if
"""

#################
### FOR LOOPS ###
#################
# For loops will "loop" through each item in an object
# Basic use with lists
a = [1, 2, 3]
b = []
# For each item in a run the following code
for item in a:
    # Run this code
    b.append(item)
print(b)

# Basic use with dicts - keys only
a = {"foo": 1, "bar": 2, "baz": 3}
b = []
# Running a for loop on a dict will loop through it's keys
for key in a:
    # Run this code
    b.append(key)
print(b)

# Basic use with dicts - keys and values
a = {"foo": 1, "bar": 2, "baz": 3}
b = {}
# To get keys and values invoke the items method
for key, value in a.items():
    # Run this code
    b[key] = value
print(b)

# Using with if criteria
a = [1, 2, 3]
b = []
# For each item in a run the following code
for item in a:
    # Run this code
    if item < 3:
        b.append(item)
    else:
        b.append("Computer says no")
print(b)

# Zipping
a = ["foo", "bar", "baz"]
b = [1, 2, 3]
# Zipping creates a pair of values for the 1st, 2nd...nth values
for item1, item2 in zip(a, b):
    print(a, b)

# Nesting loops
a = [[1, 2], [3, 4], [5, 6]]
# Lists can have lists inside them (nesting). Each loop will use
# the whole list for its value
for item in a:
    print(item)
# To access the items in the list inside the main list you need another loop
for item in a:
    for value in item:
        print(f"{value} is part of {item}")


# Using with enumerate
a = ["foo", "bar", "baz"]
b = {}
# Running a for loop on a dict will loop through it's keys
for index, item in enumerate(a):
    # Run this code
    b[item] = index
print(b)

# WATCHOUTS
# Not always the fastest way to do things (especially nested lists)
# Data types don't have to be consistent but it helps
