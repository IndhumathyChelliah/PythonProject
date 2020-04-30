
import datetime

today=datetime.date.today()
print (today)
print(today.year)
print (today.month)
print (today.day)

t=datetime.time(4,20,1)
print (t)
print (t.hour)

d1=datetime.date(1982,12,25)
d2=datetime.date(2020,4,28)
print (d2-d1)