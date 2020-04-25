import numpy as np
import matplotlib.pyplot as plt


mainList = []
with open("three.txt") as fd:
    lines = fd.readlines()
    for line in lines:
        three = line.split()
        three = list(map(int, three))
        mainList.append(three)

with open("eight.txt") as fd:
    lines = fd.readlines()
    for line in lines:
        three = line.split()
        three = list(map(int, three))
        mainList.append(three)

y = []
for i in range(256):
    elem = 0
    for j in range(400):
        elem += mainList[j][i]
    y.append(elem/400)
y = np.array(y)
img = y.reshape(16,16,order='F')
plt.imshow(img, cmap="gray")
plt.show()