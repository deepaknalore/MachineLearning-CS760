import numpy as np
import matplotlib.pyplot as plt


X = []
with open("three.txt") as fd:
    lines = fd.readlines()
    for line in lines:
        three = line.split()
        three = list(map(int, three))
        X.append(three)

with open("eight.txt") as fd:
    lines = fd.readlines()
    for line in lines:
        three = line.split()
        three = list(map(int, three))
        X.append(three)

y = []
for i in range(256):
    elem = 0
    for j in range(400):
        elem += X[j][i]
    y.append(elem/400)
#y = np.array(y)
X = np.array(X)
y = np.mean(X.T, axis=1)
X = X - y
# S = np.dot(X.T,X)
# S = np.divide(S,399)
S = np.cov(X.T)
w, v = np.linalg.eig(S)
print(w[:2])
v1 = v[:,0]
v2 = v[:,1]
# v1 = np.divide(v1,(np.amax(v1)/255.0))
# v2 = np.divide(v2,(np.amax(v2)/255.0))
img = v1.reshape(16,16,order='F')
plt.imshow(img, cmap="gray")
plt.show()
img = v2.reshape(16,16,order='F')
plt.imshow(img, cmap="gray")
plt.show()