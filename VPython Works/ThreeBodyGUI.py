import random as rand
import numpy as np
import scipy as sci
from scipy import integrate
from vpython import *

# Prepare variables
# Define masses
m1=1.1 #First ball
m2=0.907 #Second ball
m3=1.3 #Third ball
# Define initial position vectors
r1=[-0.5,0,0] #m
r2=[0.5,0,0] #m
r3=[0,1,0] #m

# Construct GUI
running = True

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
canvas = canvas(background=vector(225/255, 226/255, 225/255), width=800, height=600, center=vector(0,0,0))

button = button(text="⏸", pos=canvas.caption_anchor, bind=run, disabled = True)
slider = slider(min=0, max=49999, value=1, length=700, bind=setspeed, right=15, step=1, disabled = True)
text = wtext(text='{}'.format(slider.value))

# Set mass
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
mass1text = wtext(text="m1:", pos=canvas.title_anchor)
mass1input = winput(prompt="m1:", text=1.1, pos=canvas.title_anchor, bind=setm1)
mass2text = wtext(text="m2:", pos=canvas.title_anchor)
mass2input = winput(prompt="m2:", text=0.907, pos=canvas.title_anchor, bind=setm1)
mass3text = wtext(text="m3:", pos=canvas.title_anchor)
mass3input = winput(prompt="m3:", text=1.3, pos=canvas.title_anchor, bind=setm1)
canvas.append_to_title("\n")
wtext(text="r1: x:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r1.x:", text=-0.5, pos=canvas.title_anchor, bind=setr1x)
wtext(text="y:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r1.y:", text=-0.5, pos=canvas.title_anchor, bind=setr1y)
wtext(text="z:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r1.z:", text=-0.5, pos=canvas.title_anchor, bind=setr1z)
canvas.append_to_title("\n")
wtext(text="r2: x:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r2.x:", text=-0.5, pos=canvas.title_anchor, bind=setr2x)
wtext(text="y:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r2.y:", text=-0.5, pos=canvas.title_anchor, bind=setr2y)
wtext(text="z:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r2.z:", text=-0.5, pos=canvas.title_anchor, bind=setr2z)
canvas.append_to_title("\n")
wtext(text="r3: x:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r3.x:", text=-0.5, pos=canvas.title_anchor, bind=setr3x)
wtext(text="y:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r3.y:", text=-0.5, pos=canvas.title_anchor, bind=setr3y)
wtext(text="z:", pos=canvas.title_anchor)
r1xinput = winput(prompt="r3.z:", text=-0.5, pos=canvas.title_anchor, bind=setr3z)
canvas.append_to_title("\n")


#Define universal gravitation constant
G=6.67408e-11 #N-m2/kg2
#Reference quantities
m_nd=1.989e+30 #kg #mass of the sun
r_nd=5.326e+12 #m #distance between stars in Alpha Centauri
v_nd=30000 #m/s #relative velocity of earth around the sun
t_nd=79.91*365*24*3600*0.51 #s #orbital period of Alpha Centauri
#Net constants
K1=G*t_nd*m_nd/(r_nd**2*v_nd)
K2=v_nd*t_nd/r_nd

#Convert pos vectors to arrays
r1=np.array(r1,dtype="float64")
r2=np.array(r2,dtype="float64")
r3=np.array(r3,dtype="float64")
#Find Centre of Mass
r_com=(m1*r1+m2*r2+m3*r3)/(m1+m2+m3)
#Define initial velocities
v1=[0.01,0.01,0] #m/s
v2=[-0.05,0,-0.1] #m/s
v3=[0,-0.01,0] #m/s
#Convert velocity vectors to arrays
v1=np.array(v1,dtype="float64")
v2=np.array(v2,dtype="float64")
v3=np.array(v3,dtype="float64")
#Find velocity of COM
v_com=(m1*v1+m2*v2+m3*v3)/(m1+m2+m3)

#A function defining the equations of motion 
def ThreeBodyEquations(w,t,G,m1,m2,m3):
    r1=w[:3]
    r2=w[3:6]
    r3=w[6:9]
    v1=w[9:12]
    v2=w[12:15]
    v3=w[15:18]

    #Calculate magnitude or norm of vector
    r12=sci.linalg.norm(r2-r1)
    r13=sci.linalg.norm(r3-r1)
    r23=sci.linalg.norm(r3-r2)

    dv1bydt=K1*m2*(r2-r1)/r12**3+K1*m3*(r3-r1)/r13**3
    dv2bydt=K1*m1*(r1-r2)/r12**3+K1*m3*(r3-r2)/r23**3
    dv3bydt=K1*m1*(r1-r3)/r13**3+K1*m2*(r2-r3)/r23**3
    dr1bydt=K2*v1
    dr2bydt=K2*v2
    dr3bydt=K2*v3

    r12_derivs=np.concatenate((dr1bydt,dr2bydt))
    r_derivs=np.concatenate((r12_derivs,dr3bydt))
    v12_derivs=np.concatenate((dv1bydt,dv2bydt))
    v_derivs=np.concatenate((v12_derivs,dv3bydt))
    derivs=np.concatenate((r_derivs,v_derivs))
    return derivs

#Package initial parameters
init_params=np.array([r1,r2,r3,v1,v2,v3]) #create array of initial params
init_params=init_params.flatten() #flatten array to make it 1D
time_span=np.linspace(0,50,50000) #8 orbital periods and 500 points
#Run the ODE solver
three_body_sol=sci.integrate.odeint(ThreeBodyEquations,init_params,time_span,args=(G,m1,m2, m3))

r1_sol=three_body_sol[:,:3]
r2_sol=three_body_sol[:,3:6]
r3_sol=three_body_sol[:,6:9]

# Vpython parts
sphere1 = sphere(pos=vector(r1_sol[0,0],r1_sol[0,1],r1_sol[0,2]), radius=0.1, texture="minecraft_tree_wood.jpg")
sphere2 = sphere(pos=vector(r2_sol[0,0],r2_sol[0,1],r2_sol[0,2]), radius=0.1, color=color.red, shininess=0.5, texture=textures.metal)
sphere3 = sphere(pos=vector(r3_sol[0,0],r3_sol[0,1],r3_sol[0,2]), radius=0.12, color=color.green, shininess=0.1, texture=textures.metal)

# i = 1
# while i<len(r1_sol):
#     rate(2000)
#     sphere1.pos = vector(r1_sol[i,0],r1_sol[i,1],r1_sol[i,2])
#     sphere2.pos = vector(r2_sol[i,0],r2_sol[i,1],r2_sol[i,2])
#     sphere3.pos = vector(r3_sol[i,0],r3_sol[i,1],r3_sol[i,2])
#     slider.value = i
#     text.text = '{}'.format(i)
#     i += 1

# sphere1.make_trail = False
# sphere2.make_trail = False
# sphere3.make_trail = False
slider.disabled = False
button.disabled = False
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