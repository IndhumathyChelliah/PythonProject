
def my_timer(orig_func):
	import time

	def wrapper(*args,**kwargs):
		t=time.time()
		reuslt=orig_func(*args,**kwargs)
		t1=time.time()-t
		print ("{} ran in {} sec".format(orig_func.__name__,t1))

	return wrapper
	
@my_timer
def display_info(name,age):
	print ("display_info ran with arguments {} ,{} ".format (name,age))

display_info("indhu",25)			
