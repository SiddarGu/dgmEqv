import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 85, 75, 80, 90],
                [75, 80, 90, 85, 80],
                [70, 80, 85, 75, 90],
                [95, 90, 85, 80, 85],
                [85, 90, 75, 80, 80]])

data_labels = ['History', 'Anthropology', 'Psychology', 'Philosophy', 'Literature']
line_labels = ['Research Quality (Score)', 'Teaching Quality (Score)', 'Student Satisfaction (Score)', 'Publications (Score)', 'Impact Factor (Score)']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])
    
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)

ax.set_rlabel_position(0)
max_value = np.amax(data)
ax.set_ylim(0, max_value)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

plt.title('Analysis of Performance in Social Sciences and Humanities Departments')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/80_202312302350.png')

plt.clf()