import numpy as np
from numpy.linalg import inv
A=np.matrix([[1,2,3],[2,4,5],[3,5,6]])
print(A)
B=inv(A)
C=A*B
print(C)