import random as rand
import numpy as np
import scipy as sci
from scipy import integrate
import scipy.integrate
from vpython import *

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

#Define masses
m1=1.1 #First ball
m2=0.907 #Second ball
m3=1.3 #Third ball
#Define initial position vectors
# r1=[-0.5,0,0] #m
# r2=[0.5,0,0] #m
# r3=[0,1,0] #m
r1=[-rand.random(),0,0] #m
r2=[rand.random(),0,0] #m
r3=[0,rand.random(),0] #m
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

canvas(background=vector(225/255, 226/255, 225/255), width=1280, height=720, center=vector(0,0,0))

sphere1 = sphere(pos=vector(r1_sol[0,0],r1_sol[0,1],r1_sol[0,2]), radius=0.1, make_trail=True, texture="minecraft_tree_wood.jpg")
sphere2 = sphere(pos=vector(r2_sol[0,0],r2_sol[0,1],r2_sol[0,2]), radius=0.1, color=color.red, make_trail=True, shininess=0.5, texture=textures.metal)
sphere3 = sphere(pos=vector(r3_sol[0,0],r3_sol[0,1],r3_sol[0,2]), radius=0.12, color=color.green, make_trail=True, shininess=0.1, texture=textures.metal)


i = 1
while (i<len(r1_sol)):
    rate(1000)
    sphere1.pos = vector(r1_sol[i,0],r1_sol[i,1],r1_sol[i,2])
    sphere2.pos = vector(r2_sol[i,0],r2_sol[i,1],r2_sol[i,2])
    sphere3.pos = vector(r3_sol[i,0],r3_sol[i,1],r3_sol[i,2])
    i += 1