import numpy as np
import random
import numpy as np

A = np.random.randint(1,31, (3,3))

B = A.T


print(A, "\n")
print(B)
print()

str_row = ""
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        str_row += str(A[i,j]) + "+" + str(B[i,j]) + " "  # Added the missing + operator
    print(str_row)
    str_row = ""
        


res = A - B
print("res:\n",res)