
import matplotlib.pyplot as plt
import numpy as np

data = [[[30, 50, 70, 90, 120], [20, 40, 60, 80, 110], [25, 45, 65, 85, 105], [15, 35, 55, 75, 95], [40, 60, 80, 100, 130]],
        [[], [140], [10, 130], [110, 140], [115]]]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

for i, (box, outlier) in enumerate(zip(data[0], data[1])):
    ax.boxplot(box, whis=1.5, positions=[i + 1], widths=0.3,
               showmeans=True, showfliers=False, medianprops=dict(color='black'), meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='black'))
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro', alpha=0.5, label='Outliers')

ax.set_title('Share Prices Distribution of Stocks in the Financial Market (2021)', fontsize=14)
ax.set_xticks(np.arange(1, 6))
ax.set_xticklabels(['Stock A', 'Stock B', 'Stock C', 'Stock D', 'Stock E'], rotation=30, fontsize=12, wrap=True)
ax.set_ylabel('Share Prices (USD)', fontsize=12)
ax.grid(axis='y', linestyle='-.')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/9_202312251520.png')
plt.clf()