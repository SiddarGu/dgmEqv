import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize

# Transform data
str_data = """Discipline,Research Funding (Million $),Publication Count,Impact Factor,Average Years of Study
Anthropology,150,1000,2.5,6
Sociology,200,1500,3.0,8
Psychology,250,1800,2.8,7
History,100,800,2.2,6
Philosophy,75,700,2.0,7
Linguistics,120,900,2.1,7
Ethics,80,750,2.3,6"""
lines = str_data.split("\n")
data_labels = lines[0].split(",")[1:]
data = [line.split(",")[1:] for line in lines[1:]]
data = np.array(data, dtype=float)
line_labels = [line.split(",")[0] + ": " +str(val[2]) for line, val in zip(lines[1:], data)]

# Create variables for scatter plot
size = (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * 5000 + 600
color = data[:,3]
cmap = get_cmap("viridis")

# Plot bubble chart
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot()
sc = ax.scatter(data[:,0], data[:,1], s=size, c=color, cmap=cmap, alpha=0.6, edgecolors="w", linewidth=2, label=None)

# Plot empty points for legend
for i in range(data.shape[0]):
    ax.scatter([], [], label=line_labels[i], s=20, c=cmap((color[i] - color.min()) / (color.max() - color.min())))

# Decorate plot
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title("Research Funding, Publications, and Impact across Humanities and Social Science Disciplines")

# Plot legend
plt.legend(title=data_labels[2], loc='upper left')

# Plot color bar
norm = Normalize(data[:, 3].min(), data[:, 3].max())
cbar = fig.colorbar(mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical')
cbar.set_label(data_labels[3], rotation="vertical")

# Save as png
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/172_202312310045.png")
plt.close()
