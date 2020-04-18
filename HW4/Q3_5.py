import os
import math

path = "/Users/dsrinath/Downloads/hw4/NewFolder"

map = {}
total = 0
for filename in os.listdir(path):
    newFile = []
    if(filename.startswith("e")):
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

bagOfCharacters = {}
path = "/Users/dsrinath/Downloads/hw4/languageID/"
for filename in os.listdir(path):
    if (filename.startswith("e10")):
        inputFile = open("/Users/dsrinath/Downloads/hw4/languageID/" + filename, "r")
        lines = inputFile.readlines()
        for line in lines:
            for ch in line:
                if ch != '\n':
                    total += 1
                    if ch in bagOfCharacters:
                        bagOfCharacters[ch] = bagOfCharacters[ch] + 1
                    else:
                        bagOfCharacters[ch] = 1

value = 1.0
for key in map:
    map[key] = math.log(map[key],10)
    value += map[key]*bagOfCharacters[key]

print(value)