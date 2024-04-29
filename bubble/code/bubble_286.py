import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import array
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Given Data
data_raw = """Lawyer,Number of Cases,Success Rate (%),Average Settlement ($),Years of Experience
John Smith,50,80,50000,10
Emily Johnson,30,75,60000,8
Michael Davis,45,85,55000,12
Sarah Thompson,40,70,65000,9
David Wilson,50,90,45000,15"""

# Parsing the given data into array
data_list = [item.split(",") for item in data_raw.split("\n")]

# Transforms the given data
data_labels = data_list[0][1:]
data = array([item[1:] for item in data_list[1:]], dtype=float)
line_labels = [f"{item[0]} {item[-2]}" for item in data_list[1:]]

# Creating a figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Normalizing the range of color and size values
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
norm_size = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
cmap = get_cmap("viridis")

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=cmap(norm(data[i, 3])), alpha=0.6, edgecolors='w', s=(norm_size(data[i, 2])*4400)+600)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), alpha=0.6, edgecolors='w', label=line_label)

# Adding grid, legend, and labels
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Performance of Lawyers - Law and Legal Affairs')
ax.legend(title=data_labels[2], loc='upper left')

# Adding a color bar
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3], pad=0.02)

# Save and show the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/393_202312311429.png")
plt.clf()
