import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from matplotlib.collections import PathCollection
import csv

data_text = "Product,Online Sale (Million $),Offline Sale (Million $),Profit Margin (%),Reliability (Score)\nElectronics,1000,450,35,9\nClothing,1200,750,32,8\nHome essentials,980,820,40,10\nBeauty Products,900,600,30,7\nBooks,800,700,28,9\nFurniture,700,650,25,8"
data_lines = data_text.split("\n")
csvreader = csv.reader(data_lines)

data_labels = None
line_labels = []
data = []
for i, row in enumerate(csvreader):
    if i==0:
        data_labels = row[1:]
    else:
        line_labels.append(row[0] + " " + str(row[2]))
        data.append([float(x) for x in row[1:]])

data = np.array(data)

fig, ax = plt.subplots(figsize=(10,6), dpi=200)
fig.suptitle('Comparison of Online and Offline Sales in Retail and E-commerce 2023')

norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
colormap = cm.viridis

for i, line_label in enumerate(line_labels):
    size = ((data[i, 2]-data[:,2].min())/(data[:,2].max()-data[:,2].min())*(5000-600))+600
    ax.scatter(data[i, 0], data[i, 1], c=colormap(norm(data[i, 3])), s=size, label=None)
    ax.scatter([], [], c=colormap(norm(data[i, 3])), s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

s_m = cm.ScalarMappable(cmap=colormap, norm=norm)
plt.colorbar(s_m, ax=ax).set_label(data_labels[3])

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/58_202312301731.png')
plt.cla()
