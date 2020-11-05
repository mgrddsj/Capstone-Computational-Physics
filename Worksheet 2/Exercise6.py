# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:19:42 2020

@author: Jesse
@title: Exercise 6
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# a
def v(x, mu, exp):
    return [1-np.exp(x/mu), 1-np.exp(1/mu), (1-np.exp(x/mu))/(1-np.exp(1/mu))]

# b
x_list = np.linspace(0, 1, 50)
mu = 1e-3

for x in x_list:
    print(v(x, mu, math.exp))
    print(v(x, mu, np.exp))

# c
x = np.linspace(0, 1, 10000)
plt.plot(x, v(x, 1, np.exp)[2])
plt.plot(x, v(x, 0.1, np.exp)[2])
plt.plot(x, v(x, 0.01, np.exp)[2])
plt.show()