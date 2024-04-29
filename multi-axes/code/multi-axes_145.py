import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# processing input data
input_data = """Department,Number of Employees,Average Salary (USD),Employee Turnover Rate (%),Sick Days Per Employee
               Human Resources,55,60000,10,5
               Marketing,45,65000,12,3
               Sales,75,70000,15,6
               IT,60,75000,8,2
               Customer Service,70,55000,20,7
               Legal,30,80000,5,3
               Finance,40,70000,7,2
               Operations,80,60000,18,4
               Administration,35,50000,22,8"""
input_data = [i.split(',') for i in input_data.split('\n')]
data_labels = input_data[0][1:]
line_labels = [i[0] for i in input_data[1:]]
data = np.array([i[1:] for i in input_data[1:]], dtype=float)

# creating multi-axes chart
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.set_tick_params(colors='b')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.yaxis.set_tick_params(colors='r')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='g', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='g')
ax3.yaxis.set_tick_params(colors='g')
ax3.yaxis.set_major_locator(AutoLocator())

ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], color='c', alpha=0.3, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color='c')
ax4.yaxis.set_tick_params(colors='c')
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.title('Human Resources Analysis: Employee Management Metrics')
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/254_202312311051.png')
plt.clf()
