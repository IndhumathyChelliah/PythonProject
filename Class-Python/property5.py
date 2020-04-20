class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last
	@property	
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	@fullname.setter
	def fullname(self,name):
		first,last =name.split(" ")
		self.first=first
		self.last=last
	@fullname.deleter
	def fullname(self):
		print ("Delete Name")
		self.first=None
		self.last=None
		

	@property
	def email(self):
		return "{}.{}@email.com".format(self.first,self.last)

e1=Employee("indhu","mathy")
e1.last=("chellaih")
print (e1.fullname)
print (e1.email)
e1.fullname="indhu mathyc"
print (e1.last)
del e1.fullname
print (e1.first)



