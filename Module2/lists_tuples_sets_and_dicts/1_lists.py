"""Tutorial around what lists are and how they work"""

#############
### LISTS ###
#############
# Lists are a colleciton of items made using []
# items are separated by ,
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Select an item in a list using it's index
# Indexes start from 0 being the first item
# and length -1 being the last
a[0]  # the first item
a[-1]  # The last item

# You can select a slice of the list using : separator
# everything between the 2nd and 4th item (includes the 2nd but not the 4th)
a[1:3]
# everything between the 2nd and last item (includes the 2nd but not the last)
a[1:-1]
# everything from the start to the 3rd item (does not include the 3rd item)
a[:2]
# everything from the 3rd item to the end (includes the 3rd item and goes to the end)
a[2:]

# You can also select every nth item using ::
a[::2]  # select every other item from the start to the end

# Or reverse the order
a[::-1]  # Select every 1 item in reverse
a[::-2]  # Select every 2nd item in reverse

# And combine these
a[1:8:3]  # select every third item between the 2nd and 9th items

# Lists are "mutable" (this means that items in them can be modified)
a[2] = "foo"  # change the 3rd item to foo
print(a)

# Lists can be combined
b = [1, 2, 3] + [4, 5, 6]
print(b)
# Or added to
b += [7, 8, 9]
print(b)

# You'll append used a lot
c = [1, 2, 3]
print(c)
c.append(4)
print(c)

# You'll extend used a lot
c = [1, 2, 3]
print(c)
c.extend([4, 5, 6])
print(c)

# Note the difference
c = [1, 2, 3]
c.append([4, 5, 6])
print(c)
d = [1, 2, 3]
d.extend([4, 5, 6])
print(d)

# You can get the length of a list with len
len(d)

# Strings can be treated as lists of letters (sometimes)
e = "string"
e[::-1]

# You can check if an item is in a list with "in"
f = [1, 2, 3]
3 in f  # this will return True

# You can turn a string into a list of words by splitting it
g = "Hello world, what a wonderful day it is today"
g = g.split(" ")

# Similarly you can stitch a list of words into a sentence with join
h = ['Hello', 'world,', 'what', 'a', 'wonderful', 'day', 'it', 'is', 'today']
" ".join(h)


# WATCHOUTS
# Be careful when changing multiple items
a[3:5] = "bar"  # change the 4th to 6th item to the letters of bar
print(a)
a[3:5] = ["bar", "bar", "bar"]  # change the 4th to 6th item to bar
print(a)
