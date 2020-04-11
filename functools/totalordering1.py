from functools import total_ordering

@total_ordering
class car:

	def __init__(self,model,mileage):
		self.model=model
		self.mileage=mileage

	def __eq__(self,other):
		return self.mileage==other.mileage


	def __lt__(self,other):
		return self.mileage<other.mileage

c1=car("BMW",600)
c2=car("Audi",700)

print (c1==c2)
print (c1<c2)	
print (c1>c2)
print(c1>=c2)
		
		