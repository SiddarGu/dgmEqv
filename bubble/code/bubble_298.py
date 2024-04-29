# Importing relevant libraries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Data transformation
raw_data = 'Destination,Tourist Arrivals (Millions),Tourism Revenue (Billion $),Hotel Occupancy Rate (%),Sustainability Score/n London,30,40,80,8/n New York,25,30,70,7/n Paris,50,60,90,9/n Dubai,20,25,65,6/n Bangkok,35,45,85,8/n Sydney,15,20,60,7/n Rome,40,45,75,9/n Barcelona,45,55,85,9/n Tokyo,10,15,70,8'
raw_data = raw_data.split('/n ')
data_labels = raw_data[0].split(',')[1:]
data = [line.split(',') for line in raw_data[1:]]
line_labels = [f'{line[0]} {line[2]}' for line in data]
data = np.array([[float(val) for val in line[1:]] for line in data])

# Normalizing color and bubble size data
norm = Normalize(vmin=min(data[:,3]), vmax=max(data[:,3]))
cmap = cm.get_cmap('viridis')

# Creating figure
fig, ax = plt.subplots(figsize=(12,8))

# Plotting the scatter plot
for i in range(len(line_labels)):
    color = cmap(norm(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], color=color, s=(data[i, 2]-min(data[:,2]))/(max(data[:,2])-min(data[:,2]))*4400 + 600, edgecolors='black', linewidth=1, alpha=0.75, label=None)
    ax.scatter([], [], label=line_labels[i], color=color)

# Setting up the color bar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])
ax.grid(True)
 
# Adding labels, titles, and legend
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.legend(title=data_labels[2], loc='upper left')
ax.set_title('Tourism and Hospitality Performance in Major World Destinations', fontsize=16, pad=20)

# Saving figure and clearing plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/327_202312310045.png')
plt.clf()
