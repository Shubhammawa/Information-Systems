import numpy as np
from scipy import linalg
A = np.array([[1,8,-9,7,5],[0,1,0,4,4],[0,0,1,2,5],[0,0,0,1,-5],[0,0,0,0,1]])
det_A = linalg.det(A)
print("Determinant of the matrix\n")
print(det_A)
inv_A = linalg.pinv(A)
print("\nInverse of the matrix\n")
print(inv_A)
print("\nTranspose of the matrix\n")
transpose = np.matrix.transpose(A)
print(transpose)
eig_A = linalg.eig(A)
print("\nEigen pairs of the matrix\n")
print(eig_A)
