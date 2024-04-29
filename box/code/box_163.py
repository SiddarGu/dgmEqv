import matplotlib.pyplot as plt
import numpy as np

data = [["Social Networking", 1, 2, 3, 4, 5, []], 
        ["Online Shopping", 1.2, 1.8, 2.5, 3.2, 4, []], 
        ["Online Gaming", 0.8, 1.6, 2.4, 3.2, 4, [0.2, 5.6]], 
        ["Streaming", 1.1, 1.7, 2.8, 3.4, 4.1, []], 
        ["Virtual Learning", 1.3, 2, 3, 4, 5, [6]]]

box_data = [item[1:6] for item in data]
outliers_data = [item[6] for item in data]
labels = [item[0] for item in data]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

bp = ax.boxplot(box_data, patch_artist=True, notch=True, vert=1, whis=1.5)
ax.set_xticklabels(labels, rotation=45, ha="right", rotation_mode="anchor", wrap=True)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'yellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for i,outlier in enumerate(outliers_data):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x', color='k', markersize=4)
        
ax.set_title('Internet Activity Duration Distribution (2022)')
ax.set_ylabel('Duration (Hours)')
ax.yaxis.grid(True)
ax.xaxis.grid(False)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/189_202312310058.png')
plt.clf()
