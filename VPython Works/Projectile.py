from vpython import *

ball = sphere(pos=vector(0, 0.1, 0), radius=0.1, color=color.white)
floor = box(pos=vector(0, 0, 0), size=vector(1, 0.05, 1), color=color.blue)

ball.velocity = vector(0, 5, 0)
ball.mass = 0.5
ball.p = ball.velocity*ball.mass
g = vector(0, -9.8, 0)
Fnet = g*ball.mass
t_max = 100
steps = 100000
dt = t_max/steps
t = 0

while t<t_max:
    rate(500)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    ball.p = ball.p + Fnet*dt
    t = t + dt

    if ball.pos.y < (floor.pos.y + ball.radius):
        ball.p = -ball.p
