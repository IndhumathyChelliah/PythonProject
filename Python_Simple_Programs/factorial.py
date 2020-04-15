

def getfactorial(num):
	if num<0:
		return -1
	elif num<2:
		return 1
	else:
		return num*getfactorial(num-1)
print (getfactorial(5))

def getfac(n):
	if n<0:
		print (-1)
	elif n<2:
		print (1)
	else:
		fac=1
		for i in range(1,n+1):
			fac=fac*i
		print (fac)
			
getfac(1)
		

		


		
	

	
	


	
    

		
