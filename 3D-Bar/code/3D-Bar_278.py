import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# The given data
data_string = """Country,Art Exhibitions (Number),Museum Visitors (Thousands),Cultural Events (Number)
USA,300,7000,450
UK,280,6500,400
France,310,7500,500
Italy,290,6800,490
Germany,320,7800,520"""

# Parsing the data
data_list = [line.split(',') for line in data_string.split('\n')]
y_values = data_list[0][1:]
x_values = [line[0] for line in data_list[1:]]
data = np.array([list(map(np.float32, line[1:])) for line in data_list[1:]])

# Create 3D Plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Drawing 3D Bars
for c, z in zip(['r', 'g', 'b'], y_values):
    xs = np.arange(len(x_values))
    ys = data[:, y_values.index(z)]

    ax.bar(xs, ys, zs=y_values.index(z), zdir='y', color=c, alpha=0.8)

# Labeling and rotating X-axis 
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation = 45, horizontalalignment='right')

# Setting Y-axis labels
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Setting the chart title
plt.title('Arts and Culture Activities Statistics by Country')

# Saving the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/128_202312302126.png')

# Clearing the current figure
plt.clf()
