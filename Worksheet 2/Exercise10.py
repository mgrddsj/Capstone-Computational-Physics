# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:08:53 2020

@author: Jesse
@title: Exercise 10
"""

import numpy as np
import matplotlib.pyplot as plt

# a
def logistic(x, r):
    return r*x*(1-x)

# b
for r in [0.5, 1.5, 2.5, 3.2, 3.5, 3.56, 3.7]:
    x_list = []
    x = 0.5
    for i in range(1, 101):
        x_list.append(x)
        x = logistic(x, r)
        
    plt.plot(range(1, 101), x_list)
    plt.legend(['r={}'.format(r)])
    plt.show()
