import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Graduation Rate', 'Student Satisfaction', 'Faculty Qualification', 'Course Diversity', 'Research Output']
line_labels = ['Public High School', 'Community College', 'State University', 'Ivy League Institutes', 'Online Learning Platform']
data = np.array([[85,70,95,99,60],
                [80,75,90,95,70],
                [90,80,95,98,85],
                [70,80,85,90,95],
                [65,70,90,99,60]])

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

for i, line_label in enumerate(line_labels):
    ax.plot(angles, data[i], linewidth=2, label=line_label)

ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
ax.set_rticks([0, 20, 40, 60, 80, 100])
ax.set_ylim(0, 100)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

plt.title('Comparison of Educational Institutions Performance')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/193_202312310100.png')
plt.close(fig)