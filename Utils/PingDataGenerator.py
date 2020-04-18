import subprocess
import time
from datetime import datetime

pingCount = 10
count = 0
ipList = ['www.google.com']

def WritePingStats():
    t = datetime.utcnow()
    for ip in ipList:
        p = subprocess.Popen(["ping", "-c " + str(pingCount),ip], stdout = subprocess.PIPE)
        out = str(p.communicate()[0])
        timeUnit = out.split()[-1][:2]
        averageLatency = str(out.split()[-2]).split('/')[1]
        maxLatency = str(out.split()[-2]).split('/')[2]
        stdDev = str(out.split()[-2]).split('/')[3]
        print(str(maxLatency) + str(timeUnit))
        print(str(averageLatency) + str(timeUnit))
        print(stdDev)
        with open(str(ip) + ".csv", "a") as fd:
            fd.write(str(t) + "," + averageLatency + "," + maxLatency + "," + stdDev + "\n")


while(True):
    if count == 2:
        break
    WritePingStats()
    count += 1
    time.sleep(10)

