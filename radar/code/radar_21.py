
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
line_labels = ['Employee Engagement (Score)', 'Workplace Environment (Score)', 'Job Satisfaction (Score)', 'Training Efficiency (Score)', 'Workplace Safety (Score)']
data = np.array([[80, 85, 90, 95, 100], [70, 75, 80, 85, 90], [75, 80, 85, 90, 95], [60, 65, 70, 75, 80], [85, 90, 95, 100, 100]])

data = np.concatenate((data, data[:, 0:1]), axis=1)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(polar=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, 100)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2)
    ax.fill(angles, data[i], alpha=0.2)

ax.legend(loc='upper right')
plt.title('Employee Management Evaluation - 2023', fontsize=20)
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9_202312262320.png')
plt.clf()