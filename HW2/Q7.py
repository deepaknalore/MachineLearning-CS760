import math
from random import shuffle

nodeNumber = 0

def findBestSplit(list):
    if(len(list) == 0):
        return
    firstSortedList = sorted(list, key=lambda tup: tup[0], reverse=True)
    thresholdList = findThresholds(firstSortedList, 0)
    infoGain = 0
    leftList = []
    rightList = []
    bestThreshold = 0
    x = 0
    for threshold in thresholdList:
        tempIG, tempLeftList, tempRightList = informationGain(firstSortedList, threshold, 0)
        if tempIG > infoGain:
            x = 0
            infoGain = tempIG
            bestThreshold = threshold
            leftList = tempLeftList
            rightList = tempRightList

    secondSortedList = sorted(list, key=lambda tup: tup[1], reverse=True)
    thresholdList = findThresholds(secondSortedList, 1)
    for threshold in thresholdList:
        tempIG, tempLeftList, tempRightList =  informationGain(secondSortedList, threshold, 1)
        if tempIG > infoGain:
            x = 1
            infoGain = tempIG
            bestThreshold = threshold
            leftList = tempLeftList
            rightList = tempRightList
    if bestThreshold == 0:
        return list[0][2]
    return {'index': x, 'threshold': bestThreshold, 'groups': {'left': leftList, 'right': rightList}}


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
    return temp,leftList,rightList


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

def split(node):
    global nodeNumber
    nodeNumber += 1
    leftList = node["groups"]["left"]
    rightList = node["groups"]["right"]
    del (node['groups'])
    if not leftList or not rightList:
        node['left'] = node['right'] = to_terminal(leftList + rightList)
        return
    node['left'] = findBestSplit(leftList)
    if isinstance(node['left'], dict):
        split(node['left'])
    node['right'] = findBestSplit(rightList)
    if isinstance(node['right'], dict):
        split(node['right'])

# Create a terminal node value
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)


def buildTree(list):
    root = findBestSplit(list)
    split(root)
    return root

def printTree(node, depth):
    if isinstance(node, dict):
        print('%s[X%d >= %.3f]' % ((depth * ' ', (node['index'] + 1), node['threshold'])))
        printTree(node['left'], depth+1)
        printTree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

def predict(node, row):
    if(row[node['index']] >= node['threshold']):
        if isinstance(node['left'],dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

#####           MAIN        #########
inputFile = open("/Users/dsrinath/Downloads/hw2/Dbig.txt", "r")
lines = inputFile.readlines()
list = []

for line in lines:
    smallList = line.strip().split(" ")
    smallList = [float(i) for i in smallList]
    list.append(smallList)
shuffle(list)

training_set = list[:8192]
test_set = list[8192:]

# d32 = training_set[:32]
# d128 = training_set[:128]
# d512 = training_set[:512]
# d2048 = training_set[:2048]
d8192 = training_set[:8192]

tree = buildTree(d8192)
error = 0
for row in test_set:
    actual = predict(tree, row)
    if(actual != row[2]):
        error += 1

print("Error: " + str(error))
print("Number of Nodes : " + str(nodeNumber))
#printTree(tree,0)


#### Number of Nodes, Error ####
# D32           6           315
# D128          12          178
# D512          28          104
# D2048         59          56
# D8192         107         32




