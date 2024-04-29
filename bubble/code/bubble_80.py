import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Transform the given data
data_labels = ['Revenue (Million $)', 'Market Share (%)', 'Profit Margin (%)', 'Customer Satisfaction Score (out of 10)']
data = np.array([
    [5000, 25, 15, 8],
    [4000, 20, 12, 7],
    [3000, 15, 10, 9],
    [2000, 10, 8, 7],
    [1500, 8, 10, 6],
    [1000, 5, 5, 7]
])
line_labels = ['Coca-Cola', 'PepsiCo', 'Nestle', 'Unilever', 'Danone', 'Kraft Heinz']

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Normalize data for color mapping
sm = cm.ScalarMappable(cmap='viridis', norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm.set_array([])

for i in range(data.shape[0]):
    line_label = line_labels[i] + str(data[i, 2])
    size = ((data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min())) * (5000 - 600) + 600
    color = sm.to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=size, c=[color], edgecolors='black', label=None)
    ax.scatter([], [], c=[color], s=20, label=line_label)

ax.legend(title=data_labels[2])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Performance Comparison of Leading Food and Beverage Companies')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/352_202312311429.png')
plt.clf()
