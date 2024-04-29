
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform data into three variables: data_labels, data, line_labels.
data_labels = np.array(["Visitors (Millions)", "Satisfaction Score (1-10)", "Average Spending ($)", "Hotel Capacity (Millions)"])
data = np.array([[12, 8, 1000, 3.5],
                 [90, 7, 2000, 20],
                 [180, 9, 3000, 45],
                 [170, 7, 2500, 30],
                 [50, 6, 1500, 10],
                 [25, 9, 3000, 12]])
line_labels = np.array(["Caribbean", "USA", "Europe", "Asia", "Africa", "Australia"])

# Create figure before plotting.
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1)

# Plot the data with the type of bubble chart
# Color should be normalized to the range of cmap values
# Bubble size should range from 60 to 500
for i in range(len(data)):
    cmap = cm.ScalarMappable(norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()), cmap="Blues")
    size = 600 + 5000 * (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())
    ax.scatter(data[i, 0], data[i, 1], s=size, c=cmap.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=cmap.to_rgba(data[i, 3]), label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot the legend with the title.
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
cbar = fig.colorbar(cmap, ax=ax)
cbar.set_label(data_labels[3], rotation=270)

# Adjusting techniques such as background grids and other parameter settings
ax.set_title("Tourism Statistics for Popular Destinations in the World")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/20_2023122261326.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/20_2023122261326.png')

# Clear the current image state at the end of the code.
plt.clf()