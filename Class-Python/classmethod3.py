
class Student:
	count=0
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
		Student.count=Student.count+1
	@classmethod
	def obj_count(cls):
		return cls.count
	@classmethod
	def from_marks(cls,name,actual_marks):
		return cls(name,(actual_marks/600)*100)
	@staticmethod
	def get_age(age):
		if age>18:
			print ("eligible")
		else:
			print ("Not eligible")
		


s1=Student("indhu",100)
s2=Student("karthi",200)
s3=Student.from_marks("indhum",500)
print (s3.marks)
s1.get_age(19)
Student.get_age(21)



print (Student.obj_count())