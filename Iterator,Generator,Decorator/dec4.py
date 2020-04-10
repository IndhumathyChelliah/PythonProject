def divdec(func):
	def inner(x,y):
		if y==0:
			return ("give number greater than zero")
		return func(x,y)
	return inner
@divdec
def div(x,y):
	return (x/y)


print (div(4,0))
