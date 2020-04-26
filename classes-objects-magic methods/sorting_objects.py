
from operator import attrgetter
class Employee:
	raise_amount=1.05

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
	@property	
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	
	def __repr__(self):
		return "Fullname:{} {} Pay:{}".format(self.first,self.last,self.pay)
		

e1=Employee("indhu","mathy",5000)
e2=Employee("karthi","palani",750)
e3=Employee("sarvesh","palani",1000)

e4=[e1,e2,e3]

#sorting by defining function	

def e_sort(emp):
	return emp.first
e5=sorted(e4,key=e_sort)
print (e5)	

# by using lambda function
e6=sorted(e4,key=lambda e : e.pay)
print (e6)

#by using attrgetter:
e7=sorted(e4,key=attrgetter('pay'))
print (e7)

