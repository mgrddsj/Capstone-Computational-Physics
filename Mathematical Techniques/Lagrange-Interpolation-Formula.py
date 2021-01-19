#%% Lagrange's Interpolation Formula Implementation
import numpy as np

def L_k(x, k, xp, yp):
    product = 1 
    i = 0
    n = len(xp) - 1
    while i <= n:
        if i != k:
            product *= float(x - xp[i]) / (xp[k] - xp[i])
        i += 1
    return product


def p_L(x, xp, yp):
    sum = 0
    n = len(xp) - 1
    for k in range(n+1):
        sum += yp[k] * L_k(x,k,xp,yp)
    return sum

def test_p_L(xp, yp):
    n = len(xp) - 1
    precision = 0.00000000000001
    count = 0
    for k in range(n+1):
        if abs(p_L(xp[k],xp,yp) - yp[k]) > precision:
            count +=1
    if count == 0:
        print("The Lagrange interpolation polynomial indeed passes through all the points.")
    else:
        print("There are", count, "points where the interpolation polynomial fails to pass through.")
    
