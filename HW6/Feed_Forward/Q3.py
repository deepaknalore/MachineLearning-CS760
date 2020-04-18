import math

hidenLayer = []
depth = 5
def out(b, w1, x1, w2, x2):
    return max(b + w1*x1 + w2*x2, 0)

def sigma(input):
    return (1/(1 + math.exp(-input)))

def firstLayer(b, x1, x2, depth):
    if depth == 5:
        return
    hidenLayer.append(out(b, 1, x1, 1, x2))
    hidenLayer.append(out(b, 1, x1, 1, x2))
    firstLayer(b,hidenLayer[-2],hidenLayer[-1], depth+1)

def outLayer():
    val = 1
    val += hidenLayer[-2]
    val += hidenLayer[-1]
    return sigma(val)


##############MAIN###############
x1 = -1
x2 = -1
b = 1

firstLayer(b,x1,x2,0)
for elem in hidenLayer:
    print(elem)
print(outLayer())


