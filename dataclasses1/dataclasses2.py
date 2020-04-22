
from dataclasses import dataclass

@dataclass(order=True)
class Person:
	name:str
	age:int
	city:str

p=Person("karthi",9,"chennai")	
p1=Person("Sarvesh",8,"chennai")

print (p!=p1)
print (p.age>p1.age)
print (p.age<p1.age)
print (p>p1)


