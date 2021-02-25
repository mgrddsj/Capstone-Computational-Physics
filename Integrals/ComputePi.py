#%%
import numpy as np

N = 100000000
points = 2*np.random.random((N, 2)) - 1
m = np.sum(np.linalg.norm(points, axis=1) <= 1)
print(m/N*4)