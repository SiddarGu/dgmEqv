
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Transform the data 
data_labels = ['Number of Employees','Productivity (Units/Hour)','Average Wage (Dollars/Hour)','Average Leave (Hours)']
line_labels = ['Manufacturing','Research and Development','Sales and Marketing','Human Resources','Accounting and Finance','Customer Service','IT and Software','Technical Support']
data = np.array([[8900,14,17,20],[4500,19,24,18], [7200,16,20,25], [2800,12,15,15], [5600,14,18,17], [3100,11,13,22], [6500,17,21,19], [3600,14,16,21]])

#Plot the data
fig = plt.figure(figsize = (15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width = 0.15, color = '#6699FF', alpha = 0.6, label = data_labels[0])
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color = '#6699FF')
ax1.tick_params(axis = 'y', colors = '#6699FF')
ax1.set_title('Human Resources and Employee Management: A Comprehensive Overview of Performance')
ax1.legend(loc = 'lower left')
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'o-', color = '#FF9933', label = data_labels[1])
ax2.set_ylabel(data_labels[1], color = '#FF9933')
ax2.tick_params(axis = 'y', colors = '#FF9933')
ax2.legend(loc = 'upper left')
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], 'o-', color = '#99CC00', label = data_labels[2])
ax3.set_ylabel(data_labels[2], color = '#99CC00')
ax3.tick_params(axis = 'y', colors = '#99CC00')
ax3.spines['right'].set_position(('axes', 1.1))
ax3.legend(loc = 'lower right')
ax4 = ax1.twinx()
ax4.plot(line_labels, data[:, 3], 'o-', color = '#FF6666', label = data_labels[3])
ax4.set_ylabel(data_labels[3], color = '#FF6666')
ax4.tick_params(axis = 'y', colors = '#FF6666')
ax4.spines['right'].set_position(('axes', 1.2))
ax4.legend(loc = 'upper right')

# Autolocator for all ax
ax1.autoscale(enable = True, axis = 'x', tight = True)
ax2.autoscale(enable = True, axis = 'x', tight = True)
ax3.autoscale(enable = True, axis = 'x', tight = True)
ax4.autoscale(enable = True, axis = 'x', tight = True)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/38_2023122261325.png')

# Clear the current image state
plt.clf()