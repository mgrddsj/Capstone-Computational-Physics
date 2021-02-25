#%%
import numpy as np

N = 100000000
D = 4 # Dimensions
points = 2*np.random.random((N, D)) - 1
m = np.sum(np.linalg.norm(points, axis=1) <= 1)
print(m/N*(2**D))

#%%
import numpy as np
import math
def AccurateVHypersphere(n, R):
    print(np.pi**(n / 2)*R**n / math.gamma(n/2 + 1))

AccurateVHypersphere(4, 1)
