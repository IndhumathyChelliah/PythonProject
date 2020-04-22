from dataclasses import dataclass

class Person:
	def __init__(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def __repr__(self):
		return "Person('name'={},'age'={},'city'={})".format(self.name,self.age,self.city)
	def __eq__(self,other):
		return (self.name,self.age,self.city)==(other.name,other.age,other.city)


p=Person("karthi",7,'chennai')
p1=Person("karthi",7,'chennai')
print (p)
print (p==p1)


@dataclass
class NewPerson:
	name:str
	age:int
	city:str
p=NewPerson("karthi",7,'chennai')
p1=NewPerson("karthi",7,'chennai')
print (p)
print (p==p1)





		
		