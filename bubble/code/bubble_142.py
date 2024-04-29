import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import numpy as np

# Data Transformation
data = '''Research Field,Annual Budget (Million $),Number of Research Papers Published,Population (Millions),Innovation Index (Score)
Physics,2000,5000,120,85
Chemistry,1500,4000,110,80
Biology,1800,4500,115,75
Aerospace Engineering,2200,4800,130,90
Computer Science,2500,5300,140,95
Electrical Engineering,2000,4900,120,80
Mechanical Engineering,2100,5100,125,85'''

data = data.split('\n')[1:]
data_labels = ["Annual Budget (Million $)", "Number of Research Papers Published", "Population (Millions)", "Innovation Index (Score)"]

line_labels = [d.split(',')[0] for d in data]
data = np.array([list(map(float, d.split(',')[1:])) for d in data])

# Plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Normalization for the marker size and color
norm_size = Normalize(vmin=data[:,2].min(), vmax=data[:,2].max())
norm_color = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], label=None, s=600 + 4400*norm_size(data[i, 2]),
               c=plt.cm.viridis(norm_color(data[i, 3])))
    line_label = '\n'.join([line_labels[i], "Population: "+str(data[i, 2])])
    ax.scatter([], [], color=plt.cm.viridis(norm_color(data[i, 3])), label=line_label)

ax.legend(title=data_labels[2], loc='upper left')
ax.grid(True)

# Color Bar
sm = ScalarMappable(cmap=plt.cm.viridis, norm=norm_color)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Analysis of Budget, Research Paper Publication, and Innovations in Science and Engineering Fields')
plt.tight_layout()

# Save and Show the plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/55_202312301731.png')

# Clearing plot
plt.clf()
