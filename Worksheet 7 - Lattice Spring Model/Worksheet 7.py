#%% Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#%% C
x0 = 5
y0 = 10
l0 = 10
m = 5
t_max = 100
steps = 1000
dt = t_max/steps

t_arr = np.linspace(0, t_max, steps)
vx_arr = np.zeros(steps)
vy_arr = np.zeros(steps)
x_arr = np.zeros(steps)
y_arr = np.zeros(steps)
x_arr[0] = x0
y_arr[0] = y0

def vx_next(x, vx, k):
    return vx + ((-2*k*x)/m)*dt

def x_next(x, vx):
    return x + vx*dt

images = []

for i in range(1, steps):
    vx_arr[i] = vx_next(x_arr[i-1], vx_arr[i-1], 1)
    vy_arr[i] = vx_next(y_arr[i-1], vy_arr[i-1], 2)
    x_arr[i] = x_next(x_arr[i-1], vx_arr[i])
    y_arr[i] = x_next(y_arr[i-1], vy_arr[i])

# plt.plot(x_arr, y_arr)
# plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-10, 10))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = x_arr[:i]
    y = y_arr[:i]
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=20, blit=True)

anim.save('pic.gif', writer='imagemagick')

#%% A
#problem setup#
L0 = 1
k = 1
m = 1

#Euler setup#
right = 10000
interval = right * 1
t = np.linspace(0, right, interval+1)
dt = right/interval
x = np.zeros(len(t))
y = np.zeros(len(t))
vx = np.zeros(len(t))
vy = np.zeros(len(t))

#initial points#
x[0] = 1
y[0] = 0
vx[0] = 2
vy[0] = 2

#Euler method#
for i in range(0, interval, 1):
    vx[i+1] = vx[i] + (- k * ((x[i]**2 + y[i]**2) ** (1/2) - L0) * x[i] / ((x[i]**2 + y[i]**2) ** (1/2))) * dt
    x[i+1] = x[i] + vx[i+1] * dt
    vy[i+1] = vy[i] + (- k * ((x[i]**2 + y[i]**2) ** (1/2) - L0) * y[i] / ((x[i]**2 + y[i]**2) ** (1/2))) * dt
    y[i+1] = y[i] + vy[i+1] * dt

# plt.plot(x, y)
# plt.axis('equal')

fig = plt.figure()
ax = plt.axes(xlim=(-6, 6), ylim=(-4, 4)) # Set x and y limit. Change according to your graph. 
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    # Generates a graph for current i. Change x and y to your x and y data list. 
    _x = x[:i] 
    _y = y[:i]
    line.set_data(_x, _y) 
    return line,

# Change frame and interval according to your data. 
# frames should be the length of your data array. 
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10000, interval=10, blit=True) 

anim.save('10000.gif', writer='imagemagick')