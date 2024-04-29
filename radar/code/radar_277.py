
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Region A', 'Region B', 'Region C', 'Region D']
line_labels = ['Education', 'Infrastructure', 'Employment', 'Healthcare', 'Public Safety']
data = [[80, 85, 90, 95], [75, 80, 85, 90], [70, 75, 80, 85], [65, 70, 75, 80], [90, 95, 100, 105]]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i, row in enumerate(data):
    row = np.append(row, row[0])
    ax.plot(angles, row, linewidth=1, label=line_labels[i], color=f'C{i}')
    ax.fill(angles, row, 'teal', alpha=0.1)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.amax(data))
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.title('Government and Public Policy Performance Report')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/7.png')
plt.clf()