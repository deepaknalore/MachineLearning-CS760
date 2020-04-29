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
print(S[:5,:5])