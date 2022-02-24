"""Training guide to using functions"""

#################
### FUNCTIONS ###
#################
# Basic function


def function_name(variable1, variable2):
    # Functions give you a response when you type return
    # return can be anything
    return variable1 + variable2


# You call a function like this
function_name(1, 2)

# Nesting functions
# One functions can be put in another
# and even written inside another
# This function...


def func(a, b):
    def add(c, d):
        return c + d
    c = add(a, b)
    return c


func(1, 2)
# Is the same as this function...


def add(c, d):
    return c + d


def func(a, b):
    c = add(a, b)
    return c


func(1, 2)

# You can give a function default values if one is not entered
# (these are call keyword arguments or kwargs)


def add_x(a, x=1):
    return a + x


add_x(2)
# But entering an object will overrule this
add_x(2, 2)

# Non-kwarg argument must be given in the correct order
def div_ab(a, b):
    return a / b
div_ab(1, 2)
div_ab(2, 1)
# But kwargs do not need to be given in the correct order
def div_ab(a=1, b=2):
    return a / b
div_ab(a=10, b=20)
div_ab(b=20, a=10)

# You will often see the type of a variable in the method
# this is for guidance so other people use your functions right


def add_x(a: int, x: int = 1):
    return a + x


# it doesn't change how the function works
add_x(2, 2)

# Do one thing principal
# This function is doing 2 unrelated things


def func_a(a, b, name):
    c = a + b
    name2 = name.lower()
    return c, name2
# This function is doing 3 different but related things
# these should really each be in their own functions


def func_b(a, b):
    c = a+b
    c = c / 2
    c = c - b
    return c


func_b(1, 2)
# Like this


def add(a, b):
    return a + b


def div2(a):
    return a / 2


def minus(a, b):
    return a - b


def func_b(a, b):
    c = add(a, b)
    c = div2(c)
    c = minus(c, b)
    return c


func_b(1, 2)

# Do things once principal
# This should be in a function
c = add(1, 2)
c = div2(c)
c = minus(c, 2)
print(c)

c = add(2, 3)
c = div2(c)
c = minus(c, 3)
print(c)

c = add(3, 4)
c = div2(c)
c = minus(c, 4)
print(c)
# Like this


def func_c(a, b):
    c = add(a, b)
    c = div2(c)
    c = minus(c, b)
    print(c)


func_c(1, 2)
func_c(2, 3)
func_c(3, 4)
