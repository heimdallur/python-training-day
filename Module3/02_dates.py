import datetime

now_dt = datetime.datetime.now()

# print(now_dt)
# print(now_dt.day)
# print(now_dt.month)
# print(now_dt.year)

print(now_dt.strftime("%A"))

my_dt = datetime.datetime(2020, 5, 17)

print(my_dt)

# https://strftime.org/