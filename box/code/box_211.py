

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data = [[8,15,20,30,50],
        [12,18,24,36,56],
        [10,16,22,28,46],
        [6,14,20,26,42],
        [9,17,23,33,53]]

outliers = [[],
            [71],
            [0.8,65],
            [50,60],
            [62]]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)

labels = ["Structural Engineering", "Mechanical Engineering",
          "Electrical Engineering", "Civil Engineering", "Chemical Engineering"]
ax.set_xticklabels(labels, rotation=45, ha="right")

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.full(len(outlier), i+1), outlier, "ro")

ax.set_title("Weight Distribution in Engineering Fields in 2021")
ax.set_ylabel('Weight (kg)')
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/24_202312270030.png')

plt.clf()