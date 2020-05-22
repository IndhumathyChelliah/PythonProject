import numpy as np 

l1=[[1,2,3],[4,5,6]]
#Array creation from list
arr=np.array(l1)
print (l1)
print (arr)
print (type(arr))
print (arr.shape)
print(arr.dtype)

#to change th dtype of array

arr1=np.array(l1,dtype=float)
print (arr1)
print (arr1.dtype)