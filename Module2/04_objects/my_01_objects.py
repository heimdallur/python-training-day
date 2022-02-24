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
a.split(" ")  # This splits the string into words using " " to split around
a.upper()  # This puts the whole string in upper case
a.replace("world", "Jesus")  # This replaces "world" with "Jesus"

# To see what the methods available are you can look at the object
# itself
str  # in VSCode ctrl + click on this to see the object
# Have a look around
# Look at some methods
# Look at the dunder methods EG __len__

# Object is actually short for Class object
# This is how you make a class


class MyClass:
    # Classes should have an init dunder method
    def __init__(self):
        # the "self" variable here is used
        # throughout to refer to the object itself
        self.my_var = "hi"  # this is a variable

    # This is a methd inside the class
    def my_method(self):
        print(self.my_var)  # here we can print my_var becasue it's part of self

    # One method can call another
    def my_method2(self):
        self.my_method()

    # You can pass in additional paramaters
    def my_method3(self, name):
        print(f"{self.my_var} {name}")


# To access a class you instantiate it (basically start it up)
my_class = MyClass()
# Now we have access to all the things inside the class
print(my_class.my_var)
# This calls the my_method
my_class.my_method()
# This calls the my_method2 (which in turn calls my_method)
my_class.my_method2()
# This calls my_method3 with an input you choose
my_class.my_method3("INSERT NAME HERE")


# When you build a class you can pass in variables to start with as
# part of init
class MyClass:
    # Classes should have an init dunder method
    def __init__(self, name: str = "INSERT NAME HERE"):
        # the "self" variable here is used
        # throughout to refer to the object itself
        self.my_var = "hi"  # this is a variable
        self.name = name  # this is a variable

    # This is a method inside the class
    def print_name(self):
        # here we can print my_var becasue it's part of self
        print(f"{self.my_var} {self.name}")


# You pass in these parameters when you instantiate the class
my_class = MyClass("Rob")
my_class.print_name()

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


class AClass:
    def __init__(self, a):
        self.a = a

    def add_1(self):
        self.a = self.a+1

    def div_2(self):
        self.a = self.a/2

    def square(self):
        self.a = self.a**2


a_class = AClass(5)
a_class.add_1()
a_class.div_2()
a_class.square()
# Notice i don't need to keep track of the value of "a", the class does it for me.

# It's up to you to decide when to use functions and when to use classes

# Some obejcts are included like "str" and "list"
# Other objects have to be imported EG
# Sometimes you may have to pip install them first
# When you import them you can rename them EG
# You can also import specific parts of the object EG

# Classes can inherit properties from other classes (referred to as their parents)
# this means we can build on existing work


class Animal:
    def __init__(self, name, leg_count):
        self.name = name
        self.leg_count = leg_count

    def say_my_name(self):
        print(f"My name is {self.name}")

    def how_many_legs(self):
        print(f"I have {self.leg_count} legs")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", 4)

    def full_description(self):
        print(f"My name is {self.name}, and i have {self.leg_count} legs")


d1 = Dog()
d1.say_my_name()
d1.how_many_legs()
d1.full_description()

# WATCHOUT
# There are tonnes of things which can go wrong in classes so be careful when
# using them
