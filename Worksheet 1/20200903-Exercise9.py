# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:21:51 2020

@author: Jesse
@title: Exercise 9: Fitting graphs to data
"""

import math
import numpy as np
import matplotlib.pyplot as plt

l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
t = [0.6, 0.9, 1.1, 1.3, 1.4, 1.6, 1.7, 1.8, 1.9, 2.0]

coeff1 = np.polyfit(t, l, 1)
coeff2 = np.polyfit(t, l, 2)
coeff3 = np.polyfit(t, l, 3)
p1 = np.poly1d(coeff1)
p2 = np.poly1d(coeff2)
p3 = np.poly1d(coeff3)
y_fitted1 = p1(t)
y_fitted2 = p2(t)
y_fitted3 = p3(t)

plt.plot(t, l, 'o')
plt.plot(t, y_fitted1)
plt.plot(t, y_fitted2)
plt.plot(t, y_fitted3)
plt.legend(["data", "degree 1", "degree 2", "degree 3"])
plt.show()