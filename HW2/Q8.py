import matplotlib.pyplot as plt

#####           MAIN        #########
nodes = [5, 9, 25, 65, 133]
error = [677, 158, 76, 42, 13]
n = ["d32", "d128", "d512", "d2048", "d8192"]

plt.plot(nodes, error)
plt.title("Err_n v/s Number of nodes")
plt.xlabel("Number of nodes")
plt.ylabel("Number of Errors")

for i, txt in enumerate(n):
    plt.annotate(txt, (nodes[i], error[i]))
plt.show()


#### Number of Nodes, Error ####
# D32           5           677
# D128          9           158
# D512          25          76
# D2048         65          42
# D8192         133         13