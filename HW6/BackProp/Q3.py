import math

# 0.1 -0.2 0.3 -0.4 0.5 -0.6 0.7 -0.8 0.9, input 1 -1, and label y =1

w1 = 0.1
w2 = -0.2
w3 = 0.3
w4 = -0.4
w5 = 0.5
w6 = -0.6
w7 = 0.7
w8 = -0.8
w9 = 0.9
x1 = 1
x2 = -1
y = 1

def RELU(u):
    return max(u, 0)

def sigmoid(input):
    return (1/(1 + math.exp(-input)))

def E(vc,y):
    return 0.5*(pow(vc-y,2))

def dE_dvc(vc,y):
    return vc-y

def dE_duc(vc,y):
    return dE_dvc(vc,y) * vc * (1-vc)

def dE_dva(w8, derr_duc):
    return w8*derr_duc

def dE_dvb(w9, derr_duc):
    return w9*derr_duc

def dE_dua(derr_dva, uj):
    if uj < 0:
        return 0
    else:
        return derr_dva

def dE_dub(derr_dvb, uj):
    if uj < 0:
        return 0
    else:
        return derr_dvb


ua = 1*w1 + x1*w2 + x2*w3
ub = 1*w4 + x1*w5 + x2*w6
va = RELU(ua)
vb = RELU(ub)
uc = va * w8 + vb * w9 + 1 * w7
vc = sigmoid(uc)

err = E(vc,y)
derr_dvc = dE_dvc(vc,y)
derr_duc = dE_duc(vc,y)

derr_dva = dE_dva(w8, derr_duc)
derr_dvb = dE_dvb(w9, derr_duc)
derr_dua = dE_dua(derr_dva, ua)
derr_dub = dE_dub(derr_dvb, ub)

print(str(derr_dva) + " " + str(derr_dua) + " " + str(derr_dvb) + " " + str(derr_dub))