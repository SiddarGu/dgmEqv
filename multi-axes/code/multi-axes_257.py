import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Unpack the data
data = """2010,3217,220,120
2011,3566,230,115
2012,4002,245,110
2013,4520,260,105
2014,4879,275,100
2015,5300,290,95
2016,5700,305,90
2017,6130,320,85
2018,6530,335,80
2019,7060,350,75
2020,7580,365,70"""
data = np.array([line.split(',') for line in data.split('\n')]).astype(int)
line_labels = data[:, 0]
data = data[:, 1:]

data_labels = ["Number of Houses Sold", "Median Price (Thousands)", "Average Time on Market (Days)"]

plot_types = ['bar', 'line', 'scatter']

fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='blue')
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params('y', colors='blue')
ax1.xaxis.grid(True)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='green')
ax2.set_ylabel(data_labels[1], color='green')
ax2.tick_params('y', colors='green')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], label=data_labels[2], color='red')
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params('y', colors='red')
ax3.yaxis.set_major_locator(AutoLocator())

fig.suptitle('Real Estate Market Analysis: Sales Trends, Price Dynamics, and Selling Times', fontsize=16)
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
fig.tight_layout()
fig.subplots_adjust(top=0.9)
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/188_202312310150.png")
plt.clf()
