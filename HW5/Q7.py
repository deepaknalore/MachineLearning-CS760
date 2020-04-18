import math
import numpy as np

mendota = "mendota.csv"
monona = "monona.csv"

f = open(mendota, "r", encoding='utf-8-sig')
lines = f.readlines()
mendotaList = []
xMendota = []
yMendota = []
prevx = 1985
for line in lines:
    line = line.split(',')
    entry = []
    if line[0] == '""""':
        x = prevx
    else:
        x = line[0].split('-')[0]
    if '-' in line[3]:
        prevx = x
        continue
    y = line[3].strip()
    entry.append(int(x))
    xMendota.append(int(x))
    entry.append(int(y))
    yMendota.append(int(y))
    mendotaList.append(entry)

f = open(monona, "r", encoding='utf-8-sig')
lines = f.readlines()
mononaList = []
xMonona = []
yMonona = []
prevx = 1985
for line in lines:
    line = line.split(',')
    entry = []
    if line[0] == '""""':
        x = prevx
    else:
        x = line[0].split('-')[0]
    if '-' in line[3]:
        prevx = x
        continue
    y = line[3].strip()
    entry.append(int(x))
    xMonona.append(int(x))
    entry.append(int(y))
    yMonona.append(int(y))
    mononaList.append(entry)

trainYMon = yMonona[:116]
trainYMen = yMendota[:116]
testYMon = yMonona[117:]
testYMen = yMendota[117:]

#normalize
xMonona = np.array(xMonona)
yMonona = np.array(yMonona)
xMonona = xMonona / np.linalg.norm(xMonona)
yMonona = yMonona / np.linalg.norm(yMonona)

xMonona = xMonona - xMonona.mean()
xMonona = xMonona / xMonona.max()

yMonona = yMonona - yMonona.mean()
yMonona = yMonona / yMonona.max()

train = []

for i in range(len(yMonona[:116])):
    list = []
    list.append(1)
    list.append(xMonona[i])
    list.append(yMonona[i])
    train.append(list)

#2/n * xt * (xB-y)
beta = [0,0,0]

for i in range(100):
    x = 1855
    err = 0
    for i in range(len(trainYMon)):
        newY = beta[0] + beta[1] * xMonona[i] + beta[2] * yMonona[i]
        err += math.pow((trainYMen[i] - newY),2)
        x += 1
    print(err/len(trainYMon))
    beta = np.array(beta)
    X = np.array(train)
    xb = np.dot(X,beta)
    Y = np.array(yMendota[:116])
    xb = xb - Y
    Xt = np.transpose(X)
    newBeta = np.dot(Xt,xb)
    newBeta = newBeta/58
    beta = beta - (0.5) * newBeta
    # print("New Beta: ")
    # print(beta)
print(beta)