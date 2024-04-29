
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

# Transform data into three variables
data_labels = ["Production Volume (Million Tonnes)", "Land Used (Million Hectares)", "Profit Margin (%)", "Sustainability (Score)"]
line_labels = ["Wheat","Corn","Rice","Soybeans","Potatoes","Apples","Oranges","Bananas","Avocados","Pears","Tomatoes"]
data = np.array([[730,220,20,8],
                 [1150,180,25,6],
                 [490,160,15,10],
                 [350,120,30,7],
                 [370,100,18,10],
                 [150,80,20,9],
                 [220,90,15,7],
                 [280,100,30,8],
                 [60,50,25,6],
                 [90,40,20,10],
                 [130,30,18,9]])

# Create figure
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the data with the type of bubble chart
cmap = get_cmap('tab20', lut=len(data))
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
sizes = (data[:, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * (5000 - 600) + 600
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), label=line_label + f' {data[i, 2]}', s=20)

# Plot the legend with the title
ax.legend(title=data_labels[2], loc="lower right")

# Add a color bar for the bubble colors
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.7, anchor=(0.3, 0.5))
cbar.ax.set_title(data_labels[3], fontsize=12)

# Drawing techniques
ax.grid(True, linestyle='--', which='major',
            color='grey', alpha=.25)

# Show the labels of two axes
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)

# The title of the figure
ax.set_title("Maximizing Profits with Sustainable Crop Production - Agriculture 2023", fontsize=16)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/5_2023122270050.png")

# Clear the current image state
plt.clf()