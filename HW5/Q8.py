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

train = []

for i in range(len(yMonona[:116])):
    list = []
    list.append(1)
    list.append(xMonona[i])
    train.append(list)

#X^TX-1 X^T Y
X = np.array(train)
Xt = np.transpose(X)
Y = np.array(yMendota[:116])
XtX = np.linalg.inv(np.dot(Xt,X))
temp = np.dot(XtX,Xt)
ans = np.dot(temp, Y)
print(ans)

