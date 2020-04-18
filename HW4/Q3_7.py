import os
import math

path = "/Users/dsrinath/Downloads/hw4/NewFolder"

map1 = {}
map2 = {}
map3 = {}
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
                    if ch in map1:
                        map1[ch] = map1[ch] + 1
                    else:
                        map1[ch] = 1

for key in map1:
    map1[key] = (map1[key] + 1)/(total + 27)

total = 0
for filename in os.listdir(path):
    newFile = []
    if(filename.startswith("j")):
        inputFile = open("/Users/dsrinath/Downloads/hw4/NewFolder/" + filename, "r")
        lines = inputFile.readlines()
        for line in lines:
            for ch in line:
                if ch != '\n':
                    total += 1
                    if ch in map2:
                        map2[ch] = map2[ch] + 1
                    else:
                        map2[ch] = 1

for key in map2:
    map2[key] = (map2[key] + 1)/(total + 27)
map2['x'] = 0.00006

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
                    if ch in map3:
                        map3[ch] = map3[ch] + 1
                    else:
                        map3[ch] = 1

for key in map3:
    map3[key] = (map3[key] + 1)/(total + 27)

bagOfCharacters = {}
path = "/Users/dsrinath/Downloads/hw4/Test/"
for filename in os.listdir(path):
    if (filename.startswith("s1")):
        inputFile = open("/Users/dsrinath/Downloads/hw4/Test/" + filename, "r")
        lines = inputFile.readlines()
        for line in lines:
            for ch in line:
                if ch != '\n':
                    total += 1
                    if ch in bagOfCharacters:
                        bagOfCharacters[ch] = bagOfCharacters[ch] + 1
                    else:
                        bagOfCharacters[ch] = 1

        value1 = 1.0
        value2 = 1.0
        value3 = 1.0
        tempmap1 = {}
        tempmap2 = {}
        tempmap3 = {}
        for key in map1:
            if key not in bagOfCharacters:
                bagOfCharacters[key] = 1
            tempmap1[key] = math.log(map1[key],10)
            value1 += tempmap1[key]*bagOfCharacters[key]
            tempmap2[key] = math.log(map2[key], 10)
            value2 += tempmap2[key] * bagOfCharacters[key]
            tempmap3[key] = math.log(map3[key], 10)
            value3 += tempmap3[key] * bagOfCharacters[key]
        if (value1 > value2):
            if(value1 > value3):
                print("1")
            else:
                print("3")
        else:
            if(value2 > value3):
                print("2")
            else:
                print("3")