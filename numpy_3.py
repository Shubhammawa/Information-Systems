import numpy as np
A=np.random.rand(5,5)
print(np.concatenate((A[:1,:],A[1:2,:],A[2:3,:],A[3:4,:],A[4:,:]),axis=1)) 
