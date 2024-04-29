import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase
import numpy as np
import pandas as pd

# Converting raw data to  pandas dataframe
raw_data = {
    'Farm': ['Green Valley', 'Blue Hills', 'Red Meadows', 'Golden Fields', 'Silver Lake', 'Bright Acres', 'Dark Woods'],
    'Annual Revenue (Million $)': [500, 300, 800, 650, 400, 300, 200],
    'Crop Diversity (Score)': [10, 8, 6, 7, 9, 10, 4],
    'Labor Force (Number)': [200, 100, 400, 350, 150, 100, 50],
    'Organic Certification (Yes=1, No=0)': [1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(raw_data)

# Transform the given data into three variables
data_labels = df.columns[1:]
line_labels = df['Farm'] + ' ' + df['Crop Diversity (Score)'].map(str)
data = df.values[:, 1:]

# Normalize the bubble size and color value
color_norm = Normalize(data[:, 3].min(), data[:, 3].max())
size_norm = Normalize(data[:, 2].min(), data[:, 2].max())

# Create figure
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot()

# Plotting data
cmap = cm.get_cmap('viridis')
for i in range(len(data)):
    color = cmap(color_norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], c=color, s=600+4300*size_norm(data[i, 2]), label=None, alpha=0.6)
    ax.scatter([], [], c=color, s=20, label=line_labels[i])

# Setting labels and title
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_title('Revenue and Sustainability in Different Farms - Agriculture 2023', fontsize=14)

# Plotting legend 
lgnd = ax.legend(title=data_labels[2], loc='upper left')
for handle in lgnd.legendHandles:
    handle.set_sizes([20])

# Add a color bar
sm = cm.ScalarMappable(cmap=cmap, norm=color_norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, orientation='vertical', label=data_labels[3])

# fine-tune and save image
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/271_202312310045.png')
plt.close()
