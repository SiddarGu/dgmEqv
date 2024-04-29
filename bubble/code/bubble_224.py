import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.cm as cm
from matplotlib.cm import ScalarMappable

#transform the data
data_str = "Product,Annual Production (Million Tonnes),Market Size (Billion $),Company Share (%),Customer Satisfaction (Score)\nBeer,2000,150,15,85\nCoffee,1500,105,20,90\nTea,1200,95,18,92\nWine,800,65,25,88\nWhiskey,200,40,30,91\nSoft drinks,1700,120,22,84\nMilk,3000,220,10,89"
data_lines = data_str.split("\n")
line_labels = [line.split(",")[0]+" "+line.split(",")[2] for line in data_lines[1:]]
data_labels = data_lines[0].split(",")[1:]
data = np.array([line.split(",")[1:] for line in data_lines[1:]], dtype=float)

#create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Create a colormap
colormap = cm.get_cmap("RdBu")
color_norm = mcol.Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3]))
bubble_map = cm.ScalarMappable(norm=color_norm, cmap=colormap)
bubble_map.set_array([])

for i, line_label in enumerate(line_labels):
    size = (data[i,2] - np.min(data[:,2]))/(np.max(data[:,2])-np.min(data[:,2]))*4400 + 600
    ax.scatter(data[i, 0], data[i, 1], color=bubble_map.to_rgba(data[i, 3]), s=size, label=None, alpha=0.5)
    ax.scatter([], [], c='k', alpha=0.5, s=20, label=line_label)

ax.legend(title=data_labels[2], fontsize='small', loc='upper left')

# Add a color bar for the bubble colors.
cbar = plt.colorbar(bubble_map)
cbar.set_label(data_labels[3])

plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Evaluation of Different Products in Food and Beverage Industry 2023', wrap=True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/205_202312310045.png', dpi=300)
plt.clf()
