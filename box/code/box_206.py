import matplotlib.pyplot as plt
import numpy as np

categories = ['Hotel Alpha', 'Hotel Bravo', 'Hotel Charlie', 'Hotel Delta', 'Hotel Echo']
box_data = [[5,8,10,12,15], [7,9,11,13,16], [6,8,10,12,14], [4,7,9,11,14], [5,8,11,13,15]]
outliers_data = [[], [3,4], [17], [2,16,18], [20]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(box_data, whis=1.5, vert=False, patch_artist=True, notch=True, bootstrap=5000)

colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers_data):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "o", color='black') 

ax.set_yticklabels([h.replace(' ', '\n') for h in categories])
ax.set_xlabel('Check In Time (Minutes)')
ax.set_title('Check In Time Distribution in Different Hotels')
gridlines = ax.get_xticklines() + ax.get_yticklines()
for line in gridlines:
    line.set_linewidth(0.3)

plt.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/101_202312270030.png')
plt.clf()
