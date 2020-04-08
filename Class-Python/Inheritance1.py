class Employee:
	raise_amount=1.05
	No_of_Employees=0
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		Employee.No_of_Employees += 1

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		return int(self.pay*self.raise_amount)


class Developer(Employee):
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang=prog_lang

class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees= []
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp  not in self.employees:
			self.employees.append(emp)

	def rem_emp(self,emp):
	    if emp  in self.employees:
	    	self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print ("-->", emp.fullname())
	    	

			
		  	
dev1=Developer("indhu","mathy",500,"python")
dev2=Developer("chelliah","mathy",500,"python")

mgr=Manager("karthi","sarvesh",700,[dev1])

print (mgr.fullname())

print (mgr.print_emp())

mgr.add_emp(dev2)
print (mgr.print_emp())

mgr.rem_emp(dev1)
print (mgr.print_emp())


print (dev1.prog_lang)
print (dev1.fullname())

print (isinstance(mgr,Manager))
print (isinstance(mgr,Developer))

print (isinstance(mgr,Employee))

print (issubclass(Manager,Developer))
print (issubclass(Manager,Employee))






