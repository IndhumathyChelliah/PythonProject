def div(a,b):
	print (a/b)

def smartdiv(func):
	def inner(a,b):
		if a<b: 
			a,b=b,a
		return func(a,b)
	return inner

div=smartdiv(div)

div(2,4)

