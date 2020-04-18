import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

hidenLayer = []
index = 0

def norm():
    global index
    temp = s[index]
    index += 1
    return temp

def out(b, w1, x1, w2, x2):
    return max(b + w1*x1 + w2*x2, 0)

def sigma(input):
    return (1/(1 + math.exp(-input)))

def firstLayer(x1,x2):
    global index
    hidenLayer[:] = []
    index = 1
    for i in range(10):
        hidenLayer.append(out(s[0],norm(),x1,norm(),x2))

def outLayer():
    val = norm()
    for elem in hidenLayer:
        val += elem*norm()
    return sigma(val)


##############MAIN###############
s = np.random.normal(0, 1,32)
x1 = 1
x2 = 1
x1List = []
x2List = []
yList = []
zList = []
for x1 in np.arange(-5,+5,0.1):
    yList = []
    for x2 in np.arange(-5,5,0.1):
        firstLayer(x1,x2)
        x1List.append(x1)
        x2List.append(x2)
        yList.append(outLayer())
    zList.append(yList)

x1List = np.arange(-5,+5,0.1)
x2List = np.arange(-5,+5,0.1)
X, Y = np.meshgrid(x1List, x2List)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, np.array(zList), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()




