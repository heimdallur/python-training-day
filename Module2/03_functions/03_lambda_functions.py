"""Tutorial on writing lambda functions"""

# Lambda functions are a great way to write simple functions quickly

# For example a typical function could be


def multiply_3(x):
    return x * 3


print(multiply_3(3))

# This is fine but for something this simple it's much easier to write
# INPUT - Write the above funciton as a lambda function

# All in one line and it does the same thing
# This is useful when you want to do a manipulation of a list
a = [1, 2, 3, 4, 5]
# Using map you can tell it to run the lambda function on every item in a
# INPUT - Use lambda to loop over a list apply a transformation