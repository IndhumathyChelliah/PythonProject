import numpy as np 
# Array Reshaping

arr=np.array([1,2,3,4,5,6,7,8])
print (arr)

#Reshaping (1,8) as (2,4)-> (4,2)->(2,2,2)->(8,)->(2,2,2,1) - multiplication should be equal to 8

#Row major order (1,2,3,4 - 5,6,7,8)
# can use order="C"
arr1=arr.reshape((2,4))
print (arr1)

#Column major order (1,3,5,7) - 2,4,6,8
arr2=arr.reshape((2,4),order='F')
print(arr2)

#Array Flattening or collapsing

arr3=np.array([[1,2,3],[4,5,6]])
arr4=arr3.flatten()
print (arr4)

#column major order

arr5=arr3.flatten(order="F")
print(arr5)





