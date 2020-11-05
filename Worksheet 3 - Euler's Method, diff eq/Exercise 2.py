# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:11:24 2020

@author: Jesse
@title: Exercise 2
"""

#%%
import matplotlib.pyplot as plt
import numpy as np

n_0a = 10
n_0b = 0
tao_a = 0.5
tao_b = 0.4
t_max = 10
steps = 10000
dt = t_max / steps

t_list = np.linspace(0, t_max, steps)
n_a_list = []
n_b_list = []

def n_a_next(n_a):
    return n_a + (-n_a/tao_a)*dt

def n_b_next(n_a, n_b):
    return n_b + (n_a/tao_a - n_b/tao_b)*dt

n_a = n_0a
n_b = n_0b

for t in t_list:
    n_a_list.append(n_a)
    n_b_list.append(n_b)
    n_b = n_b_next(n_a, n_b)
    n_a = n_a_next(n_a)
    
plt.plot(t_list, n_a_list)
plt.plot(t_list, n_b_list)
plt.title("Radioactive decay using Euler's method")
plt.legend(['Na', 'Nb'])
plt.show()

# Check for errors 
def n_a_true(t):
    return n_0a * np.exp(-t/tao_a)

def n_b_true(t):
    return (n_0a*(np.exp(-t/tao_a)-np.exp(-t/tao_b)))/(((1/tao_b)-(1/tao_a))*tao_a)

n_a_true_list = []
n_b_true_list = []

for t in t_list:
    n_a_true_list.append(n_a_true(t))
    n_b_true_list.append(n_b_true(t))
    
plt.figure(1)
plt.plot(t_list, n_a_true_list)
plt.plot(t_list, n_b_true_list)
plt.title("Radioactive decay true graph")
plt.legend(['Na', 'Nb'])
plt.show()

plt.figure(2)
plt.plot(t_list, n_a_list)
plt.plot(t_list, n_a_true_list)
plt.title("Radioactive decay for Na")
plt.legend(["Na using Euler's method", "True Na"])
plt.show()

plt.figure(3)
plt.plot(t_list, n_b_list)
plt.plot(t_list, n_b_true_list)
plt.title("Radioactive decay for Nb")
plt.legend(["Nb using Euler's method", "True Nb"])
plt.show()

# Calculate the error
error_list_na = []
error_list_nb = []
for i in range(len(n_a_list)):
    error_list_na.append(n_a_true_list[i] - n_a_list[i])
    error_list_nb.append(n_b_true_list[i] - n_b_list[i])
    
plt.figure(4)
plt.plot(t_list, error_list_na)
plt.plot(t_list, error_list_nb)
plt.title("Error")
plt.legend(["Na error", "Nb error"])
plt.show()