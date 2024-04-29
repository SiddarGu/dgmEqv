import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

data_labels = ['Ticket Sale Revenue (Millions)', 'Average Number of Spectators', 'Social Media Engagements (Millions)']
line_labels = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([[367, 68230, 56], 
                 [405, 71580, 68],
                 [438, 74190, 74],
                 [461, 77980, 82],
                 [491, 81250, 94],
                 [200, 21900, 136],
                 [400, 61100, 159]])

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

ax1.plot(line_labels, data[:, 0], color='blue', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')

ax2 = ax1.twinx()
ax2.fill_between(line_labels, data[:, 1], alpha=0.5, color='green', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='green')
ax2.spines['right'].set_position(('outward', 60)) 

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='red',label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='red')
ax3.spines['right'].set_position(('outward', 120)) 

ax1.set_xlabel('Year')
ax1.xaxis.set_tick_params(rotation=30)
ax1.xaxis.label.set_color('black')

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

plt.grid(True)
plt.title('Yearly Analysis of the Sports and Entertainment Industry')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/68_2023122292141.png')
plt.clf()
