#%% Trapezoidal method
import numpy as np

def integrate(f, a, b, n):
    h = (b-a)/n
    x_arr = np.linspace(a, b, n)
    sum = - (f(a) + f(b))
    for xi in x_arr:
        sum += 2*f(xi)
    return (1/2)*h*sum

print(integrate(lambda x: x**3, 2, 4, 1000000))