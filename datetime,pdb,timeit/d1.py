from datetime import datetime,timedelta

now=datetime.now() 
print (now)
# access thorugh methods
print (now.date())
print (now.time())
# access through attributes
print(now.hour)
print (now.minute)
print (now.second)

d1=now.date()
print(d1.month)
print(d1.day)
print(d1.year)
print (d1.weekday())

# convert date given in string format to datetime object

mytime="2020-05-16 19:33:59"
d2=datetime.strptime(mytime,"%Y-%m-%d %H:%M:%S")
print (d2)
print(d2.time())

#timedelta

now=datetime.now()
then=now+timedelta(hours=1)
print (then)
print (then-now)


#how to combine date and time object into datetimeobject

d=now.date()
t=now.time()
c=datetime.combine(d,t)
print (c)

#how to display time 

t1=now.strftime("%H-%M-%S")
print (t1)
print (now.isoformat())