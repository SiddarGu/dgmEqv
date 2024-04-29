import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
import numpy as np

# Prepare data
raw_data = [
    ['Film', 6000, 50000, 75, 90], 
    ['Music', 8000, 80000, 60, 100],
    ['Visual Arts', 4000, 25000, 50, 80],
    ['Theatre', 3000, 10000, 40, 70],
    ['Literature', 2000, 8000, 30, 65],
    ['Sculpture', 1000, 3000, 20, 60 ]
]

data_labels = ['Number of Artists (Thousands)', 'Overall Revenue (Million $)', 'Average Salary (Thousand $)', 'Global Popularity (Score)']
line_labels = [i[0] + str(i[2]) for i in raw_data]
data = np.array([i[1:] for i in raw_data])

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Normalize bubble size and color 
size_norm = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
sizes = size_norm(data[:, 2])*5000 + 600
color_norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

# Plot bubble chart
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=[cm.viridis(color_norm(data[i, 3]))], s=sizes[i], label=None)
    ax.scatter([], [], c=cm.viridis(color_norm(data[i, 3])), s=20, label=line_labels[i])
    
# Add legend and title
ax.legend(title=data_labels[2])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('The Impacts of Various Art Forms in the Global Arts and Culture Industry')

# Add colorbar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=color_norm)
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

# Show grid
ax.grid(True)

# Resize and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/135_202312301731.png')

# Clear current figure
plt.clf()
