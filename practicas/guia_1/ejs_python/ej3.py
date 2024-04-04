import numpy as np
from numpy.random import rand
from numpy.linalg import *
 

# ej 3:
    
def mult(A, B):

    n, _ = A.shape
    A11 = A[0:(n//2), 0:(n//2)]
    A12 = A[0:(n//2), (n//2):n]
    A21 = A[(n//2):n, 0:(n//2)]
    A22 = A[(n//2):n, (n//2):n]

    B11 = B[0:(n//2), 0:(n//2)]
    B21 = B[(n//2):n, 0:(n//2)]
    B22 = B[(n//2):n, (n//2):n]

    C1 = A11 @ B11 + A12 @ B21 
    C2 = A12 @ B22
    C3 = A21 @ B11 + A22 @ B21
    C4 = A22 @ B22
    
    res = np.bmat([[C1, C2],[C3, C4]])
    return res

# testing 
# generate a random matrix full of int values
for i in range(15):
    # A = rand(8,8)
    # B = rand(8,8)
    A = np.random.randint(99, size = (8,8))
    B = np.random.randint(99, size = (8,8))
    B = np.tril(B) # convert B to lower triangle

    C = mult(A,B)
    D = A @ B
    # all() compares all elements and returns only one bool, C == D returns a boolean masked matrix.
    print(C.all() == D.all())

