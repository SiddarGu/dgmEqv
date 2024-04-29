import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap 
from matplotlib.colors import Normalize 
from matplotlib.colorbar import ColorbarBase
from matplotlib.patches import Patch 

data_string = "Product,Revenue (Million $),Units Sold (Millions),Market Share (%),Health Score (rating out of 10)/n Beer,5000,700,25,2/n Wine,4000,500,20,5/n Whisky,3000,400,15,1/n Coffee,7000,800,30,6/n Tea,3000,500,15,8/n Soft Drinks,6000,900,25,2/n Fruit Juice,2000,300,10,10"
data_list= data_string.split('/n')

data_labels = data_list[0].split(',')

raw_data = [item.split(',') for item in data_list[1:]]
data = np.array([[float(y) for y in x[1:]] for x in raw_data])
line_labels = [x[0]+' '+str(y[2]) for x,y in zip(raw_data, data)]

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(1,1,1)

norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
cmap = get_cmap("viridis")

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=600 + 4400*(data[i, 2]/data[:,2].max()), c=cmap(norm(data[i,3])), label=None, alpha=0.5, edgecolors='w')
    ax.scatter([], [], color=cmap(norm(data[i,3])), alpha=0.5, s=20, label=line_label)     

ax.legend(title=data_labels[2])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, pad=0.02, label=data_labels[3])

ax.set_xlabel(data_labels[1], fontsize=12)
ax.set_ylabel(data_labels[2], fontsize=12)
ax.set_title("Revenue and Market Share Analysis of Different Beverages in Food and Beverage Industry 2023", fontsize=14)
ax.grid(True)

plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/164_202312310045.png')
plt.clf()
