import matplotlib.pyplot as plt
from matplotlib import ticker, cm, colors
import numpy as np

# Data preprocessing
data_str = 'Product,Annual Sales (Billion $),Online Presence (Score),Customer Base (Millions),Digital Marketing Expenditure (Million $)/n Electronics,2000,90,100,750/n Clothing,1500,85,120,600/n Groceries,2500,70,300,400/n Books,500,75,80,100/n Beauty & Health,1200,85,90,200/n Toys & Games,700,80,50,150/n Home & Furniture,1500,75,60,300'
data_str = data_str.split('/n')
data_labels = data_str[0].split(',')[1:]
data = np.array([row.split(',')[1:] for row in data_str[1:]], dtype=float)
line_labels = [row.split(',')[0] + ' ' + str(dat[2]) for row, dat in zip(data_str[1:], data)]

# Set bubble size and color limits
size_scale = (600, 5000)
color_scale = (data[:, 3].min(), data[:, 3].max())

fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.get_cmap("tab20c")

# Plotting data
for i in range(data.shape[0]):
    size = size_scale[0] + (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * (size_scale[1] - size_scale[0])
    color = (data[i, 3] - color_scale[0]) / (color_scale[1] - color_scale[0])
    ax.scatter(data[i, 0], data[i, 1], s=size, c=[cmap(color)], alpha=0.6, edgecolors="w", linewidth=2, label=None)
    ax.scatter([], [], c=cmap(color), alpha=0.6, s=20, label=line_labels[i])

# Setting legend
lgnd = ax.legend(title=data_labels[2], loc="upper left")
for handle in lgnd.legendHandles:
    handle.set_sizes([20])

# Adding color bar
norm = colors.Normalize(color_scale[0], color_scale[1])
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

# Setting labels and title
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('E-commerce Product Wise Annual Sales and Online Presence Analysis')

# Other Settings
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Save the image and close figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/134_202312301731.png")
plt.clf()
