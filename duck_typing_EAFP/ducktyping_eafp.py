
class Duck:
	def quack(self):
		print ("Quack,Quack")
	def fly(self):
		print ("Flap,Flap")
class Person:
	def quack(self):
		print ("I am quacking like a duck")
	def fly(self):
		print ("I am flapping my arms")

def quack_and_fly(thing):
	try:
		thing.quack()
		thing.fly()
		thing.bark()
	except AttributeError as e:
		print (e)
		print ()
		
d=Duck()
p=Person()
quack_and_fly(d)
quack_and_fly(p)

		



		


		