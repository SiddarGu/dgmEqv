import matplotlib.pyplot as plt
import numpy as np

data = [
    ["Restaurant A", 5, 12, 20, 28, 35, []],
    ["Restaurant B", 8, 10, 15, 20, 28, [45]],
    ["Restaurant C", 10, 15, 25, 30, 40, [2, 50]],
    ["Restaurant D", 6, 13, 22, 31, 40, [1, 55]],
    ["Restaurant E", 7, 15, 23, 32, 39, [60]],
    ["Restaurant F", 5, 10, 15, 20, 30, [70]]
]

data_stats = [i[1:6] for i in data]
outliers = [i[6] for i in data]
labels = [i[0] for i in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(data_stats, patch_artist=True, notch=True, vert=1, whis=1.5)
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF', '#FF0000']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.7)

ax.set_axisbelow(True)
ax.set_title('Price Range per Meal in Food and Beverage Establishments (2023)', fontsize=14, fontweight='bold')
ax.set_xlabel('Restaurant', fontsize=12, fontweight='bold')
ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')

plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_xticklabels(labels, fontsize=10)

ax.margins(y=0.05)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/161_202312310058.png')
plt.clf()
