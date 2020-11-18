import numpy as np
from vpython import *

canvas(background=color.white)

g = 9.8

ball = sphere(pos=vector(5, 2, 0), radius=1, color=color.red)
pivot = vector(0, 20, 0)
roof = box(pos=pivot, size=vector(10, 0.5, 10), color=color.green)
spring = helix(pos=pivot, axis=ball.pos-pivot, radius=0.5, color=color.yellow)

t = 0
t_max = 100
steps = 10000
dt = t_max/steps

l = mag(ball.pos-pivot) # Length of pendulum
cs = (pivot.y-ball.pos.y)/l # cos(theta) 
theta = acos(cs) # Angle with vertical direction
vel = 0.0 # Angular velocity

while (t<100):
    rate(100) # Maximum 100 calculations per second
    acc = -g/l*np.sin(theta) # Updating of angular acceleration
    theta = theta+vel*dt # Updating of angular position
    vel = vel+acc*dt # Updating of angular velocity
    ball.pos = vector(l*sin(theta),pivot.y-l*cos(theta),0) # Cal. position
    spring.axis = ball.pos-spring.pos # Updating other end of rod of pendulum
    t += dt # Updating time