
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2015, 80, 50, 90], 
               [2016, 90, 60, 100], 
               [2017, 95, 75, 110],
               [2018, 100, 85, 120],
               [2019, 110, 90, 130]])

plt.figure(figsize=(10,5))

plt.plot(data[:, 0], data[:, 1], label="Revenue from Stadium", marker="o")
plt.plot(data[:, 0], data[:, 2], label="Revenue from Merchandise", marker="o")
plt.plot(data[:, 0], data[:, 3], label="Revenue from Broadcasting", marker="o")

plt.xticks(data[:, 0], fontsize=10)

plt.title("Revenue sources of a professional sports team from 2015 to 2019")
plt.xlabel("Year")
plt.ylabel("Revenue (million dollars)")

for i in range(data.shape[0]):
    plt.annotate(data[i, 1], xy=(data[i, 0], data[i, 1]), rotation=45, ha="right", wrap=True, fontsize=10)
    plt.annotate(data[i, 2], xy=(data[i, 0], data[i, 2]), rotation=45, ha="right", wrap=True, fontsize=10)
    plt.annotate(data[i, 3], xy=(data[i, 0], data[i, 3]), rotation=45, ha="right", wrap=True, fontsize=10)

plt.legend(loc='best')
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig("line chart/png/581.png")
plt.clf()