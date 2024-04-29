
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# transform the given data into three variables
data_labels = ['Attitudes to Education (Score)', 'Perception of Intelligence (Score)', 'Career Path (Score)', 'Satisfaction (Score)']
line_labels = ['Men', 'Women', 'Non-Binary', 'Transgender', 'Intersex']
data = np.array([[9, 7, 8, 5], [8, 8, 9, 7], [7, 9, 7, 9], [6, 7, 8, 8], [5, 6, 9, 6]])

# plot the data with type of bubble chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()
cmap = cm.get_cmap('viridis')
scalar_map = cm.ScalarMappable(norm=Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3])), cmap=cmap)

for i in range(len(line_labels)):
    # scatter an empty point
    ax.scatter([], [], label=line_labels[i] + f' {data[i, 2]}', color=scalar_map.to_rgba(data[i, 3]), s=20)
    # scatter not empty points
    ax.scatter(data[i, 0], data[i, 1], label=None, color=scalar_map.to_rgba(data[i, 3]), s=600 + 5000*(data[i, 2]-np.min(data[:, 2]))/(np.max(data[:, 2])-np.min(data[:, 2])))

# add legend with title and set legend location
ax.legend(title=data_labels[2], loc='lower center')

# add color bar
cb = fig.colorbar(scalar_map, ax=ax)
cb.set_label(data_labels[3])

# set background grid, labels and title
ax.grid(linestyle='dotted')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
fig.suptitle('Perception of Education, Intelligence, and Career Paths by Gender in Social Sciences and Humanities')

# automatically resize the image by tight_layout()
plt.tight_layout()
# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/39_2023122270050.png')

# clear the current image state
plt.clf()