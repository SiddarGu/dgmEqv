import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Transforming data into variables
data_labels = ['Popularity Index', 'Social Impact (Score)', 'Global Reach (Millions)', 'Aesthetic Value (Score)']
line_labels = ['Literature 1000', 'Fine Art 500', 'Theater 300', 'Music 2000', 'Film 1500', 'Animation 1200', 'Podcast 800']
data = np.array([[80, 90, 1000, 9], [70, 87, 500, 10], [75, 85, 300, 8], [90, 95, 2000, 9], 
                 [85, 92, 1500, 10], [82, 89, 1200, 9], [78, 86, 800, 8]])

# Create a figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()

cmap = cm.get_cmap('viridis')

# Normalize bubble sizes and color values
size_scale = Normalize(np.min(data[:, 2]), np.max(data[:, 2]))
color_scale = Normalize(np.min(data[:, 3]), np.max(data[:, 3]))

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=[cmap(color_scale(data[i, 3]))], s=size_scale(data[i, 2])*3900+600, 
               label=None)
    ax.scatter([], [], c=[cmap(color_scale(data[i, 3]))], s=20, label=line_label)

ax.legend(title=data_labels[2])
plt.colorbar(cm.ScalarMappable(norm=color_scale, cmap=cmap), ax=ax).set_label(data_labels[3])

ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title("The Influence and Reach of Various Cultural Phenomena in Social Sciences and Humanities")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/190_202312310045.png')
plt.clf()
