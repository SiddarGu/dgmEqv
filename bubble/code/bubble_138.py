import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Given data
table_data = [
    ['Paris',40,80,150,5],
    ['London',35,75,175,4],
    ['Tokyo',30,70,200,6],
    ['New York',25,65,225,3],
    ['Rome',20,60,250,5],
    ['Sydney',15,55,275,4]
]

# Extract variable data
data_labels = ['Number of Tourists (Millions)','Hotel Occupancy Rate (%)','Revenue per Available Room (USD)','Average Length of Stay (Days)']
line_labels = [f'{line[0]} {line[2]}' for line in table_data]
data = np.array([line[1:] for line in table_data])

# Set bubble sizes from 600 to 5000 by normalization
sizes = 600 + 4400 * (data[:,2] - np.min(data[:,2])) / (np.max(data[:,2]) - np.min(data[:,2]))

# Create color map based on the 4th column
colors = plt.cm.viridis((data[:,3] - np.min(data[:,3])) / (np.max(data[:,3]) - np.min(data[:,3])))

# Create figure and adjust plot parameters
fig, ax = plt.subplots(figsize=(10,8))
ax.grid(True, which='both', color='grey', linewidth=0.3)

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], label=None, color=colors[i], s=sizes[i])
    ax.scatter([], [], color=colors[i], label=line_label)

# Plot legend and color bar
ax.legend(title=data_labels[2], loc='upper left')
sm = plt.cm.ScalarMappable(cmap='viridis', norm=mcolors.Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3])))
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Add labels and title
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Tourism and Hospitality Statistics of Major Cities')

# Adjust plot and save figure
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/362_202312311429.png')

# Clean up
plt.cla()
plt.clf()
plt.close()
