import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.collections import PathCollection
from matplotlib.colorbar import ColorbarBase
from matplotlib.colorbar import Colorbar
from matplotlib.text import Text

data = """Artist,Artwork Sold (Millions USD),Attendance (Millions),Social Impact (Score),Cultural Impact (Score)
Picasso,500,8,9,10
Da Vinci,800,15,10,9
Van Gogh,700,12,8,9
Monet,300,10,7,8
Michelangelo,400,9,8,7
Rembrandt,200,7,7,6
Warhol,600,14,6,7
Banksy,450,13,5,6"""

lines = data.split("\n")
data_labels = lines[0].split(",")
data = np.empty((len(lines) - 1, len(data_labels) - 1), dtype=np.float32)
line_labels = []

# Parsing data
for i, line in enumerate(lines[1:]):
    parts = line.split(",")
    line_labels.append(parts[0] + " " + parts[3])
    for j, part in enumerate(parts[1:]):
        data[i, j] = float(part)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Color and size mappings
cmap = plt.get_cmap('viridis')
color_norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
bubble_sizes = Normalize(vmin=np.min(data[:, 2]), vmax=np.max(data[:, 2]))(data[:, 2]) * 1000

# Scatter plot
for i, (x, y, _, color) in enumerate(data):
    ax.scatter(x, y, label=None, s=bubble_sizes[i], c=cmap(color_norm(color)), alpha=0.6, edgecolors='w')
    ax.scatter([], [], c=cmap(color_norm(color)), alpha=0.6, s=20, label=line_labels[i])

# Title and layout
plt.title('Impact and Success of Artists in Arts and Culture')
# Legend and labels
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Colorbar
cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb = ColorbarBase(cax, cmap=cmap, norm=color_norm)
cb.set_label(data_labels[3])

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/220_202312310045.png', dpi=300, bbox_inches='tight')
plt.clf()
