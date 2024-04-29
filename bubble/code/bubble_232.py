
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Cost Per KWh (cents)', 'Carbon Emissions (kg per KWh)',
               'Renewable Capacity (MWh)', 'Efficiency (%)']
line_labels = ['Coal', 'Natural Gas', 'Solar', 'Wind', 'Hydro', 'Nuclear']
data = np.array([[9, 1050, 2000, 30],
                 [7, 550, 4000, 35],
                 [8, 0, 6000, 25],
                 [6, 0, 8000, 45],
                 [5, 0, 10000, 50],
                 [10, 50, 12000, 40]])

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)

# For each row of data, the third value is mapped to the bubble size, and the fourth value is mapped to the color value.
for i, line_label in enumerate(line_labels):
    # Normalize the bubble size to the range of 60 to 500
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max()
                                             - data[:, 2].min()) * 5000 + 600
    # Normalize the color value
    vmin, vmax = data[:, 3].min(), data[:, 3].max()
    norm = Normalize(vmin=vmin, vmax=vmax)
    color = cm.jet(norm(data[i, 3]))
    # Plot the data
    ax.scatter(data[i, 0], data[i, 1], label=None,
               s=size, c=color)
    # Plot an empty point with the same color
    ax.scatter([], [], label=line_label + f' {data[i, 2]}',
               s=20, c=color)

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar
sm = cm.ScalarMappable(cmap=cm.jet, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, shrink=0.9, pad=0.02)
cbar.set_label(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# The title of the figure should be  Evaluating the Cost and Efficiency of Different Energy Sources
ax.set_title('Evaluating the Cost and Efficiency of Different Energy Sources')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/8_2023122261326.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/8_2023122261326.png')

# Clear the current image state at the end of the code
plt.close()