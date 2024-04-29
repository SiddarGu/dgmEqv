import matplotlib.pyplot as plt
import numpy as np

# Restructure data
data = [
    ['Air', 3, 7, 10, 13, 20, [30, 35]],
    ['Rail', 10, 15, 20, 25, 35, []],
    ['Road', 5, 10, 15, 20, 30, [40, 45]],
    ['Sea', 20, 35, 50, 65, 80, [98]],
    ['Pipeline', 12, 18, 24, 30, 36, [7, 50]]
]

labels, min_time, q1_time, median_time, q3_time, max_time, outliers = zip(*data)

stats = [list(times) for times in zip(min_time, q1_time, median_time, q3_time, max_time)]

# Plotting
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

bp = ax.boxplot(stats, vert=True, patch_artist=True, whis=1.5)

colors = ['#D1C1E9', '#D1C1E9', '#D1C1E9', '#D1C1E9', '#D1C1E9']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.set_title('Delivery Time Distribution in Different Modes of Transport (2022)')
ax.set_ylabel('Time (Hours)')
ax.set_xticks(np.arange(1, len(labels) + 1))
ax.set_xticklabels(labels,rotation=45)

ax.yaxis.grid(True)
ax.xaxis.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/113_202312270030.png')
plt.clf()
