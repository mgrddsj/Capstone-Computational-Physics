# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 08:54:36 2020

@author: Jesse
@title: Exercise 1
"""

# %%
import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 1
v = 100
v0 = 100
t_max = 10
steps = 1000
dt = t_max / steps

t_list = np.linspace(0, t_max, steps)
v_list = []
v_list_true = []
error_list = []

def next_v(v):
    return v+(a-b*v)*dt

def v_true(t):
    return v0 * np.exp(-b*t) + (a/b)*(1-np.exp(-b*t))

for t in t_list:
    v_list.append(v)
    v_list_true.append(v_true(t))
    error_list.append(v_true(t) - v)
    v = next_v(v)
    
plt.plot(t_list, v_list)
plt.plot(t_list, v_list_true)
plt.figure(0)
plt.plot(t_list, error_list)
plt.show()