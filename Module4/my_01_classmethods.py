"""Tutorial on classmethods"""

# Classes use methods inside them which take the self argument


from datetime import datetime


class Employee:
    # Classes should have an init dunder method
    def __init__(self,
                 firstname: str,
                 surname: str,
                 pay: int
                 ):
        # the "self" variable here is used
        # throughout to refer to the object itself
        self.firstname = firstname
        self.surname = surname
        self.pay = pay

    # This is a method inside the class
    def print_name(self):
        # here we can print my_var because it's part of self
        print(f"EMPLOYEE NAME: {self.firstname} {self.surname}")


# We can access the class by instantiating it and calling a method
# INPUT - Instantiate the class and print the name

# Classmethds are put inside the class with a decorator and take cls as
#   the first argument
# INPUT - Using this class add a class var for annual rise and an init var
#   for a personal pay rise. Add a method to set the annual pay rises
#   and print the two different pay rises
# You call it like this
# INPUT - Init the class for ("Elsa", "of Arendel", 30000) and ("Anna", "of Arendel", 10000)
#   set the class var of pay rise and show the difference in values


# Why do this? It keeps functions nicely organised into the space they're
#   associated with

# Another use is to actually create the class in different ways
# INPUT - Use the above class but add a method to create it from
#   a string


# Now we cna use this to create a class
# INPUT - Init with ("Harry,Potter,100000")

# Some great examples of this is datetime
# INPUT - Show examples with datetime now today fromisoformat