#%% Imports
import numpy as np
import matplotlib.pyplot as plt

#%%
m = 80
f = 400
rho = 1.293
a = 0.45
cd = 1.2
w = 0
t_max = 10
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
v_arr = np.zeros(steps)
x_arr = np.zeros(steps)

def next_v(x, v):
    return v + ((f - (1/2)*rho*cd*a*(v-w)**2)/m)*dt

def next_x(x, v):
    return x + v*dt

for i in range(1, steps):
    v_arr[i] = next_v(x_arr[i-1], v_arr[i-1])
    x_arr[i] = next_x(x_arr[i-1], v_arr[i-1])

plt.plot(t_arr, x_arr)
plt.subplots(1)
plt.plot(t_arr, v_arr)
plt.show()

# Find race time for 100m race
def find_x_index(x, arr):
    for i in range(len(arr)):
        if (arr[i] > x):
            return i

print("It takes ", t_arr[find_x_index(100, x_arr)], " seconds for 100m race.")

print("Theoretical maximum velocity: ", np.max(v_arr))

#%% h
m = 80
f = 400
rho = 1.293
a = 0.45
cd = 1.2
w = 1
tc = 0.67
fc = 488
fv = 25.8
t_max = 10
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
v_arr = np.zeros(steps)
x_arr = np.zeros(steps)
a_arr = np.zeros(steps)

def f_c(t):
    return fc * np.exp(-(t/tc)**2)

def A(t):
    return a - 0.25*a*np.exp(-(t/tc)**2)

def d(v, t):
    return (1/2)*A(t)*rho*cd*(v-w)**2

def acceleration(v, t):
    return (f + f_c(t) - fv - d(v,t))/m

def next_v(x, v, t):
    return v + ((f + f_c(t) - fv - d(v,t))/m)*dt

def next_x(x, v):
    return x + v*dt

for i in range(1, steps):
    a_arr[i] = acceleration(v_arr[i-1], t_arr[i-1])
    v_arr[i] = next_v(x_arr[i-1], v_arr[i-1], t_arr[i-1])
    x_arr[i] = next_x(x_arr[i-1], v_arr[i-1])

plt.plot(t_arr, x_arr)
plt.subplots()
plt.plot(t_arr, v_arr)
plt.subplots()
plt.plot(t_arr, a_arr)
plt.show()

# Find race time for 100m race
def find_x_index(x, arr):
    for i in range(len(arr)):
        if (arr[i] > x):
            return i

print("It takes ", t_arr[find_x_index(100, x_arr)], " seconds for 100m race.")

print("Theoretical maximum velocity: ", np.max(v_arr))


#%%
