
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Each line_label should be suffixed with data[i, 2].
# Data represent the numerical array in the data. 
data = np.array([[600, 80, 750, 20],
                 [300, 50, 1500, 10],
                 [200, 40, 2500, 15],
                 [250, 60, 2000, 18],
                 [150, 30, 500, 12],
                 [100, 70, 1000, 25]])
data_labels = ['Revenue (Billion $)', 'Average Transaction Price (USD)', 'Number of Transactions (Millions)', 'Profit Margin (%)']
line_labels = ['Online Shopping', 'Grocery Stores', 'Clothing Stores', 'Electronics Stores', 'Home Improvement Stores', 'Sports & Outdoor']

# Plot the data with the type of bubble chart. 
# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# The value of figsize should be set larger than 16 to prevent content from being displayed.
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

# For the plotting using plt.scatter, the color should be normalized to the range of cmap values, 
# the bubble size should range from 60 to 500 by normalization, and parameters can be set to accurately reflect the differences in data values. 
# The label here must set as None, i.e., ax.scatter(data[i, 0], data[i, 1], label=None).
for i in range(data.shape[0]):
    cmap = cm.get_cmap('RdYlGn')
    norm = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
    colors = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=data[i, 2] * 2, c=colors, label=None)
    ax.scatter([], [], s=20, c=colors, label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot the legend with the title, by using ax.legend(title=data_labels[2]). 
# The legend should not be overlapped with the main plot area and the title.
leg = ax.legend(title=data_labels[2], loc='lower right')

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize based on the range of color value. 
# Place the color bar in a location that doesn't interfere with the legend or the main plot. 
# Set the title of the color bar by data_labels[3].
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, orientation='vertical', shrink=0.8, pad=0.05, aspect=10)
cbar.ax.set_title(data_labels[3], fontsize=12)

# Drawing techniques such as background grids and other parameter settings can be adjusted. 
# Show the labels of two axes.
ax.grid(True, ls='dashed', color='gray', alpha=0.3)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)

# The title of the figure should be  Profitability of Different Retail and E-Commerce Categories.
ax.set_title('Profitability of Different Retail and E-Commerce Categories', fontsize=16)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/32_2023122261326.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/32_2023122261326.png')

# Clear the current image state at the end of the code.
plt.clf()