
import matplotlib.pyplot as plt
import numpy as np

# restructure data into two 2d list
data = [[3,7,12,16,20], [4,10,14,18,22,30], [2,6,10,14,18,0.5,20], [5,9,13,17,21,19.5], [4,8,12,16,20, 18]]
outliers = [[], [30], [0.5, 20], [19.5], [18]]

# create figure and draw box plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, whis=1.5, patch_artist=True)

# add outlier points
for i, outlier in enumerate(outliers):
    if len(outlier) != 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'o', markersize=4,
                color='black', alpha=0.6)

# set labels
ax.set_xticklabels(['Chemical Reaction', 'Heat Treatment', 'Laser Cutting', 'Welding', 'Plating'], fontsize=12)
ax.set_ylabel('Processing Duration (Hours)', fontsize=14)
ax.set_title('Processing Duration Distribution in Science and Engineering (2021)', fontsize=16)

# draw background grids
ax.grid(True, axis='y', ls='--', lw=.5, alpha=0.8)

# shrink image size
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/7_202312251608.png')

# clear current image state
plt.clf()