
from dataclasses import dataclass,field

@dataclass
class Person:
	name:str=field(compare=False)
	age:int=field(init=False,default=7,repr=False)
	city:str=field(default='chennai')

p=Person("karthi")
p1=Person("Sarvesh")

p.age=7
print (p,p1)

print (p==p1)