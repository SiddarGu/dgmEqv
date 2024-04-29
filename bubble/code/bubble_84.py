import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# data prepared
raw_data = '''Category,Annual Revenue (Million $),Number of Employees,Online Sales (%),Customer Satisfaction (Score)
Clothing,2500,5000,35,8
Electronics,3000,6000,50,7
Home Decor,1500,3000,25,9
Beauty and Personal Care,2000,4000,40,8
Books and Media,1000,2000,20,9
Toys and Games,1200,2500,30,7
Grocery,3500,7000,60,9'''
raw_lines = raw_data.split('\n')
data_labels = raw_lines[0].split(',')[1:]
lines = [line.split(',') for line in raw_lines[1:]]
line_labels = [f'{lines[i][0]} {lines[i][2]}' for i in range(len(lines))]
data = np.array([[float(x) for x in line[1:]] for line in lines])

# normalization
norm_colors = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
norm_sizes = Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
colors = [cm.plasma(norm_colors(value)) for value in data[:, 3]]
sizes = [600 + 4400*norm_sizes(value) for value in data[:, 2]]

# plot setup
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Analysis of Retail and E-commerce Categories')

# scatter plot
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], c=colors[i], s=sizes[i], label=None)
    ax.scatter([], [], c=colors[i], label=line_labels[i])

ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
# color bar
sm = ScalarMappable(norm=norm_colors, cmap='plasma')
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/357_202312311429.png')
plt.clf()  # Clear the current image state
