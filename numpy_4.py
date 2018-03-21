import numpy as np
A=np.arange(10000).reshape(100,100)
sum1=0

for i in range(0,100):
    for j in range(0,100):
        sum1=np.where(A[i][j]>50,sum1+A[i][j],sum1)
print(sum1)
