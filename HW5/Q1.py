import matplotlib.pyplot as plt

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

mon = plt.scatter(xMonona,yMonona,color='red', label = 'Monona')
men = plt.scatter(xMendota,yMendota,color='blue', label = 'Mendota')
plt.legend((mon,men), ('Monona', 'Mendota'))
plt.title("Year v/s Ice days")
plt.xlabel("Year")
plt.ylabel("Ice days")
plt.show()

mon1 = plt.plot(xMonona,yMonona,color='red', label = 'Monona')
men1 = plt.plot(xMendota,yMendota,color='blue', label = 'Mendota')
plt.legend(loc="upper right")
plt.title("Year v/s Ice days")
plt.xlabel("Year")
plt.ylabel("Ice days")
plt.show()

yDiff = []
for i in range(len(xMonona)):
    yDiff.append(yMonona[i] - yMendota[i])
diff = plt.plot(xMonona, yDiff)
plt.title("Year v/s Ice days")
plt.xlabel("Year")
plt.ylabel("Ice days")
plt.show()