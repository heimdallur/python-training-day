import datetime

dt_now = datetime.datetime.now()
print(dt_now)
print(dt_now.year)
print(dt_now.strftime("%A"))

dt_set = datetime.datetime(2020, 5, 17)

print(dt_set)