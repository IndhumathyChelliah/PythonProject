import datetime
import pytz
#convert the given input to date format
d=datetime.date(2020,4,4)
print (d)
#to print today date
tdaydate=datetime.date.today()
print (tdaydate)
#to print the year alone
print (tdaydate.year)
#to check whether its weekday or not
print (tdaydate.weekday())
print (tdaydate.isoweekday())
# to print the after one week
tdelta=datetime.timedelta(days=7)
print (tdaydate+tdelta)
# to calculate how many days are there for my bday
bday=datetime.date(2020,7,12)
till_bday=bday-tdaydate
print (till_bday)
# in seconds
print (till_bday.total_seconds())
# time
ttime=datetime.time(3,4,50,300)
print (ttime)
print (ttime.hour)
#datetime
#how to pass both date and time info
tday_ttime=datetime.datetime(2020,4,26,5,45,45,300)
print (tday_ttime)
print (tday_ttime.time())
print (tday_ttime.date())
print(tday_ttime.year)
print(tday_ttime.hour)

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
print (dt_today)
print(dt_now)
print(dt_utcnow)

#using pytz
dt=datetime.datetime(2020,4,26,5,45,45,tzinfo=pytz.UTC)
print (dt)
dt_now=datetime.datetime.now(tz=pytz.UTC)
print (dt_now)

#timezone
for tz in pytz.all_timezones:
    print (tz)
dt_est=dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print (dt_est)    

# date in soem format
print (dt.strftime('%B %d,%Y'))

#how to convert string - date to datetime 
dt_str='April 26,2020'
dt_1=datetime.datetime.strptime(dt_str,'%B %d,%Y')
print(dt_1)



