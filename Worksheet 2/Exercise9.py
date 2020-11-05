# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:57:09 2020

@author: Jesse
@title: Exercise 9
"""

import numpy as np
import matplotlib.pyplot as plt

# a
def gvalue(x, n):
    return np.sin(x)/(x**n)

# b
x_list = np.linspace(-5, 5, 10000)
n1_list = []
n2_list = []
n3_list = []

for x in x_list:
    n1_list.append(gvalue(x, 1))
    n2_list.append(gvalue(x, 2))
    n3_list.append(gvalue(x, 3))
    
plt.plot(x_list, n1_list, x_list, n2_list, x_list, n3_list)
plt.legend(["n=1", "n=2", "n=3"])
plt.show()

# c
plt.plot(x_list, n1_list, x_list, n2_list, x_list, n3_list)
plt.ylim([-10, 10])
plt.show()