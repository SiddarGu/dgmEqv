import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy import linspace
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

#define our data as a list
raw_data = [
    ["Facebook", 2790, 38, 70, 98],
    ["Instagram", 1400, 29, 20, 90],
    ["Twitter", 330, 11, 3, 80],
    ["LinkedIn", 310, 10, 2, 70],
    ["YouTube", 2000, 40, 15, 95],
    ["Snapchat", 500, 26, 1, 85],
]

#define the labels and data
data_labels = ["Active Users (Millions)", "Average Time Spent (Minutes)", "Advertising Revenue (Billion $)", "Popularity (Score)"]
line_labels = [row[0] + ": " + str(row[3]) for row in raw_data]
data = np.array([row[1:] for row in raw_data])

# define color range for colormap
start = 0.0
stop = 1.0
number_of_lines = len(data)
cm_subsection = linspace(start, stop, number_of_lines)

# create normalizer and scalar mappable for colormap
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
mappable = ScalarMappable(cmap=cm.cool, norm=norm)

# create figure and subplot
fig, ax = plt.subplots(figsize=(12, 6))

# plot data
for i in range(data.shape[0]):
    # set size of bubble between 600 to 5000
    bubble_size = 600 + (data[i, 2] / data[:, 2].max()) * 4400
    ax.scatter(data[i, 0], data[i, 1], s=bubble_size, color=mappable.to_rgba(data[i, 3]), label=None, edgecolor='#000000', linewidth=0.5)
    ax.scatter([], [], c=mappable.to_rgba(data[i, 3]), label=line_labels[i])

#create legend with title
ax.legend(title=data_labels[2], loc='upper left')

# set title for color bar
fig.colorbar(mappable, ax=ax, label=data_labels[3])
    
# set x and y labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# title for figure
plt.title('Usability and Profitability of Top Social Media Platforms')

# resize image before saving
plt.tight_layout()

# save image in the defined path
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/191_202312310045.png')

# clear the current image state
plt.clf()
