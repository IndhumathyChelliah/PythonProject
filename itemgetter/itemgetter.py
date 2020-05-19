from operator import itemgetter
record=[('indhu',25,12),('karthi',7,15),('sarvesh',3,20)]

k=itemgetter(1)
print (list(map(k,record)))
#sorting based on key index 1 (age)
print (sorted(record,key=itemgetter(1)))

#sorting based on key index 1 , if same sort based on key index 2

print (sorted(record,key=itemgetter(1,2)))

data=[{'name':'indhu','age':25},{'name':'karthi','age':7},{'name':'sarvesh','age':3}]

print (sorted(data,key=itemgetter('age')))
