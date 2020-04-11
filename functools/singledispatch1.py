from functools import singledispatch

def appendone(obj):
	if type(obj)==list:
		return obj + [1]
	elif type(obj)==set:
		return obj. union({1})
	elif type(obj)==str:
		return obj+ str(1)
	else:
		print ("unsupported type")
		return (obj)
	  	

		
l=appendone([2,3,4])
print (l)
s=appendone({2,3,4})	
print (s)
s1=appendone("indhu")
print (s1)
d=appendone(3)
print (d)
d1=appendone({'a':1,'b':2})	
print (d1)

@singledispatch
def append_one(obj):
	print ("unsupported type")
	return (obj)

@append_one.register
def _(obj:list):
	return obj +[1]

@append_one.register
def _(obj:set):
	return obj.union({1})

@append_one.register(str)
def _(obj):
	return obj+str(1)

l1=append_one({2})

print (l1)

n=append_one(1)
print (n)


