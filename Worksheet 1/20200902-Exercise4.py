# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:51:00 2020

@author: Jesse
@title: Exercise 4: Water density
"""

import math
import numpy as np
import matplotlib.pyplot as plt

t_c = np.linspace(0, 100, 101)
rho = 5.5289e-8*(t_c**3)-8.5016e-6*(t_c**2)+6.5622e-5*t_c+0.99987

plt.plot(t_c, rho)
plt.xlabel("Temperature (C)")
plt.ylabel("Density (g/cm^3)")
plt.title("Density versus temperature of freshwater")
plt.show()