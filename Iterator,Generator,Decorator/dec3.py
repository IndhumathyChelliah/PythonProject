def strupper(func):
	def up():
		str1=func()
		s2=str1.upper()
		return s2
	return up

def st():
	return ("hello")

a=strupper(st)

print (a())	

@strupper
def st1():
	return("hi everyone")

print (st1())	

