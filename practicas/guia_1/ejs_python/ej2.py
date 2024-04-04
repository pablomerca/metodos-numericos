import numpy as np
from numpy.random import rand
from numpy.linalg import *

# ej 2:

def es_simetrica(x):
    rows, cols = x.shape   
    for i in range(rows):
        for j in range(i, cols):
            if x[i,j] != x[j,i]: return False
    return True

# testing
for i in range(10):
    A = rand(4,4)
    # .T is the transopose atribute of a multidimensional array. @ is the matrix multiplication operator.
    B = A.T@A*0.1/0.1 # multiplying and dividing for 0.1 to introduce some sort of float representation error.
    print("es simetrica:", es_simetrica(B))