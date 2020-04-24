
from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)

	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		logging.info("Ran with args:{},kwargs:{}".format(*args,**kwargs))
		return orig_func(*args,**kwargs)
	return wrapper

def my_timer(orig_func):
	import time
	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		t=time.time()
		reuslt=orig_func(*args,**kwargs)
		t1=time.time()-t
		print ("{} ran in {} sec".format(orig_func.__name__,t1))

	return wrapper


import time	
@my_logger
@my_timer
def display_info(name,age):
	time.sleep(1)
	print ("display_info ran with arguments {} ,{} ".format (name,age))

display_info("indhu",25)




