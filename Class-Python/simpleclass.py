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

	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount=amount
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split("-")
		return cls(first,last,pay)
	@staticmethod
	def is_workday(day):
		if day.weekday==5 or day.weekday==5:
			return False
		return True	
import datetime
day1=datetime.date(2020,3,4)

print (Employee.is_workday(day1))



emp_str1="sarvesh-palani-750"
new_emp1=Employee.from_string(emp_str1)
print (new_emp1.first)




print (Employee.No_of_Employees)
emp1=Employee("indhu","mathy",500)
emp2=Employee("karthi","palanichamy",600)
print (emp1.__dict__)

print (Employee.No_of_Employees)

print (Employee.fullname(emp2))
print (emp1.apply_raise())
Employee.set_raise_amount=1.05
print(emp1.raise_amount)

