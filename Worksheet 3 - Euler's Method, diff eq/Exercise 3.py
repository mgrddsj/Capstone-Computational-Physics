# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 08:32:36 2020

@author: Jesse
@title: Exercise 3
"""

#%%
import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 0.01
n0 = 1000
t_max = 1
steps = 1000

dt = t_max/steps
t_list = np.linspace(0, t_max, steps)
n_list = []

def n_next(n_now):
    if (n_now + (a - b * n_now) * n_now < 0):
        return 0
    return n_now + (a - b * n_now) * n_now * dt

n = n0
for t in t_list:
    n_list.append(n)
    n = n_next(n)
    
plt.plot(t_list, n_list)
plt.title("Population growth")
plt.show()