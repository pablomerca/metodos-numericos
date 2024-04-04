import numpy as np
from numpy.random import rand
from numpy.linalg import *

# matriz de testeo
A_test = np.array([[1, 5, 1], [1, 1, 4], [1, 3, 1]], dtype = float) 
b_test = np.array([1, 1, 1], dtype = float)



def Triangular_matriz(A: np.array, b: np.array):
    # A.shape devuelva una tupla de las dimensiones de la matriz
    print("b al entrar: \n", b)

    n = A.shape[0]

    if A.shape[0] != A.shape[1]:
        raise Exception("La matriz tiene que ser cuadrada")
    if b.size != n:
        raise Exception("El tamaño de b y la cantidad de columnas de A tienen que ser los mismos") 

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (A[i, i] == 0):
                raise Exception("No se puede hacer eliminación Gaussiana en esta matriz, tiene un elemento nulo en la diagonal")
            
            f = A[j, i] / A[i, i]
            for k in range(i, n):
                A[j, k] = A[j, k] - f * A[i, k]
            b[j] = b[j] - f * b[i]



def backwards_substitution(A, b):
    #recibe matriz escalonada
    n, m = A.shape # (n,m)
    x = np.ones(n)

    if(A[n-1, n-1] == 0):
        raise Exception("No se puede hacer eliminación Gaussiana en esta matriz, tiene un elemento nulo en la diagonal")

    # el ultimo elemento de x se trata por separado
    x[-1] = b[-1]/A[-1, -1]

    for i in range(n-2, -1, -1):
        if(A[i, i] == 0):
            raise Exception("No se puede hacer eliminación Gaussiana en esta matriz, tiene un elemento nulo en la diagonal")
        acu = 0.0
        for j in range(i+1, n): # n es el num de cols en este caso
            acu += A[i,j] * x[j]
        x[i] = (b[i] - acu)/A[i,i]
    return x



def EG_sin_pivot(A: np.array, b: np.array):

    print("Matriz input: \n", A)
    Triangular_matriz(A, b)
    print("b al salir: \n", b)
    
    print("matriz triangulada A: \n", A)
    x = backwards_substitution(A, b)

    print("resultado x: \n", x)
    return x


# testing
EG_sin_pivot(A_test, b_test)


#1b)
"""
0 1 2
3 4 4
5 4 6
"""

def EG_con_pivot(A):
    pass

