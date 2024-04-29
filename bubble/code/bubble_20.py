
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np

# transform the given data into three variables
data_labels = ['Price (Millions)', 'Popularity (Score)', 'Demand (Score)', 'Creativity (Score)']
data = np.array([[5, 90, 85, 95], [3, 85, 90, 85], [2, 75, 80, 90], [1, 75, 70, 95], [1, 80, 75, 90]])
line_labels = ['Painting', 'Sculpture', 'Photograph', 'Installation', 'Performance']

# plot the data with the type of bubble chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()

for i in range(data.shape[0]):
    # normalize the color value to the range of cmap values
    norm = colors.Normalize(vmin=data[:, 3].min()-5, vmax=data[:, 3].max())
    cmap = cm.ScalarMappable(norm=norm, cmap='hsv')
    # normalize the bubble size to range from 60 to 500
    norm_size = colors.Normalize(vmin=data[:, 2].min(), vmax=data[:, 2].max())
    size = np.interp(data[i, 2], (data[:, 2].min(), data[:, 2].max()), (600, 6000))
    # plot the data
    ax.scatter(data[i, 0], data[i, 1], c=cmap.to_rgba(data[i, 3]), s=size, label=None)
    # scatter an empty point
    ax.scatter([], [], c=cmap.to_rgba(data[i, 3]), s=20, label=line_labels[i]+f' ({data[i, 2]})')

# plot the legend with the title
ax.legend(title=data_labels[2])

# add a color bar for the bubble colors
cbar = fig.colorbar(cmap, ax=ax)
cbar.set_label(data_labels[3])

# adjust the plotting techniques
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Market Valuation of Artworks by Popularity and Creativity.')

# show the labels of two axes
plt.xticks(np.arange(0, 6))
plt.yticks(np.arange(70, 101))

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/1_2023122261326.png')

# clear the current image state
plt.clf()