#%% 
import numpy as np
import matplotlib.pyplot as plt

ω = 2 * np.pi
e_list = [0, 1/4, 1/2, 3/4]
t_list = np.linspace(0, 1, 10000)
x_list_list = []
y_list_list = []

# relaxation method
def accFunction(g, x0, Nmax, accuracy):
    n = 1
    x_current = x0
    acc = 100
    while n < Nmax and acc > accuracy:
        x = g(x_current)
        acc = np.abs(x_current - x)
        x_current = x
        n += 1
    # if acc > accuracy:
    #     print("The function may not be diverged. ")
    # else:
    #     print("The root of this function is ", x_current, "\nThe accuracy is ", acc)
    return x_current

# For each e, calculate E and convert them into lists of x and y
for e in e_list:
    a = 1/(1-e)
    b = np.sqrt((1+e)/(1-e))
    x_list = []
    y_list = []

    for t in t_list:
        E = accFunction(lambda E : ω*t + e*np.sin(E), 0, 100000, 10**(-6))
        x_list.append(a*(e - np.cos(E)))
        y_list.append(b*np.sin(E))
    
    x_list_list.append(x_list)
    y_list_list.append(y_list)

# Plot the x and y lists
for i in range(len(x_list_list)):
    plt.plot(x_list_list[i], y_list_list[i])

plt.axis()
plt.show()