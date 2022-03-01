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
        "sell_price":2.00
    },
    {
        "name":"chocolate fudge",
        "ingredients_cost":2.39,
        "labour_time":15,
        "people_required":3,
        "sell_price":4.15
    },
    {
        "name":"delicious surprise",
        "ingredients_cost":15.24,
        "labour_time":240,
        "people_required":3,
        "sell_price":19.99
    }
]

"""Now look at the function and decide if it can be split out using the "do
one thing" principal.
"""

"""Finally make a new function which can tell Rob what price he should be charging 
if he wants to make a 45% margin (note margin not mark up). Add this as an extra
field called "rrp" to each cake.
"""

def calc_profit(cakes: dict, hr_rate, margin=False):
    for cake in cakes:
        time_cost = cake['people_required'] * ((hr_rate / 60) * cake['labour_time'])
        ingredients_cost = cake['ingredients_cost']
        sell_price = cake['sell_price']
        net = ingredients_cost + time_cost
        print(f'Profit: {round(sell_price - net, 2)}')
        if margin:
            print(f'New Price: {add_margin(net, margin)}')

def add_margin(net, margin):
    print(f'New Price: {(net/margin)*100}')

calc_profit(cakes, 9.15, 0.45)