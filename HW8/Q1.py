import numpy as np
import matplotlib.pyplot as plt

with open("three.txt") as fd:
    three = fd.readline()
three = three.split()
three = list(map(int, three))
three = np.array(three)
img = three.reshape(16,16,order='F')
plt.imshow(img, cmap="gray")
plt.show()

with open("eight.txt") as fd:
    three = fd.readline()
three = three.split()
three = list(map(int, three))
three = np.array(three)
img = three.reshape(16,16,order='F')
plt.imshow(img, cmap="gray")
plt.show()