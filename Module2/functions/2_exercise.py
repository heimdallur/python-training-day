### EXERCISE ###
"""Rob has a cake shop. He needs to work out the profit margin for each
of the cakes he sells.

Make a function which will calculate the profit of each item and print
a sentence expressing this.

Costs and prices are in £
Time is in minutes
All employees are paid £9.15 per hour
"""
cakes = [
    {
        "name":"victoria sponge",
        "ingredients_cost":1.00,
        "labour_time":45,
        "people_required":1,
        "sell price":2.00
    },
    {
        "name":"chocolate fudge",
        "ingredients_cost":2.39,
        "labour_time":15,
        "people_required":3,
        "sell price":4.15
    },
    {
        "name":"delicious surprise",
        "ingredients_cost":15.24,
        "labour_time":240,
        "people_required":3,
        "sell price":19.99
    }
]

"""Now look at the function and decide if it can be split out using the "do
one thing" principal.
"""

"""Finally make a new function which can tell Rob what price he should be charging 
if he wants to make a 45% margin (note margin not mark up).
"""