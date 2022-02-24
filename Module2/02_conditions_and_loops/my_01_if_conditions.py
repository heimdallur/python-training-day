"""Training guide to using if conditions"""

"""
Glossary:
if - the keyword for starting an if criteria check
< - check if the first value is less than the second
> - check if the first value is greather than the second
<= - check if the first value is less than or equal to the second
>= - check if the first value is greather than or equal to the second
== - check if the first value is equal to the second
!= - check if the first value is NOT equal to the second
and - logic operator to combine 2 or more checks. Only True if
"""

################
### IF LOOPS ###
################
# If loops with evaluate criteria and return True or False.
# When True is returned the code in the "if" section will be processed.
# When False is returned the code is skipped or the code in the "else"
#   section will be processed (if an else is given).
# Basic use
a = 1
b = 2
if a < b: # Here is the criteria
    # If the criteria above is met then this happens
    print("A is the little one")
else:
    # If the criteria above is NOT met then this happens
    print("B is the little one")

# Elif use
a = 1
b = 2
if a < b: # Here is the first criteria
    # If the first criteria is met then this happens
    print("A is the little one")
elif a > b: # If the first criteria is not met then this criteria is checked 
    # If the second criteria is met then this happens
    print("B is the little one")
else:
    # If neither criteria are met then this happens
    print("A and B are the same size")

# and criteria
a = 1
b = 2
if a < b and b == "foo": # Here are the criteria - BOTH must be true to pass
    # If the criteria above are BOTH met then this happens
    print("A is the little one AND b is foo")
else:
    # If EITHER of the criteria above are NOT met then this happens
    print("B is the little one OR b is not foo")

# or criteria
a = 1
b = 2
if a < b or b == "foo": # Here are the criteria - one must be true to pass
    # If EITHER of the criteria above are met then this happens
    print("A is the little one OR b is foo")
else:
    # If BOTH of the criteria above are NOT met then this happens
    print("B is the little one AND b is foo")

# Single line use
a = 1
b = 2
print("A is the little one" if a < b else "B is the little one")

# WATCHOUT
# If you declare a varibale inside an if loop
x = 1
y = 2
if x > y:
    z = "Y is the little one"
print(z)
# None does not use ==
a = False
if a is None:
    print("a is None")
else:
    print("a is not None")
