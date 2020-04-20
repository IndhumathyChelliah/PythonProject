
class Employee:
	raise_amount=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay

	@classmethod
	def setraise_amount(cls,amount):
		cls.raise_amount=amount


	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split("-")
		emp_str1=cls(first,last,pay)
		return emp_str1

emp_str2="indhu-mathy-500"

emp1=Employee.from_string(emp_str2)

print (emp1.first)

print (emp1.raise_amount)
print (Employee.raise_amount)
Employee.setraise_amount(1.05)
print (emp1.raise_amount)
print (Employee.raise_amount)






