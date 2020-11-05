# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:08:49 2020

@author: Jesse
@title: Exercise 5
"""

import numpy as np
import matplotlib.pyplot as plt

def diff(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2*h)

print(diff(lambda x : np.exp(x), 0))
print(diff(lambda x : np.exp(-2*x**2), 0))
print(diff(lambda x : np.exp(-x), 0))
print(diff(lambda x : np.cos(x), np.pi*2))
print(diff(lambda x : np.log(x), 1))
