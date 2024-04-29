import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Red Cross', 'Oxfam', 'Doctors Without Borders', 'UNICEF', 'Greenpeace']
line_labels = ['Donor Satisfaction', 'Fund Utilization', 'Public Awareness', 'Impact Evaluation', 'Volunteer Experience']

data = np.array([[85, 80, 75, 90, 70],
                 [70, 75, 80, 65, 75],
                 [75, 80, 85, 90, 70],
                 [90, 85, 80, 75, 95],
                 [70, 75, 80, 85, 80]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='lower right')

plt.title('Performance Analysis of Charity and Nonprofit Organizations')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/203_202312310100.png')
plt.close()