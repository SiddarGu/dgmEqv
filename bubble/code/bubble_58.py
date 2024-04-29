import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import cm
from matplotlib.cm import ScalarMappable
import numpy as np

data = np.array([
["Supermarket A",150,85,2000,10],
["Department Store B",100,75,1500,20],
["Clothing Store C",50,80,1000,50],
["Electronics Store D",200,90,2500,30],
["Furniture Store E",75,70,1200,15]
], dtype=object)

data_labels = ['Store','Revenue ($ million)','Customer Satisfaction (%)', 'Average Daily Visitors','Online Sales (%)']
line_labels = data[:, 0] + " " + data[:, 2].astype(str)
data = data[:, 1:].astype(float)

fig, ax = plt.subplots(figsize=(12, 8))

cmap = plt.get_cmap("viridis")

colors = data[:, 3]
norm = plt.Normalize(colors.min(), colors.max())

bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
scatter = ax.scatter(data[:, 0], data[:, 1], c=colors, cmap=cmap, norm=norm, alpha=0.6, edgecolors="w", linewidth=1, s=bubble_sizes, label=None)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=cmap(norm(colors[i])), alpha=0.6, s=20, label=line_label)

ax.legend(title=data_labels[2])

formatter = FuncFormatter(lambda val, pos: '{:.0f}'.format(val))
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

sm = ScalarMappable(norm=norm, cmap=cmap)
cbar = fig.colorbar(sm)
cbar.set_label(data_labels[3])

ax.set_title('Revenue and Customer Satisfaction in Retail Sector')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

plt.grid(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/396_202312311429.png', format='png')
plt.clf()
