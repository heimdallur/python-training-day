"""Tutorial around what tuples are and how they work"""

##############
### TUPLES ###
##############
# Tuples are a colleciton of items made using ()
# items are separated by ,
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Select an item in a tuple using it's index
# Indexes start from 0 being the first item 
# and length -1 being the last
a[0] # the first item
a[-1] # The last item

# You can select a slice of the tuple using : separator
a[1:3] # everything between the 2nd and 4th item (includes the 2nd but not the 4th)
a[1:-1] # everything between the 2nd and last item (includes the 2nd but not the last)
a[:2] # everything from the start to the 3rd item (does not include the 3rd item)
a[2:] # everything from the 3rd item to the end (includes the 3rd item and goes to the end)

# You can also select every nth item using ::
a[::2] # select every other item from the start to the end

# Or reverse the order
a[::-1] # Select every 1 item in reverse
a[::-2] # Select every 2nd item in reverse

# And combine these
a[1:8:3] # select every third item between the 2nd and 9th items

# Tuples can be combined
b = (1,2,3) + (4,5,6)
print(b)
# Or added to 
b += (7,8,9)
print(b)

# BUT tuples are "immutable" (this means that items in them CANNOT be modified)
a[2] = "foo" # this will throw an error

# You can convert tuples to lists though
a = list(a) # once you've changed it you can modify it

# You can get the length of a tuple with len
len(a)


# WATCHOUTS
# Be careful when changing multiple items
a[3:5] = "bar" # change the 4th to 6th item to the letters of bar
print(a)
a[3:5] = ["bar", "bar", "bar"] # change the 4th to 6th item to bar
print(a)
