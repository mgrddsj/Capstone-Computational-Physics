# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:37:09 2020

@author: Jesse
@title: Exercise 
"""

import numpy as np
import matplotlib.pyplot as plt

def v(t):
    if t<0:
        return 0
    elif 0<=t<=8:
        return 10*t**2-5*t
    elif 8<=t<=16:
        return 624-5*t
    elif 16<=t<=26:
        return 36*t+12*(t-16)**2
    else:
        return 2136*np.exp(-0.1*(t-26))
    
t = np.linspace(-5, 50)
v_list = []

for i in t:
    v_list.append(v(i))
    
plt.plot(t, v_list)
plt.show()