started=False

while True:
	com=input("Enter the input :").lower()
	if com=="help":
		print ("start - start the car \nstop- stop the car \nquit - to exit")
	elif com=="start":
		if started==False:
			print ("Start the car")
			started=True
		else:
			print ("Car already started")
			


	elif com=="stop":
		if started == False:
			print ("Car has not started yet. already stopped only")

		else :
			print ("Stop the car")
			started=False
	
		
			

	elif com=="quit":
		break
		
	else:
		print ("Sorry can't understand this")
		
   

		
		
	








