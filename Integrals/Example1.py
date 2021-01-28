#%%
import Simpson
import Trapezoidal
import numpy as np

print(Simpson.integrate(lambda z: np.exp(-(z/(1-z))**2)*1/(z-1)**2, 0, 0.9999, 1000000))
print(Trapezoidal.integrate(lambda z: np.exp(-(z/(1-z))**2)*1/(z-1)**2, 0, 0.9999, 1000000))
