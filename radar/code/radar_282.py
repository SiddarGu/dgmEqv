import numpy as np
import matplotlib.pyplot as plt

# start by transforming our data into np arrays
data_labels = np.array(['Q1', 'Q2', 'Q3', 'Q4'])

line_labels = np.array(['Residential Sales', 'Commercial Sales', 'Rentals', 'Property Prices', 'Mortgage Rates'])

data = np.array([[60, 65, 70, 75], [70, 75, 80, 85], [55, 60, 65, 70], [80, 85, 90, 95], [40, 35, 30, 25]])

# rotate data for plotting
data = np.concatenate([data, data[:, 0, np.newaxis]], axis=1)

# create figure and PolarAxes instance
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

# set up number of vars
num_vars = len(data_labels)

# compute angle for each axis
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# draw the polygon grid
for i, row in enumerate(data):
    ax.plot(angles, np.full_like(angles, (i + 1) * data.max() / num_vars), color='silver', alpha=0.25)

# plot data & connect last point
for i, row in enumerate(data):
    color = plt.cm.viridis(i / len(data))
    ax.plot(angles, row, color=color, alpha=0.6, label=line_labels[i])
    ax.fill(angles, row, color=color, alpha=0.25)

# set labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# set yticks & labels
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.4, 1.1))

plt.title("Real Estate and Housing Market Trends", size=20, color='black', y=1.1)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/161_2023122292141.png")
plt.clf()
