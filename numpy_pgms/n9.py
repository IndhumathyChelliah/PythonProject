import numpy as np 
today=np.datetime64('2020-04-26')
print (today)
print (np.datetime64(today,'Y'))

#creating array of dates in a month
dates=np.arange('2020-01','2020-02',dtype='datetime64[D]')
print (dates)

#arithmetic operations on dates
dur=np.datetime64('2020-04-26')-np.datetime64('2020-07-12')
print (dur)

print (np.timedelta64(dur,'W'))

#sorting dates
print (np.array(['2020-07-12','2020-04-26','2020-01-21'],dtype='datetime64'))

