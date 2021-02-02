#%% Locate the maximum of the humps function
import random

humps_func = lambda x: 1/((x-0.3)**2+0.01)+1/((x-0.9)**2+0.04)-6

maximum = humps_func(0)

for i in range(0, 1000000):
    randnum = random.uniform(0, 2)
    if humps_func(randnum) > maximum:
        maximum = humps_func(randnum)
    
print(maximum)

#%% two-dimensional function
two_dimen_func = lambda x,y: y-x-2*x**2-2*x*y-y**2

maximum = two_dimen_func(-2, 1)
x = -2
y = 1

for i in range(0, 1000000):
    randx = random.uniform(-2, 2)
    randy = random.uniform(1, 3)
    if two_dimen_func(randx, randy) > maximum:
        maximum = two_dimen_func(randx, randy)
        x = randx
        y = randy
    
print("maximum", maximum)
print("x", x)
print("y", y)