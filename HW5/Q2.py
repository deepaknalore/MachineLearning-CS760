import math

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

meanMon = 0
meanMen = 0

for i in range(len(trainYMen)):
    meanMon += trainYMon[i]
    meanMen += trainYMen[i]

print("Mendota: " + str(meanMen/116))
print("Monona: " + str(meanMon/116))

meanMen = meanMen/116
meanMon = meanMon/116
stdMon = 0
stdMen = 0

for i in range(len(trainYMon)):
    stdMon += math.pow(trainYMon[i] - meanMon, 2)
    stdMen += math.pow(trainYMen[i] - meanMen, 2)
stdMon = stdMon/115
stdMen = stdMen/115

print("STD Mendota: " + str(math.sqrt(stdMen)))
print("STD Monona: " + str(math.sqrt(stdMon)))
