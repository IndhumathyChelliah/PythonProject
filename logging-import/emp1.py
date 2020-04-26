from loggingbasic import GetLog 

logger =GetLog.getLog('emp1.py')
class Employee:
	def __init__(self,firstname,lastname):
		self.firstname=firstname
		self.lastname=lastname

		logger.info("Created Employee {}-{}".format(self.fullname,self.mailid))
	@property	


	def fullname(self):
		return ("{} {}".format(self.firstname,self.lastname))
	@property	

	def mailid(self):
		return ("{}.{}@email.com".format(self.firstname,self.lastname))

e1=Employee("indhu","mathy")	