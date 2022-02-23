"""Tutorial around what sets are and how they work"""

##############
### SETS ###
##############
# Sets are a colleciton of items made using {}
# items are separated by ,
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(a)
# Sets will only keep unique values
b = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(b)

# Sets are unordered and so indexes cannot be used
a[0] # this will throw an error

# Sets are "immutable" (this means that items in them CANNOT be modified)
a[2] = "foo"  # this will throw an error

# You can convert sets to lists though
a = list(a)  # once you've changed it you can modify it

# You can get the length of a set with len
len(b)