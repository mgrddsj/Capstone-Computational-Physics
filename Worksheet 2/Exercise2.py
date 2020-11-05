# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:55:19 2020

@author: Jesse
@title: Exercise 2
"""

import numpy as np
import matplotlib.pyplot as plt

def x_1(x, a):
    return (x+a/x)/2

def error(x_new, x_old):
    return np.abs((x_new-x_old)/x_new)

# a
count = 0
a = 10
x = 5
while error(x_1(x, a), x) > 0.1:
    count = count + 1
    x = x_1(x, a)
    
print(x)


# b
a_list = np.linspace(1, 1e10)
count_list = []
for a in a_list:
    count = 0
    x = 1
    while error(x_1(x, a), x) > 0.1:
        count = count + 1
        x = x_1(x, a)
    count_list.append(count)

#print(a_list)
#print(count_list)

plt.semilogx(a_list, count_list)
plt.show()
