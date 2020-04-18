import os

path = "/Users/dsrinath/Downloads/hw4/languageID"

map = {}
total = 0
for filename in os.listdir(path):
    newFile = []
    if(filename.startswith("e10")):
        inputFile = open("/Users/dsrinath/Downloads/hw4/languageID/" + filename, "r")
        lines = inputFile.readlines()
        for line in lines:
            for ch in line:
                if ch != '\n':
                    total += 1
                    if ch in map:
                        map[ch] = map[ch] + 1
                    else:
                        map[ch] = 1

print(map)