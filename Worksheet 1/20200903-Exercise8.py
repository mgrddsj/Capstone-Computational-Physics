# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:11:44 2020

@author: Jesse
@title: Exercise 8: The sunflower
"""

import math
import numpy as np
import matplotlib.pyplot as plt

fi = ((1+np.sqrt(5))/2)
s = np.linspace(1, 500,500)
r = np.sqrt(s)
theta = 2*np.pi*s/fi

plt.polar(theta, r, 'o')
plt.show()