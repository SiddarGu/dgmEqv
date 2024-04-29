import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Transform the given data into three variables: data_labels, data, line_labels
raw_data = """Google,90,160,4000,95
Facebook,2,70,2800,85
Microsoft,7,143,2500,90
Amazon,0.8,386,300,92
Apple,0.2,275,1000,97
Netflix,0.4,25,200,86
Twitter,0.1,3.7,330,80"""

data_labels = ["Market Share (%)", "Revenue (Billion $)", "User Base (Millions)", "Innovation Score (Out of 100)"]

lines = raw_data.split("\n")
data = np.empty((len(lines), len(data_labels)))
line_labels = []
for i, line in enumerate(lines):
    parts = line.split(",")
    line_labels.append(parts[0] + ' ' + str(parts[2]))
    data[i] = parts[1:]

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Normalizations
size_scale = mcolors.Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = get_cmap("viridis")
# Bubble chart
for i in range(data.shape[0]):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=size_scale(data[i, 2]) * 5000 + 600, alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

# Plot legend
ax.legend(title=data_labels[2], loc='upper right')

# Add a color bar
sm = plt.cm.ScalarMappable(cmap="viridis", norm=mcolors.Normalize(vmin=data[:,3].min(),
                     vmax=data[:,3].max()))
sm.set_array([])
fig.colorbar(sm, orientation="vertical", shrink=0.6, pad=0.05).set_label(data_labels[3])

# Adjustments
plt.title('Technology and Internet Companies Performance Metrics')
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/225_202312310045.png')

# Clear the current image state
plt.clf()         
