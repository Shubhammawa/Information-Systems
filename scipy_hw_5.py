import numpy as np
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from scipy import special

c = [-5,2,-3]
A_ub = np.array([[-2,-2,1],[3,-4,0],[0,1,3]])
b_ub = np.array([-2,3,5])
result = optimize.linprog(c,A_ub,b_ub)
print(result.fun)

Result=[]
for i in range(0,11):
    b_ub1 = np.array([-2,i,i])
    result_i = optimize.linprog(c,A_ub,b_ub1)
    Result.append(result_i.fun)


fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 11)
Y = np.arange(0, 11)
X, Y = np.meshgrid(X, Y)
A = np.array(Result)
Z = Result
print(Z)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

    
