import numpy as np
import matplotlib.pyplot as plt

data = np.array([[85, 80, 75, 70, 65],
                 [90, 85, 80, 75, 70],
                 [75, 80, 85, 90, 95],
                 [80, 85, 90, 95, 95],
                 [70, 65, 60, 55, 60]])

data_labels = ['Management', 'HR', 'Training', 'Recruitment', 'Policy']
line_labels = ['Employee Retention (%)', 'Job Satisfaction (Score)', 'Training Effectiveness (Score)', 'Recruitment Efficiency (Score)', 'Policy Understanding (Score)']

data = np.concatenate((data, data[:, 0:1]), axis=1)

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(data)):
    ax.plot(angles, data[i], marker='o', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim([0, np.max(data)])
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='lower center')
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

plt.title("Human Resources and Employee Management Performance Analysis")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/98_202312302350.png')
plt.clf()