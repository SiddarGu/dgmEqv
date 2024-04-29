import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into variables
data_str = '''Parameter,Wind Turbine,Solar Panel,Hydroelectric Generator,Nuclear Reactor,Geothermal Plant
Efficiency (%),80,75,90,95,85
Durability (Years),20,25,30,35,40
Output Power (MW),3,2,5,6,4
Maintenance Cost ($K),25,20,30,35,28
Environmental Impact (Score),75,80,55,50,85'''

data_list = data_str.split('\n')
data_labels = data_list[0].split(',')[1:]
data = [[int(x) for x in row.split(',')[1:]] for row in data_list[1:]]
line_labels = ['Efficiency', 'Durability', 'Output Power', 'Maintenance Cost', 'Environmental Impact']

# Create figure and plot data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, np.array(data)[:, 0:1]), axis=1)

# Iterate over each row in the data array and plot data lines
colors = ['r', 'g', 'b', 'y', 'm']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])
    
# Set axis labels and radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data) + 10)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# Plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper left')

# Set title
title = 'Comparative Analysis of Energy Systems in Science and Engineering'
plt.title(title, fontsize=14)

# Add background grid
ax.grid(True, linestyle='dashed')

# Adjust plot and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/60_202312302350.png', dpi=300)

# Clear current image state
plt.clf()
plt.close()