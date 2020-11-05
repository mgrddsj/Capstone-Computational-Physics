# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:18:49 2020

@author: Jesse
@title: Exercise 1: How to cook the perfect egg
"""

import math
import numpy as np
import time

def t(t_0):
    m = 67
    rho = 1.038
    c = 3.7
    k = 5.4e-3
    t_w = 100
    t_y = 70
    t = (((m**(2/3))*c*rho**(1/3))/(k*math.pi**2*(4*math.pi/3)**(2/3))*math.log(0.76*((t_0-t_w)/(t_y-t_w))))
    return time.strftime("%M minutes and %S seconds", time.gmtime(t))

print("t for a large egg taken from the fridge is {}".format(t(4)))
print("t for a large egg taken from room temperature is {}".format(t(20)))
