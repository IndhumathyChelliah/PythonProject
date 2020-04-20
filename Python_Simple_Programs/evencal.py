
import sys
#using sys.argv ( getting numbers in commandline)
print (list(map(lambda i : int(i)%2==0,sys.argv[1:])))

# using function
def even(*args):
	l1=[]
	for i in args:
		if i%2==0:
			l1.append(i)
	return l1
print (even(10,11,2,3,4,5,6))	

#using *args and filter
def even(*args):
	return args

l1=even(1,2,3,4,5,6,7,8)	

evennumber=list(filter(lambda x: x%2==0,l1))

print (evennumber)

#using list comprehension
def even(*args):
	return [i for i in args if i%2==0]

print (even(1,2,3,4,5,6,7,8,9,10))	







