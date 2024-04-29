

import matplotlib.pyplot as plt
import numpy as np

data = [[500, 900, 1500, 2100, 3000], [350, 750, 1200, 1750, 2500], 
[400, 800, 1300, 1800, 2700], [600, 1000, 1600, 2100, 3000], 
[450, 750, 1200, 1750, 2500]]
outliers = [[], [5000], [300, 4000], [2, 3500], [3000, 4500]]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

ax.boxplot(data, whis=1.5, patch_artist=True)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', mfc='none', mec='black', ms=7, mew=2)

ax.set_ylabel('Cost (USD)', fontsize=14)
ax.set_title('Price Range of Different Arts and Culture Forms in 2021', fontsize=14)
ax.set_xticklabels(['Painting', 'Music', 'Photography', 'Theater', 'Dance'], fontsize=14)
ax.grid(axis='y', linestyle='dotted')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14_202312270030.png')
plt.clf()