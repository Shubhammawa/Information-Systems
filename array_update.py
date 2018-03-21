import numpy as np
import math
n = int(input())
num = []
num.append(input().strip().split(" "))
Num = np.array(num)
sum_num = np.sum(Num)
x = (sum_num+1)/n
print(math.ceil(x))
