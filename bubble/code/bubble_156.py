import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm

# Transformed data into three variables.
data_labels = ['Production Volume (Million Units)', 'Machinery Cost (Million $)', 'Profit Margin (%)', 
               'Quality Score (Out of 10)']
data = np.array([[10, 50, 20, 8],
                 [20, 40, 25, 7],
                 [30, 30, 15, 9],
                 [25, 35, 22, 8],
                 [15, 25, 18, 7],
                 [40, 20, 20, 6]])
line_labels = ['Cars', 'Computers', 'Mobile Phones', 'Televisions', 'Furniture', 'Clothes']

# Create figure before plotting.
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

# Normalize color and bubble size based on the data.
color = data[:, 3]
bubble_sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))
normalize_color = mcolors.Normalize(vmin=color.min(), vmax=color.max())
cmap = cm.get_cmap('viridis')

# Plotting bubble chart.
for i in range(data.shape[0]):
    line_label = f'{line_labels[i]} {data[i, 2]}'
    ax.scatter(data[i, 0], data[i, 1], c=cmap(normalize_color(color[i])), s=bubble_sizes[i], label=None)
    ax.scatter([], [], c=cmap(normalize_color(color[i])), s=20, label=line_label)

# Plot the legend and color bar.
ax.legend(title=data_labels[2], loc='upper left')
fig.colorbar(cm.ScalarMappable(norm=normalize_color, cmap=cmap), ax=ax, label=data_labels[3])

# Set plot parameters.
plt.title('Profitability and Quality in Different Product Manufacturing')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.grid()

# Save and show the figure.
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/251_202312310045.png')
plt.show()

# Clear the current image state.
plt.close()
