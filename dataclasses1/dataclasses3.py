from dataclasses import dataclass,field

@dataclass
class Person:
	name:str
	age:int
	city:str
	is_senior:bool=field(init=False)

	def __post_init__(self):
		if self.age>=60:
			self.is_senior=True
		else:
			self.is_senior=False
		

p=Person('karthi',7,'chennai')
print (p)
print (p.is_senior)
	
		


	
