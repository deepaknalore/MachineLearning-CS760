import matplotlib.pyplot as plt

#####           MAIN        #########
nodes = [6, 12, 28, 59, 107]
error = [315, 178, 104, 56, 32]
n = ["d32", "d128", "d512", "d2048", "d8192"]

plt.plot(nodes, error)
plt.title("Err_n v/s Number of nodes")
plt.xlabel("Number of nodes")
plt.ylabel("Number of Errors")

for i, txt in enumerate(n):
    plt.annotate(txt, (nodes[i], error[i]))
plt.show()