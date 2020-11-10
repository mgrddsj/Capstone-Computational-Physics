#%% Imports
import numpy as np
import matplotlib.pyplot as plt
import pylab

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data)
pylab.gray()
pylab.show()

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data, origin="lower")
pylab.gray()
pylab.show()

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data, origin="lower", extent=[0, 10, 0, 5])
pylab.gray()
pylab.show()

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data, origin="lower", extent=[0, 10, 0, 5], aspect=2.0)
pylab.gray()
pylab.show()

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data, origin="lower", extent=[0, 10, 0, 5], aspect=2.0)
pylab.gray()
pylab.colorbar()
pylab.show()

# %%
data = np.loadtxt("circular.txt", float)
pylab.imshow(data, origin="lower", extent=[0, 10, 0, 5], aspect=2.0)
pylab.jet()
pylab.colorbar()
pylab.show()

#%% ripples.py
wavelength = 5.0
k = 2*np.pi/wavelength
xi0 = 1.0
separation = 20.0      # Separation of centers in cm
side = 100.0           # Side of the square in cm
points = 500           # Number of grid points along each side
spacing = side/points  # Spacing of points in cm


# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
xi = np.empty([points,points],float)

# Calculate the values in the array
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r1 = np.sqrt((x-x1)**2+(y-y1)**2)
        r2 = np.sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j] = xi0*np.sin(k*r1) + xi0*np.sin(k*r2)

# Make the plot
pylab.imshow(xi, origin="lower", extent=[0,side,0,side])
pylab.gray()
pylab.show()

#%% stm.txt
data = np.loadtxt("stm.txt", float)
pylab.imshow(data, origin="lower", extent=[0, 10, 0, 5], aspect=2.0)
pylab.jet()
pylab.colorbar()
pylab.show()

#%% 3D Graphics
import vpython
vpython.sphere()