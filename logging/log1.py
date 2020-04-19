
import logging
import employee

#logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)


def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		logger.exception("Tried divide by zero")
	
		

	
x1=10
y1=5

add_result=add(x1,y1)
logger.debug("Add: {}+{}={}".format(x1,y1,add_result))
sub_result=sub(x1,y1)
logger.debug("Sub:{}-{}={}".format(x1,y1,sub_result))
div_result=div(x1,y1)
logger.debug("Div:{}-{}={}".format(x1,y1,div_result))




