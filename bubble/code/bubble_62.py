import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.colorbar import Colorbar
from matplotlib.cm import ScalarMappable
import numpy as np

# Data
table = """Sales,1000,18,80,200
IT,500,15,85,250
HR,120,20,90,300
Operations,1500,15,75,220
Marketing,400,12,88,200
R&D,220,10,92,330
Finance,300,14,83,250"""
table = [i.split(',') for i in table.split('\n')]
data_labels = ['Employee Count', 'Annual Turnover (%)', 'Job Satisfaction (Score)', 'Training Hours per Year']
line_labels = [f"{row[0]} ({row[2]})" for row in table]
data = np.array([[int(j) for j in i[1:]] for i in table])

# Create bubble sizes and normalize colors
bubble_sizes = (data[:,2] - np.min(data[:,2])) / np.ptp(data[:,2]) * (5000-600) + 600
colors = data[:, 3]
cmap = cm.get_cmap('viridis')
norm = mcolors.Normalize(vmin=np.min(colors), vmax=np.max(colors))
mappable = ScalarMappable(norm=norm, cmap=cmap)

# Create figure and axis
fig = plt.figure(figsize=(12,8))
ax = plt.subplot(111)

# Plot data
for i, line_label in enumerate(line_labels):
    scatter = ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=mappable.to_rgba(colors[i]), label=None, alpha=0.7)
    ax.scatter([], [], c=mappable.to_rgba(colors[i]), alpha=0.7,label=line_label, s=20)
    
# Adding legend and colorbar
legend_title = data_labels[2]
legend1 = ax.legend(title=legend_title, loc='lower right')
ax.add_artist(legend1)
cbar = plt.colorbar(mappable, ax=ax)
cbar.set_label(data_labels[3], fontsize=10)

# Setting additional plot things
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True, linestyle='--', alpha=0.6)
plt.title('Employee Management Analysis in Different Departments')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/211_202312310045.png')
plt.clf()
