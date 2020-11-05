# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:24:55 2020

@author: Jesse
@title: Exercise 2: The sine function
"""

import math
import numpy as np

def sin(x, terms):
    result = x
    for i in range(2, terms):
        if i % 2 == 0:
            result -= (x**(2*i-1)/math.factorial(2*i-1))
        else: 
            result += (x**(2*i-1)/math.factorial(2*i-1))
    return result

def percentage_error(true, approx):
    return (true-approx)/true*100

print("""sin(0.9) = {}, 
true sin(0.9) = {}, 
percentage error: {}%""".format(sin(0.9, 9), math.sin(0.9), percentage_error(math.sin(0.9), sin(0.9, 9))))
