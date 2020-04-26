import itertools

#itertools.count()
counter=itertools.count()
print (next(counter))
print (next(counter))

data=[100,200,300]

daily_data=list(zip(itertools.count(),data))
print (daily_data)

daily_data1=list(zip(range(10),data))
print (daily_data1)

#itertools.zip_longest
daily_data2=list(itertools.zip_longest(range(10),data))
print (daily_data2)

#itertools.cycle()
counter1=itertools.cycle(("on","off"))
print (next(counter1))
print (next(counter1))
print (next(counter1))

#itertools.repeat()
counter2=itertools.repeat(2)
print (next(counter2))
print (next(counter2))
print (next(counter2))

square=map(pow,range(10),itertools.repeat(2))

print (list(square))

squares=itertools.starmap(pow,[(0,2),(1,2),(2,2)])

print (list(squares))
