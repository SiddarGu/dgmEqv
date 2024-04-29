import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Converting data into variables
data_labels = ['Number of Donors', 'Total Donations (USD)', 'Average Donation Size (USD)']
content = """Education,5000,1000000,200
Health,3000,500000,167
Environment,2000,300000,150
Poverty Alleviation,4000,800000,200
Arts and Culture,1000,200000,200
Animal Welfare,1500,150000,100
Disaster Relief,2500,600000,240"""
line_labels = [line.split(',')[0] for line in content.split('\n')]
data = np.array([line.split(',')[1:] for line in content.split('\n')], dtype=float).T

# Creating figure
plt.figure(figsize=(22,12))
ax1 = plt.subplot(111)

# Bar chart
ax1.bar(line_labels, data[0], color='b', label=data_labels[0])

# Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[1], color='g', label=data_labels[1])

# Scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[2], color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))

# Setting settings for axes
for ax in [ax1, ax2, ax3]:
    ax.xaxis.set_tick_params(rotation=45)
    ax.yaxis.get_major_locator().set_params(integer=True)

# Labels
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])
ax1.yaxis.label.set_color('b')
ax2.yaxis.label.set_color('g')
ax3.yaxis.label.set_color('r')

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Grids
ax1.grid(True)
ax2.grid(False)
ax3.grid(False)

# Title
plt.title('Chart Title,Donations Analysis by Category')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/337_202312311430.png')
plt.cla()
