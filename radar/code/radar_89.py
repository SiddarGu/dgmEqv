import numpy as np
import matplotlib.pyplot as plt

data_labels = ["Wheat", "Corn", "Rice", "Barley", "Soybeans"]
data = np.array([[32, 78, 68, 24, 35],
                 [25, 22, 23, 21, 24],
                 [35, 45, 40, 30, 50],
                 [22, 25, 20, 18, 27],
                 [20, 15, 18, 23, 12]])

line_labels = ["Yield (kg/ha)", "Water Usage (box/hectare)", "Pesticide Use (kg/ha)",
               "Labor Cost (%)", "Market Price (USD/kg)"]

# Append the first numerical element of each row to the end of that row
data = np.concatenate((data, data[:, [0]]), axis=1)

# Create figure and axes
fig = plt.figure(figsize=(10, 10))  
ax = fig.add_subplot(111, polar=True)

# evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# plot each row of data
colors = ["r", "g", "b", "orange", "purple"]
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], linewidth=2, label=line_labels[i])

# set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# adjust radial limits to accommodate the maximum of data
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

# plot legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# set title
plt.title("Agricultural and Food Production Analysis")

# add background grids
ax.grid(True)

# automatically resize the image before saving
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/115_202312302350.png')

# clear the current figure state
plt.clf()