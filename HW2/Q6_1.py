import matplotlib.pyplot as plt

#####           MAIN        #########
inputFile = open("/Users/dsrinath/Downloads/hw2/D1.txt", "r")
lines = inputFile.readlines()
x = []
y = []
col =[]

for line in lines:
    smallList = line.strip().split(" ")
    x.append(float(smallList[0]))
    y.append(float(smallList[1]))
    col.append(float(smallList[2]))
plt.title("D1 dataset")
plt.scatter(x,y,c=col,cmap=plt.cm.autumn)
plt.show()


