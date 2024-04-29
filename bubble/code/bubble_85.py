import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
from matplotlib.colors import Normalize

# Data
data_labels = ["Employee Count", "Job Satisfaction (%)", "Annual Turnover Rate (%)","Training Hours Per Employee"]
data_str = ["HR,80,80,15,30", "Sales,200,70,30,20", "R&D,150,90,10,40", "Production,400,75,20,25", 
            "Finance,100,85,15,35", "Marketing,120,80,25,30", "IT,180,75,12,40" ]
line_labels = [s.split(',')[0] for s in data_str]
data = np.array([list(map(int, s.split(',')[1:])) for s in data_str])

# Normalize data for plotting
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
colors = cm.viridis(norm(data[:,3]))

# Interpolating sizes for each data point
sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

# Create figure and axes
fig, ax = plt.subplots(figsize=(10,6))

# Make a scatter plot for each row of data
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=[colors[i]], s=sizes[i], edgecolors='k', linewidths=1, alpha=0.6, label=None)
    scatter = ax.scatter([], [], color=colors[i], edgecolors="none", label=line_label + f' {data[i, 2]}')

# Add legend and labels
ax.legend(title=data_labels[2], loc='upper right', borderaxespad=0.)
ax.set_xlabel(data_labels[0], wrap=True)
ax.set_ylabel(data_labels[1], wrap=True)
ax.set_title('Employee Management and Satisfaction Across Different Departments')

# Add colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cm.viridis), cax=cax)
cbar.set_label(data_labels[3])
cbar.ax.yaxis.set_label_position('left')

# Tight layout and save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/200_202312310045.png', format='png', dpi=300)

# Clear figure
plt.clf()
