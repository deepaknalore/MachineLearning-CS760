from random import shuffle
import csv

#####           MAIN        #########
inputFile = open("/Users/dsrinath/Downloads/hw3/D2b.txt", "r")
lines = inputFile.readlines()
list = []

for line in lines:
    smallList = line.strip().split(" ")
    smallList = [float(i) for i in smallList]
    list.append(smallList)
#shuffle(list)

# training_set = list[:8192]
# test_set = list[8192:]
#
# d32 = training_set[:32]
# d128 = training_set[:128]
# d512 = training_set[:512]
# d2048 = training_set[:2048]
# d8192 = training_set[:8192]

with open("/Users/dsrinath/Desktop/d2b.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list)


