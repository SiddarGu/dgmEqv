import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

raw_data = "Artist,Artwork Sold (In Thousands),Cultural Influence (Score),Global Recognition (Score),Artistic Impact (Score)\n Picasso,120,90,85,80\n Van Gogh,80,85,88,84\n Da Vinci,200,95,98,92\n Monet,60,82,86,80\n Hockney,50,80,83,76\n Koons,45,78,79,72\n Rembrandt,90,84,86,82\n Warhol,110,89,93,90\n Michelangelo,150,94,97,95"
data_lines = raw_data.split("\n")

# Prepare data
data_labels = data_lines[0].split(",")
data = np.array([list(map(float, line.split(",")[1:])) for line in data_lines[1:]])
line_labels = [line.split(",")[0] + ' ' + str(line.split(",")[2]) for line in data_lines[1:]]

# Normalize bubble sizes
sizes = Normalize()(data[:, 2]) * 5000

# Normalize colors
colors = Normalize()(data[:, 3])

fig, ax = plt.subplots(figsize = (10, 8))

cmap = get_cmap("viridis")

# Plot
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(colors[i])], s=sizes[i], alpha=0.6, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], c=cmap(colors[i]), s=20, label=line_labels[i])
ax.legend(title=data_labels[2], loc='upper right', fontsize=10)

# Color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(min(data[:, 3]), max(data[:, 3])))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

ax.grid(True)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

plt.title('Impact and Success of Notable Artists in the World of Arts and Culture', fontsize=16)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/301_202312310045.png')

# Clear the current figure state
plt.clf()
