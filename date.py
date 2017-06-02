import datetime

t = datetime.time(5, 25, 1)

print t
print t.minute
print t.hour
print t.tzinfo

print datetime.date.today()
print datetime.date.today().day

today = datetime.date(2017, 6, 3)
print today

dt = today.replace(year=2015)
print dt
