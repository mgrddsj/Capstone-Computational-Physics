# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:13:23 2020

@author: Jesse
@title: Exercise 8
"""

import numpy as np
import matplotlib.pyplot as plt

v_0 = int(input('v0?'))
m = int(input('m?'))
g = 9.8
t_list = np.linspace(0, 2*v_0/g, 1000)

def y(t):
    return v_0*t-(1/2)*g*t**2

def v(t):
    return v_0-g*t

p_list = []
k_list = []
pk_list = []

for t in t_list:
    p_list.append(m*g*y(t))
    k_list.append((1/2)*m*v(t)**2)
    pk_list.append(m*g*y(t)+(1/2)*m*v(t)**2)
    
plt.plot(t_list, p_list, t_list, k_list, t_list, pk_list)
plt.legend(['P', 'K', "P+K"])
plt.show()