# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:19:52 2020

@author: Jesse
@title: Exercise 7: Lennard-Jones potential
"""

import math
import numpy as np
import matplotlib.pyplot as plt

sigma = 3.4e-10
epsilon = 1.65e-21
r_0 = 2**(1/6)*sigma

r = np.linspace(r_0*0.9, r_0*1.1, 1000)
u = 4*epsilon*((sigma/r)**12-(sigma/r)**6)

# a
plt.plot(r, u)
plt.title("U(r)")
plt.show()

# b 
f = 24*epsilon*sigma**6*((2*sigma**6)/(r**13)-(1/(r**7)))
plt.plot(r, f)
plt.show()

# c 
v_0 = -epsilon
v = v_0+(1/2)*(24*epsilon*sigma**6*((26*sigma**6-7*r_0**6)/(r_0**14)))*(r-r_0)**2

plt.plot(r, v)
plt.show()