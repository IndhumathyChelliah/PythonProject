
from abc import ABC,abstractmethod

class Shape(ABC):
	@abstractmethod

	def area():
		pass
	@abstractmethod	

	def perimeter():
		pass

class square(Shape):
	def __init__(self,side):
		self.side=side
	def area(self):
		return(self.side*self.side)

	def perimeter(self):
		return (4*self.side)
		

s=square(5)

print (s.area())	

print (s.perimeter())	
		


		













