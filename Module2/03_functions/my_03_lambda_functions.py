"""Tutorial on writing lambda functions"""

# Lambda functions are a great way to write simple functions quickly

# For example a typical function could be


def multiply_3(x):
    return x * 3


print(multiply_3(3))

# This is fine but for something this simple it's much easier to write


multiply_3 = lambda x: x * 3


print(multiply_3(3))

# All in one line and it does the same thing
# This is useful when you want to do a manipulation of a list
a = [1, 2, 3, 4, 5]
# Using map you can tell it to run the lambda function on every item in a
b = list(map(lambda x: x + 2, a))

# WATCHOUT
# AWS use the term "lambda function" to refer to their event triggered cloud
# applicaitons. Do not get them confused.