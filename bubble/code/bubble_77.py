import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

raw_data = '''Product,Units Produced (Millions),Production Cost ($ Billion),Profit Margin (%),Efficiency (Score)
Cars,20,500,25,85
Computers,15,400,30,80
Smartphones,10,300,35,90
Furniture,25,200,20,70
Appliances,30,150,15,75
Clothing,35,100,10,65
'''

# Cleaning data
data_lines = raw_data.split('\n')[:-1]
data_labels = data_lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in data_lines[1:]], dtype=float)
line_labels = [f"{line.split(',')[0]} {line.split(',')[2]}" for line in data_lines[1:]]

# Create new figure
fig, ax = plt.subplots(figsize=(10,8))

# Normalizing size and color of bubbles
size_norm = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
color_norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
bubble_sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

for i in range(len(data)):
    ax.scatter(data[i,0], data[i,1], c=cm.viridis(color_norm(data[i,3])), s=bubble_sizes[i], alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c=cm.viridis(color_norm(data[i,3])), s=20, label=line_labels[i])

# Add colorbar
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=color_norm)
sm.set_array([])
fig.colorbar(sm, label=data_labels[3], pad=0)

# Add labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Productivity and Profitability in Manufacturing Industry 2023')

# Add legend
ax.legend(title=data_labels[2], loc='best')

# Adjust layout
plt.tight_layout()

# Save and clear figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/165_202312310045.png')
plt.clf()
