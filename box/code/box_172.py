import matplotlib.pyplot as plt
import numpy as np

# preprocessed data
data = [['Philosophy', [2, 5, 10, 15, 20], []],
        ['Literature', [3, 6, 12, 18, 24], [1, 30]],
        ['Anthropology', [2, 7, 11, 17, 23], [4, 28]],
        ['History', [3, 6, 13, 19, 25], [0, 32]],
        ['Sociology', [2, 4, 8, 12, 16], [26]]]

# data restructing
labels = [item[0] for item in data]
data_to_plot = [item[1] for item in data]
outliers = [item[2] for item in data] 

# figure and subplot
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)

# plotting
bp = ax.boxplot(data_to_plot, notch=True, vert=1, whis=1.5, patch_artist=True, labels=labels, manage_ticks=True)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']
for box, color in zip(bp['boxes'], colors):
    box.set(color='#000000', linewidth=2)
    box.set_facecolor(color)

# adding outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ko")

# styling
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_title('Study Time Distribution in Humanities Subjects (Semester-1 2021)')
ax.set_ylabel('Study Time (Hours)')
plt.xticks(rotation=45)

# save and display
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/136_202312270030.png', dpi=300)
plt.clf()
