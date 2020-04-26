import logging

class GetLog:
	@staticmethod
	def getLog(nm):
		logger=logging.getLogger(nm)
		logger.setLevel(logging.DEBUG)
		formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
		file_handler=logging.FileHandler('test.log')
		file_handler.setFormatter(formatter)
		logger.addHandler(file_handler)
		return logger