"""Tutorial around what dictionaries are and how they work"""

####################
### DICTIONARIES ###
####################
# Dictionaries are a colleciton of items made using {} and
# : to create pairings of keys nad values
# items are separated by ,
a = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
}

# Select an item in a dictionary using it's key
a["c"]

# You cannot use indexes on dictionaries
a[0]  # will throw an error

# You can get the keys with keys()
keys = a.keys()
print(keys)

# Dictionaries are "mutable" (this means that items in them can be modified)
a["c"] = "foo"  # change the 3rd item to foo
print(a)

# Dictionaries can be combined using | (python 3.9+)
b = {
    "a": 1,
    "b": 2,
    "c": 3
} | {
    "d": 4,
    "e": 5,
    "f": 6
}
print(b)
# Or added to
b |= {
    "g": 7,
    "h": 8,
    "i": 9
}
print(b)

# But if the key already exists it will overwrite it
b |= {
    "g": "foo",
    "h": "bar",
    "i": "baz"
}
print(b)

# You can get the length of a dictionary with len
len(b)

# You can check if an item is in a dictionary's keys with "in"
f = {
    "a": 1,
    "b": 2,
    "c": 3
}
"c" in f  # this will return True

# You can use get to fetch the value and a default if it's not there
g = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(g.get("c", "nothing to see here")) # this will find the value fo c
print(g.get("d", "nothing to see here")) # d is not in here so the defualt will be returned

### BONUS ###
# Dicts and lists are often combined, especially in data science/engineering
cakes = [
    {
        "name":"victoria sponge",
        "ingredients_cost":1.00,
        "labour_time":45,
        "people_required":1,
        "sell price":2.00
    },
    {
        "name":"chocolate fudge",
        "ingredients_cost":2.39,
        "labour_time":15,
        "people_required":3,
        "sell price":4.15
    },
    {
        "name":"delicious surprise",
        "ingredients_cost":15.24,
        "labour_time":240,
        "people_required":3,
        "sell price":19.99
    }
]