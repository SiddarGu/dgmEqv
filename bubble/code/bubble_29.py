

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize

# Transform the given data into three variables
data_labels = ['Revenue Collected (Billion $)', 'Compliance Rate (%)', 'Employment (Millions)', 'Economic Growth (Score)']
line_labels = ['Income Tax', 'Corporate Tax', 'Property Tax', 'Sales Tax', 'Import Tax']
data = np.array([[750, 90, 70, 6], [350, 85, 50, 8], [200, 80, 20, 10], [500, 75, 40, 7], [150, 70, 30, 9]])

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Normalize the color and the bubble size
color_norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
size_norm = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())

# Plot the data
for i in range(len(line_labels)):
    ax.scatter(data[i, 0], data[i, 1], s=size_norm(data[i, 2])*500+60, c=plt.cm.jet(color_norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=plt.cm.jet(color_norm(data[i, 3])), label=f'{line_labels[i]} {data[i, 2]}')

# Plot legend
ax.legend(title=data_labels[2])

# Plot color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=color_norm)
sm._A = []
cbar = plt.colorbar(sm, orientation='horizontal')
cbar.ax.set_title(data_labels[3])

# Adjust figure
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)
plt.title('Impact of Taxation on Economic Growth and Employment in Government and Public Policy')
fig.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/38_2023122270050.png')
plt.clf()