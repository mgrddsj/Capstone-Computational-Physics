import numpy as np
from vpython import *

canvas(background=vector(225/255, 226/255, 225/255), width=1280, height=720, center=vector(0,8,0))

g = 9.8
m = 1
k = 10

ball = sphere(pos=vector(5, 2, 0), radius=1, color=vector(245/255, 245/255, 246/255))
pivot = vector(0, 20, 0)
roof = box(pos=pivot, size=vector(10, 0.5, 10), color=vector(0/255, 169/255, 240/255))
spring = helix(pos=pivot, axis=ball.pos-pivot, radius=0.5, color=vector(0/255, 124/255, 192/255))

t = 0
t_max = 100
steps = 10000
dt = t_max/steps

l = mag(ball.pos-pivot) # Length of pendulum
l0 = mag(ball.pos-pivot)
cs = (pivot.y-ball.pos.y)/l # cos(theta) 
theta = acos(cs) # Angle with vertical direction
vel = 0.0 # Angular velocity
f_el = k * (l-l0)
vel_el_x = 10
vel_el_y = 10

while (t<t_max):
    rate(200) # Maximum 100 calculations per second
    l = mag(ball.pos-pivot) # Update the length of the spring
    f_el = k * (l-l0) # Update the force of spring
    f_el_x = f_el * sin(theta)
    f_el_y = - m*g + f_el * cos(theta)
    vel_el_x += f_el_x/m * dt
    vel_el_y += f_el_y/m * dt

    acc = -g/l*sin(theta) # Updating of angular acceleration
    theta = theta+vel*dt # Updating of angular position
    vel = vel+acc*dt # Updating of angular velocity
    ball.pos = vector(l*sin(theta) + vel_el_x*dt,pivot.y-l*cos(theta) + vel_el_y*dt,0) # Cal. position
    spring.axis = ball.pos-spring.pos # Updating other end of rod of pendulum
    t += dt # Updating time