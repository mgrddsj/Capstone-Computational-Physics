import random as rand
import numpy as np
import scipy as sci
from scipy import integrate
from vpython import *
from ThreeBodyMotionSolver import *
from timeit import default_timer as timer
import threading

# Prepare variables
# Define masses
m1=1.1 #First ball
m2=0.907 #Second ball
m3=1.3 #Third ball
# Define initial position vectors
r1=[-0.5,0,0] #m
r2=[0.5,0,0] #m
r3=[0,1,0] #m

# Prepare functions for GUI
running = False

def run(b):
    global running
    running = not running
    if running: b.text = "⏸"
    else: b.text = "▶️"

def setspeed(s):
    global i 
    i = int(s.value)
    text.text = '{}'.format(i)
    sphere1.pos = vector(r1_sol[i,0],r1_sol[i,1],r1_sol[i,2])
    sphere2.pos = vector(r2_sol[i,0],r2_sol[i,1],r2_sol[i,2])
    sphere3.pos = vector(r3_sol[i,0],r3_sol[i,1],r3_sol[i,2])

def generate(b): 
    print("started re-generating")
    # Disable all buttons first
    slider.disabled = True
    play_button.disabled = True
    running = False
    # Clear trails
    trail1.clear()
    trail2.clear()
    trail3.clear()

    start = timer()
    r1_sol, r2_sol, r3_sol = solveThreeBodyMotion(m1, m2, m3, r1, r2, r3)
    end = timer()
    print("finished calculating, time elapsed:", (end-start))
    sphere1.pos = vector(r1_sol[0,0],r1_sol[0,1],r1_sol[0,2])
    sphere2.pos = vector(r2_sol[0,0],r2_sol[0,1],r2_sol[0,2])
    sphere3.pos = vector(r3_sol[0,0],r3_sol[0,1],r3_sol[0,2])
    scene.center = vector(0,0,0) # Reset camera
    scene.autoscale = False

    for i in range(0, 50000, 35):
        trail1.append(vector(r1_sol[i][0], r1_sol[i][1], r1_sol[i][2]))
        trail2.append(vector(r2_sol[i][0], r2_sol[i][1], r2_sol[i][2]))
        trail3.append(vector(r3_sol[i][0], r3_sol[i][1], r3_sol[i][2]))

    print("finished re-generating")
    slider.disabled = False
    play_button.disabled = False
    running = True

# functions for vpython widgets
def setm1(m): m1 = m
def setm2(m): m2 = m
def setm3(m): m3 = m
def setr1x(i): r1[0] = i
def setr1y(i): r1[1] = i
def setr1z(i): r1[2] = i
def setr2x(i): r2[0] = i
def setr2y(i): r2[1] = i
def setr2z(i): r2[2] = i
def setr3x(i): r3[0] = i
def setr3y(i): r3[1] = i
def setr3z(i): r3[2] = i

