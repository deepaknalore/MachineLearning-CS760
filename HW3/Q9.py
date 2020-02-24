import math

def distance(testElement, trainElement):
    temp = 0
    for i in range(2):
        temp += (testElement[i] - trainElement[i])**2
    return math.sqrt(temp)

def validate(train, test):
    error = 0
    for testElement in test:
        min = 999.0
        value = 1
        for trainElement in train:
            if min > distance(testElement,trainElement):
                min = distance(testElement,trainElement)
                value = trainElement[2]
        if value != testElement[2]:
            error += 1
    return error

def normalize(list):
    normalizedList = []
    mean = []
    stddev = []
    for elem in list:
        if len(mean) == 0:
            mean.append(elem[0])
            mean.append(elem[1])
            # mean.append(elem[2])
            # mean.append(elem[3])
            # mean.append(elem[4])
            # mean.append(elem[5])
        else:
            mean[0] += elem[0]
            mean[1] += elem[1]
            # mean[2] += elem[2]
            # mean[3] += elem[3]
            # mean[4] += elem[4]
            # mean[5] += elem[5]
    for i in range(2):
        mean[i] = mean[i]/200

    for elem in list:
        if len(stddev) == 0:
            stddev.append((elem[0] - mean[0])**2)
            stddev.append((elem[1] - mean[1]) ** 2)
            # stddev.append((elem[2] - mean[2]) ** 2)
            # stddev.append((elem[3] - mean[3]) ** 2)
            # stddev.append((elem[4] - mean[4]) ** 2)
            # stddev.append((elem[5] - mean[5]) ** 2)
        else:
            stddev[0] += (elem[0] - mean[0])**2
            stddev[1] += (elem[1] - mean[1]) ** 2
            # stddev[2] += (elem[2] - mean[2]) ** 2
            # stddev[3] += (elem[3] - mean[3]) ** 2
            # stddev[4] += (elem[4] - mean[4]) ** 2
            # stddev[5] += (elem[5] - mean[5]) ** 2

    for i in range(2):
        stddev[i] = math.sqrt(stddev[i]/200)

    for elem in list:
        tempList = []
        for i in range(2):
            tempList.append((elem[i] - mean[i])/stddev[i])
        tempList.append(elem[2])
        normalizedList.append(tempList)
    return normalizedList

def newNormalization(list):
    normalizedList = []
    #maxFeature = [0,0,0,0,0,0]
    maxFeature = [0,0]
    for elem in list:
        for i in range(2):
            if maxFeature[i] < elem[i]:
                maxFeature[i] = elem[i]

    for elem in list:
        tempList = []
        for i in range(2):
            tempList.append(elem[i]/maxFeature[i])
        tempList.append(elem[2])
        normalizedList.append(tempList)

    return normalizedList

file1 = open('/Users/dsrinath/Downloads/hw3/D2b.txt', 'r')
Lines = file1.readlines()

count = 0
trainList = []
# Strips the newline character
for line in Lines:
    count+=1
    list = line.rstrip().split(" ")
    new_list = []
    for item in list:
        new_list.append(float(item))
    trainList.append(new_list)
print(count)

allError = 0
for i in range(5):
    testList = []
    tempTrain = []
    tempCount = 0
    #trainList = newNormalization(trainList)
    for element in trainList:
        #Put the elements of i*40 - (i+1)*40 as part of validation
        if tempCount>= i*(count/5) and tempCount < ((i+1)*(count/5)):
            testList.append(element)
        else:
            tempTrain.append(element)
        tempCount += 1
    error = validate(tempTrain, testList)
    allError += error
    print("Number of errors" + str(error))

print("Number of errors" + str(allError/5))
