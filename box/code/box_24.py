
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data = [[10,30,45,60,75],
        [20,35,50,70,90],
        [15,40,55,70,85],
        [5,25,37,50,62],
        [13,32,45,60,77]]
outliers = [[],
            [120,135],
            [2,5],
            [80],
            [95]]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.boxplot(data, whis=1.5)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i+1] * len(outlier), outlier, "o")

ax.set_title("Delivery Time Distribution of Transportation and Logistics Services in 2021")
ax.set_xlabel("Delivery Service")
ax.set_ylabel("Delivery Time (Minutes)")

labels = ["Delivery Company A", "Delivery Company B", "Delivery Company C", "Delivery Company D", "Delivery Company E"]
ax.set_xticklabels(labels, rotation=45, ha="right", wrap=True)
ax.grid(True)

fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/25_202312270030.png")
plt.clf()