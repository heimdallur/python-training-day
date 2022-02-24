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
# INPUT - Create a for loop over a list printing each item in turn

# Basic use with dicts - keys only
# Running a for loop on a dict will loop through it's keys
a = {"foo": 1, "bar": 2, "baz": 3}
# INPUT - Create a for loop over a dictionary printing each key in turn

# Basic use with dicts - keys and values
a = {"foo": 1, "bar": 2, "baz": 3}
# To get keys and values invoke the items method
# INPUT - Create a for loop over a dictionary printing each key and 
#   value in turn

# Using with if criteria
a = [1, 2, 3]
# For each item in a run the following code
# INPUT - Create a for loop using an if statement inside

# Zipping
a = ["foo", "bar", "baz"]
b = [1, 2, 3]
# Zipping creates a pair of values for the 1st, 2nd...nth values
# INPUT - Zip two lists together and loop over them

# Nesting loops
a = [[1, 2], [3, 4], [5, 6]]
# Lists can have lists inside them (nesting). Each loop will use
# the whole list for its value
# INPUT - Create a single level for loop
# To access the items in the list inside the main list you need another loop
# INPUT - Create a nested for loop

# Using with enumerate
a = ["foo", "bar", "baz"]
# Running a for loop on a dict will loop through it's keys
# INPUT - Create a enumerated for loop

# You can leave a loop early with break
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# INPUT - Create a loop which breaks early

# You can skip to the next iteration in a loop with continue
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# INPUT - Create a loop with a continue statement
