
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ['Number of Users (Millions)', 'Time Spent (Minutes)', 'Ad Revenue (Billions $)', 'Engagement (Score)'] 
data = np.array([[1, 240, 20, 9], [330, 90, 15, 7], [2.5, 180, 50, 10], [1.9, 120, 30, 8], [750, 60, 10, 9]]) 
line_labels = ['Instagram', 'Twitter', 'Facebook', 'YouTube', 'TikTok']

# Plot the data with the type of bubble chart
fig = plt.figure() 
ax = fig.add_subplot() 

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
plt.title('Social Network Usage and Revenue in 2021')

# For the plotting using plt.scatter, the color should be normalized to the range of cmap values
cmap = cm.get_cmap('jet')
normalize = plt.Normalize(min(data[:,3]), max(data[:,3]))
s_m = cm.ScalarMappable(cmap=cmap, norm=normalize)
s_m.set_array([])

# The bubble size should range from 60 to 500 by normalization
sizes = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600, 5000))

# Parameters can be set to accurately reflect the differences in data values
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], s=sizes[i], c=s_m.to_rgba(data[i, 3]), label=None)
    ax.scatter([], [], c=s_m.to_rgba(data[i, 3]), s=20, label=line_label + f' {data[i, 2]}')

# Plot the legend with the title, by using ax.legend(title=data_labels[2])
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize
cb = fig.colorbar(s_m, ax=ax, shrink=0.8)
cb.set_label(data_labels[3], rotation=270, labelpad=20, fontsize='x-large')

# Drawing techniques such as background grids and other parameter settings can be adjusted
ax.grid()
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Show the labels of two axes
ax.set_yticks(data[:,1])
ax.set_yticklabels(data[:,1])

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/47_2023122270050.png
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/47_2023122270050.png")

# Clear the current image state at the end of the code
plt.clf()