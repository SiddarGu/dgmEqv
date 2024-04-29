import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Parse the data
raw_data = "Quarter,Total Revenue ($M),Net Profit ($M),Number of Employees/n Q1-2020,200,50,500/n Q2-2020,210,55,510/n Q3-2020,225,60,530/n Q4-2020,240,70,550/n Q1-2021,250,80,580/n Q2-2021,260,85,600 ".split('/n ')
header = raw_data[0].split(',')
y_values = header[1:]
x_values = [row.split(',')[0] for row in raw_data[1:]]
data = np.array([row.split(',')[1:] for row in raw_data[1:]]).astype(np.float32)

# Create figure and 3D subplot
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over the data
width = 0.3
colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    # Plot each column of data separately
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             width, width, data[:, i], color=colors[i%len(colors)], shade=True, alpha=0.6)

# Rotate the x-axis labels for better readability
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=-30, horizontalalignment='center')

# Set the y-axis ticks and labels 
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Set the title and other plot details
ax.set_title('Business Financial Performance and Employee Count 2020-2021')
ax.set_xlabel('Quarter')
ax.grid(True)

# Adjust the viewing angle for better readability
ax.view_init(30, -45)

# Resize the image by tight_layout
plt.tight_layout(pad=2)

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/223_202312302235.png', dpi=300)

# Clear the current image state
plt.clf()
