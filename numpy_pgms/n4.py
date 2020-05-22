import numpy as np 
#Array Indexing

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print (arr[2][1])
#Poitive tuple indexing
print (arr[2,1])

#Array slicing
#first two rows
print (arr[:2])
#first two columns
print(arr[:,:2])
#first two rows and 2 columns
print(arr[:2,:2])

#Integer Array Indexing
#[(0,0),(1,1),(2,2)]

print(arr[[0,1,2],[0,1,2]])

#Boolean Array Indexing

print (arr>1)

#prints all the elements gretaer than 3
print (arr[arr>3])
