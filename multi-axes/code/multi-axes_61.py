import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

data_labels = ['Number of Employees', 'Annual Turnover Rate (%)', 'Average Monthly Salary (Dollars)', 'Average Employee Satisfaction Score (Out of 5)']
line_labels = ['Sales', 'Marketing', 'Customer Service', 'IT', 'HR', 'Finance', 'Operations', 'Admin', 'Legal', 'R&D']
data = np.array([[356,15,4500,3.5], [245,12,4000,3.8], [500,18,3500,3.2], [300,10,6000,4.0], [150,7,5000,4.2], [200,9,5500,3.9], [400,17,4000,3.6], [100,5,4500,4.1], [75,4,7000,4.3], [150,8,6500,4.5]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='blue', alpha=0.6, label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='green', linestyle='-', marker='o', markersize=4, linewidth=1, label=data_labels[1])

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:,2], color='red', alpha=0.5, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:,3], color='purple', label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))

fig.suptitle('Human Resources Report: Salary, Turnover, and Satisfaction Analysis')

ax1.set_xlabel('Department')
ax1.set_ylabel(data_labels[0], color='blue')
ax2.set_ylabel(data_labels[1], color='green')
ax3.set_ylabel(data_labels[2], color='red')
ax4.set_ylabel(data_labels[3], color='purple')

ax1.yaxis.grid(True)
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend()

fig.autofmt_xdate()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/235_202312311051.png')
plt.clf()
