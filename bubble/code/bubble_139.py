import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable

# Data Pre-process
data = '''Policy,Annual Cost (Billion $),Affected Population (Millions),Efficiency (Score out of 10),Transparency (Score out of 10)
Health Care,1000,300,8,5
Social Security,900,250,7,6
Education,800,200,9,7
Defense,700,150,6,4
Infrastructure,600,100,8,8
Environment,500,50,9,9
Immigration,400,40,5,3 '''
data = data.split('\n')
data = [i.split(',') for i in data]
data_labels = data[0][1:]
line_labels = [i[0]+' '+str(i[2]) for i in data[1:]]

# Numerical data for plotting
data = np.array([i[1:] for i in data[1:]], dtype=float)

# normalizing color and bubble size
bubble_size = (data[:,2] - data[:,2].min()) / (data[:,2].max() - data[:,2].min()) * (5000 - 600) + 600
normalize = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
colormap = plt.get_cmap("viridis")

# Create figure and plot data
fig, ax = plt.subplots(figsize=(12,8))
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=colormap(normalize(data[i, 3])), s=bubble_size[i], label=None)
    ax.scatter([], [], c=colormap(normalize(data[i, 3])), s=20, label=line_labels[i])

# Optimize plot settings
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.xticks(wrap=True)

# Add legend and color bar
ax.legend(title=data_labels[2], loc="best")
sm = ScalarMappable(norm=normalize, cmap=colormap)
plt.colorbar(sm, label=data_labels[3])

# Set the title and save figure
plt.title('Public Policy Impact Analysis - Cost, Efficiency and Transparency')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/244_202312310045.png')

# Clear figure
plt.clf()
