# In this section we will:
# Raise
# Assert
# Try/Except

def first_error(name):
    allows= ['Gareth', 'Rob']
    if name not in allows:
        raise ValueError('You cannot have that name')
    else:
        print(f'Hi {name}')

# first_error('Tom')

def data_checker(data):
    assert data['day'] == 'Monday', f"Day recieved was {data['day']} which is not equal to Monday"
    assert isinstance(data['day'], int), f"DataType for day should be int, but received {type(data['day'])}"

# d = {'nams': 'Clive', 'day': 'Monday'}

# data_checker(d)
a = 1
b = 0

import weather_api as w

res = w.current_for_city('London')

try:
    assert res['location']['name'] == 'Paris'

except:

    assert res['location']['name'] == 'London'

finally:
    print('Viola')