import matplotlib.pyplot as plt

#####           MAIN        #########
inputFile = open("/Users/dsrinath/Downloads/hw2/D2.txt", "r")
lines = inputFile.readlines()
x = [0,0,1,1]
y = [0,1,0,1]
col =[0,1,1,0]

plt.title("Sample dataset")
plt.scatter(x,y,c=col,cmap=plt.cm.autumn)
plt.show()


