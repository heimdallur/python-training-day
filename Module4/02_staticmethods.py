"""Tutorial on static methods"""

# Static methods are used to organise functions alongside associated
#   functions

# This is a basic class holding a list of lists
import math


class MyLists:
    def __init__(self,
                *args
                 ):
        self.lists = list(args)
# Create it like this
MyLists([1,2,3], [4,5,6]).lists

# Now we can add a statcmethod to combine 2 lists together
class MyLists:
    def __init__(self,
                *args
                 ):
        self.lists = list(args)

    @staticmethod
    def combine_lists(*args):
        out = []
        for l in args:
            out += l
        return out

# Use it like this
MyLists.combine_lists([1,2,3], [4,5,6])

# This is actually similar to how the math class works
math.ceil(1.1111)
math.dist([1,2,3], [4,5,6])