import numpy as np
import statistics
from numpy.random import rand
from numpy.linalg import *

v1 = np.array([4,6,2,6,7,232,6,1677,323,6,77])

# ej 1:

def media(x):
    return np.sum(x)/x.size

def varianza(x):
    med = media(x)
    n = x.size
    med_arr = np.full(n, med)
    return (np.linalg.norm(x - med_arr)**2)/n

# testing
# create a randon vector of size 10 with float elements between 0 and 99
for i in range(1):

    v1 = np.random.uniform(0, 99, size=10)
    # v1 = np.random.randint(99, size=10)
    print(v1)
    print("media:", media(v1), "varianza:", varianza(v1))
    print("media:", statistics.mean(v1), "varianza:", statistics.variance(v1))
    print(statistics.mean(v1) == media(v1))
    print(statistics.variance(v1) == varianza(v1))


