import matplotlib.pyplot as plt
import numpy as np

# set data
data_labels = ['Farm A', 'Farm B', 'Farm C', 'Farm D']
line_labels = ['Wheat', 'Corn', 'Rice', 'Soybean', 'Potato', 'Tomato']
data = np.array([
    [75, 80, 85, 90],
    [70, 75, 80, 85],
    [65, 70, 75, 80],
    [90, 95, 100, 105],
    [80, 85, 90, 95],
    [75, 70, 65, 60]
])

# create figure and add subplot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(polar=True)

# set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# iterate over each row in the data array
for i in range(len(data)):
    # plot data lines
    ax.plot(angles, np.append(data[i], data[i][0]), label=line_labels[i])
    # plot gridlines
    r = np.ones_like(angles) * 15 * (i + 1)
    ax.plot(angles, r, color='gray', linestyle='dashed')

# set axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14, ha='right', wrap=True)
ax.set_rgrids([15 * i for i in range(1, len(data))], labels=[f'{15 * i}' for i in range(1, len(data))], angle=0)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels, rotation=45)

# adjust the radial limits
ax.set_ylim(0, np.amax(data))

# plot legend
legend = ax.legend(ax.get_legend_handles_labels()[0], line_labels, 
                   loc='upper right', bbox_to_anchor=(1.2, 1.1))

# remove circular gridlines and background
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# set title
ax.set_title('Farm Produce-Yield Statistics')

# adjust layout and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/19_2023122292141.png')

# clear current figure
plt.clf()
