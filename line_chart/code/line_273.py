
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))
ax = plt.subplot()

x = np.arange(2015, 2020)
y1 = np.array([1000, 1200, 800, 1500, 1100])
y2 = np.array([800, 900, 1100, 1200, 1400])
y3 = np.array([1200, 1100, 1300, 1400, 1600])

plt.plot(x, y1, label="Wheat (metric tons)")
plt.plot(x, y2, label="Rice (metric tons)")
plt.plot(x, y3, label="Maize (metric tons)")

plt.title("Crops Production in the UK from 2015-2019")
plt.xlabel("Year")
plt.ylabel("Metric Tons")

ax.set_xticks(x)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.savefig('line chart/png/191.png')

plt.clf()