# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:14:54 2020

@author: Jesse
@title: Exercise 4
"""

import numpy as np
import matplotlib.pyplot as plt

def pathlength(x, y):
    sum = 0
    for i in range(1, len(x)):
        sum += np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return sum
        
print(pathlength([0, 1], [0, 1]))

for k in range(2,10):
    n = 2**k
    x = (1/2)*np.cos(2*np.pi*np.linspace(0, n, n+2)/n)
    y = (1/2)*np.sin(2*np.pi*np.linspace(0, n, n+2)/n)
    pi = pathlength(x, y)
    print(pi)
    print("Error: {}".format([(np.pi-pi)]))