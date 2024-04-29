
import numpy as np
import matplotlib.pyplot as plt

data = [[1,3,4.5,6,7.5],
        [2,4,5.5,7,9],
        [1.5,3.5,4.7,6.1,8.5],
        [2.5,4.5,6,7.5,9.5],
        [1.2,3.2,4.3,5.8,7.2]]

outliers = [[], [10, 11], [0.5], [15], [9.9]]
line_labels = ['Wheat', 'Rice', 'Corn', 'Soybean', 'Barley']

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5)
ax.set_title('Crop Yield Distribution in Agriculture and Food Production in 2021')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Yield (Tonnes)')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i+1, len(outlier)), outlier, 'r*', markersize=10)

plt.grid(True, lw=1, ls='--', c='.9')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/38_202312270030.png')
plt.clf()