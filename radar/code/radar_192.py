import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Given data
data="Route,January,February,March,April/n Route 1,30,35,40,45/n Route 2,40,45,50,55/n Route 3,50,55,60,65/n Route 4,60,65,70,75/n Route 5,70,75,80,85"

# Parse data to data_labels, line_labels and data
temp_data = [item.split(",") for item in data.split("/n ")]
data_labels = temp_data[0][1:]
line_labels = [item[0] for item in temp_data[1:]]
data = np.array([list(map(int, item[1:])) for item in temp_data[1:]])

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Set up of angles for plot
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array
colors = cm.viridis(np.linspace(0, 1, len(line_labels)))

for idx, val in enumerate(data):
    # Append the first numerical element
    val = np.append(val, val[0])
    # Plot
    ax.plot(angles, val, label=line_labels[idx], color=colors[idx])
    
    # Radius vector
    radius_vect = np.full_like(angles, (idx+1) * data.max() / len(line_labels))
    ax.plot(angles, radius_vect, color='grey', ls='dashdot')

# Plot axis labels and radial limits
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=10, wrap=True)
ax.set_rlim(0, data.max() + 5)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Set gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# Set legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right", fontsize=10)
    
# Set figure title
plt.title('Logistics Performance on Different Routes - First Quarter', size=20, color='black', y=1.1)

# Resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/153_2023122292141.png', dpi=300)

# Clear the current image state
plt.clf()
