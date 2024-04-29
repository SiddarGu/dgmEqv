import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib import ticker

data_raw = """Product,Production Units (Thousand),Factory Size (Square feet),Profit Margin (%),Efficiency (Score)
Cars,3000,500,20,85
Smartphones,5000,250,30,90
Furniture,1500,400,25,80
Clothing,7000,300,15,75
Consumer Electronics,2000,350,22,87
Pharmaceuticals,1000,450,28,92
Food Products,2500,200,18,85
Cosmetics,800,150,24,89
Footwear,600,100,20,83
"""

data_lines = data_raw.split("\n")

data_labels = data_lines[0].split(",")[1:]
line_labels = [x.split(",")[0] for x in data_lines[1:-1]]
data = np.array([[float(y) for y in x.split(",")[1:]] for x in data_lines[1:-1]])

fig, ax = plt.subplots(figsize=(10, 8))

cmap = get_cmap("viridis")
norm = colors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

for i, line_label in enumerate(line_labels):
    size = (data[i, 2] / np.max(data[:, 2])) * 5000 + 600
    color = sm.to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], color=color, s=size, label=None)
    ax.scatter([], [], color=color, label=f"{line_label} {data[i, 2]}", s=20)

plt.colorbar(sm, ax=ax).set_label(data_labels[3])
ax.legend(title=data_labels[2])

plt.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Production and Profit in Different Manufacturing Sectors")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/86_202312301731.png")
plt.clf()
