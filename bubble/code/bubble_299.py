
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np

data_labels = ["Reliability (Score)", "Convenience (Score)",
               "Security (Score)", "Speed (Mbps)"]
line_labels = ["Desktop", "Laptop", "Tablet", "Smartphone", "Router"]
data = np.array([[90,50,80,100], [80,60,70,200], [75,65,60,150], [60,75,50,50], [95,40,90,300]])

# Create figure
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111)

# Plot data
for i in range(data.shape[0]):
    # Normalize the data
    norm_color = Normalize(vmin=data[:, 3].min() - 20, vmax=data[:, 3].max())
    norm_size = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
    color = cm.ScalarMappable(norm=norm_color, cmap=cm.Blues).to_rgba(data[i, 3])
    size = norm_size(data[i, 2])*5000+600
    # Scatter the data
    ax.scatter(data[i, 0], data[i, 1], s=size, c=color, label=None)
    # Add empty scatter
    ax.scatter([], [], c=color, s=20, label=line_labels[i]+': '+str(data[i, 2]))

# Set legend
ax.legend(title=data_labels[2], loc="upper right")
# Add colorbar
cbar = fig.colorbar(cm.ScalarMappable(norm=norm_color, cmap=cm.Blues), ax=ax)
cbar.ax.set_title(data_labels[3])

# Adjust figure
ax.set_title('Performance of Different Tech Devices on Reliability, Convenience, Security and Speed')
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
fig.tight_layout()

# Save figure
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/33_2023122261326.png')

# Clear figure
plt.clf()