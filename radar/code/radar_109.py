import numpy as np
import matplotlib.pyplot as plt

data_labels = ['High School', 'College', 'Bachelors', 'Masters', 'PhD']
line_labels = ['Mathematics', 'Science', 'Literature', 'History', 'Language']
data = np.array([[85, 90, 95, 97, 98],
                 [80, 83, 86, 89, 91],
                 [82, 85, 89, 92, 95],
                 [84, 88, 91, 94, 97],
                 [86, 88, 90, 92, 94]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['b', 'g', 'r', 'c', 'm']
for i in range(len(line_labels)):
    ax.plot(angles, data[i], color=colors[i], marker='o', label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45, ha='left')
ax.set_yticks([])

ax.set_rticks([])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rticks(np.arange(0, np.max(data) + 10, 10))
ax.set_rlim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

plt.title("Academic Performance in Different Educational Levels")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/97_202312302350.png')
plt.close()