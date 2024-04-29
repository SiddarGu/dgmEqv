import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Data Preparation
data_str = 'Material,Research Investment (M Billions),Patent Applications,Market Impact (Billion $),Environmental Impact (Score)' \
        '\n Steel,5,2000,100,4' \
        '\n Aluminium,3,1000,50,6' \
        '\n Plastics,8,4000,200,2' \
        '\n Silicon,10,5000,150,5' \
        '\n Copper,2,500,30,7' \
        '\n Iron,4,1500,70,6'

data_lines = data_str.split('\n')

data_labels = data_lines[0].split(',')[1:]
line_labels = [i.split(',')[0] for i in data_lines[1:]]
data = np.array([i.split(',')[1:] for i in data_lines[1:]], dtype=float)

# Normalization
c_norm = Normalize(vmin=min(data[:,3]), vmax=max(data[:,3]))
cmap = get_cmap('viridis')
bubble_scale = Normalize(vmin=min(data[:,2]), vmax=max(data[:,2]))

# Figure Preparation
fig, ax = plt.subplots(figsize=(12,8))
plt.title('Impact of Material Research in Science and Engineering - 2023')

# Plotting Bubble Chart
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(c_norm(data[i,3]))], s=bubble_scale(data[i,2])*600+400, label=None)
    ax.scatter([], [], c=cmap(c_norm(data[i,3])), alpha=0.6, s=20, label=line_labels[i] + " " + str(data[i, 2]))
    
# Legend and Colorbar
ax.legend(title=data_labels[2])
scatter = plt.scatter(data[:,0], data[:,1], c = data[:, 3], cmap = 'viridis')
cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3]) 

# Labels and Adjustment
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/115_202312301731.png')
plt.show()

# Clear current image state
plt.clf()
