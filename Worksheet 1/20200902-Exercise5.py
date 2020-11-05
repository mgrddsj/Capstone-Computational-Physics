# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:20:13 2020

@author: Jesse
@title: Exercise 5: The cosine function 
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def cos(x, terms):
    result = 1
    for i in range(1, terms):
        if i % 2 == 1:
            result -= (x**(2*i)/math.factorial(2*i))
        else: 
            result += (x**(2*i)/math.factorial(2*i))
    return result

x = np.linspace(0, (3*np.pi/2), 1000)

plt.plot(x, cos(x, 5), 'k--')
plt.plot(x, np.cos(x))
plt.legend(["series expansion line", "cos(x)"])
plt.show()