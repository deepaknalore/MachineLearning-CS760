import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

hidenLayer = []

def norm():
    mu = 0
    stdDev = 1
    return np.random.normal(mu, stdDev,1)[0]
def out(b, w1, x1, w2, x2):
    return max(b + w1*x1 + w2*x2, 0)

def sigma(input):
    return (1/(1 + math.exp(-input)))

def firstLayer(x1,x2):
    hidenLayer[:] = []
    for i in range(10):
        hidenLayer.append(out(norm(),norm(),x1,norm(),x2))

def outLayer():
    val = norm()
    for elem in hidenLayer:
        val += elem*norm()
    return sigma(val)


##############MAIN###############
x1 = 1
x2 = 1
x1List = []
x2List = []
yList = []
zList = []
for x1 in np.arange(-5,+5,1):
    yList = []
    for x2 in np.arange(-5,5,1):
        firstLayer(x1,x2)
        x1List.append(x1)
        x2List.append(x2)
        yList.append(outLayer())
    zList.append(yList)

x1List = np.arange(-5,+5,1)
x2List = np.arange(-5,+5,1)
X, Y = np.meshgrid(x1List, x2List)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, np.array(zList), linewidth=0.2, antialiased=True)
plt.show()




