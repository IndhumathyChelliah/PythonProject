import numpy as np 
a=np.array([[1,4,2],[3,2,6],[0,-1,0.5]])
#Row wise sorting
print (np.sort(a))
#column wise sorting

print (np.sort(a,axis=0))

# sort all elements into one dimensional array
print (np.sort(a,axis=None))
