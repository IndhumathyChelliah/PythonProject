from functools import cached_property

class Marksheet:
	def __init__(self,*grades):
		self.grades=grades
	@cached_property
		
	def total(self):
		print ("Calculating total")
		return sum(self.grades)

	@cached_property	

	def avg(self):
		print("calculating average")
		return self.total/len(self.grades)

m=Marksheet(20,25,30)
print(m.total)
print (m.avg)
print(m.total)
		
		