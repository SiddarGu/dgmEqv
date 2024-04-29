
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

fields = ["Biology","Chemistry","Mathematics","History","Literature"]
values = [[58,72,84,92,100],
          [56,68,80,88,96],
          [48,62,72,80,90],
          [70,78,84,90,99],
          [75,83,89,95,100]]

ax.boxplot(values,labels=fields,showmeans=True,patch_artist=True,
           medianprops=dict(linewidth=2.5, color='black'))

# handle the outlier
ax.plot([2], [95.5], marker='o', markersize=8, color="red")
ax.scatter([3,3], [20,93.5], marker='o', s=96, color="red")
ax.plot([4], [97.5], marker='o', markersize=8, color="red")
ax.plot([5], [85.5], marker='o', markersize=8, color="red")

ax.set_title("Academic Performance Distribution in Social Sciences and Humanities (2020)")
ax.set_ylabel("Grade (%)")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/19_202312251044.png")

plt.clf()