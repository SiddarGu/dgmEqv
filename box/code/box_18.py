

import matplotlib.pyplot as plt
import numpy as np

data = [[100, 500, 1000, 1500, 2000], [150, 600, 1100, 1600, 2100], [200, 700, 1200, 1700, 2200], [250, 800, 1300, 1800, 2300], [300, 900, 1400, 1900, 2400]]
outliers = [[], [2500], [50, 3000], [2500, 2900], [2800]]

line_labels = ['Plant A', 'Plant B', 'Plant C', 'Plant D', 'Plant E']

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, patch_artist=True)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

ax.set_title("Electrical Output Distribution of Power Plants in 2020")
ax.set_xticklabels(line_labels)
ax.set_ylabel("Output (KW)")
ax.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)

fig.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/3_202312251520.png")
plt.clf()