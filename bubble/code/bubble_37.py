

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

# transform the given data into three variables
data_labels = ["Data Transfer Rate (Mbps)", "Bandwidth (GHz)", "Cost ($)", "Coverage (%)"]

data = np.array([
    [100, 2, 40, 90],
    [50, 1, 30, 60],
    [1000, 20, 150, 30],
    [20, 0.5, 10, 95],
    [2000, 30, 300, 70]])

line_labels = ["Cable", "DSL", "Fiber", "Wi-Fi", "5G"]

# Create figure before plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the data with the type of bubble chart
cmap = get_cmap("Set2")
norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2] * 5, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=f"{line_label} ({data[i, 2]})")

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label(data_labels[3])

# Drawing techniques such as background grids and other parameter settings
ax.grid(True, ls='--', lw=0.5, c='k', alpha=0.3)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# The title of the figure
ax.set_title("High Speed Network Technologies and Their Cost, Coverage and Bandwidth")

# Automatically resize the image
fig.tight_layout()

# Save the image
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/15.png')

# Clear the current image state
plt.clf()