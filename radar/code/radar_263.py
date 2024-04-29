import numpy as np
import matplotlib.pyplot as plt

# Parsing the given data
data_string = 'Season,Spring,Summer,Autumn,Winter/n Number of Visitors,70,85,60,35/n ' \
              'Hotel Occupancy Rate,75,95,65,40/n Tour Guide Rating,80,85,75,70/n ' \
              'Local Cuisine Rating,85,90,80,70/n Overall Satisfaction,80,85,70,60'

split_data = [item.split(',') for item in data_string.split('/n ')]
data_labels = split_data[0][1:]
line_labels = [item[0] for item in split_data[1:]]
data = np.array([list(map(int, item[1:])) for item in split_data[1:]])

# Set up the figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)
ax.set_title('Tourism and Hospitality Seasonal Analysis')

# Constructing the grid
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, np.amax(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Remove background
ax.spines['polar'].set_visible(False)

# Plotting the data
for idx in range(data.shape[0]):
    plot_data = np.append(data[idx], data[idx, 0])
    ax.plot(angles, plot_data, label=line_labels[idx])

    # To make the outer radial grid visible
    ax.yaxis.grid((idx + 1) * np.amax(data) / (data.shape[0]))

# Plotting the legend 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/29_2023122292141.png')
plt.clf()
