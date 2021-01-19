#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#%% a)
x_list = np.linspace(0, 1, 10000)
p_list = []

p = lambda x: 924*(x**6) - 2772*(x**5) + 3150*(x**4) - 1680*(x**3) + 420*(x**2) - 42*x + 1
pd = lambda x: 5544*(x**5) - 13860*(x**4) + 12600*(x**3) - 5040*(x**2) + 840*x - 42

for x in x_list:
    p_list.append(p(x))

plt.plot(x_list, p_list)
plt.show()

#%% b)
def solve(f, fd, x0, n_max=100000, accuracy=0.00000000001):
    n = 0
    x = x0
    while n<n_max and np.abs(f(x)-0)>accuracy:
        x = x - (f(x)/fd(x))
        n += 1
    if (np.abs(f(x)-x)>accuracy):
        return "Error! May be a divergent function!"
    return x

print(solve(p, pd, 0.5))

#%% b) experiemental
x = sp.symbols('x')
pp = 924*(x**6) - 2772*(x**5) + 3150*(x**4) - 1680*(x**3) + 420*(x**2) - 42*x + 1
ppd = sp.diff(pp)

def solve(f, fd, x0, n_max=100000, accuracy=0.00000000001):
    n = 0
    xx = x0
    while n<n_max and np.abs(np.float(f.evalf(subs= {x:xx}))-0)>accuracy:
        xx = xx - np.float(f.evalf(subs= {x:xx})) / np.float(fd.evalf(subs= {x:xx}))
        n += 1
    if np.abs(np.float(f.evalf(subs= {x:xx}))-0)>accuracy:
        return "Error! May be a divergent function!"
    return xx

print(solve(pp, ppd, 0.6))