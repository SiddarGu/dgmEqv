
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform data into three variables
data_labels = ['Cost of Compliance (Million $)', 'Legality (Score)', 'Regulation Compliance (Score)', 'Business Impact (Score)']
data = np.array([[200, 75, 85, 90], 
                [150, 70, 90, 80],
                [100, 80, 75, 60],
                [50, 90, 80, 75],
                [25, 85, 90, 70],
                [10, 95, 95, 90]])
line_labels = ['Tax Law', 'Contract Law', 'Employment Law', 'Intellectual Property Law', 'Corporate Law', 'Tort Law']

# Create figure before plotting
fig, ax = plt.subplots(figsize=(16, 10))

# Plot the data with the type of bubble chart
for i in range(len(data)):
    # Normalize the color to the range of cmap values
    color = cm.jet(data[i, 3]/100)
    # Normalize the bubble size to range from 60 to 500
    size = 600 + (2000-600)*data[i, 2]/10
    # Plot data
    ax.scatter(data[i, 0], data[i, 1], c=color, s=size, label=None)
    # Plot a empty point with the same color
    ax.scatter([], [], c=color, s=20, label=line_labels[i] + f' {data[i, 2]}')

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add color bar for the bubble colors
sm = cm.ScalarMappable(cmap=cm.jet, norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
sm._A = []
cbar = fig.colorbar(sm, ax=ax, orientation="vertical")
cbar.set_label(data_labels[3])

# Add title
ax.set_title('Assessing the Legal Requirements of Different Laws')

# Adjust the figure view better
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
# Automatically resize the image
plt.tight_layout()
# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/29_2023122261326.png')
# Clear the current image state
plt.clf()