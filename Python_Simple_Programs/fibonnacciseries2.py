
# printing fibonnaci series until the given number. 

number=int(input("Enter a number: "))

if number <0:
	print ("enter number greater than zero")
elif number==0:
	print (0)



else:
	a=0
	b=1
	print (a)
	print (b)
	c=a+b
	
	while c<=number:
		print (c)
		a,b=b,c
		c=a+b


	
			

	
