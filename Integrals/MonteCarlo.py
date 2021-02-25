#%%
import numpy as np

n = 10000000
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)
f = lambda x:x*(1-x)
m = 0

for _n in range(0, n):
    if f(x[_n]) > y[_n]:
        m += 1;

print(m/n)
