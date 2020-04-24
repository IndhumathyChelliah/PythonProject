
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

	def wrapper(*args,**kwargs):
		logging.info("Ran with args:{},kwargs:{}".format(*args,**kwargs))
		return orig_func(*args,**kwargs)
	return wrapper
	
@my_logger
def display_info(name,age):
	print ("display_info ran with arguments {} ,{} ".format (name,age))

display_info("indhu",25)		
