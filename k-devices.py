import numpy as np
import math

n,k = map(int, input().strip().split(" "))
X = list()
Y = list()
X.append(input().strip().split(" "))
Y.append(input().strip().split(" "))
Len = list()
for i in range(0,n):
    Len.append(math.sqrt(((int(X[0][i]))**2)+((int(Y[0][i]))**2)))
Len1 = np.array(Len)
np.ndarray.sort(Len1)
print(Len1)
radius = math.ceil(Len1[k-1])    
print(radius)
