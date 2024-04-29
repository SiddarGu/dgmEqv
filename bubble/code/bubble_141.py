import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Transform data into labels and data array
data_labels = ['Sport', 'Revenue (Million $)', 'Attendance (Thousands)', 'TV Ratings', 'Player Salaries (Million $)']
line_labels = ['Basketball', 'Football', 'Soccer', 'Baseball', 'Tennis', 'Golf']
data = np.array([[2000,1500,8,100], [3000,2000,9,200], [2500,1800,7,150], [1500,1200,6,120], [500,400,4, 50], [750,600,5,80]])

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
figure, ax = plt.subplots()
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

# Plotting each data point with consistent color
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=bubble_sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i] + f' {data[i, 2]}')

# Add legend
ax.legend(title=data_labels[2], loc='upper left')

# Add color bar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Set labels, grid and title
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
ax.set_title("Performance Metrics in Sports and Entertainment")
ax.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/bubble/png_train/bubble_141.png')

# Clear the current figure
plt.clf()
