
class Student:
	def __init__(self,marks):
		self.__marks=marks
	def percentage(self):
		return (self.__marks/600)*100
	@property
	def marks(self):
		return self.marks
	@marks.setter
	def marks(self,value):
		if value<0 or value >600:
			print ("Invalid marks.")
		else:
			self.__marks=value
		
				
s1=Student(600)
s1.marks=5000

print (s1.percentage())
