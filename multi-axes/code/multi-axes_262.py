import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Parse the data into three parts
data_labels = ['Graduates (Thousands)', 'Employment Rate (%)', 'Average Starting Salary (Thousands of Dollars)']
data = np.array([[130, 91, 63], [135, 96, 72], [88, 90, 57], [110, 89, 64], [75, 93, 60], [80, 92, 66], [45, 88, 70], [40, 87, 59], [65, 91, 56], [55, 89, 62]])
line_labels = ['Mechanical Engineering', 'Computer Science', 'Civil Engineering', 'Electrical Engineering', 'Industrial Engineering', 'Chemical Engineering', 'Aerospace Engineering', 'Biomedical Engineering', 'Architectural Engineering', 'Environmental Engineering']

# Plot the data
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color = 'b', alpha = 0.6, label = data_labels[0])
ax1.set_ylabel(data_labels[0], color = 'b')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color = 'r', label = data_labels[1])
ax2.set_ylabel(data_labels[1], color = 'r')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color = 'g', label = data_labels[2], alpha = 0.6)
ax3.set_ylabel(data_labels[2], color = 'g')
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.set_major_locator(AutoLocator())

# Automatically adjust the position of legends to prevent overlaps
fig.legend(bbox_to_anchor=(0.5, 0.92), loc='center', ncol=len(data_labels))

# Set the title for the chart
plt.title('Analysis of Employment and Salary Statistics in Engineering Fields')

# Automatically adjust the size of the image
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/137_202312310108.png')

# Clear the current image state
plt.clf()
