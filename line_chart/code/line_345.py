
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2017, 2018, 2019, 2020])
y1 = np.array([120, 140, 150, 160])
y2 = np.array([30, 35, 40, 45])
y3 = np.array([40, 45, 50, 55])
y4 = np.array([50, 60, 60, 70])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(x, y1, color='red', marker="o", label="Total Crop Yield")
ax.plot(x, y2, color='blue', marker="o", label="Wheat Yield")
ax.plot(x, y3, color='green', marker="o", label="Corn Yield")
ax.plot(x, y4, color='orange', marker="o", label="Rice Yield")
ax.xaxis.set_ticks(x)
ax.grid(linestyle='--')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=2, fancybox=True)
plt.title("Total Crop Yield and Yield of Three Major Crops in the U.S. from 2017 - 2020")
plt.tight_layout()
plt.savefig("line chart/png/202.png")
plt.clf()