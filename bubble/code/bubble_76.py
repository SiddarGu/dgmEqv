import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

# The given data
data_string = """Subject,Enrollment (Thousands),Faculty (Thousands),Annual Budget (Million $),Research Output (Publications per Year)
Mathematics,500,50,200,3000
Physics,300,45,180,2800
Biology,450,55,210,3500
Literature,600,60,230,2000
History,550,56,220,2400
Computer Science,750,80,300,4000"""

# Split the data into lines and fields, convert to an array
lines = data_string.split('\n')
fields = [line.split(',') for line in lines]

# Extract the labels and data
data_labels = fields[0][1:]
line_labels = [f[0] + ': ' + f[2] for f in fields[1:]]
data = np.array([list(map(float, f[1:])) for f in fields[1:]])

# Create figure and ax
fig, ax = plt.subplots(figsize=(12, 8))

cmap = cm.get_cmap('viridis')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())

for i, line_label in enumerate(line_labels):
    scatter = ax.scatter(data[i, 0], data[i, 1], s=data[i, 2]*50, c=data[i, 3], cmap=cmap, norm=norm, label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_label)
    
cbar = plt.colorbar(scatter)
cbar.set_label(data_labels[3])
ax.legend(title=data_labels[2], loc='upper left')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.title('University Department Statistics - Education and Academics')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/198_202312310045.png')
plt.clf()
