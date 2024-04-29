
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Transform the given data into three variables
data_labels = ['Speed (Mbps)', 'Reliability (Score)', 'Security (Score)', 'Data Usage (GB)'] 
data = np.array([[100, 9, 8, 200], [1000, 10, 10, 500], [500, 8, 9, 1000], [2000, 9, 9, 1500], [200, 7, 8, 1000], [50, 6, 7, 500]])
line_labels = ['Wi-Fi', '5G', '4G', 'Fibre Optic', 'Cable', 'Satellite']

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# For each row of data, the third value is mapped to the bubble size, and the fourth value is mapped to the color value
norm_bubble = Normalize(vmin=np.min(data[:, 2]), vmax=np.max(data[:, 2]))
norm_color = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
cmap = plt.get_cmap("RdYlGn")

# Each line_label should be suffixed with data[i, 2]
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(norm_color(data[i, 3])), s=(norm_bubble(data[i, 2]) * 5000 + 600), label=None)
    ax.scatter([], [], c=cmap(norm_color(data[i, 3])), s=20, label=line_label + ' ' + f'{data[i, 2]}')

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize based on the range of color value
sm = ScalarMappable(cmap=cmap, norm=norm_color)
sm._A = []
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Drawing techniques such as background grids and other parameter settings
ax.grid(True)
ax.set_title('Performance of Different Network Technologies for Internet Access')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/34_2023122270050.png')

# Clear the current image state
plt.clf()