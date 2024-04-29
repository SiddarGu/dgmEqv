
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Incidence Rate (Per 1000)','Treatment Cost (USD)','Mortality Rate (%)','Recovery Rate (%)']
data = np.array([[30,5000,20,50], [25,2500,15,60], [20,10000,10,70], [15,1000,5,80], [10,500,2,90]])
line_labels = ['Cardiovascular Disease','Diabetes','Cancer','Respiratory Disease','Mental Health']

# Create figure before plotting
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(1, 1, 1)

# Plot the data with the type of bubble chart
for i in range(data.shape[0]):
    # Normalize the color to the range of cmap values
    normalized_cmap = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))
    c = cm.ScalarMappable(norm=normalized_cmap, cmap=cm.rainbow)
    # Normalize the bubble size to the range of 60-500
    normalized_size = Normalize(vmin=min(data[:, 2]), vmax=max(data[:, 2]))
    s = 5000 * (data[i, 2] - normalized_size.vmin) / (normalized_size.vmax - normalized_size.vmin) + 600
    ax.scatter(data[i, 0], data[i, 1], s=s, c=c.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], s=20, c=c.to_rgba(data[i, 3]), label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
cbar = fig.colorbar(c, ax=ax)
cbar.ax.set_title(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted
ax.grid()
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set the title of the figure
ax.set_title('Healthcare Trends - Health and Wellbeing 2023')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/43_2023122261326.png')

# Clear the current image state at the end of the code
plt.clf()