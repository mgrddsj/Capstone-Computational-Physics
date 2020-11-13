from math import cos
import vpython
import numpy as np

sun = vpython.sphere(pos=vpython.vector(0, 0, 0), radius=695500)
saturn = vpython.sphere(pos=vpython.vector(0, 1433400000, 0), radius=57316e6)
# for theta in np.arange(0, 100000*np.pi, 0.1):
#     vpython.rate(500)
#     x = np.cos(theta)
#     y = np.sin(theta)
#     s.pos = vpython.vector(x, y, 0)