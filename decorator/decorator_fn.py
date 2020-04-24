
def decorator_fn(original_function):
	def wrapper(*args,**kwargs):
		print  ("Executed before the function "+ (original_function.__name__))

		return original_function(*args,**kwargs)
	return wrapper
		
@decorator_fn			
def display():
	print ("Display fucntion ran")

d=display()

@decorator_fn
def display_info(name,age):
	print ("display_info ran with arguments {} ,{} ".format (name,age))

display_info("indhu",25)

