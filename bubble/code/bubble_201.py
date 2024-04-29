import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import MaxNLocator

data_str = 'Product,Sales Revenue (Million $),Customer Satisfaction (Score),Market Share (%),Net Profit (Million $)\n Smartphones,5000,90,25,1200\n Laptops,3000,85,20,900\n Tablets,2000,80,15,600\n Home Appliances,1500,75,10,400\n Furniture,1200,70,5,200\n Books,800,65,3,100\n Clothing,1400,60,10,300'
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
data = np.array([line.split(',')[1:] for line in data_lines[1:]]).astype(float)
line_labels = [line.split(',')[0] + str(data[i, 2]) for i, line in enumerate(data_lines[1:])]

fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.get_cmap("tab20c")
norm = colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=[data[i, 3]], cmap=cmap, norm=norm, alpha=0.6, edgecolors='w', label=None)
    ax.scatter([], [], c='k', alpha=0.6, s=20, label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper right')
plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, label=data_labels[3])

ax.grid(True)
ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

plt.title('Performance Comparison of Different Retail Product Categories in E-Commerce Market 2023', wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/183_202312310045.png')
plt.clf()
