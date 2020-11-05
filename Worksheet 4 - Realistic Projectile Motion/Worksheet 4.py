#%% 2.3
import numpy as np
import matplotlib.pyplot as plt

# Main program
p = 400
m = 70
v0 = 4
h = 1.5
c = 1 # "C approximately equal to 1"
rho = 1.2754 # Density of air
# rho = 997 # Density of water
a = 0.33 # Frontal area
eta = 2 * 10 **-5
t_max = 20
steps = 1000

dt = t_max/steps
t_list = np.linspace(0, t_max, steps)

def v_next(v):
    return v + (p/(m*v))*dt - (c*rho*a*(v**2))/(2*m) *dt - eta*a*(v/h)

def calc_v_list(_eta, _rho):
    global eta
    global rho
    eta = _eta
    rho = _rho
    v = v0
    v_list = []
    for i in t_list:
        v_list.append(v)
        v = v_next(v)
    return v_list
    

plt.figure(1)
plt.plot(t_list, calc_v_list(2*10**-5, 1.2754))
plt.show()
plt.figure(2)
plt.plot(t_list, calc_v_list(1*10**-3, 997))
plt.show()

#%% 2.4
