import matplotlib.pyplot as plt
import numpy as np

platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn", "Reddit", "Snapchat", "YouTube"]
category_data = [[2, 11, 20, 29, 38], [5, 14, 23, 32, 41], [3, 12, 21, 30, 39], [4, 13, 22, 31, 40], [1, 10, 19, 28, 37], [6, 15, 24, 33, 42], [7, 16, 25, 34, 43]]
outliers_data = [[], [50.5, 55.7], [0.1, 48.4], [1.2, 47.8], [], [52.0], [54.7]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(category_data, vert=0, whis=1.5, patch_artist=True, medianprops={'linewidth': 2})

for i, outliers in enumerate(outliers_data):
    if outliers:
        ax.plot(outliers, [i + 1] * len(outliers), "ro")

ax.set_title('User Engagement Time Distribution on Social Media Platforms (2022)')
ax.set_yticklabels(platforms)
ax.set_xlabel('Engagement Time (Minutes)')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.set_xticklabels(ax.get_xticks(), rotation=45)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/137_202312270030.png")
plt.clf()
