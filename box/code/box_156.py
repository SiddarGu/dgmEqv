
import matplotlib.pyplot as plt
import numpy as np

data = [[50, 100, 150, 200, 300],
        [60, 90, 130, 170, 250],
        [70, 110, 140, 180, 220],
        [45, 85, 115, 145, 210],
        [40, 75, 105, 135, 185]]
outliers = [[], [400], [1, 10], [300, 350], [400, 450]]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
categories = ['Network A', 'Network B', 'Network C', 'Network D', 'Network E']
ax.boxplot(data, whis=1.5, notch=True, patch_artist=True, sym='k+', labels=categories)

for i, outlier in enumerate(outliers):
    if outlier:
        x = np.array([i + 1] * len(outlier))
        ax.plot(x, outlier, 'k+')

ax.set_ylabel('Number of Posts (Daily)')
ax.set_title('Daily Post Number Distribution in Social Networks (2021)')

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/30_202312251608.png')
plt.clf()