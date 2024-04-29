import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Term 1', 'Term 2', 'Term 3', 'Term 4']
data = np.array([
    [85, 88, 90, 92],
    [90, 95, 92, 94],
    [80, 85, 90, 95],
    [70, 75, 80, 85],
    [85, 90, 95, 100]
])
line_labels = ['Mathematics', 'English', 'Science', 'History', 'Art']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
ax.set_title('Student Academic Performance Evaluation in Different Subjects', size=20, color='black', y=1.1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

colors = ["b", "r", "g", "y", "m"]

for i, row in enumerate(data):
    row = np.append(row, row[0])
    ax.plot(angles, row, color=colors[i], label=line_labels[i])
    ax.fill(angles, row, color=colors[i], alpha=0.25)
    ax.plot(angles, np.full_like(angles, (i + 1) * np.max(data) / len(data)), color=colors[i], alpha=0.1)

ax.set_rlim(0, np.max(data))
ax.xaxis.grid(True, color='gray', linestyle='dashed')
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i / 1.5 for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=30)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/112_2023122292141.png')
plt.clf()
