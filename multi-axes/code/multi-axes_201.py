
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ['Tourists (Millions)', 'Hotel Occupancy Rate (%)', 'Average Hotel Day Rate (Dollars)']
line_labels = ['Domestic', 'International', 'Cruise', 'Air Travel', 'Tour Packages', 'Hotel Bookings', 'Adventure Tourism', 'Luxury Tourism', 'Cultural Tourism', 'Eco-tourism']
data = np.array([
    [7.5, 45.6, 152.9],
    [14.2, 55.2, 170.7],
    [2.5, 35.4, 99.8],
    [15.6, 42.3, 168.9],
    [6.3, 51.2, 157.3],
    [13.4, 60.6, 199.1],
    [2.8, 40.1, 130.3],
    [1.2, 35.4, 195.2],
    [4.7, 43.6, 180.2],
    [3.5, 48.2, 149.9]
])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width=0.3, color='#00cc99', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='#00cc99')
ax1.tick_params(axis='y', labelcolor='#00cc99')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-o', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='red')
ax2.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:, 2], 'b-^', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='blue')
ax3.tick_params(axis='y', labelcolor='blue')

ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

ax1.set_xlabel('Category')

plt.title('Tourism and Hospitality Landscape: Visitor Trends and Hotel Value', fontsize=15)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/36_2023122270030.png')
plt.clf()