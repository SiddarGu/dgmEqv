import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Data processing
data_string = """Department,Number of Employees,Training Hours Per Employee,Employee Retention Rate (%)
HR,200,30,89
Marketing,180,25,92
Engineering,250,32,87
Sales,220,28,91
IT,150,35,94"""
data_list = data_string.split('\n')

# Extracting the y-axis labels (metrics)
y_labels = data_list[0].split(',')[1:]
# Extracting the x-axis values (departments)
x_labels = [row.split(',')[0] for row in data_list[1:]]
# Extracting the data
data = np.array([row.split(',')[1:] for row in data_list[1:]], dtype=float)

# 3D plot setup
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Number of bars to be placed
num_bars = len(y_labels)
# Width of each bar
bar_width = 0.2

# Iterate over each department
for i, dept in enumerate(data):
    # Position of the bars for this department
    xpos = [i + bar_width * (j - num_bars / 2) for j in range(num_bars)]
    ypos = [0, 1, 2]  # Always the same, as the y-axis is fixed for metrics
    zpos = np.zeros(num_bars)

    # Height of bars is the data values
    dz = dept
    # Set the bar properties and plot
    ax.bar3d(xpos, ypos, zpos, bar_width, bar_width, dz, alpha=0.6)

# Setting labels and titles
ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels, rotation=-45, horizontalalignment='right')
ax.set_yticklabels(y_labels, horizontalalignment='left')

ax.set_xlabel('Department')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')
ax.set_title('Departmental Overview: Employees, Training, and Retention')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/62_202312302126.png')
plt.clf()