# Construct GUI
scene = canvas(background=vector(225/255, 226/255, 225/255), width=800, height=600, center=vector(0,0,0))
play_button = button(text="⏸", pos=scene.caption_anchor, bind=run, disabled = True)
slider = slider(min=0, max=19999, value=1, length=700, bind=setspeed, right=15, step=1, disabled = True)
text = wtext(text='{}'.format(slider.value))
mass1text = wtext(text="m1:", pos=scene.title_anchor)
mass1input = winput(prompt="m1:", text=1.1, pos=scene.title_anchor, bind=setm1)
mass2text = wtext(text="m2:", pos=scene.title_anchor)
mass2input = winput(prompt="m2:", text=0.907, pos=scene.title_anchor, bind=setm1)
mass3text = wtext(text="m3:", pos=scene.title_anchor)
mass3input = winput(prompt="m3:", text=1.3, pos=scene.title_anchor, bind=setm1)
wtext(text="ball1:blue ball2:red ball3:green", pos=scene.title_anchor)
scene.append_to_title("\n")
wtext(text="r1: x:", pos=scene.title_anchor)
r1xinput = winput(prompt="r1.x:", text=-0.5, pos=scene.title_anchor, bind=setr1x)
wtext(text="y:", pos=scene.title_anchor)
r1yinput = winput(prompt="r1.y:", text=0, pos=scene.title_anchor, bind=setr1y)
wtext(text="z:", pos=scene.title_anchor)
r1zinput = winput(prompt="r1.z:", text=0, pos=scene.title_anchor, bind=setr1z)
scene.append_to_title("\n")
wtext(text="r2: x:", pos=scene.title_anchor)
r2xinput = winput(prompt="r2.x:", text=0.5, pos=scene.title_anchor, bind=setr2x)
wtext(text="y:", pos=scene.title_anchor)
r2yinput = winput(prompt="r2.y:", text=0, pos=scene.title_anchor, bind=setr2y)
wtext(text="z:", pos=scene.title_anchor)
r2zinput = winput(prompt="r2.z:", text=0, pos=scene.title_anchor, bind=setr2z)
scene.append_to_title("\n")
wtext(text="r3: x:", pos=scene.title_anchor)
r3xinput = winput(prompt="r3.x:", text=0, pos=scene.title_anchor, bind=setr3x)
wtext(text="y:", pos=scene.title_anchor)
r3yinput = winput(prompt="r3.y:", text=1, pos=scene.title_anchor, bind=setr3y)
wtext(text="z:", pos=scene.title_anchor)
r3zinput = winput(prompt="r3.z:", text=0, pos=scene.title_anchor, bind=setr3z)


print("Started calculating")
start = timer()
r1_sol, r2_sol, r3_sol = solveThreeBodyMotion(m1, m2, m3, r1, r2, r3)
end = timer()
print("finished calculating, time elapsed:", (end-start))

# Vpython parts
sphere1 = sphere(pos=vector(r1_sol[0,0],r1_sol[0,1],r1_sol[0,2]), radius=0.1, color=color.blue)
sphere2 = sphere(pos=vector(r2_sol[0,0],r2_sol[0,1],r2_sol[0,2]), radius=0.1, color=color.red, shininess=0.8, texture=textures.metal)
sphere3 = sphere(pos=vector(r3_sol[0,0],r3_sol[0,1],r3_sol[0,2]), radius=0.12, color=color.green, shininess=0.5, texture=textures.metal)
trail1 = curve(radius=0.005, color=color.blue)
trail2 = curve(radius=0.005, color=color.red)
trail3 = curve(radius=0.005, color=color.green)
def set_trail_visibility(c):
    trail1.visible = c.checked
    trail2.visible = c.checked
    trail3.visible = c.checked
trailcheckbox = checkbox(text="Show Trails", pos=scene.caption_anchor, bind=set_trail_visibility, checked=True)
scene.autoscale = False

for i in range(0, 50000, 35):
    trail1.append(vector(r1_sol[i][0], r1_sol[i][1], r1_sol[i][2]))
    trail2.append(vector(r2_sol[i][0], r2_sol[i][1], r2_sol[i][2]))
    trail3.append(vector(r3_sol[i][0], r3_sol[i][1], r3_sol[i][2]))
    
print("ready")
generate_button = button(text="Generate", pos=scene.title_anchor, bind=generate)
slider.disabled = False
play_button.disabled = False
running = True

i = 1
while True:
    if i<len(r1_sol) and running:
        rate(1000)
        sphere1.pos = vector(r1_sol[i,0],r1_sol[i,1],r1_sol[i,2])
        sphere2.pos = vector(r2_sol[i,0],r2_sol[i,1],r2_sol[i,2])
        sphere3.pos = vector(r3_sol[i,0],r3_sol[i,1],r3_sol[i,2])
        slider.value = i
        text.text = '{}'.format(i)
        i += 1