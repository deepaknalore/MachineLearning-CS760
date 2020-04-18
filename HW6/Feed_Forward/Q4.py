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

# def firstLayer(x1,x2):
#     global index
#     hidenLayer[:] = []
#     index = 1
#     for i in range(10):
#         hidenLayer.append(out(s[0],norm(),x1,norm(),x2))

def firstLayer(b, x1, x2, depth):
    if depth == 5:
        return
    hidenLayer.append(out(s[depth], norm(), x1, norm(), x2))
    hidenLayer.append(out(s[depth], norm(), x1, norm(), x2))
    firstLayer(s[depth],hidenLayer[-2],hidenLayer[-1], depth+1)

def outLayer():
    val = s[5]
    val += hidenLayer[-2] * norm()
    val += hidenLayer[-1] * norm()
    return sigma(val)


##############MAIN###############
s = np.random.normal(0, 1, 28)
x1 = -1
x2 = -1
x1List = []
x2List = []
yList = []
zList = []
for x1 in np.arange(-5,+5,0.1):
    yList = []
    for x2 in np.arange(-5,5,0.1):
        hidenLayer[:] = []
        index = 6
        firstLayer(s[0], x1, x2, 0)
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




