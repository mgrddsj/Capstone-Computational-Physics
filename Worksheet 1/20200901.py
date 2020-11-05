# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

v0 = 5
g = 9.81
t = np.linspace(0,1,1001)
y = v0*t - 0.5*g*t**2

plt.plot(t, y, '+')
plt.show()