import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Parse data
data_str = 'Year,Number of Houses Sold,Median Sale Price (Thousands of Dollars),Average Days on the Market/n 2011,15800,240,93/n 2012,17600,260,89/n 2013,18900,280,85/n 2014,20200,300,81/n 2015,21800,320,77/n 2016,23500,340,73/n 2017,25300,360,69/n 2018,27000,380,65/n 2019,28800,400,61/n 2020,30800,420,57'
data = []
line_labels = []
data_rows = data_str.split('/n')
for row in data_rows[1:]:
    values = row.split(',')
    line_labels.append(values[0])
    data.append([float(v) for v in values[1:]])
data_labels = data_rows[0].split(',')[1:]
data = np.array(data)

colors = ['r', 'g', 'b', 'c']

# Create figure and ax
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot data
for i, (y_data, plot_type) in enumerate(zip(data[:, 1:].T, ['bar', 'line', 'scatter'])):
    ax = ax1.twinx() if i else ax1
    if plot_type == 'bar':
        ax.bar(line_labels, y_data, color=colors[i], alpha=0.6)
    elif plot_type == 'line':
        ax.plot(line_labels, y_data, color=colors[i])
    else:
        ax.scatter(line_labels, y_data, color=colors[i])
    ax.set_ylabel(data_labels[i])
    ax.yaxis.label.set_color(colors[i])
    ax.yaxis.set_major_locator(AutoLocator())
    if i:
        ax.spines['right'].set_position(('outward', (i-1)*60))

# Set title and legends
plt.title('Real Estate and Housing Market Overview: Sales, Prices, and Market Time')
ax1.legend(data_labels, loc='upper left')
ax1.set_xlabel('Year')

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/60_2023122292141.png')
plt.clf()
