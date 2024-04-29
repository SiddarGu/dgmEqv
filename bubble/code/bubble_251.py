

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Average Price (USD)", "Sales Volume (Million Units)", "Consumer Satisfaction (Score)", "Brand Recognition (Score)"]
data = np.array([[50, 900, 90, 80], [100, 350, 85, 75], [200, 250, 89, 95], [40, 1000, 80, 90], [500, 50, 95, 98]])
line_labels = ["Clothing" + f" {data[i, 2]}" for i in range(data.shape[0])]

# plot the data with the type of bubble chart
plt.figure(figsize=(12, 10))
ax = plt.subplot()

# set up color map and normalize data
norm = Normalize(vmin=data[:, 3].min() - 10, vmax=data[:, 3].max())
cmap = plt.cm.Blues

# plot data
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2] * 100, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=line_labels[i])

# add legend and colorbar
legend = ax.legend(title=data_labels[2])
cax = plt.axes([0.9, 0.2, 0.02, 0.6])
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, cax=cax, label=data_labels[3])

# set figure parameters
ax.set_title("Profit and Impact of Retail and E-commerce Products")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle='--', color='gray')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/48_2023122261326.png")
plt.clf()