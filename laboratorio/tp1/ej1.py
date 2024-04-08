import numpy as np
from numpy.random import rand
from numpy.linalg import *



def triangular_matriz(A: np.array, b: np.array):
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
    triangular_matriz(A, b)
    x = backwards_substitution(A, b)
    return x


#1b)


# pivoteamos la i-esima columna
def pivot(A: np.array, i):
    # A[i, i] = 0 al entrar
    # print("A al entrar a pivotear: ", A)
    n = A.shape[0]
    maxPiv = 0
    candidate = i
    # buscamos la row con el max elemento, en modulo, en la i-esima col
    for row in range(i+1, n):
        if(abs(A[row, i]) > maxPiv):
            maxPiv = abs(A[row, i])
            candidate = row
    #swap row i and row candidate
    A[[i, candidate]] = A[[candidate, i]]
    if maxPiv == 0:
        raise Exception("no se pudo encontrar un pivot no nulo")



def triangular_matriz_p(A: np.array, b: np.array, eps):
    # A.shape devuelva una tupla de las dimensiones de la matriz
    n = A.shape[0]

    if A.shape[0] != A.shape[1]:
        raise Exception("La matriz tiene que ser cuadrada")
    if b.size != n:
        raise Exception("El tamaño de b y la cantidad de columnas de A tienen que ser los mismos") 

    for i in range(n - 1):
        for j in range(i + 1, n):

            if (A[i, i] == 0): pivot(A, i)
            if abs(A[i,i]) < eps: print("division por numero menor a epsilon, posible perdida de precision")

            f = A[j, i] / A[i, i]
            # realizamos la elimnacion
            for k in range(i, n):
                A[j, k] = A[j, k] - f * A[i, k]
            b[j] = b[j] - f * b[i]
            # checkeamos si se anulo una row, elementos de la row j, de i a n
            # print(f"tras hacer elimnacion en la col: {i} , row: {j}, la row {j} queda: ")
            # print(A[j:j+1, i:n])

            # null_row tiene errores al detectar 0s, por perdidas de presicion, algunos
            # numeros que deberian dar 0 terminan siendo MUY chicos, pero no 0.
            null_row = np.all(A[j:j+1, i:n] == 0) 
            if null_row: 
                if b[j] == 0: print("hay infinitas soluciones!")
                else: print("sistema incompatible, no existen soluciones!")


def EG_con_pivot(A, b, eps):
    triangular_matriz_p(A, b, eps)
    x = backwards_substitution(A, b) # todo, agregar epsilon para ver si dividimos aca por nums muy chicos.
    return x








