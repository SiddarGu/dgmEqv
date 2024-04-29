
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# transform data
data_labels = ['Tonnes Per Year', 'Renewable Resources (%)', 'Pollution (Score)', 'Greenhouse Gases (MT)']
line_labels = ['China', 'US', 'India', 'Germany', 'UK', 'Japan']
data = np.array([[100000, 20, 300, 20000], [90000, 25, 400, 17000], [80000, 30, 450, 15000], [70000, 35, 500, 13000], [60000, 40, 550, 11000], [50000, 45, 600, 9000]])

# plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# normalize the bubble size and color
min_bubble_size = 600
max_bubble_size = 2000
normalize_bubble_size = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
bubble_size = [min_bubble_size + (x - min(data[:, 2])) * (max_bubble_size - min_bubble_size) / (max(data[:, 2]) - min(data[:, 2])) for x in data[:, 2]]

min_color_value = min(data[:, 3])
max_color_value = max(data[:, 3])
normalize_color_value = Normalize(vmin=min_color_value, vmax=max_color_value)
cmap = plt.get_cmap('viridis')

# plot the data of each line
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=bubble_size[i], c=cmap(normalize_color_value(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(normalize_color_value(data[i, 3])), label=line_labels[i]+ ' ' + str(data[i, 2]))

# plot the legend
ax.legend(title=data_labels[2], loc='lower left')


# show the labels of two axes
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# plot the title
plt.title('Environmental Impact of Different Countries - Sustainability 2023')

# plot the color bar
sm = ScalarMappable(cmap=cmap, norm=normalize_color_value)
sm.set_array([])
cax = fig.add_axes([0.88, 0.35, 0.03, 0.5])
cbar = fig.colorbar(sm, cax=cax)
cbar.ax.set_title(data_labels[3])

# adjust the figure view
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/3.png')

# clear the current image state
plt.clf()