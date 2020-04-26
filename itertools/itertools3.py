import itertools
import operator
#itertools.accumulate

numbers=[1,2,3,4,5]

result=itertools.accumulate(numbers)

for item in result:
	print (item,end=" ")
print ("\n")	

result1=itertools.accumulate(numbers,operator.mul)
for item in result1:
	print (item,end=" ")
print ("\n")

def get_state(person):
	return person['state']

people=[
         {'name':"indhu",
          'city':'chennai',
          'state':"TN"} ,
          {
          'name':"karthi",
          'city':'nellai',
          'state':"TN"
          },
           {
          'name':"Sarvesh",
          'city':'nellai',
          'state':"NC"
          }
]

person_group=itertools.groupby(people,get_state)

for key,group in person_group:
	print (key,len(list(group)))


for key,group in person_group:
	print (key)
	for person in group:
		print (person)



