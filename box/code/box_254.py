import matplotlib.pyplot as plt
import numpy as np

data = [['Mechanical Engineering', [6, 12, 18, 24, 30], []],
        ['Civil Engineering', [8, 15, 22, 29, 36], [48]],
        ['Chemical Engineering', [7, 14, 21, 28, 35], [50, 52]],
        ['Electrical Engineering', [9, 18, 27, 36, 45], [4, 60]],
        ['Aerospace Engineering', [5, 10, 15, 20, 25], [35]]]

labels, box_data, outliers = zip(*data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the boxplot
bp = ax.boxplot(box_data, whis=1.5, vert=False, patch_artist=True, widths=0.7)

colors = ['pink', 'lightblue', 'lightgreen', 'tan', 'purple']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'o', color='black')

ax.set_yticklabels(labels, rotation=0)

ax.set_xlabel('Project Duration (Months)')
ax.set_title('Project Duration Distribution in Various Engineering Fields (2022)')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Saving the figure to the specified path
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/76_202312270030.png')

plt.clf()
