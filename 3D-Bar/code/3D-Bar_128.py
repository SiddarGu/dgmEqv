import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data:
dataset = """Product,Annual Sales (Million $),Market Share (%),Projected Growth (%)
           Wine,1200,25,10
           Beer,1500,32,12
           Spirits,1100,23,15
           Non-Alcoholic Beverages,800,20,18"""

# Transform data into required format 
data = dataset.split("\n")
y_values = data[0].split(",")[1:]
x_values = [row.split(",")[0] for row in data[1:]]
data_values = np.array([list(map(float, row.split(",")[1:])) for row in data[1:]])

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set the bar settings
bar_width = 0.25
bar_depth = 0.5
colors = ['r', 'g', 'b', 'y']

# Plot bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
              bar_width, bar_depth, data_values[:, i], color=colors[i], alpha=0.8)

# set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# set title and other settings
ax.set_title('Sales and Market Analysis in Food and Beverage Industry')
ax.view_init(elev=25., azim=-50)
ax.grid(False)

# Resize figure layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/104_202312302126.png', dpi=300)

# Clear the current figure
plt.clf()
