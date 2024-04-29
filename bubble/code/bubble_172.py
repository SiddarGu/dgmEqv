import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Preparing data
input_str = ["Green Valley Farm,1500,1800,35,9", 
             "Red Hills Farm,1900,2100,42,7", 
             "Blue Lake Farm,1700,1500,32,8", 
             "Golden Plains Farm,2050,2300,50,7", 
             "Silver Mountain Farm,1800,2000,40,10"]
data_labels = ["Fruit Yield (Metric Tonnes)", "Vegetable Yield (Metric Tonnes)", "Revenue (Million $)", "Bio-diversity (Score)"]
line_labels = [str.split(",")[0]+': '+str.split(",")[2] for str in input_str]
data = np.array([[*map(int, str.split(",")[1:])] for str in input_str])

# Configuration for sizes and colors
size_scale = 6500
color_scale = 1
sizes = (data[:, 2]/np.max(data[:, 2]))*size_scale
colors_values = (data[:, 3]/np.max(data[:, 3]))*color_scale
norm = Normalize(vmin=data[:, 3].min() - 5, vmax=data[:, 3].max())
cmap = get_cmap("Blues")

fig, ax = plt.subplots(figsize=(10,10))

for i in range(len(data)):
    color = cmap(norm(data[i, 3]))
    scatter = ax.scatter(data[i, 0], data[i, 1], color=color, s=sizes[i], alpha=0.6, edgecolors="w", linewidth=1)
    catter = ax.scatter([], [], color=color, edgecolors="none", label=line_labels[i])

ax.grid(True)
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

norm = plt.Normalize(data[:,3].min() - 5, data[:,3].max())
sm = plt.cm.ScalarMappable(cmap="Blues", norm=norm)
sm.set_array([])

plt.colorbar(sm, label=data_labels[3])
plt.title('Comparative Analysis of Farm Performance in Food Production 2024')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/219_202312310045.png')
plt.clf()
