#%%
# from vpython import sphere
# from vpython import vector

# import vpython
# print(dir(vpython))
# sphere(radius = 0.5, pos = vector(1,2,3))
# %%
from vpython import sphere, vector, color
L = 5
R = 0.3
for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L - 5):
            sphere(pos = vector(i, j, k), radius = R)

