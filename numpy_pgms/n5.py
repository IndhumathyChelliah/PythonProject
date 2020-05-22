import numpy as np 

arr=np.array([[1,2,3],[4,5,6]])
#Elementwise Operation
#adds one to all elements in the array
print (arr+1)

print (arr**2)

#Unary Operators:

print(arr.sum())

# column wise addition - axis=0
print (arr.sum(axis=0))
# row wise addition - axis=0
print(arr.sum(axis=1))

print(arr.min(axis=0))
print (arr.min(axis=1))

#Binary Operators
# if both arrays have same size, then we will do element wise operation

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print (a+b)

#Universal Functions

# sin,cos, exp

print (np.sin(a))
print (np.exp(a))


