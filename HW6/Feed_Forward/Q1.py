import math

hidenLayer = []
def out(b, w1, x1, w2, x2):
    return max(b + w1*x1 + w2*x2, 0)

def sigma(input):
    return (1/(1 + math.exp(-input)))

def firstLayer(x1,x2):
    hidenLayer.append(out(1,1,x1,1,x2))
    hidenLayer.append(out(1,1,x1,1,x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))
    hidenLayer.append(out(1, 1, x1, 1, x2))

def outLayer():
    val = 1
    for elem in hidenLayer:
        val += elem
    return sigma(val)


##############MAIN###############
x1 = -1
x2 = -1
firstLayer(x1,x2)
for elem in hidenLayer:
    print(elem)
print(outLayer())


