import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Smith High School', 'Jones Middle School', 'Baker Elementary School', 'Wilson Private School', 'Lee University']
line_labels = ['Literacy Rate (%)', 'Dropout Rate (%)', 'Teacher-Student Ratio', 'SAT Average Score', 'Graduation Rate (%)']
data = np.array([[98, 97, 96, 99, 100],
                 [1, 3, 2, 0, 0],
                 [18, 22, 24, 15, 12],
                 [12, 0, 0, 14, 15],
                 [98, 0, 0, 100, 95]])

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i, row in enumerate(data):
    color = plt.cm.Set2(i / len(data))
    ax.plot(angles, row, color=color, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.1, 1))
ax.set_title('Comparative Analysis of Education Institutions')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/89_202312302350.png')
plt.close()