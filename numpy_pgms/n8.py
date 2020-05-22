import numpy as np 
#broadcasting

a=np.array([1,2,3])
b=np.array([2,2,2])
print (a*b)
#here broadcasting happens. it saves memory space. no need to memtion 3- twos
c=np.array([2])
print (a*c)

d=np.array([0,10,20,30])
e=np.array([0,1,2])
d=d.reshape(4,1)
print(d)

# broadcasting 4*1 , 1*3  ===> 4*3 
print (d+e)