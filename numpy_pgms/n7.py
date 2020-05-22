import numpy as np 
#Array Stacking and Splitting

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print (np.vstack((a,b)))
print (np.hstack((a,b)))
c=np.array((0,0))
print (np.column_stack((a,c)))
print(np.row_stack((a,c)))

# more than two dimensional means , concatenate 

print(np.concatenate((a,b),axis=0))

#Splitting - np.hsplit,np.vsplit,np.array_split
a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print (np.hsplit(a,2))
#splitting along vertical axis
print (np.vsplit(a,2))

# more than 2 dimensions= array_split
print (np.array_split(a,2,axis=0))

