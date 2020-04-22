from dataclasses import dataclass,asdict,astuple

@dataclass
class Address:
	street:str
	city:str
	state:str

@dataclass	
class Person:
	name:str
	age:int
	add:Address

a=Address("sundrop","chennai","tamilnadu")
p=Person("karthi",7,a)
print (p)

print (asdict(p))
print (astuple(p))

