import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parsing the string to get values
data_string = 'Platform,Active Users (Million),Monthly Visited (Million),Yearly Revenue ($Billion)/n Facebook,2449,900.6,850.8/n Instagram,1000,643.2,200/n YouTube,2000,1323.3,150.1/n Twitter,330,166.5,307/n LinkedIn,690,130.9,802 '
data_list = data_string.split('/n ')
labels, *data = [s.split(',') for s in data_list]

x_values = [item[0] for item in data]
y_values = labels[1:]
data = np.array([list(map(np.float32, item[1:])) for item in data])

# Create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bar chart
colors = ['r', 'g', 'b']  # colors for different y_values (Active Users, Monthly Visited, and Yearly Revenue)
for c, y_value in zip(colors, y_values):
    xpos = np.arange(len(x_values))
    ypos = [y_values.index(y_value)]*len(x_values)
    zpos = np.zeros(len(x_values))
    dx = np.ones(len(x_values))*0.5  # width
    dy = np.ones(len(x_values))*0.5  # depth
    dz = data[:, y_values.index(y_value)]  # height
    
    # Draw a group of bars
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=c, alpha=0.6)

# Labels and title set up
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right', va='bottom')  # x-axis labels with rotation
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')  # y-axis labels
ax.set_title('Social Media Platforms: User Activity And Yearly Revenue Analysis')

# Save and show the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/278_202312310050.png', format='png')
plt.clf()  # Clear the current figure
