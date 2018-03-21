import numpy as np
A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])

sum1=A.sum(axis=1)    # Array of column sums
sum2=A.sum(axis=0)    # Array of row sums
sumd1=np.trace(A,0)    # Sum of diagonal 1 elements
sumd2=sum(A[i][4-i] for i in range(0,5))   # Sum of diagonal 2 elements
Sum1=sum1-int(sum1.mean())
Sum2=sum2-int(sum2.mean())
print(Sum1,Sum2,sum1.mean(),sum2.mean(),sumd1,sumd2,sum1)
if (sum1.all != sum2.all):
   print("Not Magic")
else:
    print("Magic")
