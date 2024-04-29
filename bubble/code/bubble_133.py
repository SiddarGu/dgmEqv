import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data = [['Clothing',85,2000,500,8],
 ['Electronics',90,1500,400,9],
 ['Beauty and Personal Care',95,1000,300,7],
 ['Home and Furniture',80,1200,200,6],
 ['Sports and Outdoor',75,900,250,7]]

data_labels = ['Customer Satisfaction (%)', 'Sales (Million $)', 'Advertising Budget (Thousand $)', 'Online Presence (Score)']
line_labels = [f"{line[0]} {line[2]}" for line in data]
data = np.array([[line[1], line[2], line[3], line[4]] for line in data])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

cmap = cm.get_cmap('rainbow')
data_colors = cmap(Normalize()(data[:,3]))

bub_sizes = Normalize()(data[:,2])
bub_sizes = 5400 * bub_sizes + 600

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=bub_sizes[i], c=np.array([data_colors[i]]), label=None, alpha=0.6)
    ax.scatter([], [], c=np.array([data_colors[i]]), s=20, label=line_labels[i])
    
ax.legend(title = data_labels[2])

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(data[:,3]), vmax=max(data[:,3])))
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Performance Metrics of Retail and E-commerce Products')

plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/344_202312311429.png')
plt.clf()
