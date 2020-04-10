import time

def add(x,y):
	return (x+y)

def sub(x,y):
	return (x-y)

def calculatetime(func):

	def inner(a,b):
		start=time.time()
		print (func(a,b))
		end=time.time()
		print (end-start)
	return inner	

ad1=calculatetime(add)

ad1(10,5)

s1=calculatetime(sub)

s1(10,5)


