# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:54:23 2020

@author: Jesse
@title: Nuclear decay
"""

import matplotlib.pyplot as plt
import numpy as np

lamb = 0.693
n = 100
n_true = 100
steps = 1000
t_max = 10

dt = t_max/steps
t_list = np.linspace(0, t_max, steps)
n_list = []
n_list_true = []
error_list = []

def next_n(n):
    return n - lamb*n*dt

def next_n_true(n, t):
    return n*np.exp(-lamb*t)

for t in t_list:
    n_list.append(n)
    n_list_true.append(n_true)
    error_list.append(n - n_true)
    n = next_n(n)
    n_true = next_n_true(n_true, t)
    
    
plt.plot(t_list, n_list)
plt.plot(t_list, n_list_true)
plt.legend(['calculated', 'real'])
plt.figure(0)
plt.plot(t_list, error_list)
plt.title('Error')
plt.show()