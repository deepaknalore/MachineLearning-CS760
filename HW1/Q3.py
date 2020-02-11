import math

def findBestSplit(list):
    firstSortedList = sorted(list, key=lambda tup: tup[0], reverse=True)
    thresholdList = findThresholds(firstSortedList, 0)
    print("Split based on the first features - x1")
    for threshold in thresholdList:
        print("Threshold : " + str(threshold) + " Information Gain: " + str(informationGain(firstSortedList, threshold, 0)))

    secondSortedList = sorted(list, key=lambda tup: tup[1], reverse=True)
    thresholdList = findThresholds(secondSortedList, 1)
    print("Split based on the first features - x2")
    for threshold in thresholdList:
        print("Threshold : " + str(threshold) + " Information Gain: " + str(informationGain(secondSortedList, threshold, 1)))



def findThresholds(sortedList, index):
    list = []
    list.append(sortedList[0][index])
    threshold = sortedList[0][index]
    for element in sortedList:
        if(float(element[index]) < float(threshold)):
            list.append(element[index])
            threshold = element[index]
    return list

def informationGain(sortedList, threshold, index):
    overallEntropy = entropy(sortedList)
    leftList = []
    rightList = []
    for element in sortedList:
        if(float(element[index]) >= float(threshold)):
            leftList.append(element)
        else:
            rightList.append(element)
    leftEntropy = entropy(leftList)
    rightEntropy = entropy(rightList)
    temp = overallEntropy - (leftEntropy * (len(leftList)/len(sortedList)) + (rightEntropy * len(rightList)/len(sortedList)))
    return temp


def entropy(sortedList):
    if(len(sortedList) == 0):
        return 0
    overallCount = 0
    posCount = 0
    for element in sortedList:
        overallCount += 1
        if(element[2] == 1):
            posCount += 1

    left = posCount/overallCount
    right = (overallCount - posCount)/overallCount
    temp = 0
    if left > 0:
        temp += left * math.log2(left)
    if right > 0:
        temp += right * math.log2(right)
    return temp*(-1)

#####           MAIN        #########
inputFile = open("/Users/dsrinath/Downloads/hw2/Druns.txt", "r")
lines = inputFile.readlines()
list = []

for line in lines:
    smallList = line.strip().split(" ")
    smallList = [float(i) for i in smallList]
    list.append(smallList)
findBestSplit(list)




