

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
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
	def __str__(self):
		return "{} {}".format(self.first,self.last)
		
		

e1=Employee("indhu","mathy",5000)
e2=Employee("karthi","palani",750)
e3=Employee("sarvesh","palani",1000)

print (e1)