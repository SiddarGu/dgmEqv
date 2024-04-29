import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.ticker import FuncFormatter
import numpy as np

# transforming data
raw_data = """Destination,Annual Visitors (Millions),Revenue Generated (Billion $),Hospitality Employment (%),Satisfaction (Score)
Paris,40,82,20,9
London,38,89,22,9
New York,30,75,18,9
Tokyo,25,60,19,9
Sydney,20,53,17,9
Bali,15,35,25,8
Dubai,14,70,23,9"""
lines = raw_data.split("\n")
data_labels = lines[0].split(",")

# construct variables
line_labels, data = [], []
for line in lines[1:]:
    parts = line.split(",")
    line_labels.append(parts[0] + str(parts[2]))
    data.append(list(map(float, parts[1:])))

# Normalise data for color mapping and bubble size
data = np.array(data)
color = data[:, 3]
size = data[:, 2]
color_norm = Normalize(min(color), max(color))
size_norm = Normalize(min(size), max(size))

fig, ax = plt.subplots(figsize=(15, 10))

sc = ax.scatter(data[:, 0], data[:, 1], c=color_norm(color), cmap='viridis', s=size_norm(size) * 5000, label=None)

# plot empty points with labels
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2])
ax.grid(True)

# color bar
cbar = plt.colorbar(sc)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_title(data_labels[3])

ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

plt.title('Tourism Impact and Hospitality Employment in Major Destinations')
plt.tight_layout()
# Save the figure before showing it
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/217_202312310045.png")
plt.clf()
