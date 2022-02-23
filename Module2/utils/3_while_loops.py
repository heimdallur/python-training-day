"""Training guide to using while loops"""

"""
Glossary:
while - the keyword for starting a while loop
< - check if the first value is less than the second
> - check if the first value is greather than the second
<= - check if the first value is less than or equal to the second
>= - check if the first value is greather than or equal to the second
== - check if the first value is equal to the second
!= - check if the first value is NOT equal to the second
and - logic operator to combine 2 or more checks. Only True if
+= - operator to reassign value of a varibale to it's current value
    plus whatever follows
"""

###################
### WHILE LOOPS ###
###################
# Basic use
a = 1
# Start a while loop
while a < 10:
    print(f"a is {a}")
    a += 1

# WATCHOUTS
# Infinate loops are killers
a = 1
while a < 10:
    print(f"a is {a}")
    a += -1
