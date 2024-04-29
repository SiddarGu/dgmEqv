import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [85, 90, 88, 87, 89],
    [90, 89, 91, 92, 90],
    [93, 92, 94, 93, 95],
    [88, 90, 89, 91, 92],
    [78, 80, 79, 82, 83]
])
data_labels = ['Harvard', 'Yale', 'Stanford', 'Oxford', 'Cambridge']
line_labels = ['Research Output (Score)', 'Student Satisfaction (Score)', 'Faculty Quality (Score)', 'Infrastructure Quality (Score)', 'International Outlook (Score)']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(data)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='center')

ax.set_title('Comparative Analysis of Top Universities')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/123_202312302350.png')
plt.close(fig)