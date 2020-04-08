class Employee:
	raise_amount=1.05
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay

	@property	
		
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@property	

	def email(self):
		return "{}.{}@email.com".format(self.first,self.last)
		

	def apply_raise(self):
		return int(self.pay*self.raise_amount)

	@fullname.setter
	def fullname(self,name):
		first,last=name.split(" ")
		self.first=first
		self.last=last

emp1=Employee("indhu","mathy",500)
emp1.first="chelliah"
emp1.fullname="indhu chelliah"
print (emp1.first)
print (emp1.fullname)
print (emp1.email)



	


