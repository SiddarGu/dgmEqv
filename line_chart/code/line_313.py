
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2017,100,200,250,300],
                [2018,110,220,270,320],
                [2019,120,210,280,310],
                [2020,130,230,290,330]])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(data[:, 0], data[:, 1], label="Wheat")
ax.plot(data[:, 0], data[:, 2], label="Rice")
ax.plot(data[:, 0], data[:, 3], label="Corn")
ax.plot(data[:, 0], data[:, 4], label="Barley")

plt.xticks(data[:, 0])
plt.legend()
plt.title('Crop yields in four major crops from 2017-2020')
plt.tight_layout()
plt.savefig("line chart/png/56.png")
plt.clf()