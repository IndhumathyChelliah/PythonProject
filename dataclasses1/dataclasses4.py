from dataclasses import dataclass,field

@dataclass
class Person:
	firstname:str
	lastname:str
	age:int
	city:str
	fullname:str=field(init=False)
	

	def __post_init__(self):
		self.fullname=self.firstname +self.lastname
		

p=Person('karthi','palani',7,'chennai')
print (p)
print (p.fullname)

