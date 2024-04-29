import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# Convert data to arrays
raw_data = ["Sport,Revenue (Billion $),Global Popularity (Score),Facilities (Number),Athlete Salaries (Million $)",
            "Football,44,85,30000,400",
            "Basketball,25,75,20000,280",
            "Baseball,10,60,15000,200",
            "Tennis,6,65,10000,120",
            "Golf,4,50,9000,90",
            "Motorsport,5,70,8000,150",
            "Cricket,3,55,7000,50",
            "Boxing,2,60,5000,80"]
data_labels = raw_data[0].split(',')
data = np.array([row.split(',')[1:] for row in raw_data[1:]], dtype=float)
line_labels = [row.split(',')[0] for row in raw_data[1:]]

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 8))

# Normalize color and size of bubbles
color = Normalize(data[:, 3].min(), data[:, 3].max())(data[:, 3])
size = Normalize(600, 5000)(data[:, 2])

# Plot bubbles
for i in range(data.shape[0]):
    line_label = line_labels[i] + str(data[i, 2])
    ax.scatter(data[i, 0], data[i, 1], s=size[i]*1000, color=get_cmap('viridis')(color[i]), label=None, edgecolors='w')
    ax.scatter([], [], s=20, c='k', label=line_label)

plt.title('Revenue Breakdown of Global Sports and Entertainment Industry')

# Add legend and colorbar
ax.legend(title=data_labels[2], loc="upper left")
cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb = ColorbarBase(cax, cmap=get_cmap('viridis'), norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()), label=data_labels[3])

# Add axis labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
# Show grid
ax.grid(True)

# Apply layout and save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/206_202312310045.png")
plt.clf()
