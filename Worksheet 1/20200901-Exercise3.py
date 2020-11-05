# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:10:11 2020

@author: Jesse
@title: Exercise 3: Charge plot
"""

import math
import numpy as np
import matplotlib.pyplot as plt

q_0 = 10
r = 60
l = 9
c = 0.00005
t = np.linspace(0, 0.8, 1000)

q = q_0*np.exp((-r*t)/(2*l))*np.cos(np.sqrt((1/(l*c))-((r/(2*l))**2))*t)

plt.plot(t, q)
plt.xlabel("Time (s)")
plt.ylabel("Charge on capacitor (C)")
plt.title("The charge on the capacitor q(t) as a function of time")
plt.show()