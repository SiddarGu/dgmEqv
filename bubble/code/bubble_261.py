import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

data = np.array([
    ['Electronics', 500, 80, 20, 90],
    ['Furniture', 300, 85, 15, 800],
    ['Clothing', 700, 90, 30, 950],
    ['Books', 200, 70, 10, 900],
    ['Groceries', 800, 95, 40, 850],
    ['Beauty', 600, 75, 25, 920],
    ['Toys', 150, 65, 5, 960]
], dtype=object)

data_labels = ['Annual Sales (Billion $)', 'Customer Satisfaction (Score)', 'Number of Sales (Millions)', 'E-commerce Adoption (Score)']
line_labels = [f'{row[0]} {row[2]}' for row in data]
data = np.array(data[:, 1:], dtype=float)

fig, ax = plt.subplots(figsize=(12,8))
colors = Normalize(min(data[:,2]), max(data[:,2]))
bubble_sizes = np.interp(data[:,1], (data[:,1].min(), data[:,1].max()), (600,5000))

scatter = ax.scatter(data[:,0], data[:,1], label=None,
                     c=data[:,2], cmap='viridis',
                     s=bubble_sizes, alpha=0.7,
                     norm=colors)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, s=20,
               label=line_label)

#legend
lgnd = ax.legend(title=data_labels[2], fontsize='small', title_fontsize='medium', loc='upper left')
for handle in lgnd.legendHandles:
    handle._sizes = [30] 

#add colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
cbar = fig.colorbar(ScalarMappable(norm=colors, cmap='viridis'),
             ax=ax, cax=cax, orientation='vertical')
cbar.set_label(data_labels[3])

plt.grid(True)
ax.set_title('Analysis of Retail and E-commerce Sales by Product')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/147_202312301731.png')
plt.clf()
