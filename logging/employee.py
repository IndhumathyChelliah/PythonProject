
import logging

#logging.basicConfig(filename="employee.log",level=logging.INFO,format='%(levelname)s:%(name)s:%(message)s')
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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
		
		
		

