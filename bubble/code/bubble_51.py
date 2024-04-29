import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy import linspace
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

data_array = [["Cars",70,800,3.5,7],
              ["Smartphones",180,1200,10.6,8],
              ["Furniture",30,200,2.3,9],
              ["Appliances",90,700,1.5,9],
              ["Clothing",200,1000,5.7,7],
              ["Toys",60,300,4,8],
              ["Electronic Devices",160,1100,8,8]]

data_labels = ['Annual Production (Million Units)', 'Factory Workers Employed (Thousands)', 'Growth Rate (%)', 'Safety Score (Out of 10)']
data = np.array([item[1:] for item in data_array], float)
line_labels = [f'{item[0]} ({item[1][2]})' for item in zip(data_array, data)]

fig, ax = plt.subplots()
fig = plt.figure(figsize= (8,8))

cmap = plt.get_cmap("tab20")
colors = cmap(np.arange(len(line_labels)) / len(line_labels))
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = ScalarMappable(norm=norm, cmap=cmap)

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], color=colors[i], s=600 + 4400 * (data[i, 2] / data[:, 2].max()), label=None)
    ax.scatter([], [], c=colors[i], alpha=0.6, s=20,label=line_labels[i])
    
ax.legend(title=data_labels[2])
plt.colorbar(sm, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title("Overview of Product Manufacturing and Growth Rate")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/290_202312310045.png")
plt.clf()
