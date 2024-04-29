import matplotlib.pyplot as plt
import numpy as np

subject_areas = ["Psychology", "Philosophy", "Sociology", "Linguistics", "History"]
data_box = [[10, 45, 70, 95, 120], [30, 60, 80, 100, 150], [20, 50, 70, 95, 140], [15, 35, 55, 75, 110], [25, 55, 75, 100, 130]]
outliers_data = [[5, 160], [], [10, 190], [150], [180]]

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot(111)
ax.boxplot(data_box, whis=1.5)

for i, outlier in enumerate(outliers_data):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")
        
ax.set_title('Study Time Distribution in Humanities Subject Areas (2020)')
ax.set_ylabel('Study Time (Hours)')
plt.xticks(np.arange(1, len(subject_areas) + 1), subject_areas, rotation=30)
ax.yaxis.grid(True)
ax.xaxis.grid(True)
fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/212_202312310058.png')
plt.clf()
