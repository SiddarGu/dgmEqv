import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data
data_labels = ['Passenger Traffic (Millions)', 'Freight Loads (Millions of tons)', 'Revenue (Billions of dollars)', 'Average Fuel Consumption (Millions of gallons)']
line_labels = ['Bus', 'Rail', 'Air', 'Marine', 'Auto', 'Truck', 'Bicycle', 'Pedestrian', 'Taxi', 'Motorcycle', 'Pipelines']
data = np.array([
    [450, 5, 1.2, 600],
    [200, 50, 2, 1000],
    [150, 40, 5, 1500],
    [50, 300, 3, 1200],
    [2000, 300, 50, 15000],
    [100, 1000, 15, 5000],
    [500, 0, 0.2, 0],
    [800, 0, 0, 0],
    [300, 0, 3, 800],
    [100, 0, 0.5, 200],
    [0, 400, 1.5, 500]])

# creating figure
fig = plt.figure(figsize=(25, 10))

# plot types
plot_types = ['bar', 'plot', 'plot', 'bar']

# colors
colors = ['b', 'g', 'r', 'c']

# creating subplot
ax1 = fig.add_subplot(111)
# plotting first column
ax1.bar(line_labels, data[:, 0], color=colors[0], alpha=0.6, width=0.4)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color(colors[0])
ax1.tick_params(axis='y', colors=colors[0])
ax1.set_ylim(bottom=0)

# plot others
axs = [ax1]
for i in range(1, len(data_labels)):
    ax = axs[0].twinx()
    getattr(ax, plot_types[i])(line_labels, data[:, i], color=colors[i], alpha=0.6 if plot_types[i] == 'bar' else 1)
    ax.yaxis.label.set_color(colors[i])
    ax.tick_params(axis='y', colors=colors[i])
    ax.set_ylabel(data_labels[i])
    ax.spines['right'].set_position(('outward', 60*(i-1)))
    ax.yaxis.set_major_locator(AutoLocator())
    axs.append(ax)

# setting title
plt.title("Transportation and Logistics: A Comparative Analysis of Transit Modes")

# showing legends
for ax, color in zip(axs, colors):
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='lower left', framealpha=0.2, labelcolor=color, facecolor='white')

# saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/57_2023122292141.png')

# clearing current figure
plt.clf()
