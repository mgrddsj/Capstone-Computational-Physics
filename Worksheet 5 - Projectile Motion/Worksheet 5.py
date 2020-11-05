#%% Worksheet 5
import numpy as np
import matplotlib.pyplot as plt

#%% B.1
x0 = 0
y0 = 0
v0 = 700
g = 9.8
theta = np.pi/6
t_max = 2*(v0*np.sin(theta)/g)
steps = 1000
bm = 4 * 10 ** -5 # b/m

# Using Euler's method 
dt = t_max/steps
t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
y_arr = np.zeros(steps)
vx_arr = np.zeros(steps)
vy_arr = np.zeros(steps)

x_arr[0] = x0
y_arr[0] = y0
vx_arr[0] = v0 * np.cos(theta)
vy_arr[0] = v0 * np.sin(theta)

def distance_next(x, vx):
    return x + vx*dt

def vx_next(vx, vy = 0, airDrag = False):
    if airDrag:
        return vx - (bm*np.sqrt(vx**2+vy**2)*vx)*dt
    return vx

def vy_next(vy, vx=0, airDrag=False):
    if airDrag:
        return vy - g * dt - (bm*np.sqrt(vx**2+vy**2)*vy)*dt
    return vy - g * dt
    
for i in range(1, steps):
    vx_arr[i] = vx_next(vx_arr[i-1])
    vy_arr[i] = vy_next(vy_arr[i-1])
    x_arr[i] = distance_next(x_arr[i-1], vx_arr[i])
    y_arr[i] = distance_next(y_arr[i-1], vy_arr[i])

# Find the domain
def findDomainIndex(arr):
    for i in range(len(arr)):
        if (arr[i] < 0):
            return i

# Find the range
def findRange(arr):
    max = 0
    for i in arr:
        if (i > max):
            max = i
    return max

print("Range: {}".format(findRange(y_arr)))
domain = findDomainIndex(y_arr)

# Find the exact solution
x_true_arr = np.zeros(steps)
y_true_arr = np.zeros(steps)
for i in range(steps):
    _t = t_arr[i]
    x_true_arr[i] = v0*np.cos(theta)*_t
    y_true_arr[i] = (v0*np.sin(theta)*_t)-(g*(_t**2)/2)

plt.plot(x_arr[:domain], y_arr[:domain], x_true_arr[:domain], y_true_arr[:domain])
plt.title("Cannon shell trajectory ignoring air drag")
plt.legend(["Euler's method", "Exact"])
plt.show()

#%% B.2 
x0 = 0
y0 = 0
v0 = 700
g = 9.8
theta = 1
t_max = 2*(v0*np.sin(theta)/g)
steps = 1000
bm = 4 * 10 ** -5 # b/m

dt = t_max/steps
t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
y_arr = np.zeros(steps)
vx_arr = np.zeros(steps)
vy_arr = np.zeros(steps)

x_arr[0] = x0
y_arr[0] = y0
vx_arr[0] = v0 * np.cos(theta)
vy_arr[0] = v0 * np.sin(theta)

def distance_next(x, vx):
    return x + vx*dt

def vx_next(vx, vy = 0, airDrag = False):
    if airDrag:
        return vx - (bm*np.sqrt(vx**2+vy**2)*vx)*dt
    return vx

def vy_next(y, vy, vx=0, airDrag=False):
    G = 6.673*10**-11 # Gravitational constant
    M = 5.972*10**24 # Mass of Earth
    _g = G*M/((y+6371000)**2)
    if airDrag:
        return vy - _g * dt - (bm*np.sqrt(vx**2+vy**2)*vy)*dt
    return vy - _g * dt
    
for i in range(1, steps):
    vx_arr[i] = vx_next(vx_arr[i-1])
    vy_arr[i] = vy_next(y_arr[i-1], vy_arr[i-1])
    x_arr[i] = distance_next(x_arr[i-1], vx_arr[i])
    y_arr[i] = distance_next(y_arr[i-1], vy_arr[i])

# Find the domain
def findDomainIndex(arr):
    for i in range(len(arr)):
        if (arr[i] < 0):
            return i

# Find the range
def findRange(arr):
    max = 0
    for i in arr:
        if (i > max):
            max = i
    return max

print("Range: {}".format(findRange(y_arr)))
domain = findDomainIndex(y_arr)

plt.plot(x_arr[:domain], y_arr[:domain])
plt.title("Cannon shell trajectory ignoring air drag with changing g")
plt.show()

