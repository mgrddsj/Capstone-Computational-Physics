#%% Simpson's Rule
import numpy as np

def integrate(f, a, b, n=1000):
    h = (b-a)/n
    k = 0.0
    x = a+h
    for i in range(1, int(n/2) + 1):
        k += 4*f(x)
        x += 2*h

    x = a+2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

print(integrate(lambda x: x**3, 2, 4, 1000000))