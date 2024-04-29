

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

# Transform the given data into three variables
data_labels = ['Sales (Millions $)','Cost (Millions $)','Profit Margin (%)','Sustainability (Score)']
data = np.array([[1200, 300, 25, 4], 
                 [800, 220, 20, 8], 
                 [400, 150, 30, 7], 
                 [600, 100, 18, 10], 
                 [500, 90, 16, 6]])
line_labels = ['Fast Food', 'Casual Dining', 'Fine Dining', 'Home Delivery', 'Street Food']

# Plot the data with the type of bubble chart
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# For each row of data, the third value is mapped to the bubble size
# and the fourth value is mapped to the color value.
cmap = get_cmap("Greens")
norm = Normalize(vmin=min(data[:, 3]) - 1, vmax=max(data[:, 3]))

for i in range(len(data)):
    sc = ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*20 + 60, c=cmap(norm(data[i, 3])), cmap='Greens', label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = plt.cm.ScalarMappable(cmap='Greens', norm=plt.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])))
sm._A = []
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted
ax.grid(linestyle='--', linewidth=1, alpha=0.5)
ax.tick_params(direction='in', length=10, width=2, grid_alpha=0.5)

# Show the labels of two axes
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# The title of the figure
ax.set_title('Profit and Sustainability of Different Types of Restaurants in the Food and Beverage Industry')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/21_2023122270050.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/21_2023122270050.png')

# Clear the current image state at the end of the code
plt.clf()