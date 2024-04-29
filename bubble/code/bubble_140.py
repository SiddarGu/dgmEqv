import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Input data
data_str = "Transport Type,Operational Efficiency (Score),Fuel Consumption (Million litres),Cost (Billion $),Emission (Million Tonnes)/n Rail,80,700,250,500/n Truck,65,1400,400,1000/n Ship,75,2000,350,1500/n Air,60,1300,450,1200/n Pipeline,70,1800,300,800"

# Prepare data
rows = [row.split(',') for row in data_str.split('/n ')]
data_labels = rows[0]
lines = [[float(val) for val in line[1:]] for line in rows[1:]]
line_labels = [f"{line[0]} {data[2]}" for line, data in zip(rows[1:], lines)]
data = np.array(lines)

# Create color and size map based on range
norm = Normalize(np.min(data[:, 3]), np.max(data[:, 3]))
cmap = cm.get_cmap("viridis")

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plot data
for i in range(len(data)):
    color = cmap(norm(data[i, 3]))
    size = 600 + (data[i, 2] / np.max(data[:, 2]) * 4400)
    ax.scatter(data[i, 0], data[i, 1], c=[color], s=size, label=None)
    ax.scatter([], [], c=[color], s=20, label=line_labels[i])

# Add legend and color bar
ax.legend(title=data_labels[2])
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, pad=0.02, label=data_labels[3])

# Add titles and labels
ax.set_title('Performance Analysis of Different Transport Types in Logistics Industry', fontsize=14)
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

# Adjust settings
ax.grid(True)
ax.set_xlim(np.min(data[:, 0])-10, np.max(data[:, 0])+10)
ax.set_ylim(np.min(data[:, 1])-10, np.max(data[:, 1])+10)

# Save and clear figure
fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/130_202312301731.png", transparent=True, bbox_inches='tight')
plt.clf()
