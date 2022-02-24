"""Tutorial about objects"""

# Objects are used to group functions and varibale which apply to one
# specific area or use

# EVERYTHING IN PYTHON IS AN OBJECT
from pandas import DataFrame
import numpy as np
import pandas
import re  # this is the regex object
a = "Hello world"  # This is a string object

# Objects have functions you can call on them
# different methods do different things
# INPUT - Split a strin
# INPUT - Convert a string to upper case
# INPUT - Replace a word in a string

# To see what the methods available are you can look at the object
# itself
str  # in VSCode ctrl + click on this to see the object
# Have a look around
# Look at some methods
# Look at the dunder methods EG __len__

# Object is actually short for Class object
# This is how you make a class
# INPUT - Create a class with an init and 3 methods


# To access a class you instantiate it (basically start it up)
# INPUT - Instantiate the class
# Now we have access to all the things inside the class
# INPUT - Print a varibale form the class
# This calls the my_method
# INPUT - Call a method from the class
# This calls the my_method2 (which in turn calls my_method)
# INPUT - Call another method from the class


# When you build a class you can pass in variables to start with as
# part of init
# INPUT - Create a class with a default variable and a method using
#   that variable


# You pass in these parameters when you instantiate the class
# INPUT - Instantiate the class and run a method

# Classes are very handy when you want to keep track of variables without
# passing them from one object to another
# EG if I want to do a number of things to a number
# Thsi is how i'd do it with functions


def add_1(a):
    return a+1


def div_2(a):
    return a/2


def square(a):
    return a**2


a = 5
a = add_1(a)
a = div_2(a)
a = square(a)

# Whereas with a class
# INPUT - Create a class which tracks the variable a, then run the methods

# Notice i don't need to keep track of the value of "a", the class does it for me.

# It's up to you to decide when to use functions and when to use classes

# Some obejcts are included like "str" and "list"
# Other objects have to be imported EG
# Sometimes you may have to pip install them first
# When you import them you can rename them EG
# You can also import specific parts of the object EG

# Classes can inherit properties from other classes (referred to as their parents)
# this means we can build on existing work
# INPUT - Create 2 classes, one which inherits properties from the other
# INPUT - Call some of the methods