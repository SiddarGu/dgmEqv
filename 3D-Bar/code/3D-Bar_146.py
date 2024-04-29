import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define data
raw_data = [['January',300,250,200,300],
 ['February',280,140,180,280],
 ['March',350,250,220,350],
 ['April',390,150,250,390],
 ['May',600,266,300,600],
 ['June',650,166,320,650]]

x_values = [row[0] for row in raw_data]
y_values = ["Number of Shipments", "Average Delivery Time", "Freight Cost", "Revenue Generated"]
data = np.array([row[1:] for row in raw_data], dtype=np.float32)

# Creating figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Creating color dictionary for distinct bar colors
colors = ['r', 'b', 'g', 'y']

# Creating three dimensional bar plot
for c, k in zip(colors, range(4)):
    xs = np.arange(len(x_values))
    ys = np.full(len(x_values), k)
    
    dx = np.full(len(x_values), 0.8)
    dy = np.full(len(x_values), 0.8)
    dz = data[:,k]
    
    ax.bar3d(xs, ys, np.zeros_like(dz), dx, dy, dz, color=c, alpha=0.7)

# Setting labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values)
# Setting plot title and labels
ax.set_title('Monthly Transportation and Logistics Performance Metrics - First Half of the Year')

# Adjusting the viewing angle
ax.view_init(elev=10., azim=150)

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/82_202312302126.png')

# Clear the current figure's state
plt.clf()
