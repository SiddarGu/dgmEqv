import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn
from matplotlib.collections import PathCollection
from matplotlib.colors import Normalize

# Transform data
raw_data = """
Product,Production Units (Million),Defect Rate (%),Sale Price ($),Profit Margin (%)
Cars,120,1,20000,8
Smartphones,1000,2,1000,30
Laptops,500,1.5,1500,25
TVs,800,2,800,20
Washing Machines,600,1,400,18
"""
lines = raw_data.split('\n')[1:-1]
data_labels = lines[0].split(',')
lines = lines[1:]
line_labels = [line.split(',')[0] for line in lines]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines])

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

for i in range(len(data)):
    line_label = "{} ({})".format(line_labels[i], data[i, 2])
    colors = cm.viridis(Normalize()(data[:, 3]))
    size = (600 + (data[i, 2] / max(data[:, 2]) * 5000))
    ax.scatter(data[i, 0], data[i, 1], s=size, c=[colors[i]], alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title('Profitability and Production Efficiency in the Manufacturing Industry')

# Adding color bar
sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3])))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/136_202312301731.png')
plt.clf()
