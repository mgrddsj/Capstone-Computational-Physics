# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:55:04 2020

@author: Jesse
@title: Exercise 7
"""

import numpy as np
import matplotlib.pyplot as plt

def s(t, n, T):
    sum = 0
    for i in range(1, n+1):
        sum += (1/(2*i-1))*np.sin(2*(2*i-1)*np.pi*t/T)
    return (4/np.pi)*sum

def f(t, T):
    if 0 < t < (T/2):
        return 1
    elif t == (T/2):
        return 0
    elif (T/2) < t < T:
        return -1
    
T = 2*np.pi
t = np.linspace(0, 10, 1000)
f_list = []

for i in t:
    f_list.append(f(i, T))

plt.plot(t, s(t, 1, T))
plt.plot(t, s(t, 3, T))
plt.plot(t, s(t, 20, T))
plt.plot(t, s(t, 200, T))
plt.plot(t, f_list)
plt.show()