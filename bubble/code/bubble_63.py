import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import pandas as pd

csv_string = """Brand,Market Share (%),Revenue (Billion $),Profit Margin (%),Customer Satisfaction (/10)
Coca-Cola,15,35,20,8
PepsiCo,12,25,18,7
Nestle,10,20,15,9
Unilever,8,15,12,9
Kraft Heinz,6,10,10,7
Danone,5,8,10,8
Mars,5,8,12,9
Mondelez,4,7,10,8
Kellogg's,4,6,8,7
General Mills,3,5,8,8"""

csv_string = csv_string.split('\n')

data_labels = csv_string[0].split(',')
line_labels = [row.split(',')[0] for row in csv_string[1:]]
data = np.array([list(map(float, row.split(',')[1:])) for row in csv_string[1:]])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

cmap = plt.get_cmap("viridis")
norm = clr.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

bubble_sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=np.array([data[i, 3]]), s=bubble_sizes[i], cmap=cmap, norm=norm, label=None)
    ax.scatter([], [], color=cmap(norm(data[i, 3])), label=f"{line_label} {data[i, 2]}")

ax.legend(title=data_labels[2])
plt.colorbar(sm, ax=ax, label=data_labels[3])
ax.grid(True)

ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title('Key Metrics of Food and Beverage Brands')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/348_202312311429.png')
plt.clf()
