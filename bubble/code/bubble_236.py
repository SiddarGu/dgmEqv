import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Data preparation
raw_data = '''Product,Market Share (%),Annual Growth Rate (%),Avg. Price (USD/Tonne),Global Demand (Million Tonnes)
Wheat,18,2.5,200,740 
Rice,20,3,500,490 
Corn,15,1.5,150,1080 
Soybeans,30,2.8,350,355 
Dairy,17,2.2,400,530'''

lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

original_data = data.copy()
# Variables transformation
min_size = 600
max_size = 5000
size_scale = (max_size - min_size)/(np.max(data[:, 2]) - np.min(data[:, 2]))
data[:, 2] = min_size + size_scale*(data[:, 2] - np.min(data[:, 2]))

cmap = plt.get_cmap('viridis')
norm = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))


# Plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2], c=cmap(norm(data[i, 3])), alpha=0.6, label=None)
    ax.scatter([], [], label=line_label + f' {original_data[i, 2]}', color=cmap(norm(data[i, 3])))
    

ax.grid(True, linestyle='-', color='0.75')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Legend and color bar
ax.legend(title=data_labels[2], loc='lower right')
sm = ScalarMappable(cmap=cmap, norm=norm)
plt.colorbar(sm, ax=ax, label=data_labels[3])

# Title
plt.title("A Snapshot of Global Agriculture and Food Production in 2023")

# Save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/213_202312310045.png')
plt.close()
