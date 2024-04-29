
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Popularity (Score)', 'Accessibility (Score)', 'Creativity (Score)', 'Financial Return (Score)']
line_labels = ['Music', 'Painting', 'Dance', 'Poetry', 'Theater']
data = np.array([[90, 60, 75, 50], [60, 90, 85, 30], [80, 70, 95, 20], [70, 80, 90, 40], [50, 75, 75, 60]])

# Plot the data with the type of bubble chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

# Normalize the bubble size
norm = Normalize(60, 100)

# Normalize the color value 
cmap = cm.get_cmap('RdYlGn_r')
norm_c = Normalize(20, 70)
# Plot bubble chart
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], s=norm(data[i, 2])*5000 + 600, c=cmap(norm_c(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm_c(data[i, 3])), label=line_labels[i] + f' {data[i, 2]}')

# Plot the legend
ax.legend(title=data_labels[2])

# Add a color bar
sm = cm.ScalarMappable(norm=norm_c, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Show the labels of two axes
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set the title of the figure
plt.title('Popularity and Creativity of Art Forms - Arts and Culture 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/17.png')
plt.clf()