
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Number of Participants (Million)', 'Engagement (Hours/Week)', 'Awareness (Score)', 'Creativity (Score)']
data = np.array([[1.2, 9, 7, 8], [0.5, 6, 5, 6], [0.3, 4, 3, 9], [0.7, 3, 4, 10], [0.4, 2, 2, 7], [0.2, 1, 1, 5]])
line_labels = ['Music', 'Theatre', 'Dance', 'Visual Arts', 'Crafts', 'Literature']

# Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()
cmap = get_cmap('PuBu')
norm = Normalize(vmin=data[:, 3].min() - 1, vmax=data[:, 3].max())

# Plot the data with the type of bubble chart
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]/data[:, 2].max())*5000, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], s=20, c=cmap(norm(data[i, 3])), label=f'{line_labels[i]} {data[i, 2]:.2f}')

# Plot the legend with the title
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label(data_labels[3])

# Show the labels of two axes
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Automatically resize the image by tight_layout() before savefig()
plt.title('Cultural Engagement and Awareness of Various Artforms')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/26_2023122270050.png')

# Clear the current image state 
plt.clf()