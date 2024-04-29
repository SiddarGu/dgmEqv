import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data_str = 'Product,Revenue (Million $),Market Share (%),Growth Rate (%),Customer Satisfaction (Score)' \
           '/n Soft Drinks,5000,30,5,9/n Snack Foods,4000,25,4,8/n Dairy Products,3000,20,3,7/n Alcoholic Beverages,2000,15,2,6/n Baked Goods,1000,10,1,5/n Condiments,500,5,0.5,4' 

data_str = data_str.replace('/n ', '\n')
data_str = data_str.split('\n')
data_labels = data_str[0].split(',')[1:]
data = np.array([i.split(',')[1:] for i in data_str[1:]], dtype=float)
line_labels = [i.split(',')[0] + ': ' + str(j[2]) for i, j in zip(data_str[1:], data)]

fig, ax = plt.subplots(figsize=(10, 6))
cmap = get_cmap('Spectral')
norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None,
               c=cmap(norm(data[i, 3])), alpha=0.6, edgecolors='w', s=600 + 5000 * (data[i, 2] / data[:, 2].max()))
    ax.scatter([], [], label=line_labels[i],
               c=cmap(norm(data[i, 3])), alpha=0.6, edgecolors='w', s=20)

ax.legend(title=data_labels[2], loc='upper left')

sm = plt.cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
plt.colorbar(sm, ax=ax, label=data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title(' Market Performance of Food and Beverage Products')
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/345_202312311429.png')
plt.clf()
