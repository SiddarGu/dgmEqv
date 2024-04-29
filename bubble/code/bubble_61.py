import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from numpy import array
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# Transform the given data into variables
raw_data = '''Electronics,2000,25,20,85
Clothing,1500,40,15,90
Home and Kitchen,600,20,10,95
Beauty and Personal Care,1200,35,18,85
Books,500,60,8,90
Groceries,750,15,12,80'''

data_labels = ['Annual Sales (Million $)', 'E-commerce Sales(%)', 'Market Share (%)', 'Customer Satisfaction (Score)']
rows = [line.split(',') for line in raw_data.split('\n')]
line_labels = [row.pop(0) + str(row[2]) for row in rows]
data = np.array(rows).astype(float)

# Normalize color and size data
size_normalizer = Normalize(vmin=np.min(data[:, 2]), vmax=np.max(data[:, 2]))
size_mapping = size_normalizer(data[:, 2]) * (5000 - 600) + 600

color_normalizer = Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))
cmap = get_cmap('viridis')
color_mapping = cmap(color_normalizer(data[:, 3]))

# Correcting the colorbar implementation

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Creating scatter plots
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=size_mapping[i], c=array([color_mapping[i]]), label=None)
    ax.scatter([], [], s=20, c=array([color_mapping[i]]), label=line_labels[i])

# Title and layout adjustments
plt.title('E-commerce Impact on Different Product Sales in Retail Sector 2023')
plt.subplots_adjust(left=0.1, right=0.85)

# Adding colorbar
cbar_ax = fig.add_axes([0.92, 0.15, 0.03, 0.7])
cbar = ColorbarBase(cbar_ax, cmap=cmap, norm=color_normalizer, orientation='vertical')
cbar.set_label(data_labels[3])

# Setting labels and grid
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Creating custom legend
ax.legend(title=data_labels[2], loc='upper left')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/180_202312310045.png')
plt.clf()
