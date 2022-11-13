import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate

L = np.pi
print(type(np.pi))

x = np.arange(-L, L, 0.01)

y = abs(x)


def fc(x): return abs(x)*cos(i*x)


def fs(x): return abs(x)*sin(i*x)


n = 20
An = []
Bn = []
sum = 0

for i in range(n):
    an = integrate.quad(fc, -L, L)
    p, q = an
    An.append(p*(1.0/L))

for i in range(n):
    bn = integrate.quad(fs, -L, L)
    p, q = bn
    Bn.append(p*(1.0/L))


for i in range(n):
    if i == 0.0:
        sum = sum+An[i]/2
    else:
        sum = sum+(An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))


plt.plot(x, sum, 'g')

plt.plot(x, y, 'r--')

plt.show()
