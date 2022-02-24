"""Tutorial on decorators"""

# Everything in python is an object
# Because of that you can call a function from inside a function
# This is useful when you want to add some standard feature
# like printing a message
def add_2(x):
    return x + 2

# INPUT - Wrap this function in another function


# Try it
# INPUT - Call the parent function

# This is a bit limiting so why don't we make it work for any function
# *args is a catchall for any unspecified arguments
# **kwargs is a catchall for any unspecified keyword arguments

# INPUT - Create a generic function wrapping the basic function


# Try it
# INPUT - Call the parent function
# Try it with another function
# INPUT - Create another basic function and call it from the parent

# Take a moment to get your head around this
# any function is an object and so canbe passed to another function
# to be run later just like a string or a integer...etc

# Decorators make this easier to write
# Instead of returning the answer we return another function
# INPUT - Create a basic decorator
# And now we "decorate" another funciton with it
# INPUT - Decorate a basic funciton with it
# Try it
# INPUT - Call the child function

# The decorator automatically takes the function as the first argument.
# It can be very useful when you need to run a connection around a function.
# INPUT - Create a decorator to connect to a system.
# Try it
# INPUT - Call the child function

# Or for timing things
# INPUT - Create a decorator to time a function.
# Try it
# INPUT - Call the child function
