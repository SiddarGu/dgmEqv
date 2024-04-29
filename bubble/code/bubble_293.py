import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# Transform data to numpy array
data_labels = ['Policy', 'Impact on Economy (in Billion $)', 'Impact on Education (Score out of 100)', 'Population Impacted (in Millions)', 'Budget Allocation (%)']
line_labels = ['Foreign Policy\n1000', 'Health Policy\n500', 'Defense Policy\n200', 
               'Environmental Policy\n300', 'Immigration Policy\n50']
data = np.array([[4000,75,1000,20],[3000,85,500,30],[2000,70,200,40],[1500,90,300,7],[1000,80,50,3]])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

cmap = get_cmap('viridis')
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

bubble_sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=[cmap(norm(data[i, 3]))], label=None, alpha=0.6, edgecolors='w')
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_labels[i])

ax.legend(title=data_labels[3])
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])

plt.grid(True)
plt.title('The Impact of Different Government Policies on Economy, Education, and Population', wrap=True)
cbax = fig.add_axes([0.93, 0.1, 0.02, 0.8]) 
cb = ColorbarBase(cbax, cmap=cmap, norm=norm, orientation='vertical')
cb.set_label(data_labels[4])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/bubble/png_train/bubble_293.png')
plt.clf()
