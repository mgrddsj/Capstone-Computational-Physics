# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:31:00 2020

@author: Jesse
@title: Exercise 3
"""

import numpy as np
import matplotlib.pyplot as plt

def pathlength(x, y):
    sum = 0
    for i in range(1, len(x)):
        sum += np.sqrt((x[i], x[i-1])**2 + (y[i] - y[i-1])**2)
    return sum

