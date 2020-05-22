import numpy as np 


# Array Creation-- differnet types

arr1=np.zeros((2,3),dtype=int)
print (arr1)

arr2=np.ones((3,3),dtype=float)
print (arr2)

arr3=np.full((2,2),4)
print (arr3)

arr4=np.random.random((2,2))
print (arr4)

arr5=np.random.randint(1,10,(3,3))
print (arr5)

arr6=np.array(range(10))
print(arr6)

arr7=np.arange(10)
print (arr7)
# in python range fn, step cant be float. but in arange fn, it will accept float- step value 
arr8=np.arange(1,10,0.5)
print (arr8)

# elements equally spaced in the given range

arr9=np.linspace(1,10,20)
print (arr9)
