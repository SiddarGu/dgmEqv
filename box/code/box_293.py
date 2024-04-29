import matplotlib.pyplot as plt
import numpy as np

# restructure data
category = ['Solar', 'Wind', 'Hydro', 'Natural Gas', 'Nuclear']
data = [[12, 18, 23, 28, 35],
       [15, 22, 27, 32, 40],
       [18, 25, 30, 36, 45],
       [20, 28, 34, 40, 50],
       [22, 30, 38, 46, 55]]
outliers = [[], [10, 50], [16, 52], [18, 55], [20, 60]]

# create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# box plot
bp = ax.boxplot(data, notch=True, patch_artist=True, widths=0.4, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'cyan']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# iterate through outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# styles
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_title('Energy Efficiency Distribution by Different Sources (2022)')
ax.set_xlabel('Energy Source')
ax.set_ylabel('Efficiency (%)')

plt.setp(ax, xticks=[y + 1 for y in range(len(data))],
         xticklabels=category)

# save and show plot
plt.autoscale()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/180_202312310058.png')
plt.clf()
