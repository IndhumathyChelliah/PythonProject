class Employee:
	raise_amount=1.05
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		return int(self.pay*self.raise_amount)

	def __repr__(self):
		return "Employee('{}' '{}' {})".format(self.first,self.last,self.pay)

	def __str__(self):
		return "{}" .format(self.fullname())

	def __add__(self,other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())
		
		

emp1=Employee("indhu","mathy",500)
emp2=Employee("karthi","sarvesh",700)


print (emp1)	
print (repr(emp1))	
print (str(emp1))

print (emp1 + emp2)
print (len(emp1))
	

