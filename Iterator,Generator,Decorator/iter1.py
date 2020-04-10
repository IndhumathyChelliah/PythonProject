class topten:

	def __init__(self):
		self.n=1

	def __iter__(self):
		return self


	def __next__(self):

		if self.n<=10:
			val=self.n
			self.n+=1
			return val
		else:
			raise StopIteration
		  	
t=topten()

for i in t :
	print (i)





