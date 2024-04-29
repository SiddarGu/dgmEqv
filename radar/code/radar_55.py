import numpy as np
import matplotlib.pyplot as plt

data = np.array([[80, 85, 90, 80, 75],
                 [84, 80, 78, 82, 85],
                 [80, 82, 84, 86, 88],
                 [75, 80, 85, 80, 75],
                 [70, 75, 80, 85, 90]])

data_labels = ["HR Team 1", "HR Team 2", "HR Team 3", "HR Team 4", "HR Team 5"]
line_labels = ["Employee Engagement (Score)", "Recruitment Efficiency (Score)", "Performance Management (Score)", "Learning and Development (Score)", "Employee Retention (Score)"]

data = np.concatenate((data, data[:, :1]), axis=1)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], linewidth=2, label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(1.1, 0.9))

plt.title("Human Resources and Employee Management Efficiency Analysis")

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/141_202312302350.png')

plt.clf()