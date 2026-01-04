import matplotlib.pyplot as plt

sizes = [10, 50, 100]
aco_len = [310, 1400, 2780]
sa_len = [320, 1490, 3010]

aco_t = [0.15, 4.6, 16.8]
sa_t = [0.08, 1.9, 7.4]

plt.plot(sizes, aco_len, label="ACO")
plt.plot(sizes, sa_len, label="SA")
plt.xlabel("Cities")
plt.ylabel("Tour Length")
plt.legend()
plt.show()

plt.plot(sizes, aco_t, label="ACO")
plt.plot(sizes, sa_t, label="SA")
plt.xlabel("Cities")
plt.ylabel("Runtime")
plt.legend()
plt.show()
