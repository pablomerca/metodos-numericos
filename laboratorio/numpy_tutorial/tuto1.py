import numpy as np

# el segundo parametro es opcional, podemos elegir el tipo de dato
# de adentro de la matriz, con una asignacion directa en el param
a = np.array([1,2,3], dtype='int16') 
print(a)
print("dimensiones de a:", a.ndim)
# sobre las shapes, si es un vector 1-dimensional, entonces, lo va
# a tomar como un vector "columna", nos va a decir que tiene n rows
# la otra dimension la deja vacia, ya que no tiene...
print("shape of a:",a.shape)
print()

b = np.array([[1.5,2.3,3.0,4.0],[5.1,6.1,7.4,8.9]])
print(b)
print("dimensiones de b:", b.ndim)
# si es una matriz, entonces nos va a decir (nRows, nCols)
print("shape of b:",b.shape)

# getting data type
print()
print("data type of a:", a.dtype)
#get item size in bytes
print("item size of a:", a.itemsize)
# get total number of bytes used = a.size * a.itemsize
print("total number of bytes:", a.nbytes)

