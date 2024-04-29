import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 70, 75, 85, 87, 90],
                 [95, 93, 90, 88, 92, 94],
                 [87, 89, 85, 92, 95, 93],
                 [80, 85, 90, 75, 80, 85],
                 [70, 75, 80, 65, 70, 75]])

data_labels = ['Biology', 'Physics', 'Mathematics', 'English', 'Literature', 'History']
line_labels = ['Student Engagement (Score)', 'Faculty Expertise (Score)', 'Course Material Quality (Score)', 'Library Resources (Score)', 'Research Opportunities (Score)']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i, row in enumerate(data):
    ax.plot(angles, row, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

plt.title('Comparative Analysis of Academic Subjects')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/114_202312302350.png')
plt.clf()
