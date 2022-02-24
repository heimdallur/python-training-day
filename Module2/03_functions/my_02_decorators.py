"""Tutorial on decorators"""

# Everything in python is an object
# Because of that you can call a function from inside a function
# This is useful when you want to add some standard feature
# like printing a message


from datetime import datetime
from time import sleep


def add_2(x):
    return x + 2


def msg_print(a: int):
    print("I'm gonna call this function")
    resp = add_2(a)
    print(f"I just called it and the response was {resp}")
    return resp


# Try it
msg_print(2)

# This is a bit limiting so why don't we make it work for any function
# *args is a catchall for any unspecified arguments
# **kwargs is a catchall for any unspecified keyword arguments


def msg_print(func: callable, *args, **kwargs):
    print("I'm gonna call this function")
    resp = func(*args, **kwargs)
    print(f"I just called it and the response was {resp}")
    return resp


# Try it
msg_print(add_2, 2)
# Try it with another function


def what_my_full_name(first, sur):
    return first + " " + sur


msg_print(what_my_full_name, "Rob", "Franklin")

# Take a moment to get your head around this
# any function is an object and so canbe passed to another function
# to be run later just like a string or a integer...etc

# Decorators make this easier to write
# Instead of returning the answer we return another function
def msg_print(func: callable):
    def inner(*args, **kwargs):
        print("I'm gonna call this function")
        resp = func(*args, **kwargs)
        print(f"I just called it and the response was {resp}")
        return resp
    return inner
# And now we "decorate" another funciton with it
@msg_print
def add_2(x):
    return x + 2
# Try it
add_2(2)

# It can be very useful when you need to run a connection around a function
def run_conn(func:callable):
    def inner(*args, **kwargs):
        print("This is here i connect to the system")
        resp = func(*args, **kwargs)
        print("This is here i disconnect from the system")
        return resp
    return inner
@run_conn
def add_2(x):
    return x + 2
# Try it
add_2(2)

# Or for timing things
def timer(func: callable):
    def inner(*args, **kwargs):
        st = datetime.now()
        resp = func(*args, **kwargs)
        run = (datetime.now() - st).total_seconds()
        print(f"Function took {run} seconds to run")
        return resp
    return inner
@timer
def add_2(x):
    sleep(1)
    return x + 2
# Try it
add_2(2)
