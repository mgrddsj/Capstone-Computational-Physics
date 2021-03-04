#%%
import numpy as np
import matplotlib.pyplot as plt

L = -10
r = [0, 0]
f = [0, L]

rx_arr = [r[0]]
ry_arr = [r[1]]
fx_arr = [f[0]]
fy_arr = [f[1]]

theta = 90

u = 5

v = 10

vr = [u, 0]
vf = [v*np.cos(theta), v*np.sin(theta)]

dt = 0.00001
t = 0

while f[1] < 0:
    r[0] += vr[0]*dt
    f[0] += vf[0]*dt
    f[1] += vf[1]*dt
    theta = np.arctan((r[1] - f[1]) / (r[0] - f[0]))
    vf = [v*np.cos(theta), v*np.sin(theta)]
    t += dt
    rx_arr.append(r[0])
    ry_arr.append(r[1])
    fx_arr.append(f[0])
    fy_arr.append(f[1])

print(t)
plt.plot(rx_arr, ry_arr)
plt.plot(fx_arr, fy_arr)
plt.show()
