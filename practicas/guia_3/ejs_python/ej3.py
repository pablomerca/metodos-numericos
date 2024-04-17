import numpy as np 

A = np.array([[2,0],[0,1]])

x = np.array([[ 11 ],[ 2 ]])
xt = x.T

y = np.array([[ 3 ],[ 5 ]])
yt = y.T

print(y)
print(yt)
print(x)
print(xt)

res_x = xt @ A @ y
res_y = yt @ A @ x

print()
print(res_x)
print()
print(res_y)