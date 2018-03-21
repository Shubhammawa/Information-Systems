import numpy as np
import random
from sympy import *
from sympy import poly
import matplotlib.pyplot as plt
x=Symbol('x')
n = int(input("Enter the degree of the polynomial "))
def function(n):
    poly1=0
    coeff = np.random.randint(-10,10,size=n)
    for i in range(0,n):
        poly1 += coeff[i]*(x**i)
    return [poly1,coeff]
poly1 = function(n)
polynomial = poly(poly1[0])
print(poly1[0])
print(poly1[1])
derivative = diff(poly1[0],x)
print(derivative)
integral = integrate(poly1[0],x)
print(integral)

f = lambdify(x,derivative, 'numpy')
y = f(np.random.randint(-10,10,size=100))
plt.plot(f(np.random.randint(-10,10,size=100)))
plt.show()
g = lambdify(x,poly1[0])
plt.plot(g(np.random.randint(-10,10,size=100)))
plt.show()
