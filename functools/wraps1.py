from functools import wraps


def mylogger(func):

	@wraps(func)
	def wrapper(*args,**kwargs):
		print (f"Runnning function : {func.__name__}")
		return func(*args,**kwargs)
	return wrapper
@mylogger

def add(a,b):
	"""add a,b"""
	return (a,b)

sum=add(3,4)
print (sum)	
print (add.__name__)
print (add.__doc__)
