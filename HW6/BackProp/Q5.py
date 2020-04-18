import math

# 0.1 -0.2 0.3 -0.4 0.5 -0.6 0.7 -0.8 0.9, input 1 -1, and label y = 1, eta = 0.1

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
eta = 0.1

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

def dE_dw1(derr_dua):
    return 1 * derr_dua

def dE_dw2(x1,derr_dua):
    return x1*derr_dua

def dE_dw3(x2,derr_dua):
    return x2*derr_dua

def dE_dw4(derr_dub):
    return derr_dub

def dE_dw5(x1, derr_dub):
    return x1*derr_dub

def dE_dw6(x2, derr_dub):
    return x2*derr_dub

def dE_dw7(derr_duc):
    return derr_duc

def dE_dw8(va, derr_duc):
    return va*derr_duc

def dE_dw9(vb, derr_duc):
    return vb*derr_duc

def print_w():
    print(str(w1) + " " + str(w2) + " " + str(w3) + " " + str(w4) + " " + str(w5) + " " + str(w6) + " " + str(w7) + " " + str(w8) + " " + str(w9))

print_w()
#forward prop
ua = 1*w1 + x1*w2 + x2*w3
ub = 1*w4 + x1*w5 + x2*w6
va = RELU(ua)
vb = RELU(ub)
uc = va * w8 + vb * w9 + 1 * w7
vc = sigmoid(uc)

#Derivatives for output layer
err = E(vc,y)
derr_dvc = dE_dvc(vc,y)
derr_duc = dE_duc(vc,y)

print(err)

#derivatives for hidden layers
derr_dva = dE_dva(w8, derr_duc)
derr_dvb = dE_dvb(w9, derr_duc)
derr_dua = dE_dua(derr_dva, ua)
derr_dub = dE_dub(derr_dvb, ub)

#derivatives for weights
derr_dw1 = dE_dw1(derr_dua)
derr_dw2 = dE_dw2(x1, derr_dua)
derr_dw3 = dE_dw3(x2, derr_dua)
derr_dw4 = dE_dw4(derr_dub)
derr_dw5 = dE_dw5(x1, derr_dub)
derr_dw6 = dE_dw6(x2, derr_dub)
derr_dw7 = dE_dw7(derr_duc)
derr_dw8 = dE_dw8(va, derr_duc)
derr_dw9 = dE_dw9(vb, derr_duc)

w1 = w1 - eta*derr_dw1
w2 = w2 - eta*derr_dw2
w3 = w3 - eta*derr_dw3
w4 = w4 - eta*derr_dw4
w5 = w5 - eta*derr_dw5
w6 = w6 - eta*derr_dw6
w7 = w7 - eta*derr_dw7
w8 = w8 - eta*derr_dw8
w9 = w9 - eta*derr_dw9

print_w()

#forward prop
ua = 1*w1 + x1*w2 + x2*w3
ub = 1*w4 + x1*w5 + x2*w6
va = RELU(ua)
vb = RELU(ub)
uc = va * w8 + vb * w9 + 1 * w7
vc = sigmoid(uc)

#Derivatives for output layer
err = E(vc,y)
print(err)