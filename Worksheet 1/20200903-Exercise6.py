# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:55:15 2020

@author: Jesse
@title: Exercise 6: Gaussian
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def g(x, sigma):
    return (1/sigma*np.sqrt(2*np.pi))*np.exp(-x**2/(2*sigma**2))

x = np.linspace(-5, 5, 100)

plt.plot(x, g(x, 1))
plt.plot(x, g(x, 1.5))
plt.plot(x, g(x, 2))
plt.legend(["σ=1", "σ=1.5", "σ=2"])
plt.title("Gaussian function")
plt.show()