#%%
import numpy as np

def f(g, x0, n_max=100000, accuracy=0.000001):
    n = 0
    x = x0
    while n<n_max and np.abs(g(x)-x)>accuracy:
        x = g(x)
        n += 1
    if (np.abs(g(x)-x)>accuracy):
        return "Error! May be a divergent function!"
    return x

print(f(lambda x:2-np.exp(-x), 2))
print(f(lambda x:np.exp(1-x**2), 2))
