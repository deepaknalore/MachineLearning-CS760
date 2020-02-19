inputFile = open("stats.log", "r")
lines = inputFile.readlines()

readLatency = 0
count = 0
successfulReads = 0
#updateLatency = 0

for line in lines:
    if line.startswith("Read Latency :"):
        readLatency += float(line.split(":")[1].strip())
        count += 1
    elif line.startswith("The number of successful Reads is :"):
        successfulReads += float(line.split(":")[1].strip())
    #elif(line.startswith("")):
    #    readLatency += float(line.split(":")[1].strip())


print(readLatency/count)
print(successfulReads/180)
#print(updateLatency/count)