
person={"name":"karthi","Age":7,"Grade":"second grade"}

try:
	print ("I am {name}.I am {Age} years old.I am studying in {Grade}".format(**person))
except KeyError as e:
	print ("Missing Key{}".format(e))


l1=[1,2,3,4,5]

try:
	print (l1[6])
except IndexError as e:
	print (e)

import os
my_file="/tmp/test.txt"

try:
	f=open(my_file)
except IOError as e:
	print ("File can not be accessed")
else:
	with f:
		print (f.read())




