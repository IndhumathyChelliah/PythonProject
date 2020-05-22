import numpy as np 
#linear algebra

'''
x+2*y=8
3*x+4*y=18
'''

#coefficients
a=np.array([[1,2],[3,4]])
#constants
b=np.array([8,18])

print (np.linalg.solve(a,b))

c=np.array([[6,1,1],[4,-2,5],[2,8,7]])
#trace of matrix
print (np.trace(c))
print (np.linalg.matrix_rank(c))
#determinant of matrix
print (np.linalg.det(c))
#inverse of matrix
print (np.linalg.inv(c))
#matrix exponentiation
print(np.linalg.matrix_power(c,3))