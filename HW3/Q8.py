import math
import matplotlib.pyplot as plt

def distance(x1, x2, element):
    temp = (x1-float(element[0]))**2
    temp += (x2 - float(element[1]))**2
    return math.sqrt(temp)



file1 = open('/Users/dsrinath/Downloads/hw3/D2z.txt', 'r')
Lines = file1.readlines()

count = 0
trainList = []
# Strips the newline character
for line in Lines:
    list = line.rstrip().split(" ")
    new_list = []
    for item in list:
        new_list.append(float(item))
    trainList.append(new_list)

testList = []
x1 = -2.0
while x1 <= 2.0:
    x2 = -2.0
    while x2 <= 2.0:
        min = 999.0
        value = 1
        for element in trainList:
            if min > distance(x1,x2,element):
                min = distance(x1,x2,element)
                value = element[2]
        tempList = []
        tempList.append(x1)
        tempList.append(x2)
        tempList.append(value)
        testList.append(tempList)
        x2 += 0.1
    x1 += 0.1

one_test_x = []
one_train_x = []
zero_test_x = []
zero_train_x = []
one_test_y = []
one_train_y = []
zero_test_y = []
zero_train_y = []

for element in testList:
    if element[2] == 1:
        one_test_x.append(element[0])
        one_test_y.append(element[1])
    else:
        zero_test_x.append(element[0])
        zero_test_y.append(element[1])

for element in trainList:
    if element[2] == 1:
        one_train_x.append(element[0])
        one_train_y.append(element[1])
    else:
        zero_train_x.append(element[0])
        zero_train_y.append(element[1])

plt.scatter(one_test_x,one_test_y,color='yellow')
plt.scatter(zero_test_x,zero_test_y,color='green')
plt.scatter(one_train_x,one_train_y,color='blue')
plt.scatter(zero_train_x,zero_train_y,color='red')
plt.title("1NN on a 2D grid")
plt.xlabel("Feature x1")
plt.ylabel("Feature x2")
plt.show()