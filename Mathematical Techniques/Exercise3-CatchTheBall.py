#%% 
import numpy as np
import matplotlib.pyplot as plt
import math as m

# def findDistance(y0, yend, v0, theta):
#     vx = v0 * np.cos(theta)
#     x = 0
#     y = y0
#     while y>yend:

def f(g, x0, n_max=100000, accuracy=0.000001):
    n = 0
    x = x0
    while n<n_max and np.abs(g(x)-x)>accuracy:
        x = g(x)
        n += 1
    if (np.abs(g(x)-x)>accuracy):
        return "Error! May be a divergent function!"
    return x

# b)
c_arr = np.linspace(0, 90, 10000)
x_arr = []
theta0 = np.pi/4
v0 = 30
x0 = 90
g = 9.8
y0 = 1.8
y = 1

ff = lambda theta : (np.tan(theta)*x0 - g/(2*v0**2*np.cos(theta)**2)*x0**2 + y0 - y)

print(f(ff, 1))
