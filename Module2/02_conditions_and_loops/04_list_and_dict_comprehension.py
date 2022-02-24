"""This is a tutorial around list and dictionary comprehension"""

# List and dict comprehension is a shortcut for performing loops
# through lists and dictionaries

# This is a regular loop
a = [1, 2, 3, 4, 5]
b = []
# INPUT - Create a for loop appending all the items of a
#   to b

# But you can write it in one line using comprehension
a = [1, 2, 3, 4, 5]
# INPUT - Do the same thing as above with list comp

# When using dictionaries
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
b = {}
# INPUT - Create a for loop appending all the keys of a
#   to b + 1

# But you can write it in one line using comprehension
# When using dictionaries
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# INPUT - Do the same thing as above with dict comp

# These are simple examples but this can be a very powerful
# (and quick) tool for doing what you need to

# You can also combine it with functions
a = [1, 2, 3, 4, 5]
# INPUT - Create list comprehension with a function

# If statements can be used inside comprehension to filter
a = [1, 2, 3, 4, 5]
# INPUT - Create list comp with an if statement to filter

# The if statement can also be used to vary the output
a = [1, 2, 3, 4, 5]
# INPUT - Create list comp with an if statement to adjust output

