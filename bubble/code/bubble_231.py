

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = np.array(['Revenue (Billion $)', 'Net Profit (Billion $)', 'Employees (Millions)', 'Market Share (%)'])
line_labels = np.array(['Apple', 'Microsoft', 'Amazon', 'Alphabet', 'Facebook', 'Alibaba'])
data = np.array([[265, 62, 1.2, 13],
                [143, 44, 1.7, 8],
                [280, 11.6, 0.6, 14],
                [162, 34.3, 0.9, 19],
                [86.3, 18.5, 0.3, 9],
                [71.4, 13.2, 0.4, 10]])

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(15, 10)) 
ax = fig.add_subplot(111)

# Plot the data with the type of bubble chart
for i in range(data.shape[0]):
    norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
    norm_bubble_size = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
    cmap = cm.get_cmap('RdYlGn')
    ax.scatter(data[i, 0], data[i, 1], s=(norm_bubble_size(data[i, 2]) * 5000 + 600), 
               c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, orientation='horizontal')
cbar.set_label(data_labels[3])

ax.set_title('Performance of the Top Five Companies in Business and Finance')

# set x, y label
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# resize figure
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/5_2023122261326.png')

# Clear the current image state
plt.clf()