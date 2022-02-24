"""This is a tutorial around list and dictionary comprehension"""

# List and dict comprehension is a shortcut for performing loops
# through lists and dictionaries

# This is a regular loop
a = [1, 2, 3, 4, 5]
b = []
for item in a:
    b.append(item + 1)
print(b)

# But you can write it in one line using comprehension
a = [1, 2, 3, 4, 5]
b = [item + 1 for item in a]
print(b)

# When using dictionaries
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
b = {}
for key in a:
    b[key] = a[key] + 1
print(b)

# But you can write it in one line using comprehension
# When using dictionaries
a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
b = {key:a[key] + 1 for key in a}
print(b)

# These are simple examples but this can be a very powerful
# (and quick) tool for doing what you need to

# You can also combine it with functions
def add_2(x):
    return x + 2
a = [1, 2, 3, 4, 5]
b = [add_2(item) for item in a]
print(b)

# If statements can be used inside comprehension to filter
a = [1, 2, 3, 4, 5]
b = [
    item for item in a
    if item < 3
]
print(b)

# The if statement can also be used to vary the output
a = [1, 2, 3, 4, 5]
b = [
    "Less than 3" if item < 3 else "Not less than 3"
    for item in a
    ]
print(b)

