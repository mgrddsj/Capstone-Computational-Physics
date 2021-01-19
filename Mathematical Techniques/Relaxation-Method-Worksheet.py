#%% Exercise 1
import numpy as np
import matplotlib.pyplot as plt

# a)
def f(g, x0, n_max=100000, accuracy=0.000001):
    n = 0
    x = x0
    while n<n_max and np.abs(g(x)-x)>accuracy:
        x = g(x)
        n += 1
    if (np.abs(g(x)-x)>accuracy):
        return "Error! May be a divergent function!"
    return x

print(f(lambda x:1-np.exp(-2*x), 1))

# b)
c_arr = np.linspace(0, 3, 30000)
x_arr = []

for c in c_arr:
    x_arr.append(f(lambda x:1-np.exp(-c*x), 1))

plt.plot(c_arr, x_arr)
plt.show()

#%% Exercise 2
import numpy as np
import matplotlib.pyplot as plt

