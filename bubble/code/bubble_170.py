import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import numpy as np


data_str = '''Product,Annual Sales (Million $),Number of Units Sold (Million),Profit Margin (%),Customer Satisfaction (Score)
Electronics,10000,500,20,8
Clothes,8000,1000,30,6
Books,5000,300,25,10
Furniture,7000,200,35,7
Cosmetics,2000,150,40,9
Toys,3000,250,15,8
Sports Equipment,4000,350,30,7'''

# Transform the data
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
data_lines = data_lines[1:]
line_labels = [line.split(',')[0] + str(line.split(',')[2]) for line in data_lines]
data = np.array([[int(val) for val in line.split(',')[1:]] for line in data_lines])

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Create a colormap
cmap = plt.get_cmap("viridis")

# Normalize data for the scatter plot
norm = colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sm = cm.ScalarMappable(norm=norm, cmap=cmap)

# Plot the data
for i in range(len(data)):
    color = sm.to_rgba(data[i, 3])
    size = 600 + 4400 * (data[i, 2] / data[:, 2].max())
    ax.scatter(data[i, 0], data[i, 1], color=color, s=size, label=None)
    ax.scatter([], [], color=color, s=20, label=line_labels[i])

ax.legend(title=data_labels[2])

# Add a color bar
cb = plt.colorbar(sm, ax=ax)
cb.set_label(data_labels[3])

# Set labels and title
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2])
plt.title('Performance of Different Products in Retail and E-commerce Market')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/292_202312310045.png')
plt.clf()
