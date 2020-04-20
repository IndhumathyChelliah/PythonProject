
class Student:
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade
	@property
	def msg(self):
		return self.name + "got" +self.grade
	@msg.setter
	def msg(self,msg): 
		text=msg.split(" ")
		self.name=text[0]
		self.grade=text[-1]
	@classmethod
	def from_string(cls,str):
		str1=str.split(" ")
		return cls(str1[0],str1[-1])

s1=Student("indhu","A")
s1.msg="Sarvesh got O grade"
print (s1.name)
print (s1.grade)
str="Karthi got A grade"
s2=Student.from_string(str)
print (s2.name)









