import numpy as np
from vpython import *

ball = sphere(pos=vector(0, 0.1, 0), radius=0.1, color=color.white)
floor = box(pos=vector(0, 0, 0), size=vector(1, 0.05, 1), color=color.blue)

ball.velocity = vector(0, 5, 0)
ball.mass = 0.5
ball.p = ball.velocity*ball.mass
g = vector(0, -9.8, 0)
c = 2
rho = 1.2
A = np.pi*ball.radius**2
Fnet = (g*ball.mass - 0.5*rho*c*A*mag(ball.p/ball.mass)**2*ball.p/mag(ball.p))
t_max = 100
steps = 100000
dt = t_max/steps
t = 0

posgraph = gcurve(color=color.green)

while t<t_max:
    rate(1000)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    ball.p = ball.p + Fnet*dt
    t = t + dt

    posgraph.plot(pos=(t, ball.pos.y))

    if (ball.pos.y - (floor.pos.y + ball.radius))<0.001:
        ball.p = -ball.p
