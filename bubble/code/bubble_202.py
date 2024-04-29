import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

# Given data
input_data='''Engineer Field,Annual Income (USD),Years of Experience,Average Completed Projects,Average Patent Applications
 Mechanical,80000,5,10,2
 Civil,70000,6,8,1
 Electrical,85000,4,12,3
 Chemical,90000,5,9,2
 Aerospace,95000,6,11,4
 Computer,100000,4,13,5
 Environmental,75000,5,7,1'''

data_labels = ['Annual Income (USD)', 'Years of Experience', 'Average Completed Projects', 'Average Patent Applications']
line_labels = []
data = []

# Prepare data
for line in input_data.split('\n')[1:]:
    fields = line.split(',')
    line_labels.append(fields[0] + ' ' + fields[2])
    data.append(list(map(int, fields[1:])))

data = np.array(data)

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Normalize color and size
size_scale = Normalize(min(data[:,2]), max(data[:,2]))
color_scale = Normalize(min(data[:,3]), max(data[:,3]))
cmap = cm.get_cmap('viridis')

# Scatter plot
for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(color_scale(data[i, 3])), s=600+4400*size_scale(data[i, 2]), label=None)
    ax.scatter([], [], c=cmap(color_scale(data[i, 3])), s=20, label=line_label)

# Add legend and colorbar
sc = ScalarMappable(norm=color_scale, cmap=cmap)
plt.colorbar(sc, ax=ax).set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')

# Additional settings
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
fig.suptitle('Overview of Engineer Fields in Science and Engineering')

# Save and clear
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/279_202312310045.png')
plt.clf()
