import os

path = "/Users/dsrinath/Downloads/hw4/NewFolder"

map = {}
total = 0
for filename in os.listdir(path):
    newFile = []
    if(filename.startswith("s")):
        inputFile = open("/Users/dsrinath/Downloads/hw4/NewFolder/" + filename, "r")
        lines = inputFile.readlines()
        for line in lines:
            for ch in line:
                if ch != '\n':
                    total += 1
                    if ch in map:
                        map[ch] = map[ch] + 1
                    else:
                        map[ch] = 1

for key in map:
    map[key] = (map[key] + 1)/(total + 27)

for i in sorted (map.keys()) :
     print(i + ":" + str(format(map[i],'.5f')))