from functools import partial

@partial
def add(a,b):
	print (a,b)
	return (a+b)

add1=add(3,4)

print (add1)	

add2=partial(add,1)

print (add2(2))

add3=partial(add,b=1)

print (add3(5))