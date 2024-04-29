
import numpy as np
import matplotlib.pyplot as plt

data = np.array([['Category', 'Number of Employees', 'Average Salary (USD)', 'Average Age', 'Average Work Hours'],
                 ['HR Specialists', 2300, 50000, 35, 40],
                 ['Senior Managers', 500, 90000, 45, 50],
                 ['Office Administrators', 1000, 45000, 30, 45],
                 ['Junior Managers', 200, 60000, 32, 50],
                 ['IT Specialists', 700, 65000, 25, 40],
                 ['Sales Representatives', 1000, 40000, 27, 45],
                 ['Recruiters', 400, 70000, 40, 45],
                 ['Customer Service Representatives', 1200, 35000, 24, 40]])

data_labels = data[0, 1:]
line_labels = data[1:, 0]
data = data[1:, 1:].astype(float)

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width=0.5, color='#00A0A0', alpha=1)
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='#00A0A0')
ax1.tick_params(axis='y', labelcolor='#00A0A0')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], '-b', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='b')
ax2.tick_params(axis='y', labelcolor='b')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], '-r', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', labelcolor='r')
ax3.spines['right'].set_position(('axes', 1.1))

ax4 = ax1.twinx()
ax4.plot(line_labels, data[:, 3], '-g', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='g')
ax4.tick_params(axis='y', labelcolor='g')
ax4.spines['right'].set_position(('axes', 1.2))

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4)
ax1.grid(False)
ax1.set_title('Human Resources and Employee Management Overview: Insight into Staffing and Salaries')
ax1.autoscale(enable=True, axis='both', tight=True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/39_2023122270030.png')
plt.clf()