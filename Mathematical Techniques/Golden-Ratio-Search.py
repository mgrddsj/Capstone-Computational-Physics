#%% 
import numpy as np
import matplotlib.pyplot as plt

def minima(f, xl, xu):
    d = lambda xu, xl: ((1+np.sqrt(5))/2-1)*(xu-xl)
    x1 = xl + d(xu, xl)
    x2 = xu - d(xu, xl)

    for i in range(1000):
        if f(x1) < f(x2):
            xl = x2
            x1 = xl + d(xu, xl)
            x2 = xu - d(xu, xl)
        else:
            xu = x1
            x1 = xl + d(xu, xl)
            x2 = xu - d(xu, xl)
    return x1, x2

g = lambda c: (2*c)/(4+0.8*c+c**2+0.2*c**3)
g_inverted = lambda c: -((2*c)/(4+0.8*c+c**2+0.2*c**3))

# a)
x_arr = np.linspace(0, 10, 1000)
y_arr = []
for x in x_arr:
    y_arr.append(g(x))
plt.plot(x_arr, y_arr)
plt.show()

# b)
x1,x2 = minima(g_inverted, -1, 2)
print(x1, x2)

#%% Problem 2
A = 150
AR = 6.5
Cd0 = 0.018
rho = 0.413
W = 670000
H = 10000

f_d = 