
data=[{'name':"indhu",
        'age':23,
         'rollno':12},

        {'name':"karthi",
        'age':12,
         'rollno':5} ]

class Student:
	def __init__(self,name,age,rollno):
		self.name=name
		self.age=age
		self.rollno=rollno
	@classmethod
	def from_dicts(cls,data):
		students=[]
		for row in data:
			student=cls(row['name'],row['age'],row['rollno'])
			students.append(student)
		return students
			

students=Student.from_dicts(data)
print (students)
print (students[1].name)
