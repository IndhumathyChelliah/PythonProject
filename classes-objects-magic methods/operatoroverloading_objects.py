
from functools import total_ordering
@total_ordering
class Employee:
	raise_amount=1.05

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
	@property	
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def __eq__(self,other):
		return self.pay==other.pay
	def __lt__(self,other):
		return (self.pay<=other.pay)
	def __add__(self,other):
		return (self.pay+other.pay)
		
	def __repr__(self):
		return "Fullname:{} {} Pay:{}".format(self.first,self.last,self.pay)
		

e1=Employee("indhu","mathy",5000)
e2=Employee("karthi","palani",750)
e3=Employee("sarvesh","palani",1000)

print (e1==e2)
print (e1<e2)
print (e1>e2)
print (e2+e3)