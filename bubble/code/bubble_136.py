import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

raw_data= "Crop,Yield (Tonnes per Hectare),Water Usage (Gallons per Acre),Labour Requirement (Man Hours per Acre),Climate Change Resilience (Score)\n Wheat,3.2,25000,40,6\n Rice,7.4,40000,60,7\n Corn,10.5,22000,35,5\n Potatoes,15.2,30000,45,8\n Soybeans,2.5,20000,30,7\n Barley,2.8,24000,35,6" 

lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
lines = lines[1:]
line_labels = [line.split(',')[0]+ ' ' + line.split(',')[2] for line in lines]
data = np.array([line.split(',')[1:] for line in lines]).astype(float)

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)
colors = Normalize(data[:, 3].min(), data[:, 3].max())
sizes = Normalize(data[:, 2].min(), data[:, 2].max())

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=plt.cm.cool(colors(data[i,3])), s=sizes(data[i,2])*5000+600, label=None)
    ax.scatter([], [], c=plt.cm.cool(colors(data[i,3])), s=20, label=line_label)

ax.legend(title=data_labels[2], loc='upper left', borderaxespad=0.)
ax.grid(True)

cbar = plt.colorbar(ScalarMappable(norm=colors, cmap='cool'), ax=ax)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.title("Comparing Efficiency and Resilience of Key Agriculture Crops")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/96_202312301731.png')
plt.clf()