#%% B.3
x0 = 0
y0 = 0
v0 = 700
g = 9.8
theta = 1
t_max = 2*(v0*np.sin(theta)/g)
steps = 1000
bm = 4 * 10 ** -5 # b/m

dt = t_max/steps
t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
y_arr = np.zeros(steps)
vx_arr = np.zeros(steps)
vy_arr = np.zeros(steps)

x_arr[0] = x0
y_arr[0] = y0
vx_arr[0] = v0 * np.cos(theta)
vy_arr[0] = v0 * np.sin(theta)

def distance_next(x, vx):
    return x + vx*dt

def vx_next(vx, vy = 0, airDrag = False):
    if airDrag:
        return vx - (bm*np.sqrt(vx**2+vy**2)*vx)*dt
    return vx

def vy_next(y, vy, vx=0, airDrag=False):
    G = 6.673*10**-11 # Gravitational constant
    M = 5.972*10**24 # Mass of Earth
    _g = G*M/((y+6371000)**2)
    if airDrag:
        return vy - _g * dt - (bm*np.sqrt(vx**2+vy**2)*vy)*dt
    return vy - _g * dt
    
for i in range(1, steps):
    vx_arr[i] = vx_next(vx_arr[i-1], vy_arr[i-1], True)
    vy_arr[i] = vy_next(y_arr[i-1], vy_arr[i-1], vx_arr[i-1], True)
    x_arr[i] = distance_next(x_arr[i-1], vx_arr[i])
    y_arr[i] = distance_next(y_arr[i-1], vy_arr[i])

# Find the domain
def findDomainIndex(arr):
    for i in range(len(arr)):
        if (arr[i] < 0):
            return i

# Find the range
def findRange(arr):
    max = 0
    for i in arr:
        if (i > max):
            max = i
    return max

print("Range: {}".format(findRange(y_arr)))
domain = findDomainIndex(y_arr)

plt.plot(x_arr[:domain], y_arr[:domain])
plt.title("Cannon shell trajectory with air drag with changing g")
plt.show()

#%% B.3 with air density changing 
x0 = 0
y0 = 0
v0 = 700
g = 9.8
theta = 1
t_max = 2*(v0*np.sin(theta)/g)
steps = 1000
bm = 4 * 10 ** -5 # b/m

dt = t_max/steps
t_arr = np.linspace(0, t_max, steps)
x_arr = np.zeros(steps)
y_arr = np.zeros(steps)
vx_arr = np.zeros(steps)
vy_arr = np.zeros(steps)

x_arr[0] = x0
y_arr[0] = y0
vx_arr[0] = v0 * np.cos(theta)
vy_arr[0] = v0 * np.sin(theta)

def distance_next(x, vx):
    return x + vx*dt

def vx_next(y, vx, vy = 0, airDrag = False):
    rr0 = 1.225*np.exp(-y/1.0*10**4) # rho/rho0
    if airDrag:
        return vx - (bm*np.sqrt(vx**2+vy**2)*vx)*dt*rr0
    return vx

def vy_next(y, vy, vx=0, airDrag=False):
    G = 6.673*10**-11 # Gravitational constant
    M = 5.972*10**24 # Mass of Earth
    _g = G*M/((y+6371000)**2)
    rr0 = 1.225*np.exp(-y/1.0*10**4) # rho/rho0
    if airDrag:
        return vy - _g * dt - (bm*np.sqrt(vx**2+vy**2)*vy)*dt*rr0
    return vy - _g * dt
    
for i in range(1, steps):
    vx_arr[i] = vx_next(y_arr[i-1], vx_arr[i-1], vy_arr[i-1], True)
    vy_arr[i] = vy_next(y_arr[i-1], vy_arr[i-1], vx_arr[i-1], True)
    x_arr[i] = distance_next(x_arr[i-1], vx_arr[i])
    y_arr[i] = distance_next(y_arr[i-1], vy_arr[i])

# Find the domain
def findDomainIndex(arr):
    for i in range(len(arr)):
        if (arr[i] < 0):
            return i

# Find the range
def findRange(arr):
    max = 0
    for i in arr:
        if (i > max):
            max = i
    return max

print("Range: {}".format(findRange(y_arr)))
domain = findDomainIndex(y_arr)

plt.plot(x_arr[:domain], y_arr[:domain])
plt.title("Cannon shell trajectory with air drag with changing g and air density")
plt.show()
