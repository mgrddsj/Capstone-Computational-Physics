#%% Imports
import numpy as np
import matplotlib.pyplot as plt

#%% 1
k = 10 # Spring constant
m = 5 # mass
n = 10 # periods
t_max = n*2*np.pi*np.sqrt(m/k)
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
v_arr = np.zeros(steps)
v_arr[0] = 100

def v_next(x, v):
    return v + (-k * x) * dt

def x_next(x, v):
    return x + v * dt

for i in range(1, steps):
    v_arr[i] = v_next(x_arr[i-1], v_arr[i-1])
    x_arr[i] = x_next(x_arr[i-1], v_arr[i-1])

plt.plot(t_arr, x_arr)
plt.show()

#%% 2
k = 10 # Spring constant
m = 5 # mass
n = 10 # periods
t_max = n*2*np.pi*np.sqrt(m/k)
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
v_arr = np.zeros(steps)
v_arr[0] = 100

def v_next(x, v):
    return v + (-k * x) * dt

def x_next(x, v):
    return x + v * dt

for i in range(1, steps):
    v_arr[i] = v_next(x_arr[i-1], v_arr[i-1])
    x_arr[i] = x_next(x_arr[i-1], v_arr[i])

plt.plot(t_arr, x_arr)
plt.show()

#%% 3
k = 10 # Spring constant
m = 5 # mass
n = 1 # periods
a = 1
t_max = n*2*np.pi*np.sqrt(m/k)
steps = 1000
dt = t_max/steps

for a in [1,3]:
    t_arr = np.linspace(0, t_max, steps)
    x_arr = np.zeros(steps)
    v_arr = np.zeros(steps)
    x_arr[0] = 5
    v_arr[0] = 100

    def v_next(x, v):
        return v + (-k * x**a) * dt

    def x_next(x, v):
        return x + v * dt

    for i in range(1, steps):
        v_arr[i] = v_next(x_arr[i-1], v_arr[i-1])
        x_arr[i] = x_next(x_arr[i-1], v_arr[i])

    plt.plot(t_arr, x_arr)
plt.legend(["a=1", "a=3"])
plt.show()

#%% 4
k = 10 # Spring constant
m = 5 # mass
n = 10 # periods
a = 1 
t_max = n*2*np.pi*np.sqrt(m/k)
steps = 1000
dt = t_max/steps

for b in [0, 1, 5, 10, 100]:
    t_arr = np.linspace(0, t_max, steps)
    x_arr = np.zeros(steps)
    v_arr = np.zeros(steps)
    x_arr[0] = 5
    v_arr[0] = 100

    def v_next(x, v):
        return v + (-k*x - b*v) / m * dt  

    def x_next(x, v):
        return x + v * dt

    for i in range(1, steps):
        v_arr[i] = v_next(x_arr[i-1], v_arr[i-1])
        x_arr[i] = x_next(x_arr[i-1], v_arr[i])

    plt.plot(t_arr, x_arr)
plt.legend(["b=0", "b=1", "b=5", "b=10", "b=100"])
plt.show()

#%% 5
k = 10 # Spring constant
m = 5 # mass
n = 10 # periods
a = 1 
b = 1
f0 = 1000
omega = np.sqrt(k/m)
t_max = n*2*np.pi*np.sqrt(m/k)
steps = 1000
dt = t_max/steps

for omega_coeff in [0.001, 0.1, 1, 10, 1000]:
    t_arr = np.linspace(0, t_max, steps)
    x_arr = np.zeros(steps)
    v_arr = np.zeros(steps)
    x_arr[0] = 5
    v_arr[0] = 100

    def v_next(x, v, t):
        return v + (-k*x - b*v + f0*np.sin(omega*omega_coeff*t)) / m * dt

    def x_next(x, v):
        return x + v * dt

    for i in range(1, steps):
        v_arr[i] = v_next(x_arr[i-1], v_arr[i-1], t_arr[i-1])
        x_arr[i] = x_next(x_arr[i-1], v_arr[i])

    plt.plot(t_arr, x_arr)
plt.legend(["0.001Ω", "0.1Ω", "1Ω", "10Ω", "1000Ω"])
plt.show()

#%% 6
m = 10
l = 10
g = 9.8
t_max = 100
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
theta_arr = np.zeros(steps)
theta_arr[0] = 40*2*np.pi/360
omega_arr = np.zeros(steps)
omega_arr[0] = 0

def omega_next(theta, omega):
    return omega - g/l*np.sin(theta)*dt

def theta_next(theta, omega):
    return theta + omega*dt

for i in range(1, steps):
    omega_arr[i] = omega_next(theta_arr[i-1], omega_arr[i-1])
    theta_arr[i] = theta_next(theta_arr[i-1], omega_arr[i])

def findZeroesIndex(arr, start):
    for i in range(start, len(arr)):
        if ((arr[i] < 0 and arr[i-1] > 0) or (arr[i]>0 and arr[i-1] < 0)):
            return i

def findPeriod(arr):
    return [findZeroesIndex(arr, 1), findZeroesIndex(arr, findZeroesIndex(arr, 1) + 1)]

indexes = findPeriod(theta_arr)
period = ((t_arr[indexes[1]]+t_arr[indexes[1]-1])/2 - (t_arr[indexes[0]]+t_arr[indexes[0]-1])/2) * 2
print("Period = {}".format(period))
plt.plot(t_arr, theta_arr)
plt.show()

#%% 6.1
m = 10
l = 10
g = 9.8
t_max = 100
steps = 1000
dt = t_max/steps

theta0_arr = np.linspace(1*2*np.pi/360, 90*2*np.pi/360, steps)
period_arr = np.zeros(steps)

def omega_next(theta, omega):
    return omega - g/l*np.sin(theta)*dt

def theta_next(theta, omega):
    return theta + omega*dt

def findZeroesIndex(arr, start):
    for i in range(start, len(arr)):
        if ((arr[i] < 0 and arr[i-1] > 0) or (arr[i]>0 and arr[i-1] < 0)):
            return i

def findPeriod(arr):
    return [findZeroesIndex(arr, 1), findZeroesIndex(arr, findZeroesIndex(arr, 1) + 1)]

for i in range(len(theta0_arr)):
    t_arr = np.linspace(0, t_max, steps)
    theta_arr = np.zeros(steps)
    theta_arr[0] = theta0_arr[i]
    omega_arr = np.zeros(steps)
    omega_arr[0] = 0

    for i in range(1, steps):
        omega_arr[i] = omega_next(theta_arr[i-1], omega_arr[i-1])
        theta_arr[i] = theta_next(theta_arr[i-1], omega_arr[i])

    indexes = findPeriod(theta_arr)
    period = ((t_arr[indexes[1]]+t_arr[indexes[1]-1])/2 - (t_arr[indexes[0]]+t_arr[indexes[0]-1])/2) * 2
    print(period)
    period_arr[i] = period

plt.plot(theta0_arr, period_arr)
plt.show()