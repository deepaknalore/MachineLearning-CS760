import os

path = "/Users/dsrinath/Downloads/hw4/languageID"


for filename in os.listdir(path):
    newFile = []
    inputFile = open("/Users/dsrinath/Downloads/hw4/languageID/" + filename, "r")
    lines = inputFile.readlines()
    for line in lines:
        newLine = ""
        for letter in line:
            if letter == " ":
                newLine += "space "
            else:
                newLine += letter + " "
        newFile.append(newLine)
    with open("/Users/dsrinath/Downloads/hw4/weka/" + filename, "w", newline="") as f:
        for line in newFile:
            f.write(line)