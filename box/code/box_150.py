
import matplotlib.pyplot as plt
import numpy as np

data = [[200, 400, 550, 700, 900], 
        [300, 500, 700, 900, 1100], 
        [400, 600, 800, 1000, 1200], 
        [250, 500, 650, 800, 1000], 
        [450, 600, 800, 1000, 1200]]

outliers = [[], [1500], [100, 1400], [1200], [1400]]
line_labels = ['Rice', 'Wheat', 'Corn', 'Soybeans', 'Barley']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.boxplot(data, whis=1.5)

ax.set_title('2019 Crop Yield Distribution in Agriculture and Food Production')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Yield (Kg)')

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

ax.grid(axis='y')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/50_202312251608.png')
plt.clf()