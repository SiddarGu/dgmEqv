

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Transform the given data into three variables
data_labels = ['No. of Employees','Average Working Hour','Average Wage (Dollars)','Turnover Rate (%)']
line_labels = ['Administration','Human Resources','Security','Clerical','Retail','Manufacturing','Logistics','Maintenance','Sales']
data = np.array([[2145,37,18.6,6.2],
                 [1539,40,20.2,7.4],
                 [1790,41,23.7,4.7],
                 [1250,36,14.9,5.1],
                 [1340,37,17.3,3.6],
                 [1932,40,19.1,7.1],
                 [1450,41,20.8,4.2],
                 [1548,38,18.4,4.9],
                 [1890,38,16.2,6.3]])

# Plot the data with the type of multi-axes chart
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# The first column of data array, i.e., data[:,0] is plotted first
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='#eb5f5f', width=0.7)
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='#eb5f5f')
ax1.tick_params('y', colors='#eb5f5f')
ax1.set_ylim(1000, 2500)

# The second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2
ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], label=data_labels[1], color='#6be2f3', s=50)
ax2.set_ylabel(data_labels[1], color='#6be2f3')
ax2.tick_params('y', colors='#6be2f3')
ax2.set_ylim(30, 50)

# The third column of data array, i.e. data[:,2], is plotted after using another twinx
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], label=data_labels[2], color='#f9a24a', linewidth=3)
ax3.set_ylabel(data_labels[2], color='#f9a24a')
ax3.tick_params('y', colors='#f9a24a')
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylim(10, 30)

# The fourth column of data array, i.e. data[:,3], is plotted after using another twinx
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], 0, label=data_labels[3], alpha=0.3, color='#c3e8b2')
ax4.set_ylabel(data_labels[3], color='#c3e8b2')
ax4.tick_params('y', colors='#c3e8b2')
ax4.spines['right'].set_position(('axes', 1.2))
ax4.set_ylim(0, 10)

# Label all axes, and match their colors with the data plotted against them
ax1.set_title('Human Resources and Employee Management Performance Overview')
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower right')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/34_2023122261325.png')

# Clear the current image state at the end of the code
plt.clf()