
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Revenue (Billion $)', 'Net Profit (Billion $)', 'Employees (Thousands)', 'Debt (Billion $)']
line_labels = ['Apple', 'Microsoft', 'Amazon', 'Facebook', 'Google', 'JPMorgan']
data = np.array([[270, 60, 130, 50],
                 [130, 45, 105, 10],
                 [350, 80, 220, 35],
                 [85, 25, 90, 20],
                 [160, 50, 100, 30],
                 [90, 30, 80, 15]])

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot()
cmap = cm.get_cmap('viridis')
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

# For each row of data, the third value is mapped to the bubble size, and the fourth value is mapped to the color value.
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=5000*data[i,2]/data[:,2].max() + 600, c=cmap(norm(data[i,3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i,3])), label=line_label + f' {data[i, 2]}', s=20)

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, label=data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted
ax.grid(True, ls='--')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set the title of the figure
plt.title('Financial Performance of Top Business Companies in 2023')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/49_2023122270050.png')

# Clear the current image state at the end of the code
plt.clf()