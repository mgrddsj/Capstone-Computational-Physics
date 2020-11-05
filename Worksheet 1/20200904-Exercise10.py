# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:17:06 2020

@author: Jesse
@title: Exercise 10: Plot a wave packet
"""

import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 1001)

def f(x, t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

plt.plot(x, f(x, 0))
plt.show()